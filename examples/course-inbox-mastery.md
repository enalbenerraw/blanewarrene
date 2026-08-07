# Inbox Mastery: Leveraging Claude in Google Workspace and Microsoft 365 Outlook

## 1. Teachable Marketing Copy

**Course Title:** Inbox Mastery: Claude in Gmail and Outlook

**Subtitle / Promise:** Write faster, reply smarter, and never read a 20-email thread again.

**Course Description:**
You spend more time on email than on the work you actually got hired to do. You know it. Your team knows it. The 20-email thread sitting at the top of your inbox right now knows it.

Here's what most people don't realize: you can hand 80% of that work to Claude in a clean, repeatable workflow that takes one browser tab and zero IT-team approval.

In this free 5-lesson course, you'll learn how to set up Claude alongside Gmail or Outlook, triage your inbox in three minutes, summarize long threads in thirty seconds, and draft replies that sound like *you* — not like generic AI fluff. No code, no automations, no "send to inbox" risks. You stay in control. Claude does the heavy lifting.

By the end, you'll be able to process any 20-email thread in under three minutes — read what matters, draft a reply that sounds like you, and clear it from your queue.

**You'll Learn:**
- Set up Claude as a side-by-side co-pilot for Gmail or Outlook with zero IT involvement
- Triage your inbox by urgency in under three minutes using a single repeatable prompt
- Summarize any 20-email thread into the actual ask, the actual context, and what's missing
- Draft replies in your own voice that read like you wrote them — not like AI wrote them
- Build a personal "voice library" so Claude consistently sounds like you across emails

**This Course Is For You If…**
- You live in Gmail or Outlook all day and feel like email is eating your job
- You're a busy operator, founder, consultant, or knowledge worker — not a developer
- You want a workflow you can use today, not someday after IT approves an integration

**This Course Is NOT For You If…**
- You're looking for code, API integrations, MCP servers, or automated send tools
- You want Claude to send replies on your behalf without you reading them — this course is human-in-the-loop by design

**Prerequisites:** None. You don't need a coding background, prompt-engineering experience, or admin access to your email. You'll need a free claude.ai account (or the desktop app) and either Gmail or Outlook open in another tab.

**Instructor Bio Hook:** I've spent the last two years helping non-technical operators use Claude to claw back two hours a day from their inbox — without any IT integration, automation, or risk. This course is the exact workflow I install on day one.

---

## 2. Course Outline

1. **Setting Up Claude as Your Inbox Co-Pilot** — How to position Claude alongside Gmail or Outlook so the workflow is one click away. *Runtime: 8 min. Micro-skill: Workspace setup.*
2. **The Triage Pass: Stop Reading Threads You Don't Need To** — A single repeatable prompt that scans your morning inbox and tells you what actually needs you. *Runtime: 10 min. Micro-skill: Inbox triage.*
3. **Summarizing Long Threads in 30 Seconds** — Reduce a 20-email thread to the ask, the context, and what's missing — fast. *Runtime: 10 min. Micro-skill: Thread summarization.*
4. **Drafting Replies That Sound Like You** — The four-part prompt pattern that produces replies people read as yours. *Runtime: 10 min. Micro-skill: Voice-aware reply drafting.*
5. **Building Your Email Voice Library** — Save Claude prompts that match the recurring email scenarios in your week. *Runtime: 8 min. Micro-skill: Reusable voice templates.*

---

## 3. Full Lessons

## Lesson 1: Setting Up Claude as Your Inbox Co-Pilot

**Runtime:** ~8 minutes
**Learning objective:** By the end of this lesson, you will have Claude positioned alongside Gmail or Outlook in a configuration that makes inbox-to-Claude-and-back a one-click workflow.

### Lesson Script

Before we get to the clever prompting, let's solve the boring problem: friction.

Here's the workday frustration I want to fix in this lesson. You're in Gmail. You see a long thread you need to deal with. You think, "okay, Claude could help with this." You open a new tab. You navigate to claude.ai. You wait for it to load. You go back to Gmail. You copy the thread. You go back to Claude. You paste. You think — wait, what was I going to ask?

Three minutes gone before you've done any actual work. So you stop bothering, and the inbox wins.

The fix isn't fancy. It's setting up Claude *next to* your inbox so the round trip takes one click and zero thinking.

Here's the key idea. Throughout this course, every workflow will use the same four-part prompt pattern. I want you to memorize it now: **Context + Thread + Goal + Tone.** That's it. Every prompt you'll learn in this course is just a different combination of those four ingredients. We'll come back to it constantly.

Now — setup. There are three configurations that work, in order of recommendation:

**Configuration 1: Side-by-side browser windows.** This is what 90% of you should do. Open Gmail or Outlook in one browser window, claude.ai in another, and snap them side by side using your operating system's window manager. On Mac, drag a window to the edge of the screen and Tahoe will offer a split. On Windows, Win+Left and Win+Right.

**Configuration 2: Claude desktop app.** If you've installed the Claude desktop app, you can keep it as a floating window over your inbox. This is my preferred setup — Claude is always visible, always ready, no tab-switching.

**Configuration 3: Claude in your phone or tablet next to your laptop.** Surprisingly underrated. Email on the laptop, Claude on the iPad. Copy-paste isn't as smooth, but the cognitive separation — "this device thinks, that device sends" — keeps people from accidentally pasting AI text where they didn't mean to.

Whichever you pick, the rule is the same: Claude should be visible *while* you're in your inbox, not buried in a tab you have to dig for.

