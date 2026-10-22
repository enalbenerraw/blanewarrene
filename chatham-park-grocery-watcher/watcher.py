#!/usr/bin/env python3
"""Chatham Park Grocery Watcher.

Checks Google News, local news feeds, and Town of Pittsboro agendas for
mentions of a grocery store coming to Chatham Park, then emails a digest of
anything new. Settings live in config.yaml; memory of what was already sent
lives in seen.json.

Usage:
    python watcher.py                 # normal run: check, email, remember
    python watcher.py --dry-run       # print matches, send nothing, remember nothing
    python watcher.py --check-sources # report which sources work
    python watcher.py --test-email    # send a test email to confirm credentials
"""

from __future__ import annotations

import argparse
import hashlib
import html
import io
import json
import logging
import os
import re
import smtplib
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from pathlib import Path
from urllib.parse import quote_plus, urljoin
from zoneinfo import ZoneInfo

import feedparser
import requests
import yaml
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

HERE = Path(__file__).resolve().parent
EASTERN = ZoneInfo("America/New_York")
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36 ChathamParkGroceryWatcher/1.0"
)
TIMEOUT = 30
# CivicPlus Agenda Center document links, for example
# /AgendaCenter/ViewFile/Agenda/_10122026-490
AGENDA_RE = re.compile(r"/AgendaCenter/ViewFile/(Agenda|ArchivedAgenda)/_(\d{8})-(\d+)", re.I)

log = logging.getLogger("watcher")


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

@dataclass
class Item:
    title: str
    link: str
    source: str
    published: datetime | None
    text: str
    kind: str = "news"  # news or agenda
    doc_id: str | None = None


@dataclass
class Match:
    item: Item
    location_hits: list[str]
    grocery_hits: list[str]
    low_priority: bool
    snippets: list[str] = field(default_factory=list)
    keys: list[str] = field(default_factory=list)


@dataclass
class SourceStatus:
    name: str
    ok: bool
    detail: str
    items: int = 0


# ---------------------------------------------------------------------------
# Matching
# ---------------------------------------------------------------------------

def normalize(text: str) -> str:
    text = text.replace("’", "'").replace("‘", "'").replace(" ", " ")
    return re.sub(r"\s+", " ", text).strip()


def term_pattern(term: str) -> str:
    """Regex for a term: case-insensitive, flexible spaces, hyphens and apostrophes.

    "Lowes Foods" also matches "Lowe's Foods"; "Trader Joe's" also matches
    "Trader Joes"; plurals like "supermarkets" match "supermarket".
    """
    words = []
    for word in normalize(term).split(" "):
        w = re.escape(word).replace("'", "'?").replace(r"\-", "[- ]?")
        if len(word) > 3 and word.lower().endswith("s") and "'" not in word:
            w = w[:-1] + "'?s"
        words.append(w)
    return r"\b" + r"[\s\-]+".join(words) + r"(?:s|'s)?\b"


