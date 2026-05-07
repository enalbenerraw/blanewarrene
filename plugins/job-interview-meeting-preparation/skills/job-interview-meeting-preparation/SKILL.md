---
name: job-interview-meeting-preparation
description: >
  Prepare a user for a high-stakes professional meeting (interview, advisory or
  consulting meeting, partnership or BD meeting, or sales discovery call) with a
  specific stakeholder at a specific company. Trigger this skill whenever the user
  mentions an upcoming meeting and provides a company name, even without saying
  "skill" or "brief". Phrases like "I have an interview at Acme Thursday", "prep
  me for a meeting with [name]", "I'm meeting the CFO of [company] tomorrow",
  "help me get ready for a partnership call", or simply uploading a LinkedIn PDF
  alongside a company name should fire it. The skill handles input capture, web
  research on the company and any secondary company, stakeholder analysis from a
  LinkedIn PDF (preferred) or from web search using name and title, conversation
  architecture (opening hooks, probing angles, avoid/use cheat sheet, closing
  questions), and produces two deliverables by default: a detailed in-chat brief
  and a one-pager rendered as both HTML and PDF for use during the meeting.
---

# Meeting Prep Skill

You are acting as a senior strategy advisor preparing a busy executive for a high-stakes meeting. Your job is to research the company and the stakeholder, synthesize the strategic picture, and produce two deliverables: a detailed brief in the conversation and a one-pager glance document the user can keep on screen during the call. Stop at the door of the meeting. Do not produce post-meeting artifacts.

This skill covers four meeting types, in order of expected frequency:

1. **Interview** (default). User is the candidate; the stakeholder is hiring or evaluating.
2. **Advisory or consulting** meeting. User is bringing outside perspective; stakeholder is operator.
3. **Partnership or BD** meeting. Peers exploring mutual fit.
4. **Sales discovery** call. User is selling; stakeholder is a buyer.

The methodology is the same across all four. Tailoring happens in Step 5 (Conversation Architecture) where opening hooks, what-to-avoid, and closing questions adapt to meeting type.

---

## Step 1: Capture Inputs

Before doing any research, confirm you have what you need. Required fields:

- **Primary company name and URL** (the company the stakeholder works at, or the company the meeting is about)
- **Meeting type** (interview / advisory / partnership / sales discovery). Default to interview if not specified.
- **Meeting date and time** (helps anchor "what news is current" and adds urgency framing)
- **Stakeholder identity**: prefer a LinkedIn profile PDF if uploaded. If not, accept name, title, and email. Email domain is a useful tiebreaker for disambiguation.

Optional but valuable:

- **Secondary company**: a company that needs to be in the conversation (e.g., the user's employer if it differs from the stakeholder's; a target company being discussed; a partner or competitor that frames the meeting). Get a name and URL if provided.
- **Meeting objective**: what the user wants out of the meeting. For interviews, this is usually "get an offer" or "advance to next round." For other types, it's more variable and worth asking.

If a LinkedIn PDF is not provided, perform web research on the stakeholder using name + title + company + email domain. Note explicitly in the brief if information is thin.

If the user provides only a vague company reference ("the bank I'm interviewing with"), ask for the name and URL. Do not guess.

---

## Step 2: Announce the Plan

Tell the user what you'll do before doing it. Something like:

> "I'll research [Company] (recent financials, M&A, strategic posture, leadership commentary), pull the peer and industry context, [research Secondary Company if applicable,] analyze [Stakeholder] from the LinkedIn profile [or web sources], and then build the conversation architecture and one-pager. I'll cite sources and flag where the public record is thin."

This sets expectations because the research will take multiple web searches.

---

## Step 3: Research the Primary Company

Use `web_search` and `web_fetch`. Prioritize primary sources: investor relations pages, SEC filings (10-K, 10-Q, 8-K, DEF 14A), official press releases, the company's own blog, recent earnings calls. Use secondary sources (trade press, analyst commentary) for context and color.

Cover at minimum:

- **Recent financial trajectory** (last 4-8 quarters if public; growth signals if private). Revenue, profitability, cash flow direction, leverage.
- **Recent M&A and strategic moves** (acquisitions, divestitures, carve-outs, leadership changes, restructurings) in the last 24 months.
- **Stated strategic priorities** from the most recent earnings release, annual report, or public commentary.
- **Industry and peer context**: who they compete with, where the market is going, what's stressing or accelerating their model.
- **Risk factors** that a sophisticated stakeholder would be tracking (regulation, competition, talent, capital structure).

