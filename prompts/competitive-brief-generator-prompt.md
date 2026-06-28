# Competitive Brief Generator

A reusable prompt that turns a company name and URL into a three-page competitive intelligence brief, rendered as a styled HTML document (and PDF where a code environment is available). Built for high-stakes commercial conversations: interviews, partnership and BD calls, board prep, and sales discovery.

You give it two inputs. It researches the company and its rivals, fact-checks the load-bearing numbers, and produces a single visual deliverable in a consistent house style.

Built by Blane Warrene. blanewarrene.substack.com

## What you get

A three-page brief:

1. **Competitive Landscape**. The market dynamic, a landscape map of six to eight rivals with what matters about each, the company's position, three threats, three counter-moves, five reads for the conversation, and three ranked closing questions.
2. **Product Catalog**. The product and module set organized by buyer center, packaging and platform layer, the "suite claim" decoded, and a strategic read.
3. **Battle Card**. A three-column win/qualify/route-around card (only-us, table stakes, visible gaps) plus conversation framing.

## How to use

Paste the prompt below into Claude, replacing the bracketed inputs. If you are running in an environment with code execution (Claude with tools, or Cowork), it will also render a PDF. Otherwise you get a self-contained HTML file you can open or print to PDF yourself.

## Inputs

- `[[COMPANY_NAME]]` the company the brief is about
- `[[COMPANY_URL]]` the company's primary website
- `[[AUDIENCE_CONTEXT]]` optional. Who the brief is for and the nature of the conversation, for example "practitioner-peer technology diligence call" or "sales discovery with a CFO buyer." Calibrates tone and the closing questions.
- `[[PREPARED_FOR]]` optional. Name for the footer.

---

## The prompt

You are a product-marketing and competitive-strategy lead preparing a board-grade competitive brief. Produce a three-page visual brief on the company below, in the exact structure and house style specified.

Inputs:
- Company: `[[COMPANY_NAME]]`
- Company URL: `[[COMPANY_URL]]`
- Audience and conversation context: `[[AUDIENCE_CONTEXT]]` (if blank, write a neutral executive brief)
- Prepared for: `[[PREPARED_FOR]]` (if blank, omit the name)
- Date: use today's date

### Step 1. Research before writing

Run multi-pass research. Do not write from memory alone.

1. Fetch the company URL. Extract the actual products, modules, editions or tiers, positioning language, and any recent launches or acquisitions.
2. Identify six to eight real competitors. For each, search for what is current: funding or revenue, M&A, analyst placements (Gartner, Forrester, IDC), product and AI or agentic announcements, and leadership changes. Search each competitor separately rather than batching.
3. Verify every load-bearing number before it goes in the brief: revenue, growth rate, ROI claims, customer counts, dates, coverage figures. If you cannot confirm a figure from a credible source, label it directional rather than asserting it, or leave it out.
4. Note who leads on what (the AI or agentic narrative, platform gravity, mid-market velocity, a specific vertical) so the landscape map reflects the real competitive shape.

### Step 2. Editorial rules

- Open every page with a BLUF (bottom line up front) block stating the conclusion first.
- Write in a direct board and C-suite voice. State conclusions. No generic best-practice filler.
- Do not use em dashes anywhere. Use periods, commas, or semicolons.
- Calibrate confidence. Flag anything you could not verify as directional. Never invent a source or attribution.
- Paraphrase your sources. Do not reproduce source text.
- Rank the closing questions by leverage, with the sharpest last.

### Step 3. Structure (three pages)

