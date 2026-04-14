# Pre-Call Briefing

A reusable Claude prompt that produces executive-grade pre-call briefings on a target company. Built for sales, BD, partnerships, and GTM teams who need to walk into a prospect, partner, or account call with a credible point of view.

Created by Blane Warrene. Licensed under MIT.

## What it does

Given a target company name and URL, the prompt guides Claude through a structured research and synthesis workflow:

1. Asks you a short set of clarifying questions so the briefing fits your actual use case.
2. Researches the company across its site, funding databases, leadership profiles, customer proof points, competitive landscape, and public messaging.
3. Synthesizes the findings as a product marketing executive would, not as a raw research dump.
4. Produces either a Word .docx briefing memo or a Markdown briefing, depending on your preference.
5. Closes with the single most important question to hold in mind during the call.

The prompt is tool-aware. On Claude surfaces with web search, web fetch, and file-creation tools (Claude.ai, Claude Code, Cowork), Claude will produce a finished .docx. On surfaces without those tools, Claude will produce a Markdown briefing inline.

## Repo contents

```
pre-call-briefing/
├── README.md              This file
├── pre-call-briefing.md   The prompt itself
├── CONTRIBUTING.md        Guidelines for extending or improving the prompt
└── LICENSE                MIT license
```

## Quick start

1. Open [`pre-call-briefing.md`](./pre-call-briefing.md).
2. Copy the prompt block (everything between the `BEGIN PROMPT` and `END PROMPT` markers).
3. Paste into Claude.
4. Provide the target company name and URL when prompted.
5. Answer the clarifying questions.
6. Receive the briefing.

## Example use cases

**Account executive prepping for a discovery call.** "I'm meeting with the CRO at Acme next Tuesday. Prep me for it."

**Partnerships lead evaluating a potential integration partner.** "Run a briefing on Beta Corp. I'm exploring an ISV partnership, so focus on their product roadmap signals and partner ecosystem."

**Customer success manager going into a QBR.** "Run a briefing on our customer Gamma Inc. Focus on leadership changes and recent public messaging shifts over the last 90 days."

**Product leader preparing for an interview.** "Run a briefing on Delta AI. I'm interviewing for their VP Product role. Focus on leadership, competitive positioning, and public messaging."

**Investor researcher screening an opportunity.** "Run a briefing on Epsilon Labs. Investor lens. Emphasize funding history, revenue signals, and competitive defensibility."

## Recommended surfaces

| Surface | Supports | Best for |
|---|---|---|
| Claude.ai web | Web search, .docx creation via artifacts | Quick, one-off briefings |
| Claude Code | Full tool access, repo integration | Version-controlling briefings into a team knowledge base |
| Cowork | Full tool access, native file output | Delivering a polished .docx to yourself or a colleague |
| Claude API | Programmatic, tool use optional | Automating briefings as part of a sales-ops workflow |

## Design principles

The prompt was built around four principles learned from executive briefing work:

1. **Clarifying questions up front.** Underspecified briefings waste the reader's time and miss the real question. The prompt forces a short interview before research begins.
2. **Synthesis over research dumps.** Every observation in the output must carry a one-sentence interpretation. Raw facts without a "so what" are not useful in a call.
3. **Structured source protocol.** The research sequence is explicit (company site, funding data, leadership, customers, competitors, messaging, risks) so the quality of the briefing does not depend on Claude's improvisation.
4. **A provocation at the end.** The briefing closes with the single most important question the reader should hold in their mind. No summary, no hedging.

## Quality bar

A briefing produced by this prompt should be strong enough to:

- Walk into a CxO-level meeting and hold a credible conversation without referring back.
- Identify at least two non-obvious insights the reader would not have surfaced on their own.
- Flag at least one risk or red flag that changes how the reader approaches the call.
- Provide a sharp question the reader can ask that signals they did real homework.

If a briefing does not meet that bar, the prompt needs improvement. See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Known limitations

- Briefing quality depends on the target company having a public footprint. Stealth-mode or pre-launch companies will produce thin briefings.
- The prompt does not access private data (CRM, internal notes, prior call transcripts). Pair it with your own context for best results.
- The 180-day messaging window is a default. For fast-moving companies, shorten it. For slow-moving enterprises, lengthen it.
- Claude's knowledge of recent events depends on the underlying model's training cutoff and tool access.

## License

MIT. See [`LICENSE`](./LICENSE).

## Feedback

If you use this prompt and find gaps, open a pull request or issue. The prompt improves through real usage patterns.
