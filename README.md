# Hello, I'm Blane Warrene

## What I Build
AI-forward product and operations systems: prompt recipes, Claude Code plugins, and small tools that automate product and product marketing workflows. Most of it starts as a workflow I run by hand, then gets packaged so someone else can run it too.

## What I'm Working On
- 🧩 Three Claude Code plugins shipping from one marketplace, versioned and released independently
- 🔌 A Chrome extension that captures meeting context and hands it off to the interview-prep plugin
- 📚 Prompt recipes for GTM intelligence, competitive briefs, and executive briefings
- 🤝 Simplifying how product managers build Claude Skills and Gemini Gems, and leverage GitHub and AI

## Claude Code Plugins

Three plugins ship from one marketplace. Add the marketplace once, then install whichever you want:

```bash
claude plugin marketplace add enalbenerraw/blanewarrene
claude plugin install product-in-acquisitions-os@blanewarrene-marketplace
claude plugin install job-interview-meeting-preparation@blanewarrene-marketplace
claude plugin install comparative-landscape-brief@blanewarrene-marketplace
```

Or from inside a Claude Code session, add the marketplace and browse:

```
/plugin marketplace add enalbenerraw/blanewarrene
```

Run `/reload-plugins` after installing or updating. Plugin changes do not take effect in a session that is already running.

| Plugin | What It Does |
|--------|-------------|
| [Product in Acquisitions OS](plugins/product-in-acquisitions-os/) | 90-Day Product Integration Framework as a working operating system for product leaders running post-acquisition integrations. Covers Week 0 readiness, roadmap convergence, positioning stability, and people integration. |
| [Job Interview Meeting Preparation](plugins/job-interview-meeting-preparation/) | Prep a candidate, advisor, or operator for a high-stakes meeting (interview, advisory, partnership, or sales discovery). Produces an in-chat brief and a printable HTML/PDF one-pager. |
| [Comparative Landscape Brief](plugins/comparative-landscape-brief/) | Produce a structured briefing document comparing 3 to 8 organizations, products, or initiatives for a third-party audience (investors, board, exec team, M&A committee, partner steering group). Includes a third-party verification pass on quantitative claims. |

Plugin privacy policy: [blanewarrene.com/plugins-privacy](https://blanewarrene.com/plugins-privacy/).

## Chrome Extension

| Extension | What It Does |
|-----------|-------------|
| [Meeting Prep Capture](extensions/meeting-prep-capture/) | Grabs a LinkedIn profile or company page, packages it into the input shape the Job Interview Meeting Preparation plugin expects, and copies a ready-to-paste handoff packet. Does no AI of its own. Manifest V3. |

## Featured Projects

| Project | What It Does | Stack | Updated |
|---------|-------------|-------|---------|
| [GTM Intel CLI](src/gtm_intel/) | Messaging analysis tool: analyze competitor, partner, and your own messaging | Python, Gemini, Google Sheets | 2026-03-26 |
| [Strategic GTM Intel](prompts/strategic-gtm-intel-prompt.md) | Competitive wedge analysis against your own GTM | Gemini, Claude Code | 2026-03-26 |
| [Competitive Brief Generator](prompts/competitive-brief-generator-prompt.md) | Turn a company name and URL into a three-page competitive brief (Landscape, Product Catalog, Battle Card) as styled HTML/PDF | Claude with web search | 2026-06-28 |
| [Signal Watch](prompts/signal-watch-instructions.md) | Executive briefing on any company's positioning, leadership, and market signals | Any LLM with web search | 2026-04-02 |
| [Morning News Brief](prompts/morning-news-brief-prompt.md) | Automated daily news brief with content opportunities tied to your themes | Any LLM with web search | 2026-03-26 |
| [LLM Memory Audit](prompts/llm-memory-audit-prompts.md) | Copy-paste prompt recipes to audit persistent memory and instructions in ChatGPT, Claude, Copilot, and Gemini | Any LLM | 2026-06-17 |
| [Teachable Course Builder](prompts/teachable-course-builder-prompt.md) | Generate an end-to-end, Teachable-ready free course on expert prompting for non-technical learners. [Copilot](prompts/teachable-course-builder-copilot.md) and [Gemini](prompts/teachable-course-builder-gemini.md) variants included | Claude, Copilot, Gemini | 2026-07-23 |
| [Built Courses](prompts/) | Two finished course outlines produced by the builder: [Inbox Mastery](prompts/course-inbox-mastery.md) (Claude in Gmail and Outlook) and [The AI Interview](prompts/course-the-ai-interview.md) | Claude | 2026-04-22 |
| [Pre-Call Briefing](pre-call-briefing/) | Executive-grade pre-call briefing on any target company for sales, BD, partnerships, and GTM teams | Claude with web search | 2026-04-14 |
| [Notes2Notion](Notes2Notion/) | Export Apple Notes to Notion-importable Markdown: CLI and native macOS GUI app | Python, AppleScript | 2026-06-10 |
| [AI SMB Toolkit](prompts/ai-smb-toolkit/) | Four Word documents that turn AI curiosity into a working plan: tech stack inventory, HR AI survey, prompt cookbook, and course builder | Word, prompt frameworks | 2026-07-09 |

## Elsewhere

Shipped surfaces that live outside this repo.

| Site | What It Is |
|------|-----------|
| [blanewarrene.com](https://blanewarrene.com) | Writing and the canonical home for everything here. Custom WordPress block theme, built for Core Web Vitals. |
| [blanewarrene.com/portfolio](https://blanewarrene.com/portfolio/) | Three-pillar showcase of the AI product work |
| [zone8a.com](https://zone8a.com) | Year-round USDA Zone 8a gardening guide. Astro static site on Cloudflare. [Source](https://github.com/enalbenerraw/zone-8a-garden) |
| [thedigitalwell.com](https://thedigitalwell.com) | Healthy-cooking articles and research, plus a voice-driven nutrition tracker |

## Connect
- 💼 [LinkedIn](https://www.linkedin.com/in/bwarrene)
- 📝 [Substack](https://blanewarrene.substack.com/)
- 📧 [Email](mailto:blane@blanewarrene.com)

---
*AI-forward product and operations executive who builds the operating systems that let B2B SaaS scale. Proven through seven acquisitions and two decades in wealthtech and compliance technology. Raleigh-Durham, NC.*