class Matcher:
    def __init__(self, cfg: dict):
        self.location = self._compile(cfg.get("location_terms", []))
        grocery = list(cfg.get("grocery_terms", [])) + list(cfg.get("grocery_chains", []))
        self.grocery = self._compile(grocery)
        self.generic = {t.lower() for t in cfg.get("grocery_terms", [])}
        self.low = {t.lower() for t in cfg.get("low_priority_terms", [])}
        self.fresh = self._compile(cfg.get("new_store_phrases", []))
        # Low-priority terms like "Northwood Landing" are context, not grocery
        # terms, so they are only used to classify, never to match.
        self.low_patterns = self._compile(cfg.get("low_priority_terms", []))
        self.all_terms = re.compile(
            "|".join(p.pattern for _, p in self.location + self.grocery + self.low_patterns),
            re.I,
        )

    @staticmethod
    def _compile(terms):
        return [(t, re.compile(term_pattern(t), re.I)) for t in terms if str(t).strip()]

    @staticmethod
    def _hits(compiled, text):
        return [term for term, pat in compiled if pat.search(text)]

    def match(self, item: Item) -> Match | None:
        text = normalize(f"{item.title}. {item.text}")
        loc = self._hits(self.location, text)
        groc = self._hits(self.grocery, text)
        if not loc or not groc:
            return None
        named = [g for g in groc if g.lower() not in self.low and g.lower() not in self.generic]
        old_news = bool(self._hits(self.low_patterns, text))
        fresh = bool(self._hits(self.fresh, text))
        # Lower priority: the item is about the existing Lowes Foods at
        # Northwood Landing, names no other chain, and has none of the
        # "new store" phrases from config.yaml.
        low_priority = old_news and not named and not fresh
        m = Match(item, loc, groc, low_priority)
        m.snippets = self.snippets(text, named or groc, 3 if item.kind == "agenda" else 1)
        return m

    def snippets(self, text: str, preferred: list[str], limit: int, width: int = 220) -> list[str]:
        pats = [p for t, p in self.grocery if t in preferred]
        spans = []
        for pat in pats:
            for m in pat.finditer(text):
                spans.append((m.start(), m.end()))
        spans.sort()
        out, last_end = [], -1
        for start, end in spans:
            if start < last_end:
                continue
            a, b = max(0, start - width), min(len(text), end + width)
            snippet = text[a:b]
            prefix = "..." if a > 0 else ""
            suffix = "..." if b < len(text) else ""
            out.append(prefix + snippet + suffix)
            last_end = b
            if len(out) >= limit:
                break
        if not out:
            out.append(text[: width * 2] + ("..." if len(text) > width * 2 else ""))
        return out

    def highlight_html(self, snippet: str) -> str:
        escaped = html.escape(snippet, quote=False)
        return self.all_terms.sub(lambda m: f"<mark><b>{m.group(0)}</b></mark>", escaped)

    def highlight_text(self, snippet: str) -> str:
        return self.all_terms.sub(lambda m: f"**{m.group(0)}**", snippet)


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------

def make_session() -> requests.Session:
    s = requests.Session()
    s.headers["User-Agent"] = USER_AGENT
    retry = Retry(total=2, backoff_factor=2, status_forcelist=(429, 500, 502, 503, 504))
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.mount("http://", HTTPAdapter(max_retries=retry))
    return s


def strip_html(raw: str) -> str:
    return normalize(BeautifulSoup(raw or "", "html.parser").get_text(" "))


def entry_date(entry) -> datetime | None:
    for key in ("published_parsed", "updated_parsed"):
        st = entry.get(key)
        if st:
            return datetime(*st[:6], tzinfo=timezone.utc)
    return None


def parse_feed(session, url):
    resp = session.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    feed = feedparser.parse(resp.content)
    if feed.bozo and not feed.entries:
        raise ValueError(f"not a valid feed ({feed.get('bozo_exception')})")
    return feed


def google_news_queries(cfg: dict) -> list[str]:
    gn = cfg.get("google_news", {}) or {}
    queries = list(gn.get("queries", []))
    if gn.get("add_chain_queries", True):
        queries += [f'"Chatham Park" {chain}' for chain in cfg.get("grocery_chains", [])]
    return queries


def fetch_google_news(session, cfg, statuses) -> list[Item]:
    recent = (cfg.get("google_news", {}) or {}).get("recent")
    items = []
    for q in google_news_queries(cfg):
        full = f"{q} when:{recent}" if recent else q
        url = f"https://news.google.com/rss/search?q={quote_plus(full)}&hl=en-US&gl=US&ceid=US:en"
        try:
            feed = parse_feed(session, url)
        except Exception as e:  # noqa: BLE001 - one bad source must not stop the run
            log.warning("Google News query failed: %s (%s)", q, e)
            statuses.append(SourceStatus(f"Google News: {q}", False, str(e)))
            continue
        for e in feed.entries:
            source = (e.get("source") or {}).get("title") or "Google News"
            title = e.get("title", "")
            if source and title.endswith(f" - {source}"):
                title = title[: -len(source) - 3]
            items.append(Item(
                title=normalize(title), link=e.get("link", ""), source=source,
                published=entry_date(e), text=strip_html(e.get("summary", "")),
            ))
        statuses.append(SourceStatus(f"Google News: {q}", True, "ok", len(feed.entries)))
        time.sleep(1)  # be polite to Google
    return items


