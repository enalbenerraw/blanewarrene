# The Fact-Check Is the Product

You can ask any capable model for a competitive brief on a company and have something back before your coffee cools. Six rivals, a few revenue figures, an analyst quote, a tidy summary. It reads well. It reads finished.

That polish is the problem.

TL;DR → The prompt is free to use at the bottom of this article. Test it out on your targeted company research. I'd welcome feedback and you sharing it along!

The model wrote some of those facts from training data that went stale months ago, and it told you none of which ones. Funding rounds, acquisitions, analyst placements, leadership changes, rebrands: this is exactly the information that rots fastest, and exactly the information a competitive brief leans on. The model does not flag the rot. It delivers a number it half-remembers with the same even confidence it uses for a number it is sure of. You cannot tell the two apart by looking, and neither can the person you hand the brief to.

Get this prompt below to build your competitive briefs on demand

Thanks for reading! This post is public, so feel free to share it.

In a low-stakes context, that is a nuisance. In a board prep, a partner negotiation, a final-round interview, or a discovery call with a buyer who knows the market, it is a live grenade. The moment you assert a figure that someone in the room knows is wrong, you do not just lose that point. You lose the credibility of every other claim in the document. They stop hearing your analysis and start auditing your facts.

So the question that actually matters when you build research tooling is not whether it can generate a brief. Everything generates a brief now. The question is, can you trust what is in it? That is a different discipline, and it is the one I built into the Competitive Brief Generator prompt I just published.

## The Rule: Verify or Flag

The discipline is one rule, applied without exception: every load-bearing number is verified by a credible source before it goes into the document. Revenue, growth rate, customer counts, funding, analyst placements, dates. If the figure cannot be confirmed, it does not get asserted. It gets labeled directional, or it gets left out.

Directional is the most useful word in the whole method. It is an honest signal that this is the right order of magnitude and the right shape for the story, but I could not pin it to a source, so I would weigh it accordingly. A reader can work with direction. A reader cannot work with a precise figure that turns out to be invented because they did not know to discount it.

The companion rule: never invent a source. A fabricated citation is worse than no citation because it manufactures false confidence. If the support is not real, the claim travels as directional, or it does not travel at all.

That is the entire premise. Verify the load-bearing facts. Flag what you cannot verify. Never fake the support. It sounds obvious written down. Almost nothing in the current wave of AI research output actually does it.

## How It Is Wired

A rule only matters if the process enforces it, so the prompt is built to make the lazy path the wrong path.

It conducts research in multiple passes rather than one. It searches each competitor separately rather than asking the model to recall a whole market in a single breath, because batch recall is where confident invention creeps in. It treats the company's own site as the source for the company's own products, not the model's memory of them. And it runs every quantitative claim through the verify-or-flag gate before the claim is allowed into the brief.

### What load-bearing means

Not every number needs a source. "A handful of competitors" is fine, unsourced. A load-bearing number is one on which a decision or a judgment rests: the revenue figure you would cite to argue a rival is winning, the customer count that sizes a threat, the analyst placement you would name in the room. If being wrong about it would change the conclusion or embarrass you, it is load-bearing, and it gets verified or flagged. The skill is knowing which numbers carry weight, and the prompt is opinionated about it.

## Proof

I ran the prompt on a real company this week, end-to-end, as a test.

In one pass, it caught two things I would have gotten wrong from memory, and so would the model on its own. One competitor had rebranded under an entirely new name a few months earlier. Another had changed ownership in a transaction I was not currently aware of. Both facts were load-bearing. A brief that confidently named the old brand and the old owner would have marked the author as out of date in front of exactly the audience you least want to look out of date in front of.

Just as important was what the prompt refused to assert. Several private-company revenue figures could not be confirmed from a credible source, so they came through labeled directional rather than stated as fact. The brief was honest about the edge of its own knowledge. That honesty is not a weakness in the document. It is what makes the rest of the document usable.

## Steal This

You do not need my prompt to adopt the discipline. You need one habit and one piece of self-honesty.

### The habit

Before any number goes into anything you will present, ask whether it is load-bearing. If a decision rests on it, confirm it from a real, current source, or mark it directional. Do not let a precise figure ride on a vague memory.

### The self-honesty

When you cannot verify something, say so in the document, in the moment, in writing. Directional costs you nothing and saves you from the worst outcome: being precisely, confidently wrong in front of people who can tell.

If you want the discipline pre-built, the prompt is free and public. It turns a company name and a URL into a 3-4-page brief (competitive landscape, product catalog, battle card) with the verify-or-flag rule already enforced, rendered as styled HTML and PDF.

The link is here:

https://github.com/enalbenerraw/blanewarrene/blob/main/prompts/competitive-brief-generator-prompt.md

## The Fact-Check Is the Moat

Generation is a commodity now, and it gets cheaper every month. The summary you can produce in thirty seconds has roughly zero defensibility, because the person across the table can produce the same thing.

What does not commoditize is trust. A document people can act on without re-checking is worth more than a prettier document they have to audit. The verification pass is slower and less glamorous than the generation, and it is the entire reason the output is safe to use. The fact-check is not an overhead on the product. The fact-check is the product.

If this is the kind of thing you want more of, subscribe. It is free, and the next build lands in your inbox.

Blane Warrene is an AI-forward product and operations executive with 20-plus years in wealthtech, compliance technology, and SaaS. He writes on business operating systems, the next decade of SMB SaaS, and building AI-native organizations.