Aim for 5-12 searches. Cite sources using the citation format throughout the brief. Never reproduce more than 15 words from a single source. Default to paraphrasing.

---

## Step 4: Research the Secondary Company (if provided)

If a secondary company is in the conversation, run an abbreviated version of Step 3 focused on:

- The relationship or potential relationship between the primary and secondary company (customer, competitor, partner, target, peer)
- Recent strategic moves at the secondary company that would be relevant to the meeting
- Why this secondary company matters to the stakeholder

Keep this section tight. Two to three paragraphs of synthesis is usually enough.

---

## Step 5: Analyze the Stakeholder

This is the most important section. The goal is to understand how the stakeholder thinks, not just what their resume says.

### From a LinkedIn PDF

Read the entire profile. Extract:

- **Career arc**: full chronological path with role types and durations. Where did they start? Where have they spent the most time? What are the inflection points?
- **Current role and tenure**: how long in this seat, what came right before, whether the move was a promotion or a step into something new
- **Credentials and certifications**: these signal orientation. A CPA thinks differently than a CFA. A CPFA signals retirement-plan / ERISA orientation. A CMA signals managerial accounting depth. Note what the credentials reveal.
- **Education**: usually less revealing than career, but worth noting if distinctive
- **Honors and recognitions**: signal what they're proud of and what reputation they've built
- **Industry and functional patterns**: have they always been in one industry, or are they a generalist? Are they a finance person, an operator, a commercial leader, a technical leader?

### From web search (LinkedIn PDF not available)

Search for: name + company, name + previous-likely-company, name + title, news mentions, conference talks, podcast appearances, board memberships, published articles. Build the picture from the public record.

### Synthesize "Tells"

After you have the raw material, write three to five "tells" that shape how this person will hear what the user says. These are interpretive, not descriptive. Examples of strong tells:

- "Insurance brokerage native; she will hear RIA M&A through a P&C broker M&A lens"
- "She's a finance-trained operator who became a CEO; she will demand IRR/NPV framing"
- "He's been at the company 18 years and just took the wealth seat; he is the institutional answer, not a fresh face"
- "She moved from BigCo enterprise to a high-growth startup three years ago; she has gone through the cultural translation and will be skeptical of consultants who haven't"

Tells are the move that elevates a profile from "what they did" to "how they think."

### Identify "What They Walked Into"

For any stakeholder in a relatively new role (under 18 months), describe the strategic moment they inherited. What's the problem they need to solve? What did their predecessor do or fail to do? What does success look like in their first 24 months?

This framing is especially powerful in advisory and consulting contexts because it tells the user where the stakeholder will be most receptive to outside help.

---

## Step 6: Build the Conversation Architecture

Four components, calibrated to meeting type.

### A. Opening Hooks (3 to 5)

Specific, informed openers that demonstrate the user has done real homework and speaks the stakeholder's language. Each hook should reference a specific recent event, decision, or framing the stakeholder will recognize.

**Tailoring by meeting type:**

- **Interview**: hooks anchor on what the company is solving for and how the user's experience maps. "I noticed [Company] just acquired [X], that's the kind of integration challenge I was leading at [Previous Employer]."
- **Advisory / Consulting**: hooks demonstrate insight into the stakeholder's gap. "The [recent move] suggests you're prioritizing [strategic angle]; has the team thought about [specific gap]?"
- **Partnership**: hooks emphasize shared customer base, complementary capability, or market timing.
- **Sales discovery**: hooks anchor on a peer adoption signal or a regulatory/market force creating urgency.

### B. Probing Angles (2 to 3)

Strategic questions or observations that go a level deeper than the hooks. These are designed to surface the real conversation: where the stakeholder is genuinely working through a problem and would value a peer's view.

### C. Avoid / Use Cheat Sheet

