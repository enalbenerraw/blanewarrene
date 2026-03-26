# Morning News Brief — Claude Prompt

A daily automated prompt that searches the web for relevant news and delivers a concise, personalized morning brief. Designed for use with [Claude](https://claude.ai) (as a scheduled task in Cowork, or adapted for any LLM workflow).

## How It Works

Each morning, this prompt instructs Claude to:

1. Search for recent news across your specified topic areas
2. Summarize the most relevant stories
3. Suggest content opportunities (e.g., LinkedIn posts) tied to your existing themes
4. Flag when current news makes one of your drafts timely

## Setup

Before using this prompt, customize the placeholder variables below:

| Variable | Description | Example |
|---|---|---|
| `{{YOUR_NAME}}` | Your name | Jane Smith |
| `{{YOUR_ROLE}}` | Your professional role/title | VP of Product Marketing |
| `{{YOUR_LOCATION}}` | General location | San Francisco, CA |
| `{{DELIVERY_METHOD}}` | Where the brief should go | a Notion page, a markdown file, an email draft, etc. |
| `{{DELIVERY_DETAILS}}` | Specifics for delivery | Parent page ID, file path, etc. |
| `{{TOPIC_AREAS}}` | News topics relevant to you | See examples below |
| `{{CONTENT_THEMES}}` | Your recurring content themes | See examples below |
| `{{ARTICLES_LIST}}` | Your current drafts/articles in progress | See examples below |

## The Prompt

Copy everything below and customize the `{{ }}` placeholders.

---

```
You are creating a daily morning news brief for {{YOUR_NAME}}, a {{YOUR_ROLE}} based in {{YOUR_LOCATION}}. The brief should be delivered as {{DELIVERY_METHOD}}.

## Objective

Search the web for the latest news and create a brief titled "Morning Brief — [Today's Date]".
{{DELIVERY_DETAILS}}

## Steps

### 1. Search for news

Use web search to find 5–8 recent stories (past 24–48 hours) across these topic areas:

{{TOPIC_AREAS}}

### 2. Create the brief

Structure the output with these three sections:

**Section 1: News Worth Knowing**

List 3–5 of the most relevant stories. For each:
- Bold headline with source name in parentheses
- One-sentence summary of what happened and why it matters
- Link to the article

**Section 2: Content Opportunities**

Pick 1–2 stories from above that align with your existing content themes and suggest a post or article angle. Your key content themes are:

{{CONTENT_THEMES}}

For each opportunity, write:
- The story it ties to
- A suggested hook (1–2 sentences you could open with — direct, first-person, from the practitioner's perspective)
- Which of your existing articles or drafts it connects to, if any (reference by title)

**Section 3: Content Pipeline Nudge**

Review your current articles/drafts and note if any could be made timely by the day's news. Your current articles include:

{{ARTICLES_LIST}}

If a story creates a timely hook for one of these pieces, mention it briefly (e.g., "Today's news about X gives your '[Article Title]' draft a timely hook — consider publishing this week."). If nothing connects, skip this section.

### 3. Tone and style

Keep the brief concise and scannable. Use a direct, experienced tone — no fluff. The whole brief should take under 3 minutes to read.
```

---

## Example Customization

Here's an example of what the placeholder sections might look like filled in:

### Topic Areas Example

```
- **Product management & strategy**: product-led growth, roadmap prioritization, platform strategy
- **Marketing & positioning**: brand positioning, GTM strategy, competitive intelligence, product marketing trends
- **AI applied to business**: AI tools for productivity, AI in marketing/sales, enterprise AI adoption
- **Broader tech & business**: SaaS trends, fintech/regtech, enterprise software M&A, notable funding rounds
```

### Content Themes Example

```
- Post-acquisition product integration (merging roadmaps, positioning after M&A)
- AI as a practical GTM and competitive intelligence tool (applied use cases, not hype)
- Workplace productivity (meetings, time management, collaboration tools)
- Product positioning and messaging strategy
```

### Articles List Example

```
- "Why Product Integrations Fail In An Acquisition"
- "Turning AI into a Force Multiplier for Product Marketing"
- "Making Meetings Matter"
```

## Usage Notes

- **With Claude Cowork (scheduled task):** Use this prompt directly when creating a scheduled task. Set a cron schedule like `0 7 * * 1-5` for weekday mornings at 7 AM.
- **With Claude.ai:** Paste the customized prompt into a conversation each morning, or save it as a Project prompt.
- **With the Claude API:** Use this as a system or user prompt in an automated pipeline.
- **With other LLMs:** The prompt is model-agnostic — adapt as needed for your preferred tool.

## License

MIT — use, modify, and share freely.