Now let's do one quick worked example so you see the pattern in action. Suppose I'm in Gmail. I see a long client thread. I copy the whole thread (just select all the visible email body text — you don't need anything fancy). I paste it into Claude with this:

```
You're helping me process an email thread.

Context:
- I'm an account manager at a B2B analytics company.
- The client is a marketing director at a mid-sized retailer.
- We've been talking about renewing for Q3.

Thread:
[paste the thread here]

Goal:
- Tell me in 4 bullets: what they want, what's blocking, what
  they decided, and what they're waiting on me for.

Tone:
- Plain, no editorializing.
```

And Claude comes back with something like:

```
- They want to renew, but are debating between the Pro and
  Enterprise tiers.
- Blocked by: needing buy-in from their CFO before signing.
- Decided: they'll move forward at one of the two tiers — not
  walking away.
- Waiting on you for: a one-page comparison of Pro vs.
  Enterprise focused on their use cases (segmentation +
  attribution), to send to the CFO.
```

That's a 14-email thread reduced to four lines you can act on, in about thirty seconds. That technique — separating context, content, goal, and tone with structured labels — is called **structured prompting with XML-style tags** in prompt-engineering circles. In plain English: when you label the parts of your prompt, Claude knows which part is the email, which part is your instruction, and which part is the constraint. It stops mixing them up.

That's it for Lesson 1. Pick a setup, get Claude visible next to your inbox, and burn the **Context + Thread + Goal + Tone** pattern into memory. Tomorrow we'll use that pattern to triage your entire morning inbox in three minutes.

### On-Screen / Slide Outline
- **Slide 1 — Title:** "Setting Up Claude as Your Inbox Co-Pilot."
- **Slide 2 — The Friction Problem:** "Three minutes lost before any work happens."
- **Slide 3 — The Pattern:** "Context + Thread + Goal + Tone." Four boxes.
- **Slide 4 — Setup Option 1:** Side-by-side browser windows. Show the visual.
- **Slide 5 — Setup Option 2:** Claude desktop app as a floating window.
- **Slide 6 — Setup Option 3:** Phone/tablet companion.
- **Slide 7 — Worked Example:** The 14-email thread → 4 bullets demo.
- **Slide 8 — Coming Up:** Lesson 2 — The Triage Pass.

### Try It Yourself (Exercise)
Set up your workspace. Pick one of the three configurations. Get Gmail or Outlook visible on one half of your screen and Claude on the other.

Then take any one email thread in your inbox right now (pick something boring — a meeting confirmation, a vendor update). Copy the thread. Paste it into Claude with this:

```
You're helping me process an email thread.

Context:
- [One sentence on who you are and the relationship.]

Thread:
[paste the thread here]

Goal:
- Tell me in 3-4 bullets: what they want, what's blocking, what
  they decided, and what they're waiting on me for.

Tone:
- Plain, no editorializing.
```

**Success criterion:** You'll know it worked when you got the four-bullet summary in under a minute and you didn't have to switch windows to read it.

**Common failure mode:** You skip the Context line because the thread "speaks for itself." It doesn't — Claude doesn't know your role or relationship, so the summary will be flatter than it needs to be. Fix: always include one sentence of context.

### Knowledge Check
1. What's the four-part prompt pattern this course uses for every email workflow?
   - a) Subject + Body + Signature + Attachment
   - b) Context + Thread + Goal + Tone
   - c) From + To + CC + BCC
   - d) Greeting + Ask + Close + Sign-off
   - **Correct: b.** Context + Thread + Goal + Tone is the central pattern. You'll see it in every lesson.

2. Why does positioning Claude visibly next to your inbox matter so much?
   - a) Claude works faster when it's on the same screen
   - b) It removes the tab-switching friction that stops people from using Claude on real emails
   - c) It improves the AI's accuracy
   - d) It's required by Claude's terms of service
   - **Correct: b.** Friction kills the workflow. The point of the setup is to make using Claude cheaper than not using it.

3. Why label the parts of your prompt (Context, Thread, Goal, Tone) instead of writing it as one paragraph?
   - a) Claude charges less for labeled prompts
   - b) Labeling tells Claude which part is the email vs. your instruction vs. the constraint, so it stops mixing them up
   - c) It makes the prompt look professional
   - d) Labels are required by Claude's API
   - **Correct: b.** Structured prompting prevents Claude from misreading your instruction as part of the email content.

### Instructor Notes
- Demo the side-by-side window setup live. Most learners have never split-screened on their OS and don't realize how easy it is.
- Skip the phone/tablet option if you're tight on time — it's a niche move.
- The "structured prompting" terminology lands well if you say it once and never again. Don't lecture.

---

## Lesson 2: The Triage Pass — Stop Reading Threads You Don't Need To

**Runtime:** ~10 minutes
**Learning objective:** By the end of this lesson, you will be able to use a single repeatable triage prompt that scans your unread inbox and tells you which threads need you, which can wait, and which can be ignored — in under three minutes.

### Lesson Script

Pop quiz. Of the unread emails sitting in your inbox right now, what percentage actually require *you* — your judgment, your decision, your reply — versus what percentage are CCs, FYIs, status updates, or threads where someone else is the right responder?

If you guessed "less than half," you're probably right. The data on knowledge workers' inboxes consistently lands around 30–40% of email actually requiring the recipient.

So here's the problem. You don't know *which* 30-40% until you read everything. So you read everything. And the inbox eats your morning.

This lesson installs the fix: a triage pass.

Here's how it works. You're going to copy a batch of subject lines + first two lines of preview text from your unread inbox, paste them into Claude, and ask Claude to sort them for you. Three categories: **needs me now**, **can wait**, **ignore or delegate**.

Let's see it in action. In Gmail or Outlook, scroll your inbox. Select the visible text — subject lines, sender, preview snippets. Copy. Paste into Claude with this prompt:

```
You're helping me triage my inbox.

Context:
- I'm a head of operations at a 60-person SaaS company.
- I'm in deep-work mode this morning. Anything that doesn't
  truly need me, I want to defer.
- I have direct reports who can handle most ops questions.

Inbox preview:
[paste the list of subjects + previews here]

Goal:
- Sort each item into one of three buckets:
  1. NEEDS ME NOW — has to be handled by me, today.
  2. CAN WAIT — valid email, but not today; I'll batch-process
     these later.
  3. IGNORE/DELEGATE — CC, FYI, or something a direct report
     should own.

For each item, give me:
- A one-line "why" (so I can argue with you if I disagree)
- For DELEGATE items, who on a typical ops team should own it.

Tone:
- Decisive. Don't hedge. If you're wrong, I'll correct you.
```

And Claude comes back with something like:

```
NEEDS ME NOW
- "Q3 board deck — final review needed by EOD"
  Why: explicit deadline today, board-facing, your name in
  ask line.
- "Vendor renewal — auto-renew Friday"
  Why: financial commitment with a hard deadline 4 days out.

CAN WAIT
- "Updated PTO policy draft for review"
  Why: HR-driven, not time-sensitive, async-friendly.
- "Customer Q3 health check report"
  Why: reading material, no decision requested.

IGNORE/DELEGATE
- "[CC] Engineering all-hands notes"
  Why: pure FYI, no ask.
- "Office snack reorder approval"
  Why: should go to the office manager, not you.
- "[CC] Onboarding doc updated"
  Why: information-only, your direct report Sara owns this area.
```

In thirty seconds, you went from a 25-email morning queue to two emails that need you today, plus a clear plan for everything else. The technique here is called **classification with named categories and reasoning**. Two parts to it: you give Claude clear, mutually exclusive buckets, *and* you ask Claude to explain its reasoning. The explanation part is critical — it lets you spot when Claude misjudged and override it in three seconds, instead of trusting a black-box sort.

Two pro tips.

**Tip one: tune the categories to your reality.** If you're a founder, your buckets might be "needs me," "needs CEO context but someone else can act," and "team owns it." If you're a salesperson, maybe "deal-related," "customer-success-related," and "noise." Your buckets, your call. Just make them mutually exclusive.

**Tip two: argue with Claude.** When Claude misclassifies something, push back: "You put the vendor email in CAN WAIT — actually it's auto-renewing in 4 days, that's NEEDS ME NOW." Claude will correct itself. Two or three of those corrections per session and the triage gets sharper.

One last thing. Don't trust this prompt to triage *everything*, especially the first week. Use it as a first pass — then sanity-check the NEEDS ME NOW pile. After a few days of use, you'll trust the sort enough to act on it directly.

Tomorrow we tackle the long threads themselves: how to summarize a 20-email back-and-forth in 30 seconds without losing the thread of who said what. See you then.

### On-Screen / Slide Outline
- **Slide 1 — Title:** "The Triage Pass."
- **Slide 2 — The Stat:** "Only 30-40% of your inbox truly needs you."
- **Slide 3 — The Three Buckets:** NEEDS ME NOW / CAN WAIT / IGNORE OR DELEGATE.
- **Slide 4 — The Triage Prompt:** Show the full prompt on screen.
- **Slide 5 — The Sample Output:** Show the sorted output from a real-ish inbox.
- **Slide 6 — Why It Works:** Classification + reasoning = override-able.
- **Slide 7 — Tune the Buckets:** Founder vs. salesperson vs. ops example.
- **Slide 8 — Coming Up:** Lesson 3 — Summarizing long threads.

### Try It Yourself (Exercise)
Open your inbox right now. Select 10–20 subject lines and previews from your unread queue (or recent inbox if your unreads are zero). Copy. Paste into Claude.

Adapt this starter prompt:

```
You're helping me triage my inbox.

Context:
- I'm a [your role] at [your company in one sentence].
- I have [direct reports / no direct reports].
- I'm trying to focus on [your current priority] this morning.

Inbox preview:
[paste subjects + previews]

Goal:
- Sort each item into one of three buckets:
  1. NEEDS ME NOW
  2. CAN WAIT
  3. IGNORE/DELEGATE
- For each, give a one-line "why" so I can override if I
  disagree.

Tone: Decisive. Don't hedge.
```

**Success criterion:** You'll know it worked when at least 3 items got sorted into IGNORE/DELEGATE that you would have otherwise opened and read — and Claude's reasoning lets you trust the sort.

**Common failure mode:** Your buckets are vague or overlapping ("important" vs. "urgent"). Fix: redefine them as mutually exclusive *actions* — "I respond today," "I respond this week," "I don't respond at all."

### Knowledge Check
1. Why does the triage prompt ask Claude to explain the "why" for each classification?
   - a) It uses fewer tokens
   - b) It lets you spot misclassifications and override Claude in three seconds, instead of trusting a black-box sort
   - c) Claude requires it
   - d) It looks more polished
   - **Correct: b.** The reasoning is what makes the sort overridable. Without it, you can't tell when Claude was wrong.

2. What's the most important property of the triage buckets you give Claude?
   - a) They should sound impressive
   - b) They should be mutually exclusive
   - c) There should be exactly five
   - d) They should match the GTD methodology
   - **Correct: b.** Mutually exclusive buckets force a decision and prevent items from "fitting in two places."

3. What's the right way to handle a misclassification by Claude?
   - a) Ignore it
   - b) Restart the conversation from scratch
   - c) Push back in plain language ("You put X in CAN WAIT, but it auto-renews in 4 days — that's NEEDS ME NOW") and Claude will correct itself
   - d) Switch to a different AI tool
   - **Correct: c.** Refining classifications in dialogue is how you tune the triage to your reality.

### Instructor Notes
- The 30-40% stat is your hook. Lead with it.
- Demo the triage prompt live with a faked but realistic inbox preview. Bonus points if you cover up sender names with your hand on camera.
- Some learners worry about pasting work email into Claude. Acknowledge it — say "use your judgment, follow your company policy, and never paste anything you wouldn't paste into a Google Doc."

---

## Lesson 3: Summarizing Long Threads in 30 Seconds

**Runtime:** ~10 minutes
**Learning objective:** By the end of this lesson, you will be able to take any long, messy email thread — the kind with 12 replies, three forwarded chains, and four people talking past each other — and reduce it to the ask, the context, the decisions made, and what's missing, in under thirty seconds.

### Lesson Script

Welcome back. Today we tackle the worst kind of email: the long thread.

You know the one. Twenty messages. Three forwards. Four people. Someone's CCed you halfway through. Someone else has been quietly removed. There's a question buried in there somewhere that needs your answer, but to find it you'd have to read the whole thing. And you don't have time.

So today's frustration: long threads cost you more time than the actual reply ever will. The reading is the work, not the writing.

Here's the fix. A summarization prompt that does four things in parallel:

1. Identifies the *current* ask (not the original ask, not the side asks — the one on the table).
2. Surfaces the relevant *context* — what's been decided, what's been tried.
3. Names the *decisions* already made in the thread that you should respect.
4. Flags what's *missing* — open questions, unresolved disagreements, ambiguity.

Let me show you the prompt, then we'll walk through it.

```
You're helping me process a long email thread.

Context:
- I'm a product manager at a 200-person fintech.
- The thread is between me, my engineering counterpart, our
  designer, and the head of compliance.
- I was added to the thread on message 7 and need to weigh in.

Thread:
[paste the full thread here]

Goal:
Summarize this thread in four labeled sections:

1. THE CURRENT ASK — what's on the table for me, in one
   sentence.
2. RELEVANT CONTEXT — the 3-5 most important facts I need
   to know to respond well.
3. DECISIONS ALREADY MADE — anything the group has settled
   on that I shouldn't reopen.
4. WHAT'S MISSING — open questions, unresolved tensions,
   information not yet shared.

Tone:
- Plain, factual. If two people disagree, say so explicitly —
  don't smooth it over.
```

And Claude comes back with something like:

```
1. THE CURRENT ASK
You need to confirm whether the new fee disclosure flow can
ship in the v3.2 release on March 15, given that compliance
just flagged a copy change.

2. RELEVANT CONTEXT
- The flow has been in review with compliance for 6 weeks.
- Engineering has the v3.2 release branch cut and is locked
  for code freeze on March 11.
- Compliance's flag is a wording change ("estimated fee" →
  "fee, subject to confirmation"), not a structural change.
- Design has already approved the new wording verbatim.
- Sarah (compliance) is on PTO Mar 12-14, returning Mar 15.

3. DECISIONS ALREADY MADE
- The fee disclosure WILL go in v3.2, not be deferred.
- The wording from compliance is the final wording — no
  further edits.
- QA will run a half-day regression on the changed copy only.

4. WHAT'S MISSING
- No one has confirmed whether the wording change requires
  re-translation in the 4 localized markets.
- It's unclear whether Sarah's PTO means compliance sign-off
  is needed before March 12 or whether it can wait until
  March 15.
- Engineering hasn't said if pulling the change in before
  freeze creates risk to other v3.2 features.
```

You just turned a 23-message thread into a one-screen briefing. You know exactly what's being asked, what's already been settled, and what blockers you should raise in your reply. The technique here is called **structured extraction with explicit slots** — you're not asking for a summary, you're asking for *specific information in named compartments*. Big difference. A "summarize this" prompt gives you a paragraph. A slotted prompt gives you a briefing.

A few moves to keep in your back pocket:

**The "find the ask" mini-prompt.** When all you need is the question, skip the full summary:

```
What is the single most important question being asked of me
in this thread? Quote the exact sentence if possible.
```

**The "who's saying what" mini-prompt.** When the thread is contentious and you need to map positions:

```
For each person on the thread, summarize their position in one
sentence. Note where any two people directly disagree.
```

**The "what would I have missed" prompt.** Once you've read Claude's summary, run this:

```
What's in the thread that you didn't include in your summary
but I might want to know? Be specific.
```

That last one is especially good — it surfaces tone shifts, relationship dynamics, and small details that don't fit the slotted format but matter.

One safety note. Always glance at the original thread before acting on a Claude summary. Especially the most recent message. Claude is excellent at summarization but can occasionally smooth over a sharp comment that, if you missed it, would change your reply. The summary is a shortcut, not a substitute.

Tomorrow we cover the other half of email work: drafting replies that actually sound like *you*. See you there.

### On-Screen / Slide Outline
- **Slide 1 — Title:** "Summarizing Long Threads in 30 Seconds."
- **Slide 2 — The Real Cost:** "The reading is the work, not the writing."
- **Slide 3 — The Four Slots:** Current Ask / Context / Decisions / What's Missing.
- **Slide 4 — The Prompt:** Full prompt on screen.
- **Slide 5 — Sample Output:** Side-by-side "23 messages → one screen."
- **Slide 6 — Mini-Prompts:** Find the ask / Who's saying what / What did you miss.
- **Slide 7 — Safety Note:** Always glance at the original.
- **Slide 8 — Coming Up:** Lesson 4 — Drafting replies that sound like you.

### Try It Yourself (Exercise)
Find the longest unread thread in your inbox right now. The messier, the better — five replies minimum.

Copy the entire thread. Paste it into Claude.

Adapt this starter prompt:

```
You're helping me process a long email thread.

Context:
- I'm a [your role] at [your company in one sentence].
- The thread is between [the people on it + their roles].
- [Anything special — e.g., you were added late, this is a
  vendor relationship, etc.]

Thread:
[paste the full thread]

Goal:
Summarize in four labeled sections:
1. THE CURRENT ASK
2. RELEVANT CONTEXT (3-5 facts)
3. DECISIONS ALREADY MADE
4. WHAT'S MISSING

Tone: Plain, factual. Don't smooth over disagreements.
```

Then run the follow-up:

```
What's in the thread that you didn't include but I might want
to know? Be specific.
```

**Success criterion:** You'll know it worked when you can describe the thread to someone else in 30 seconds, accurately, having only read Claude's summary.

**Common failure mode:** You ask for "a summary" instead of using the four labeled slots. The output is a paragraph that's hard to act on. Fix: always use the slotted format. Slots beat paragraphs every time.

### Knowledge Check
1. Why ask Claude for a "slotted" summary (Current Ask, Context, Decisions, What's Missing) instead of just "summarize this thread"?
   - a) It uses less context window
   - b) Slots produce briefings you can act on; paragraphs produce text you have to re-read
   - c) Claude is required to use slots
   - d) Slots get higher priority in the model
   - **Correct: b.** Structured extraction beats free-form summarization for actionable email triage.

2. What's the purpose of the follow-up prompt "What's in the thread that you didn't include but I might want to know?"
   - a) It catches tone shifts, relationship dynamics, and small details that don't fit the slotted format
   - b) It gets Claude to apologize for being incomplete
   - c) It triggers a different model
   - d) It's optional and rarely useful
   - **Correct: a.** It's the safety net for the things slots can miss.