**Page 1, Competitive Landscape.**
- Meta line: "Competitive Landscape · [audience] Prep · Confidential" on the left, "Refreshed · [date]" on the right.
- H1: "[Company] Competitive Landscape".
- BLUF (dark block): four to six sentences naming the market dynamic, the leading rivals with a one-line significance each, the company's differentiated counter, and the central strategic question the conversation will probe.
- Landscape Map table, columns: Player, Tier (a short italic descriptor such as "narrative leader," "platform gravity," "mid-market velocity," "legacy / secondary"), What Matters Now.
- A one-line company position statement below the table.
- Three Threats, numbered, each a bold lead plus one or two sentences.
- Three Counter-Moves, numbered, same format.
- Five Reads For The Call, as highlighted callout blocks.
- Closing Questions, three, ranked, the last the highest leverage.
- Footer: "Prepared for [name] · [date] · Page 1 of 3" plus a short italic pull-quote.

**Page 2, Product Catalog.**
- Meta line and H1 "[Company] Product Catalog".
- BLUF: the count of products or modules, how they are packaged into editions or tiers, and the coherence or rationalization question that follows from breadth.
- Catalog by Buyer Center table, columns: Buyer Center, Buyer, Modules.
- Packaging and Platform Layer: a short paragraph on editions, bundles, and the shared platform capabilities.
- The Suite Claim Decoded table, columns: Component, Stands For, What It Does / Who Buys.
- Strategic Read, three numbered points, including the probes a sharp counterpart would ask.
- Footer with page number and pull-quote.

**Page 3, Battle Card.**
- Meta line and H1 "[Company] Battle Card".
- BLUF: how to read the card. Win from the left column. Qualify on the middle (table stakes are where deals are lost, not won). Route around the right.
- A three-column grid:
  - "ONLY [COMPANY]" with a green header: the genuine differentiators.
  - "TABLE STAKES (EVERYONE)" with a gray header: parity capabilities every rival has.
  - "VISIBLE [COMPANY] GAPS" with a red header: where the company is exposed.
  - Each item is a bold label plus a short sub-line.
- Conversation Framing, three numbered points on how to present gaps and probe for real data.
- Footer with page number and pull-quote.

### Step 4. Output

Produce one self-contained HTML file. All CSS inline in a `<style>` block, fonts via Google Fonts `@import`, three `.page` cards separated by page breaks. Use the House Style stylesheet below verbatim so the look is consistent across briefs.

If a code execution environment is available, also render the HTML to PDF at Letter size, portrait, with backgrounds enabled, using headless Chromium (for example Playwright: load the file with `page.goto("file://...")`, `page.wait_for_load_state("networkidle")`, then `page.pdf(print_background=True, format="Letter")`). If no code environment is available, deliver the HTML only and note that the user can print to PDF.

### House Style (use this stylesheet verbatim)