def fetch_local_feeds(session, cfg, statuses) -> list[Item]:
    items = []
    for outlet in cfg.get("local_feeds", []) or []:
        name = outlet.get("name", "Local feed")
        errors = []
        for url in outlet.get("urls", []):
            try:
                feed = parse_feed(session, url)
                if not feed.entries:
                    raise ValueError("feed has no items")
            except Exception as e:  # noqa: BLE001
                errors.append(f"{url}: {e}")
                continue
            for e in feed.entries:
                body = e.get("summary", "")
                if e.get("content"):
                    body = " ".join(c.get("value", "") for c in e.content)
                items.append(Item(
                    title=normalize(strip_html(e.get("title", ""))), link=e.get("link", url),
                    source=name, published=entry_date(e), text=strip_html(body),
                ))
            statuses.append(SourceStatus(name, True, f"using {url}", len(feed.entries)))
            break
        else:
            log.warning("%s: no working feed. %s", name, "; ".join(errors))
            statuses.append(SourceStatus(name, False, "; ".join(errors) or "no URLs configured"))
    return items


def discover_agendas(session, base: str) -> dict[str, dict]:
    """Find agenda documents on a CivicPlus Agenda Center.

    Tries the Agenda Center RSS feed, the Agenda Center page, and its search
    page, and merges what they find. Returns {doc_id: info}.
    """
    docs: dict[str, dict] = {}
    errors = []

    def add(href, title, board):
        m = AGENDA_RE.search(href or "")
        if not m:
            return
        kind, mmddyyyy, num = m.groups()
        doc_id = f"{mmddyyyy}-{num}"
        try:
            meeting = datetime.strptime(mmddyyyy, "%m%d%Y").date()
        except ValueError:
            return
        info = docs.setdefault(doc_id, {
            "id": doc_id, "path": f"/AgendaCenter/ViewFile/{kind}/_{doc_id}",
            "date": meeting, "title": "", "board": "",
        })
        info["title"] = info["title"] or normalize(title or "")
        info["board"] = info["board"] or normalize(board or "")

    try:
        feed = parse_feed(session, urljoin(base, "/RSSFeed.aspx?ModID=65&CID=All-0"))
        for e in feed.entries:
            board = " ".join(t.get("term", "") for t in e.get("tags", []))
            add(e.get("link", ""), e.get("title", ""), board or e.get("title", ""))
    except Exception as e:  # noqa: BLE001
        errors.append(f"RSS: {e}")

    today = datetime.now(EASTERN).date()
    pages = [
        "/AgendaCenter",
        "/AgendaCenter/Search/?term=&CIDs=all&startDate={}&endDate={}&dateRange=&dateSelector=".format(
            quote_plus((today - timedelta(days=120)).strftime("%m/%d/%Y")),
            quote_plus((today + timedelta(days=60)).strftime("%m/%d/%Y")),
        ),
    ]
    for page in pages:
        try:
            resp = session.get(urljoin(base, page), timeout=TIMEOUT)
            resp.raise_for_status()
        except Exception as e:  # noqa: BLE001
            errors.append(f"{page}: {e}")
            continue
        soup = BeautifulSoup(resp.text, "html.parser")
        for a in soup.find_all("a", href=AGENDA_RE):
            heading = a.find_previous(["h2", "h3"])
            row = a.find_parent("tr")
            title = row.get_text(" ") if row else a.get_text(" ")
            add(a["href"], title, heading.get_text(" ") if heading else "")

    if not docs and errors:
        raise RuntimeError("; ".join(errors))
    return docs


