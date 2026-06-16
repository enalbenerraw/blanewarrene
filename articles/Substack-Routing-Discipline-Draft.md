# Connectors Are the Easy Part

*The durable advantage in working across AI surfaces is not wiring. It is deciding where every fact belongs.*

Most people wiring an AI assistant into their work stop at the same place: "I connected Notion to Claude." That move is real, it is useful, and it is one search away. There are a dozen tutorials for it, and the number grows every month. It is also not the part that matters.

The part that matters showed up the moment I was working across three Claude surfaces at once. Chat for thinking and drafting, including from my phone. Cowork for acting on my desktop and local files, a capability that only became real in early 2026. Code for building and shipping durable assets. Each surface was capable on its own. Together they had a quiet problem: each one forgot what the others knew. The fix was not another connector. It was a decision, repeated for every fact I cared about, about where that fact should live.

I have come to think of it as a routing discipline. It is the most useful operating habit I have built in the last year, and you can stand it up without writing a line of integration code.

---

## Three Surfaces, Three Jobs

Each Claude surface is good at a different kind of work, and the differences are the point.

**Chat** is where thinking happens. Reasoning through a decision, drafting, asking the dumb question safely, doing it from a laptop or a phone in a hallway between meetings.

**Cowork** is the agent that acts. It reads and writes my local files, drives desktop applications, and runs multi-step tasks where the work lives. It meets the work on my machine instead of asking me to copy the work into a chat window.

**Code** is where I build things meant to last. Plugins, tools, sites, the assets I ship and maintain over months, not the throwaway output of a single session.

The friction is that each surface has its own model of memory, and they do not fully share. Native memory syncs across Chat, Desktop, and Mobile when I am signed in. Code reads instructions from local files that the web surfaces cannot see. So a preference I taught one surface was invisible to another, and a project status I updated in one place went stale everywhere else. I want to name that gap plainly, because it is the reason the rest of this matters. The surfaces are not yet one seamless brain. You have to give them a shared spine, and you have to decide what hangs on it.

---

## The Insight: Route, Do Not Hoard

The obvious move is to build one universal memory that holds everything. Pour every fact, preference, and project note into a single store and let every surface read it.

That fails in a specific way. The store bloats. It goes stale because nobody maintains a junk drawer. And worst of all, it leaks the wrong context into the wrong place, putting personal notes in front of a work task or shipping half-formed code conventions into a strategy conversation.

The better model is to treat context like an editor, not a hoarder. Every durable fact has exactly one correct home, and the home is determined by a single question: who needs to see this?

That question resolves into three tiers.

**Code-only facts go to the repo.** Build conventions, release steps, the architecture of a specific project. These live with the work and are meant to die with it. They have no business traveling to my phone, and they would only add noise to a strategy chat.

**How-I-work facts go to a global instructions layer.** My standing preferences for how any project should be handled: tone, autonomy, what "done" means to me. These are portable across every project but local to the tool that reads them. They are about me as an operator, not about any one piece of work.

**Portable, cross-surface facts go to the hub.** Anything I want reachable from every screen I use, anything that represents a durable decision or a current status, anything I might need from my phone. This is the universal layer, and in my setup it is a single Notion page reachable from every surface through the connector.

The discipline is not the setup. The setup takes an afternoon. The discipline is the maintenance: when a durable decision or a project status changes, the hub gets updated, so the web and mobile surfaces stay current instead of confidently telling me something that stopped being true last week.

---

## The Hub in Practice

The Context Hub is deliberately boring. It is one Notion page, reachable from Chat, Cowork, web, and mobile through the connector. It is human-readable, durable, and portable, which is exactly why it works as the shared spine the surfaces lack on their own.

Walk one fact through it. Say a project moves from "drafting" to "in review." I update that status in the hub, once. The next time I am in Chat on my phone and ask where things stand, the connector reads the current state and answers correctly. When Cowork picks up the related files on my desktop, it is working from the same truth. I did not sync anything by hand across three tools. I updated one home and let the surfaces read from it.