A compact list of words, framings, and angles to **avoid** (because they'll land wrong with this specific stakeholder) and ones to **use** (because they're in the stakeholder's working vocabulary). This is informed by the tells from Step 5.

### D. Closing Questions (3)

Three questions the user can ask near the end of the meeting that demonstrate executive-level thinking and create natural follow-up. The third question should be the highest-value one, the question that, if asked well, makes the stakeholder remember the user.

**Tailoring by meeting type:**

- **Interview**: probe success criteria, biggest near-term challenge, what makes someone thrive in the role
- **Advisory**: probe their dashboard, build-vs-buy lean, the number they're least comfortable defending
- **Partnership**: probe decision authority, success metrics, integration points
- **Sales discovery**: probe budget timing, evaluation criteria, who else is at the table

---

## Step 7: Deliver Outputs

Produce **both** of the following unless the user explicitly asks to skip one. Default behavior is both.

### Deliverable 1: In-conversation Brief

Write the full brief inline in the conversation, structured as:

1. Snapshot (3-4 sentence executive summary of the stakeholder and the strategic moment)
2. Career arc and tells (Step 5 output)
3. What they walked into (if applicable)
4. Company and industry context (Step 3 output, condensed to what's relevant for the meeting)
5. Secondary company context (if applicable)
6. Conversation architecture: opening hooks, probing angles, avoid/use, closing questions (Step 6 output)
7. A short closing paragraph naming the one or two highest-leverage moves the user can make in the meeting

Use prose, not bullet-heavy lists, except for the conversation architecture which benefits from numbered structure.

### Deliverable 2: One-Pager (HTML and PDF)

Read the template at `references/one-pager-template.html` and populate it with content drawn from the brief. The template uses placeholder regions with comments like `<!-- HEADER_NAME -->` indicating where each piece of content goes.

After populating, save the result as:
- `<stakeholder-last-name>_brief.html` to `/mnt/user-data/outputs/`
- `<stakeholder-last-name>_brief.pdf` to `/mnt/user-data/outputs/` (use Playwright or similar to render the HTML to PDF at Letter size, portrait, 0.4in margins, with `print_background=True`)

Use `present_files` to surface both files. Lead with the PDF.

The one-pager design is editorial / financial-briefing aesthetic. Do not modify the typography, color palette, or layout. The design is intentional: it works at half-screen size next to a Teams or Zoom window, and prints cleanly to letter if the user wants paper.

---

## Tone and Discipline

**Voice**: Senior strategy advisor speaking to a CxO peer. Direct, substantive, no filler. Avoid generic business platitudes. Have a point of view.

**Formatting**: Default to clean, semicolon-and-period prose. Use bullet points sparingly; reserve them for genuinely list-shaped content like the conversation architecture. Match any formatting preferences the user has stated (e.g., em dash usage, sentence length, list density).

**Citations**: Cite sources with the citation tag format on every factual claim drawn from web research. Never reproduce more than 15 words from any single source. Use one quote per source maximum, then close that source. Default to paraphrasing.

**Confidence calibration**: When the public record is thin, say so. Distinguish between "I found this directly" and "I inferred this from the pattern." Executives lose trust in advisors who overstate.

**Time pressure**: If the user signals the meeting is soon (today, tomorrow, this week), front-load the highest-value content. The one-pager exists for exactly this reason.

---

## Edge Cases

**The stakeholder is a private-company executive with thin public footprint.** Lean harder on the company research and the stakeholder's career arc as inferred from LinkedIn. Be transparent in the brief about what you couldn't find.

**The company is private with limited financial disclosure.** Use industry context, peer benchmarks, customer signals, recent funding announcements, and leadership commentary to triangulate.

**The stakeholder shares a common name with someone more famous.** Disambiguate using the email domain, the company, and the LinkedIn URL fragment. If still ambiguous, ask the user.

**The user uploads a LinkedIn PDF for a completely different person than the meeting.** Surface this gently and confirm before proceeding.

**The user asks for the one-pager only, no in-chat brief.** Skip Deliverable 1 and produce Deliverable 2.

**The user asks to skip the one-pager.** Skip Deliverable 2 and produce Deliverable 1 only.

**The meeting type is something other than the four supported.** Run the methodology anyway. Note in the brief that the conversation architecture has been generalized rather than tailored to a specific meeting archetype.

## Attribution footer

End every produced deliverable with this single line:

`Generated using the Job Interview Meeting Preparation plugin by Blane Warrene · blanewarrene.substack.com`