def download_text(session, url: str, max_bytes: int) -> tuple[str, str]:
    """Download a PDF or HTML document and return (text, content kind)."""
    with session.get(url, timeout=TIMEOUT * 4, stream=True) as resp:
        resp.raise_for_status()
        length = int(resp.headers.get("Content-Length") or 0)
        if length > max_bytes:
            raise ValueError(f"file is {length // 1_000_000} MB, over the limit")
        buf = io.BytesIO()
        for chunk in resp.iter_content(1 << 16):
            buf.write(chunk)
            if buf.tell() > max_bytes:
                raise ValueError("file is over the size limit")
        data = buf.getvalue()
        ctype = resp.headers.get("Content-Type", "")
    if data[:5] == b"%PDF-" or "pdf" in ctype:
        from pypdf import PdfReader

        reader = PdfReader(io.BytesIO(data))
        pages = []
        for page in reader.pages:
            try:
                pages.append(page.extract_text() or "")
            except Exception:  # noqa: BLE001 - skip unreadable pages
                pages.append("")
        return normalize(" ".join(pages)), "pdf"
    return strip_html(data.decode(resp.encoding or "utf-8", errors="replace")), "html"


def fetch_agendas(session, cfg, state, statuses) -> list[Item]:
    tcfg = cfg.get("town_agendas", {}) or {}
    if not tcfg.get("enabled", True):
        return []
    base = tcfg.get("base_url", "https://www.pittsboronc.gov")
    boards = [b.lower() for b in tcfg.get("boards", []) or []]
    lookback = int(tcfg.get("lookback_days", 60))
    max_bytes = int(float(tcfg.get("max_file_mb", 60)) * 1_000_000)
    today = datetime.now(EASTERN).date()
    scanned = state.setdefault("scanned_docs", {})

    try:
        docs = discover_agendas(session, base)
    except Exception as e:  # noqa: BLE001
        log.warning("Town agendas: could not list agendas (%s)", e)
        statuses.append(SourceStatus("Town of Pittsboro agendas", False, str(e)))
        return []

    items, failures, considered = [], [], 0
    for doc in sorted(docs.values(), key=lambda d: d["date"], reverse=True):
        if abs((today - doc["date"]).days) > lookback:
            continue
        label = f"{doc['board']} {doc['title']}".lower()
        if boards and doc["board"] and not any(b in label for b in boards):
            continue
        considered += 1
        # Past meetings are scanned once. Upcoming meetings are re-scanned each
        # run, because packets are often amended before the meeting.
        if doc["id"] in scanned and doc["date"] < today:
            continue
        urls = [urljoin(base, doc["path"])]
        if tcfg.get("download_packets", True):
            urls.insert(0, urljoin(base, doc["path"] + "?packet=true"))
        text, used, errs = "", None, []
        for url in urls:
            try:
                text, _ = download_text(session, url, max_bytes)
                used = url
                if text:
                    break
            except Exception as e:  # noqa: BLE001
                errs.append(f"{url}: {e}")
        if used is None:
            failures.append(f"{doc['id']}: {'; '.join(errs)}")
            continue
        scanned[doc["id"]] = today.isoformat()
        board = doc["board"] or "Town of Pittsboro"
        title = doc["title"] or "Meeting agenda"
        items.append(Item(
            title=f"{board}: {title} ({doc['date']:%b %d, %Y})", link=used,
            source="Town of Pittsboro Agenda Center",
            published=datetime.combine(doc["date"], datetime.min.time(), tzinfo=EASTERN),
            text=text, kind="agenda", doc_id=doc["id"],
        ))

    detail = f"{len(docs)} agendas listed, {considered} in window, {len(items)} downloaded"
    if failures:
        detail += f", {len(failures)} failed: " + " | ".join(failures[:3])
        log.warning("Town agendas: %s", detail)
    statuses.append(SourceStatus("Town of Pittsboro agendas", not failures or bool(items), detail, len(items)))
    return items


# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------

def load_state(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {}


def save_state(path: Path, state: dict) -> None:
    # Keep the file small: forget scanned agendas after 180 days.
    cutoff = (datetime.now(EASTERN).date() - timedelta(days=180)).isoformat()
    state["scanned_docs"] = {k: v for k, v in state.get("scanned_docs", {}).items() if v >= cutoff}
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def norm_link(link: str) -> str:
    return re.sub(r"[?#].*$", "", link.strip().lower().rstrip("/")) if "news.google.com" not in link else link.strip()


def item_keys(m: Match) -> list[str]:
    it = m.item
    if it.kind == "agenda":
        # Re-alert if an amended packet names a new grocery term.
        return [f"doc:{it.doc_id}:" + "+".join(sorted(g.lower() for g in m.grocery_hits))]
    title = re.sub(r"[^a-z0-9 ]", "", it.title.lower())
    title_hash = hashlib.sha1(title.encode()).hexdigest()[:16]
    link_hash = hashlib.sha1(f"{title}|{norm_link(it.link)}".encode()).hexdigest()[:16]
    return [f"url:{norm_link(it.link)}", f"title:{title_hash}", f"titlelink:{link_hash}"]


# ---------------------------------------------------------------------------
# Email
# ---------------------------------------------------------------------------

def fmt_date(d: datetime | None) -> str:
    return d.astimezone(EASTERN).strftime("%b %d, %Y") if d else "date unknown"


def build_digest(matches, low, statuses, matcher, heartbeat=False):
    total = len(matches) + len(low)
    failed = [s for s in statuses if not s.ok]
    html_parts = [
        "<div style='font-family:Arial,Helvetica,sans-serif;max-width:720px;color:#222'>",
        "<h2 style='margin-bottom:4px'>Chatham Park grocery watch</h2>",
    ]
    text_parts = ["Chatham Park grocery watch", ""]
    if heartbeat:
        msg = "No new mentions since the last email. The watcher is running normally."
        html_parts.append(f"<p>{msg}</p>")
        text_parts += [msg, ""]

    def section(title, rows):
        if not rows:
            return
        html_parts.append(f"<h3 style='border-bottom:1px solid #ddd;padding-bottom:4px'>{html.escape(title)}</h3>")
        text_parts.extend([title, "=" * len(title)])
        for m in rows:
            it = m.item
            hits = ", ".join(m.location_hits + m.grocery_hits)
            html_parts.append(
                "<div style='margin:0 0 18px 0'>"
                f"<div style='font-size:16px'><a href='{html.escape(it.link)}'>{html.escape(it.title)}</a></div>"
                f"<div style='color:#666;font-size:13px'>{html.escape(it.source)} &middot; {fmt_date(it.published)}"
                f" &middot; matched: {html.escape(hits)}</div>"
            )
            for s in m.snippets:
                html_parts.append(
                    "<div style='background:#f6f6f6;border-left:3px solid #2a7;padding:6px 10px;margin-top:6px;"
                    f"font-size:14px'>{matcher.highlight_html(s)}</div>"
                )
            html_parts.append("</div>")
            text_parts.extend([it.title, f"{it.source} | {fmt_date(it.published)} | matched: {hits}", it.link])
            text_parts.extend(f"  > {matcher.highlight_text(s)}" for s in m.snippets)
            text_parts.append("")

    section(f"New mentions ({len(matches)})", matches)
    section(f"Lower priority: existing Lowes Foods / Northwood Landing ({len(low)})", low)

    ok = sum(1 for s in statuses if s.ok)
    health = f"Sources checked: {ok} of {len(statuses)} working."
    html_parts.append(f"<p style='color:#666;font-size:12px;margin-top:24px'>{health}</p>")
    text_parts.append(health)
    if failed:
        html_parts.append("<ul style='color:#a33;font-size:12px'>")
        for s in failed:
            html_parts.append(f"<li>{html.escape(s.name)}: {html.escape(s.detail[:300])}</li>")
            text_parts.append(f"  FAILED {s.name}: {s.detail[:300]}")
        html_parts.append("</ul>")
    html_parts.append("</div>")

    if heartbeat:
        subject = "no new mentions this week"
    else:
        subject = f"{total} new mention{'s' if total != 1 else ''}"
    return subject, "\n".join(html_parts), "\n".join(text_parts)


def send_email(cfg: dict, subject: str, html_body: str, text_body: str) -> None:
    ecfg = cfg.get("email", {}) or {}
    provider = (os.environ.get("EMAIL_PROVIDER") or ecfg.get("provider", "gmail")).lower()
    to = [a.strip() for a in os.environ.get("EMAIL_TO", "").split(",") if a.strip()]
    full_subject = f"{ecfg.get('subject_prefix', 'Chatham Park grocery watch')}: {subject}"
    if provider == "resend":
        key = os.environ.get("RESEND_API_KEY")
        sender = os.environ.get("EMAIL_FROM") or "Grocery Watch <onboarding@resend.dev>"
        if not key or not to:
            raise RuntimeError("Missing secret: RESEND_API_KEY and EMAIL_TO are required for Resend")
        resp = requests.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {key}"},
            json={"from": sender, "to": to, "subject": full_subject, "html": html_body, "text": text_body},
            timeout=TIMEOUT,
        )
        if resp.status_code >= 300:
            raise RuntimeError(f"Resend rejected the email: {resp.status_code} {resp.text[:300]}")
        return
    user, password = os.environ.get("SMTP_USER"), os.environ.get("SMTP_PASSWORD")
    if not user or not password:
        raise RuntimeError("Missing secret: SMTP_USER and SMTP_PASSWORD are required for Gmail")
    to = to or [user]
    msg = EmailMessage()
    msg["Subject"] = full_subject
    msg["From"] = os.environ.get("EMAIL_FROM") or user
    msg["To"] = ", ".join(to)
    msg.set_content(text_body)
    msg.add_alternative(html_body, subtype="html")
    host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    port = int(os.environ.get("SMTP_PORT", "465"))
    with smtplib.SMTP_SSL(host, port, timeout=TIMEOUT) as smtp:
        smtp.login(user, password.replace(" ", ""))
        smtp.send_message(msg)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def collect(cfg, state, session):
    statuses: list[SourceStatus] = []
    items: list[Item] = []
    for fetcher in (fetch_google_news, fetch_local_feeds):
        try:
            items += fetcher(session, cfg, statuses)
        except Exception as e:  # noqa: BLE001
            log.exception("Source group failed: %s", fetcher.__name__)
            statuses.append(SourceStatus(fetcher.__name__, False, str(e)))
    try:
        items += fetch_agendas(session, cfg, state, statuses)
    except Exception as e:  # noqa: BLE001
        log.exception("Town agendas failed")
        statuses.append(SourceStatus("Town of Pittsboro agendas", False, str(e)))
    return items, statuses