Why Notion specifically, rather than a purpose-built AI memory product? Because the requirements are unglamorous and Notion already meets them. It is readable by a human, so I can audit and edit it directly. It is durable, so it outlives any single session. And it is reachable by the connector across every surface, which is the precise workaround for the memory gap I named earlier. The web and mobile surfaces cannot see my local files, but they can see the hub.

> **Sidebar: how it is actually wired**
>
> Three layers, each with one job. The repo layer is a `CLAUDE.md` file checked into each project, holding that project's conventions, read by Code at session start. The global layer is a single `CLAUDE.md` in my home directory, holding my cross-project working preferences, also read by Code. The hub layer is one Notion page exposed to Chat, Cowork, and the web and mobile apps through the Notion connector. The routing rule is the glue: a fact lands in exactly one layer based on who needs to read it, and the hub is the only layer every surface can reach. No custom memory service, no vector database, no integration code. The work is the routing decision, repeated.

---

## Proof: Projects That Span the Ecosystem

The test of an operating system is whether it holds up across genuinely different work. A few of mine sit on different legs of the span.

**Product in Acquisitions OS, which I build and ship in Code.** It packages the 90-Day Product Integration Framework as a working operating system for product leaders running post-acquisition integrations, versioned and released like real software. Its conventions, release steps, and structure live in the repo, where they belong, and nowhere else. This is the durable-asset leg: deep, project-bound work that has no reason to travel.

**Notes2Notion, the bridging tools that move my notes into the hub.** I built small tools that carry knowledge from Apple Notes into Notion. That is the inbound side of the hub, the plumbing that keeps the shared spine current without manual copying. It is also a reminder that the hub is not just something the surfaces read. It is something the rest of my system feeds.

**A Zone 8a gardening site that has nothing to do with work.** A public site I run on the side. It matters here precisely because it is personal. The routing rule is what keeps personal data out of the public work and out of professional contexts where it does not belong. The discipline is not only about getting the right context to the right place. It is about keeping the wrong context out.

None of these required a custom memory product or a clever integration. Each one required the same small decision, made consistently: where does this fact belong?

---

## Steal This

You do not need my projects or my exact tools to run this. You need a spine and three rules.

Start with one question, asked of any fact worth keeping: does this die with the project, travel with me as an operator, or need to reach every screen I use? Those three answers are your three homes.

Then build the minimum, and you can do it inside a week.

Day one: create the hub. One page on whatever platform you already trust and can reach from every device, and connect it to the surfaces you actually use. Day two: write your three routing rules down, in plain language, where you will see them. Until they are written they are not rules, they are intentions. Day three through five: stop seeding, start routing. As real facts come up in your normal work, send each one to its home, and notice which ones you reach for from your phone. Those are your truest hub candidates. End of the week: do one cleanup pass. Move anything that landed in the wrong tier, and delete anything that turned out not to matter.

A few things not to do. Do not automate capture before you have decided routing, or you will faithfully archive a mess. Do not put project-bound facts in the hub, or it becomes the junk drawer that nobody maintains. And do not let the hub go stale, because a shared spine that lies is worse than no spine at all.

---

## The Advantage Is the Discipline

The connectors are commodity, and they are getting more so by the month. Anyone can wire Notion to an assistant this afternoon. That is not where the advantage lives.

The advantage is the discipline of routing context to where it belongs, so the right surface knows the right thing at the right moment, and the wrong context stays out of the room. It is a small habit, and it compounds. Over a quarter it is the difference between fighting your tools and running on them.

You do not need a budget or an engineering team to start. You need a spine, three rules, and the willingness to answer one question every time something durable comes up: where does this belong?

---

*Want the full Product in Acquisitions OS as an installable Claude plugin? It is this same routing discipline applied to one hard problem: keeping an acquired product team and roadmap coherent through the first 90 days. Premium subscribers get the working plugin, not a PDF. Subscribe to Substack Premium to install it.*

---

*Blane Warrene is an AI-forward product and operations executive with 20-plus years in wealthtech, compliance technology, and SaaS. He writes on business operating systems, the next decade of SMB SaaS, and building AI-native organizations.*