3. Why glance at the original thread before acting on Claude's summary?
   - a) It's required by your IT department
   - b) Claude can occasionally smooth over a sharp comment that would change your reply
   - c) The summary uses paid Claude credits
   - d) Claude can't read email properly
   - **Correct: b.** Summarization is a shortcut, not a substitute. A 5-second sanity check on the most recent message is enough.

### Instructor Notes
- The fintech worked example is dense — read it slowly on camera. The point is that the slots make a complex situation legible.
- The "who's saying what" mini-prompt is gold for political threads. If you have a contentious example, demo it.
- Don't skip the safety note. Trust comes from acknowledging the limits.

---

## Lesson 4: Drafting Replies That Sound Like You

**Runtime:** ~10 minutes
**Learning objective:** By the end of this lesson, you will be able to draft an email reply with Claude that reads like you wrote it — using a four-part prompt that names your relationship, your tone, your goal, and the constraints of the reply.

### Lesson Script

You've triaged your inbox. You've summarized the thread. Now comes the moment that breaks people: you have to actually reply.

And here's where most people make the AI-tells. The reply comes out sounding like AI wrote it. The phrases are *just* a little too smooth. The closings are *just* a little too cheerful. There's an "I hope this email finds you well" that you would never write. The recipient reads it and clocks immediately that you didn't write it. Trust drops.

Today we fix that.

The pattern is the same one we've used all course: **Context + Thread + Goal + Tone.** Today we lean hard on the Tone slot. Tone is what makes a reply sound like you instead of like ChatGPT-with-different-paint.

Let me show you the prompt template, then we'll work an example.

```
You're helping me draft a reply to this email thread.

Context:
- I'm [your role + company].
- The recipient is [their role + relationship to you + how
  long you've worked together].
- The state of the relationship: [warm / strained / new /
  transactional].

Thread:
[paste the relevant portion of the thread]

Goal:
- Reply length: [2 short paragraphs / 4 sentences / one line].
- Reply outcome: [what you want the recipient to do or feel
  after reading this].
- Things to NOT do: [explicit anti-instructions — see below].

Tone:
- I sound like: [3-5 specific tone descriptors — see below].
- I do NOT sound like: [3-5 tone anti-patterns — see below].

Draft the reply.
```

Two pieces are doing the heavy lifting: the **Tone "I sound like / I do NOT sound like"** pair, and the **Goal "Things to NOT do"** anti-instructions.

Why anti-instructions? Because Claude has defaults. Without explicit "do not do this" guardrails, you get the defaults — pleasantries, hedges, over-explaining, the corporate "Please let me know if you have any questions." Naming what *not* to do is often more powerful than naming what to do.

Let's work an example. You're a head of partnerships at a B2B SaaS company. A potential partner has been slow-walking a co-marketing deal for six weeks. Today they emailed asking for *another* internal review cycle before they can commit. You need to reply firmly but without burning the relationship.

```
You're helping me draft a reply to this email thread.

Context:
- I'm head of partnerships at a B2B analytics SaaS company.
- The recipient is a partnerships lead at a mid-sized agency
  we've been talking to for 6 weeks about a co-marketing deal.
- Relationship: cordial but they've been slow-walking. I've
  done two scope revisions to accommodate their internal
  process.

Thread:
[paste the latest 3 messages]

Goal:
- Reply length: 4-5 sentences.
- Reply outcome: They commit to a yes/no decision by end of
  next week, without me sounding aggressive.
- Things to NOT do: Don't apologize for following up. Don't
  re-explain the value prop. Don't offer a third scope revision.
  Don't say "I just wanted to check in."

Tone:
- I sound like: Direct, warm, slightly dry, comfortable with
  silence, not desperate, treats the recipient as a peer.
- I do NOT sound like: Eager, salesy, hedging, over-grateful,
  apologetic, formal-corporate.

Draft the reply.
```

Claude returns something like:

```
Hi Mara,

Happy to give you the time for one more internal pass — but I
want to flag that we've been at this for six weeks now, and I
think we both deserve a clear yes or no rather than another
review loop.

Can you commit to a decision by end of next week, Friday the
22nd? If the answer is no, that's totally fine — I'd rather
know now and free up your team's time. If it's a yes, I'll
have the partnership agreement ready to sign that day.

Either way, I appreciate the work you've put in on your side.

Best,
[Your name]
```

That reads like a real human wrote it. No "I hope this finds you well." No "I just wanted to check in." It's direct, warm, sets a deadline, gives an honest off-ramp, and ends with genuine appreciation. Why? Because we explicitly told Claude what tone *not* to use — and we told Claude what *not* to do.

The technique at work has a name: **negative prompting** or **anti-pattern instructions**. Most prompting advice tells you to be specific about what you want. Equally useful: be specific about what you *don't* want. Claude follows both.

A few patterns to keep in your back pocket:

**The "match the energy" move.** Add to Tone: *"Match the recipient's energy level — if they were brief, be brief; if they were warm, be warm."* This stops Claude from over-formalizing replies to casual emails.

**The "real-human flaws" move.** Add to Tone: *"Allow small natural imperfections — sentence fragments, a one-line paragraph, an em-dash — that make the reply read as written, not generated."* This kills the AI-uniformity tell.

**The "draft three" move.** When you can't decide on tone:

```
Draft 3 versions of this reply:
1. Slightly warmer than my usual.
2. My usual.
3. Slightly more direct than my usual.

Same content, different tone calibration.
```

Pick whichever lands. This is your last lesson on the *individual* email reply. Tomorrow we close the course by building your voice library — saved templates that make this whole workflow Monday-morning automatic. See you there.

### On-Screen / Slide Outline
- **Slide 1 — Title:** "Drafting Replies That Sound Like You."
- **Slide 2 — The AI Tells:** Examples of AI-flavored phrases to avoid.
- **Slide 3 — The Tone Pair:** "I sound like / I do NOT sound like."
- **Slide 4 — Anti-Instructions:** "Don't apologize. Don't re-explain. Don't say 'just checking in.'"
- **Slide 5 — Worked Example:** The slow-walking partner thread.
- **Slide 6 — The Output:** The final reply that reads as written, not generated.
- **Slide 7 — Pro Patterns:** Match energy / real-human flaws / draft three.
- **Slide 8 — Coming Up:** Lesson 5 — Building your voice library.