def find_new_matches(items, cfg, state, matcher):
    max_age = int(cfg.get("max_age_days", 90))
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age)
    seen = state.setdefault("sent", {})
    high, low, batch_keys = [], [], set()
    for it in items:
        if it.kind == "news" and it.published and it.published < cutoff:
            continue
        m = matcher.match(it)
        if not m:
            continue
        m.keys = item_keys(m)
        if any(k in seen or k in batch_keys for k in m.keys):
            continue
        batch_keys.update(m.keys)
        (low if m.low_priority else high).append(m)
    order = lambda m: m.item.published or datetime.min.replace(tzinfo=timezone.utc)  # noqa: E731
    return sorted(high, key=order, reverse=True), sorted(low, key=order, reverse=True)


def remember(state, matches, status):
    now = datetime.now(EASTERN).date().isoformat()
    for m in matches:
        for k in m.keys:
            state["sent"][k] = {"title": m.item.title[:200], "link": m.item.link, "date": now, "status": status}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="print matches; send nothing, remember nothing")
    ap.add_argument("--check-sources", action="store_true", help="report which sources work, then stop")
    ap.add_argument("--test-email", action="store_true", help="send a test email, then stop")
    ap.add_argument("--config", default=str(HERE / "config.yaml"))
    ap.add_argument("--state", default=str(HERE / "seen.json"))
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    cfg = yaml.safe_load(Path(args.config).read_text()) or {}
    state_path = Path(args.state)
    state = load_state(state_path)
    matcher = Matcher(cfg)

    if args.test_email:
        send_email(cfg, "test email", "<p>Your Chatham Park grocery watcher can send email.</p>",
                   "Your Chatham Park grocery watcher can send email.")
        log.info("Test email sent.")
        return 0

    items, statuses = collect(cfg, state, make_session())
    for s in statuses:
        log.info("%s %s: %s (%d items)", "OK  " if s.ok else "FAIL", s.name, s.detail, s.items)
    working = [s for s in statuses if s.ok]
    if args.check_sources:
        print(f"\n{len(working)} of {len(statuses)} sources working, {len(items)} items fetched.")
        return 0 if working else 1
    if not working:
        log.error("Every source failed. Nothing was checked.")
        return 1

    high, low = find_new_matches(items, cfg, state, matcher)
    log.info("%d items checked: %d new matches, %d lower priority", len(items), len(high), len(low))

    ecfg = cfg.get("email", {}) or {}
    today = datetime.now(EASTERN).date()
    heartbeat_due = (
        not high and ecfg.get("weekly_heartbeat", False)
        and today.strftime("%A").lower() == str(ecfg.get("heartbeat_day", "Monday")).lower()
        and state.get("last_heartbeat") != today.isoformat()
    )
    # Lower-priority items never trigger an email alone. They wait and ride
    # along with the next real digest or the weekly heartbeat.
    pending_low = state.get("pending_low", [])

    if args.dry_run:
        subject, _, text_body = build_digest(high, low, statuses, matcher, heartbeat=not high)
        print("\n" + "=" * 70)
        print(f"DRY RUN. Would send: {'yes' if high else ('heartbeat' if heartbeat_due else 'no email')}")
        print(f"Subject: {ecfg.get('subject_prefix', 'Chatham Park grocery watch')}: {subject}")
        print("=" * 70)
        print(text_body)
        return 0

    if high or heartbeat_due:
        low_rows = low + [_pending_to_match(p) for p in pending_low]
        subject, html_body, text_body = build_digest(high, low_rows, statuses, matcher, heartbeat=not high)
        send_email(cfg, subject, html_body, text_body)
        log.info("Email sent: %s", subject)
        remember(state, high + low, "sent")
        state["pending_low"] = []
        if heartbeat_due:
            state["last_heartbeat"] = today.isoformat()
    else:
        log.info("Nothing new to send.")
        remember(state, low, "held")
        state["pending_low"] = pending_low + [
            {"title": m.item.title, "link": m.item.link, "source": m.item.source,
             "published": m.item.published.isoformat() if m.item.published else None,
             "snippet": m.snippets[0] if m.snippets else "", "hits": m.location_hits + m.grocery_hits}
            for m in low
        ][-50:]
    state["last_run"] = datetime.now(EASTERN).isoformat(timespec="seconds")
    save_state(state_path, state)
    if len(working) < len(statuses):
        print(f"::warning::{len(statuses) - len(working)} source(s) failed; see the log above.")
    return 0


def _pending_to_match(p: dict) -> Match:
    published = datetime.fromisoformat(p["published"]) if p.get("published") else None
    item = Item(p["title"], p["link"], p.get("source", ""), published, "")
    hits = p.get("hits", [])
    return Match(item, hits, [], True, [p.get("snippet", "")])


if __name__ == "__main__":
    sys.exit(main())
