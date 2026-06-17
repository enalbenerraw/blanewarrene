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

---

## Proof: Projects That Span the Ecosystem

The test of an operating system is whether it holds up across genuinely different work. A few of mine sit on different legs of the span.

**Product in Acquisitions OS, which I build and ship in Code.** It packages the 90-Day Product Integration Framework as a working operating system for product leaders running post-acquisition integrations, versioned and released like real software. Its conventions, release steps, and structure live in the repo, where they belong, and nowhere else. This is the durable-asset leg: deep, project-bound work that has no reason to travel.

**Notes2Notion, the bridging tools that move my notes into the hub.** I built small tools that carry knowledge from Apple Notes into Notion. That is the inbound side of the hub, the plumbing that keeps the shared spine current without manual copying. It is also a reminder that the hub is not just something the surfaces read. It is something the rest of my system feeds.

**A Zone 8a gardening site that has nothing to do with work.** A public site I run on the side. It matters here precisely because it is personal. The routing rule is what keeps personal data out of the public work and out of professional contexts where it does not belong. The discipline is not only about getting the right context to the right place. It is about keeping the wrong context out.

None of these required a custom memory product or a clever integration. Each one required the same small decision, made consistently: where does this fact belong?

---

## How It Is Wired

Three layers, each with one job.

The repo layer is a `CLAUDE.md` file checked into each project. It holds that project's conventions and is read by Code when a session starts. The global layer is a single `CLAUDE.md` in my home directory. It holds my cross-project working preferences and is also read by Code. The hub layer is one Notion page, exposed to Chat, Cowork, and the web and mobile apps through the Notion connector.

The routing rule is the glue. A fact lands in exactly one layer based on who needs to read it, and the hub is the only layer every surface can reach. There is no custom memory service, no vector database, no integration code. The work is the routing decision, repeated.

---

## Steal This

You now have the whole argument and the shape of the system: three surfaces, one routing question, a hub that serves as the shared spine. That is enough to start today.

What I have not handed you yet is my exact wiring. Below this line, for premium subscribers, is the step-by-step build as I actually run it: what goes in the global instructions file and what stays out, how the per-project files and the hub divide the work, the routing rule written so every surface obeys it, the inbound plumbing that keeps the hub current without copying by hand, and the maintenance cadence that keeps a shared spine from quietly going stale.

Premium subscribers also get the Product in Acquisitions OS as an installable Claude plugin, not a PDF. It is this same routing discipline applied to one hard problem: keeping an acquired product team and roadmap coherent through the first 90 days.

If you have been meaning to stop fighting your tools, this is the afternoon to do it.

<!-- ============ SUBSTACK PAYWALL GOES HERE: everything below is premium ============ -->

---

## How to Wire It Up as We Did

Here is the build, in the order I would do it again. Budget an afternoon. None of it requires writing integration code.

**1. Write the global layer first.** This is the file that travels with you as an operator, not with any project. Mine lives at `~/.claude/CLAUDE.md`, and Code reads it at the start of every session in every project. Put your standing preferences here and nothing project-specific: how much autonomy you want, what "done" means to you, your tone, your commit conventions, how you want errors handled. The test for this layer is one question. If a fact would still be true on a project you have not started yet, it belongs here.

**2. Add the repo layer, one per project.** Each project gets its own `CLAUDE.md` at the repo root, alongside the memory folder Code maintains for it. This layer holds what dies with the work: build conventions, release steps, the architecture and quirks of that one codebase. Code reads it at session start the same way it reads the global file, but it never leaves the repo. The test: if a fact would be noise in any other project, it stays here.

**3. Stand up the hub.** Create one page on a platform you already trust and can reach from every device. I use a single Notion page I call the Context Hub. Keep it human-readable and flat enough to audit at a glance. This is the only layer every surface can see, so it carries the portable facts: durable decisions, current project status, anything you might need to pull up from your phone. Then connect it. The Notion connector exposes that one page to Chat, Cowork, and the web and mobile apps, which is the exact workaround for the memory gap. The web and mobile surfaces cannot see my local files, but they can all see the hub.

**4. Write the routing rule where each surface will read it.** The rule itself is a fact, so route it. I keep it in the global `CLAUDE.md` so Code applies it, and I restate it in plain language at the top of the hub page so the web surfaces apply it too. One sentence does most of the work: code-only facts go to the repo, how-I-work facts go to the global file, anything portable or wanted from the phone goes to the hub. Until the rule is written somewhere each surface reads, it is an intention, not a rule.

**5. Feed the hub, carefully.** The hub is not only something the surfaces read. It is something the rest of your system feeds. I built small bridging tools, mine carry notes from Apple Notes into Notion, so capture does not depend on me copying by hand. One warning, learned the hard way: do not automate capture before the routing is settled, or you will faithfully archive a mess into the one layer every surface trusts.

**6. Maintain it, or it lies.** This is the actual discipline, and it is the part no tutorial covers. When a durable decision or a project status changes, update the hub once, at the moment it changes. Then do one cleanup pass a week: move anything that landed in the wrong layer, delete anything that turned out not to matter. A current spine is worth more than any clever integration. A stale one is worse than nothing, because every surface will confidently tell you something that stopped being true last week.

---

## The Advantage Is the Discipline

You can build everything above in an afternoon. That is the point, and it is also the trap. Because the wiring is easy, it is tempting to believe the wiring is the system. It is not. The connectors are commodity and getting more so every month. Anyone can wire a hub to an assistant by tonight.

The advantage is what you do every day after that. Routing each durable fact to the one place it belongs, so the right surface knows the right thing at the right moment and the wrong context stays out of the room. It is a small habit. It compounds. Over a quarter it is the difference between fighting your tools and running on them.

So the build is not the work. The work is answering one question, honestly, every time something durable comes up: where does this belong?

---

*Blane Warrene is an AI-forward product and operations executive with 20-plus years in wealthtech, compliance technology, and SaaS. He writes on business operating systems, the next decade of SMB SaaS, and building AI-native organizations.*