### Try It Yourself (Exercise)
Pick one email in your inbox that you've been avoiding replying to — something that needs a careful tone. Open Claude.

Adapt this starter prompt:

```
You're helping me draft a reply to this email thread.

Context:
- I'm [your role + company].
- The recipient is [their role + relationship + history].
- Relationship state: [warm / strained / new / transactional].

Thread:
[paste the thread]

Goal:
- Reply length: [N sentences or paragraphs].
- Reply outcome: [what you want them to do or feel].
- Things to NOT do: [3-5 explicit anti-instructions].

Tone:
- I sound like: [3-5 descriptors].
- I do NOT sound like: [3-5 anti-patterns].

Draft the reply.
```

**Success criterion:** You'll know it worked when you can send the reply with at most 1–2 small word swaps and it reads to you like something you actually wrote.

**Common failure mode:** You skip the "I do NOT sound like" line because it feels redundant. The reply comes out generically smooth. Fix: always include the anti-tone — naming what to *avoid* is often more powerful than naming what to do.

### Knowledge Check
1. What's the purpose of the "I do NOT sound like" descriptors?
   - a) They tell Claude which tones to avoid, which is often more powerful than naming what to do
   - b) They're optional and rarely matter
   - c) They make the prompt longer for billing purposes
   - d) They activate a specific Claude personality
   - **Correct: a.** Negative prompting (naming what to avoid) is one of the highest-leverage moves in tone control.

2. Why include "Things to NOT do" anti-instructions in the Goal section?
   - a) They make the prompt sound serious
   - b) Without explicit guardrails, Claude defaults to pleasantries, hedges, and over-explaining
   - c) Claude requires them
   - d) They produce shorter replies
   - **Correct: b.** The defaults are the problem. Anti-instructions are how you turn them off.

3. When you can't decide on tone for a tricky email, what's a good move?
   - a) Send the first draft Claude produces
   - b) Switch to a different AI tool
   - c) Ask Claude to draft three versions calibrated by tone (slightly warmer / usual / slightly more direct) and pick whichever lands
   - d) Avoid replying
   - **Correct: c.** Variant generation on tone is a fast way to find the right register.

### Instructor Notes
- The "AI tells" slide is the lesson — read three or four out loud so learners cringe in recognition.
- Demo the anti-instructions live. Show one prompt with them and one without. The contrast is dramatic.
- If running short, skip the "draft three" pattern. The Tone pair + anti-instructions are what really matter.

---

## Lesson 5: Building Your Email Voice Library

**Runtime:** ~8 minutes
**Learning objective:** By the end of this lesson, you will have a small library of 3–5 saved prompts — one for each recurring email scenario in your week — that turn the four-part pattern into a one-click, Monday-morning workflow.

### Lesson Script

You've now got the full workflow. Setup. Triage. Summarize. Reply. The last move is the one that turns a *technique* into a *system*: building your voice library.

A voice library is just a small collection of saved prompts — three to five to start — that match the recurring email scenarios you actually face every week. Not the rare edge cases. The boring-but-frequent ones that already eat your hours.

Here's how to build yours in fifteen minutes.

**Step one: Inventory.** Open your sent folder. Scroll back two weeks. List the *types* of email you sent more than three times. Common patterns:

- Customer status updates / check-ins
- Internal stakeholder updates (your boss, your team)
- Vendor or partner negotiations
- Cold outreach to prospects
- Difficult conversations (delays, no's, pushback)
- Meeting recaps
- Quick decisions you've been asked to weigh in on

Pick the three or four that consume the most time *or* that you find emotionally hardest. Both are great candidates — the boring time-eaters because volume matters, and the hard ones because thinking-on-paper saves stress.

**Step two: Build a four-part template for each.** Use the same **Context + Thread + Goal + Tone** structure you've been using all course, but make every reusable piece a placeholder. Like this — here's a saved template for "customer check-in reply":

```
You're helping me draft a reply to a customer email.

Context:
- I'm [my role] at [my company].
- The customer is [their name + role + company size].
- Account state: [active / at-risk / brand new / renewing].
- Last meaningful interaction: [date + topic].

Thread:
[paste the thread]

Goal:
- Reply length: 3-5 sentences max.
- Reply outcome: They feel heard, they have a clear next step,
  they're not waiting on me for anything else.
- Things to NOT do: Don't say "circling back." Don't say "I
  just wanted to check in." Don't ask multiple questions —
  pick the one that matters most.

Tone:
- I sound like: Direct, warm, treats the customer as a peer,
  comfortable saying "I don't know yet" when true.
- I do NOT sound like: Eager-to-please, apologetic, salesy,
  formal-corporate.

Draft the reply.
```

Notice everything that changes per email is in placeholders. Everything that's *me* — the tone descriptors, the anti-patterns, the structural rules — is locked in.

**Step three: Save them somewhere you'll actually use.** Three options, in order of friction:

1. A simple Notion page or Google Doc titled "Email Voice Library." Free, frictionless, works today.
2. Claude's "Projects" feature on the paid plan — attach a saved instruction to a project named "Email" and it pre-loads every conversation.
3. A snippet manager like TextExpander or Raycast. Type `;cust` to drop the customer template anywhere.

Most learners pick option 1 and it's enough. Don't over-engineer this.

**Step four: Refine through use, not in advance.** Every time a saved template produces a reply that's *almost* right, take 30 seconds to update the template. Add a missing tone descriptor. Add a new anti-instruction ("don't suggest a meeting unless I ask for one"). Within a month, your voice library will sound more like you than anything I could write for you — because it's tuned to *your* actual recurring work.

Let me show you what a mature template looks like. This is the "difficult conversation" prompt one of my consultants uses after six months of refinement:

```
You're helping me draft a reply for a difficult conversation
over email.

Context:
- I'm [my role] at [my company].
- The recipient is [their role + relationship + history].
- The hard thing: [the bad news / pushback / no I have to
  deliver].
- What I'm worried about: [the relationship cost or
  escalation risk].
- What they're likely worried about: [their stakes].

Thread:
[paste the relevant exchange]

Goal:
- Reply length: 4-7 sentences.
- Reply outcome: They walk away knowing where I stand, feeling
  respected, with a clear next step — even if they don't like
  the answer.
- Things to NOT do: Don't soften the no into a maybe. Don't
  apologize for the position. Don't bury the news in
  pleasantries. Don't offer a meeting as a way to delay the
  decision.

Tone:
- I sound like: Calm, direct, comfortable with discomfort,
  willing to name the hard thing first, generous about their
  perspective.
- I do NOT sound like: Apologetic, hedging, over-explaining,
  cheerfully evasive, formal-corporate.

Draft the reply.

After drafting, flag in one sentence: what's the most likely
pushback I'll get to this reply, and how should I prepare for
it?
```

That last line is the kicker. The template doesn't just draft the reply — it forecasts the response. Six months of use, and now her hardest emails come with a built-in second-move plan.

That's the course. You came in spending more time on email than on the work you got hired to do. You leave with a setup that puts Claude next to your inbox, a triage pass that finds the 30% of email that actually needs you, a summarization workflow that kills 20-message threads in 30 seconds, a reply pattern that sounds like you wrote it, and a voice library that makes all of it Monday-morning automatic.

Welcome to the inbox you should've had years ago. I'll see you in the capstone.

### On-Screen / Slide Outline
- **Slide 1 — Title:** "Building Your Email Voice Library."
- **Slide 2 — The Question:** "How do you make this Monday-morning automatic?"
- **Slide 3 — Step 1: Inventory.** Sent folder + Recurring types.
- **Slide 4 — Step 2: The Four-Part Template.** Show the customer check-in template.
- **Slide 5 — Step 3: Save It.** Doc / Project / Snippet — three icons.
- **Slide 6 — Step 4: Refine Over Time.** A 30-second weekly habit.
- **Slide 7 — Mature Example:** The "difficult conversation" template, six months in.
- **Slide 8 — Closing:** "The inbox you should've had years ago."

### Try It Yourself (Exercise)
Open your sent folder. Scroll back two weeks. Pick one type of email you sent more than three times.

Build a four-part template for it:

```
You're helping me draft a reply to a [type of email].

Context:
- [Reusable context with placeholders for the parts that
  change.]

Thread:
[paste the thread]

Goal:
- Reply length: [your typical length for this type].
- Reply outcome: [the reusable outcome you usually want].
- Things to NOT do: [3-5 anti-instructions specific to this
  type].

Tone:
- I sound like: [3-5 tone descriptors — your voice].
- I do NOT sound like: [3-5 tone anti-patterns].

Draft the reply.
```

Save it in a doc called "Email Voice Library." Use it the next time that type of email lands.

**Success criterion:** Within a week, you've used the saved template at least three times and edited it once based on what you learned.

**Common failure mode:** You build a "perfect" template and never use it. Fix: ship a rough version this week and refine through use, not in advance.

### Knowledge Check
1. What's the first step in building your email voice library?
   - a) Sign up for a paid Claude plan
   - b) Inventory your sent folder for recurring email types
   - c) Read three more prompt-engineering articles
   - d) Set up a Notion database with views and filters
   - **Correct: b.** The library is grounded in *your* real recurring work, not theoretical use cases.

2. Why include "Things to NOT do" in the saved templates?
   - a) Because Claude requires it
   - b) Saved anti-instructions encode the AI-tells you've already learned to avoid, so you don't have to remember them each time
   - c) It saves Claude server costs
   - d) It looks more professional
   - **Correct: b.** The whole point of a template is to bake in the lessons you've already learned, including the anti-patterns.

3. What's the right way to refine your templates over time?
   - a) Rebuild from scratch every quarter
   - b) Add a 30-second tweak every time a template produces something *almost* right
   - c) Hire someone to optimize them
   - d) Lock them once saved and never edit
   - **Correct: b.** Iterative refinement through real use beats up-front perfection. A month of small tweaks produces a sharper template than a day of careful design.

### Instructor Notes
- Push learners to ship a *rough* template this week, not a perfect one next month.
- The "difficult conversation" example is your closer — bring real warmth to it on camera. Mention that the "predict the pushback" line is the kind of thing only emerges from real use.
- If running short, skip the "where to save" slide. Google Doc is enough.

---

## 4. Capstone Project

**Brief:**
Open your inbox right now. Find the one thread you've been avoiding — the long one, the politically tense one, the one with an ask you haven't figured out how to answer. You're going to walk through the full **Triage → Summarize → Draft → Refine → Save** workflow with Claude, finishing with a reply you'd actually send and a saved template for the next time this scenario shows up.

**Deliverable:**
A finished email reply (sent or ready to send) that you produced in under 3 minutes of active collaboration with Claude, plus the saved template in your voice library that you'd use the next time a similar email arrives.

**Starter prompt:**
```
You're helping me handle a tough email thread.

Context:
- I'm [my role] at [my company].
- The thread is between [the people on it].
- Relationship state: [warm / strained / new / transactional].
- The hard thing about this thread: [why I've been avoiding it].

Thread:
[paste the full thread]

Step 1 - SUMMARIZE in four labeled sections:
1. THE CURRENT ASK
2. RELEVANT CONTEXT (3-5 facts)
3. DECISIONS ALREADY MADE
4. WHAT'S MISSING

Wait for me to confirm the summary is right before drafting
the reply.
```

After confirming the summary, run:

```
Now draft the reply.

Goal:
- Reply length: [N sentences].
- Reply outcome: [what you want them to do or feel].
- Things to NOT do: [3-5 explicit anti-instructions].

Tone:
- I sound like: [3-5 descriptors].
- I do NOT sound like: [3-5 anti-patterns].
```

Refine surgically. End with: *"What's the most likely pushback to this reply, and how should I prepare for it?"* Then take 60 seconds and turn the prompt into a saved template in your voice library.