```css
:root {
  --ink: #14110F;
  --ink-soft: #4A4540;
  --ink-mute: #7A736C;
  --paper: #FAF7F2;
  --line: #D8D2C8;
  --accent: #7B2D26;
  --accent-soft: #F2E6E2;
  --highlight: #E8DDC9;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body {
  background: #ECE7DD;
  font-family: 'Inter Tight', sans-serif;
  color: var(--ink);
  font-size: 12px;
  line-height: 1.35;
  -webkit-font-smoothing: antialiased;
}
.page {
  max-width: 760px; margin: 20px auto; background: var(--paper);
  padding: 22px 28px 18px 28px; box-shadow: 0 2px 24px rgba(20,17,15,0.08);
}
.meta {
  display: flex; justify-content: space-between; align-items: baseline;
  font-size: 9px; text-transform: uppercase; letter-spacing: 0.14em;
  color: var(--ink-mute); border-bottom: 1px solid var(--line);
  padding-bottom: 6px; margin-bottom: 10px;
}
.meta strong { color: var(--accent); font-weight: 600; }
h1 { font-family: 'Fraunces', serif; font-weight: 600; font-size: 24px; line-height: 1.05; letter-spacing: -0.01em; }
.bluf { background: #14110F; color: var(--paper); padding: 9px 13px; margin-top: 9px; font-size: 11px; line-height: 1.45; }
.bluf strong { color: var(--highlight); }
h2 {
  font-family: 'Fraunces', serif; font-size: 10px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.18em; color: var(--accent);
  border-bottom: 1px solid var(--accent); padding-bottom: 2px; margin: 12px 0 6px 0;
}
table { width: 100%; border-collapse: collapse; font-size: 10.5px; }
th {
  text-align: left; font-size: 8.5px; text-transform: uppercase; letter-spacing: 0.1em;
  color: var(--ink-mute); font-weight: 600; padding: 3px 6px 3px 0; border-bottom: 1px solid var(--line);
}
td { padding: 4px 6px 4px 0; border-bottom: 1px dotted var(--line); vertical-align: top; line-height: 1.35; }
td.name { font-weight: 600; white-space: nowrap; color: var(--ink); }
td.tier { font-family: 'Fraunces', serif; font-style: italic; font-size: 9.5px; color: var(--accent); white-space: nowrap; }
.twocol { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.item { display: grid; grid-template-columns: 18px 1fr; gap: 6px; margin-bottom: 6px; font-size: 10.5px; line-height: 1.4; }
.item .num {
  font-family: 'Fraunces', serif; font-weight: 700; color: var(--paper); background: var(--accent);
  width: 16px; height: 16px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 9.5px;
}
.item .body span { color: var(--ink-soft); }
.talk { background: var(--highlight); border-left: 3px solid var(--accent); padding: 8px 11px; margin-bottom: 5px; font-size: 10.5px; line-height: 1.4; }
.qs .q { display: grid; grid-template-columns: 14px 1fr; gap: 5px; padding: 5px 0; border-top: 1px solid var(--line); font-size: 10.5px; line-height: 1.4; }
.qs .q:first-child { border-top: none; }
.qs .qmark { font-family: 'Fraunces', serif; font-style: italic; font-weight: 600; color: var(--accent); font-size: 13px; line-height: 1; }
footer {
  margin-top: 12px; padding-top: 6px; border-top: 1px solid var(--line);
  display: flex; justify-content: space-between; font-size: 9px; text-transform: uppercase; letter-spacing: 0.12em; color: var(--ink-mute);
}
footer .pull { font-family: 'Fraunces', serif; font-style: italic; text-transform: none; letter-spacing: 0; color: var(--accent); font-size: 10.5px; }
.pagebreak { margin-top: 24px; }
.bc-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 12px; }
.bc-head { font-family: 'Fraunces', serif; font-size: 9.5px; font-weight: 700; letter-spacing: 0.14em; padding: 5px 8px; margin-bottom: 6px; color: var(--paper); text-align: center; }
.bc-green { background: #2D5A2D; }
.bc-gray { background: #7A736C; }
.bc-red { background: #7B2D26; }
.bc-item { padding: 5px 2px; border-bottom: 1px dotted var(--line); font-size: 10px; line-height: 1.35; }
.bc-item:last-child { border-bottom: none; }
.bc-item strong { display: block; font-weight: 600; color: var(--ink); }
.bc-item span { color: var(--ink-soft); font-size: 9.5px; }
@media print {
  html, body { background: white; font-size: 10px; }
  .page { box-shadow: none; margin: 0; max-width: 100%; padding: 0; }
  h1 { font-size: 19px; }
  .bluf { font-size: 9.5px; padding: 7px 11px; margin-top: 7px; }
  table { font-size: 9px; }
  .item, .talk, .qs .q { font-size: 9px; }
  .pagebreak { page-break-before: always; }
  @page { size: letter portrait; margin: 0.3in; }
}
```

Fonts to import in the HTML head:

```
https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter+Tight:wght@400;500;600;700&display=swap
```

---

## Notes and customization

- The color system is a warm paper-and-oxblood palette. To re-skin, change the CSS variables (`--accent` is the primary accent) and the three battle-card header colors.
- The brief is intentionally three pages. For a shorter version, drop page 2 and keep landscape plus battle card.
- The research quality depends on web access. Without it, the model will write from training data, which goes stale fast for funding, analyst placements, and product launches. Keep the verification and directional-flagging rule.
- License and attribution are your call.