**Self-Grading Rubric:**

| Criterion | Strong | Okay | Needs Work |
|---|---|---|---|
| **Summary quality** | Used the four-slot format; summary surfaced something you'd missed; you confirmed it before drafting | Summary captured the main ask but skipped the slots | Asked for "a summary" and got an unactionable paragraph |
| **Reply prompt quality** | Included Context, Thread, Goal (with anti-instructions), and Tone (with anti-patterns) | Three of four slots filled, anti-instructions thin | Vague — "draft a reply that sounds like me" |
| **Final reply** | You'd send it as-is or with 1–2 word tweaks; doesn't have AI-tells | Usable with light editing; one or two AI-tells slipped in | You ended up rewriting most of it manually |
| **Saved to voice library** | New template added to your library, with reusable placeholders + locked-in tone descriptors | Saved a draft template but didn't generalize the placeholders | Skipped the save step |

If you score "Strong" on three of four criteria, the workflow is yours. If not, redo with a different thread — the second pass is usually where it clicks.

---

## 5. Teachable Drip & Email Sequence

**Drip schedule:** Release one lesson every 2 days over 10 days, with the capstone unlocking on day 11. The 2-day cadence gives learners time to actually try each technique on their real inbox between lessons — that's where the workflow installs itself, not in back-to-back binge-watching.

### Email 1 — Lesson 1 release

**Subject:** Lesson 1 is live: Set up your inbox co-pilot in 8 minutes

The reason most people don't use Claude on their actual email is friction. Three minutes of tab-switching and copy-pasting before any work happens, so they stop bothering and the inbox wins.

In Lesson 1 (8 minutes), I'll show you the simple side-by-side setup that makes the round trip one click — and the four-part prompt pattern (Context + Thread + Goal + Tone) you'll use for every workflow in the rest of the course.

[Start Lesson 1 →]

### Email 2 — Lesson 2 release

**Subject:** Stop reading 70% of your inbox

Only about 30–40% of the email in your inbox actually needs you — your judgment, your decision, your reply. The rest is FYI, CC, or stuff a teammate should own. The trouble is, you don't know which is which until you read everything.

In Lesson 2 (10 minutes), I'll give you a single triage prompt that sorts your unread inbox into "needs me now," "can wait," and "ignore or delegate" — in under three minutes flat.

[Start Lesson 2 →]

### Email 3 — Lesson 3 release

**Subject:** Process any 20-email thread in 30 seconds

You know the threads I'm talking about. Twenty replies, three forwards, four people talking past each other, an ask buried somewhere in the middle. Reading the whole thing costs more time than the actual reply ever will.

In Lesson 3 (10 minutes), I'll show you the four-slot summarization prompt that turns any messy thread into a one-screen briefing — current ask, context, decisions made, what's missing.

[Start Lesson 3 →]

### Email 4 — Lesson 4 release

**Subject:** How to write replies that don't sound like AI wrote them

There are tells. The "I hope this email finds you well." The "circling back." The cheerful close that's just a hair too smooth. Recipients clock immediately when AI wrote your email — and trust drops.

In Lesson 4 (10 minutes), I'll show you the two prompt moves that kill the AI-tells: explicit tone anti-patterns and "things to NOT do" anti-instructions. Same Claude. Replies that read as *yours*.

[Start Lesson 4 →]

### Email 5 — Lesson 5 release

**Subject:** Build your email voice library in 15 minutes

You've now got the full workflow. Triage, summarize, reply. The last move turns it from a technique into a system: a small voice library of 3–5 saved templates that match the recurring email scenarios in your week.

In Lesson 5 (8 minutes), I'll walk you through building yours. By Monday morning, this is just how you do email.

[Start Lesson 5 →]

### Email 6 — Completion email

**Subject:** You did it — your inbox just got two hours shorter

You finished. Genuinely — most people who start a free course don't, so well done.

You came in spending more time on email than on the work you got hired to do. You leave with a setup that puts Claude next to your inbox, a triage prompt that finds the 30% of email that actually needs you, a summarization workflow that kills 20-message threads in 30 seconds, and a reply pattern that sounds like *you* wrote it.

If this clicked, the next step is simple: use it tomorrow morning. Open your inbox, run the triage prompt, and see how much time you save.

When you're ready for more, I send a short weekly newsletter with one new Claude workflow each Friday — drawn from real work I'm doing with operators like you. Free to join.

[Join the newsletter →]

Thanks for trusting me with five lessons of your time.

---

## 6. SEO & Discovery

**Keyword phrases:**
1. how to use claude ai for email
2. claude ai for gmail and outlook
3. inbox management with ai
4. ai email assistant for non-developers
5. how to summarize long email threads with claude

**Meta description (≤155 chars):**
Free 5-lesson course on using Claude with Gmail and Outlook. Triage, summarize, and reply to email faster — without code, automation, or IT approval.

**Social posts:**

*LinkedIn:*
Most knowledge workers spend more time on email than on the work they got hired to do. The fix isn't an automation tool. It's a workflow.

I just released a free 5-lesson course on using Claude alongside Gmail or Outlook. By the end you can triage your morning inbox in three minutes, summarize a 20-email thread in thirty seconds, and draft replies that sound like you actually wrote them.

No code, no IT approval, no "send to inbox" risk. You stay in control. Claude does the heavy lifting.

Built for operators, founders, and consultants. Link in comments.

*X / Twitter:*
You don't need an email automation tool.

You need a workflow that lets Claude triage, summarize, and draft alongside Gmail or Outlook — without ever sending on your behalf.

Made a free 5-lesson course on exactly that. Link below.

*Substack note:*
New free course is live: *Inbox Mastery — Claude in Gmail and Outlook.*

Five short lessons. By the end you can process any 20-email thread in under three minutes — read what matters, draft a reply that sounds like you, and clear it from your queue.

Built for the operators, founders, and consultants who live in their inbox and want their afternoons back. No code, no IT approval, no automated sending. Claude is your co-pilot, not your auto-pilot.

Comments open if you take it — I read everything.
