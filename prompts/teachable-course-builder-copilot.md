COPILOT COURSE‑BUILDER PROMPT (TEACHABLE‑READY)
COPY AND PASTE INTO COPILOT.
Replace the items in [brackets] with your specifics.
This prompt is designed to produce a complete, paste‑ready Teachable course on any expert‑prompting skill for Microsoft Copilot.
It uses a structured, multi‑phase workflow so Copilot thinks before it writes, plans before it drafts, and produces consistent, high‑quality instructional content.
---
Role & Context
You are a senior instructional designer who builds high‑conversion Teachable courses for non‑technical professionals. You also have deep, hands‑on expertise in writing expert‑level prompts for Microsoft Copilot across email, documents, meetings, research, and daily workflows.
Your job is to produce an end‑to‑end, Teachable‑ready course package that teaches non‑technical knowledge workers (operators, founders, consultants, marketers, ops leads) how to structure expert prompts for Copilot on a specific topic.
The learner has no coding or prompt‑engineering background and limited patience for jargon. They are smart, busy, and skeptical of “AI hype.” Every lesson must be plain‑language, example‑led, and immediately useful in their day job.
---
<course_inputs>
<course_topic>
[The expert‑prompting skill this course teaches, e.g., “writing prompts that turn messy notes into polished emails”]
</course_topic>
<learner_outcome>
[The single concrete outcome a learner can achieve by the end, e.g., “Turn any rough draft into a clear, confident email in under 5 minutes using Copilot.”]
</learner_outcome>
<course_length>
[default: 5 lessons, ~10 minutes each]
</course_length>
<author_voice>
[optional: a sentence or two on how you sound, e.g., “Collaborative, systems‑oriented, slightly witty, uses real client stories.”]
</author_voice>
</course_inputs>
---
Phase 1: Plan Before You Write (Think Step by Step)
Before producing any course content, think through the following inside  tags.
This is your scratchpad — the learner will never see it.
Inside <planning>:
1. Audience reality check
Describe the non‑technical learner in one paragraph.
What does their workday look like?
What have they already tried with Copilot (or ChatGPT) and where did it fall short?
What’s the “aha” they need?
2. Outcome decomposition
Break the <learner_outcome> into 4–6 underlying micro‑skills, in dependency order.
3. Anti‑curriculum
List 3 things this course will not cover — and why excluding them makes the course stronger.
4. The single prompt pattern
Name and describe the one core prompt pattern the course is teaching.
Use a Copilot‑friendly pattern such as:
Role + Goal + Inputs + Constraints + Steps + Output Format
5. Hook test
Draft 3 candidate one‑sentence hooks for the course landing page.
Pick the strongest and explain why in one line.
Close the <planning> tag.
---
Phase 2: Course Package (The Deliverable)
Now produce the full course as Markdown, ready to paste into Teachable.
Use the exact section structure below.
Do not skip sections.
Do not add commentary outside the sections.
---
1. Teachable Marketing Copy
Course Title
(max 60 characters, benefit‑led, no colons‑and‑subtitles cliché)
Subtitle / Promise
(one sentence, names the outcome and the audience)
Course Description
(120–180 words, written directly to the learner in second person, ends with the concrete outcome)
You’ll Learn
(5 bullets, each starts with a verb, each names a tangible skill)
This Course Is For You If…
(3 bullets describing the learner’s situation)
This Course Is NOT For You If…
(2 bullets — be honest, this builds trust)
Prerequisites
(Be explicit that no coding or prompt‑engineering experience is needed)
Instructor Bio Hook
(2 sentences the author can drop into their Teachable bio)
---
2. Course Outline
A numbered list of all lessons.
For each lesson, include:
• Lesson number
• Title
• One‑sentence description
• Runtime estimate
• The micro‑skill from Phase 1 delivers
---
3. Full Lessons
For each lesson in the outline, produce the following block.
Use ## Lesson N: [Title] as the header so it pastes cleanly into Teachable.
<lesson_template>
Lesson N: [Title]
Runtime: [estimate]
Learning objective: “By the end of this lesson, you will be able to…”
Lesson Script
A spoken‑style script that the instructor can read aloud or lightly edit.
Plain language. Short sentences. Second person (“you”).
Include natural pauses and signposts (“Here’s the key idea…”, “Let’s try it together…”).
Length: 600–900 words.
The script must:
• Open with a 2–3 sentence hook tied to a real workday frustration.
• Introduce or reinforce the single core prompt pattern from Phase 1.
• Walk through one fully worked Copilot prompt example relevant to <course_topic>.
Show the prompt in a fenced code block.
Then show a strong Copilot response in a fenced block.
Then explain why the prompt worked — name the specific technique (role, constraints, steps, output format, etc.).
• Close with a one‑sentence bridge to the next lesson.
On‑Screen / Slide Outline
A bulleted list of 5–8 slide ideas matching the script beats.
Each bullet is a slide title plus one line of supporting text.
No slide should be a wall of words.
Try It Yourself (Exercise)
Include:
• The setup (1–2 sentences)
• The exact starter prompt in a fenced code block
• The success criterion (“You’ll know it worked when…”)
• One common failure mode and how to fix it
Knowledge Check (Quiz)
Three multiple‑choice questions.
Each has 4 options, one correct answer, and a one‑sentence explanation.
Instructor Notes
2–3 bullets of behind‑the‑scenes guidance for the author.
</lesson_template>
---
4. Capstone Project
Include:
• Brief (3–4 sentences describing the scenario)
• Deliverable (what the learner will have at the end)
• Starter prompt (fenced code block they can copy and adapt)
• Self‑grading rubric (4 criteria, each with strong/okay / needs work descriptors)
---
5. Teachable Drip & Email Sequence
Drip schedule
Recommend a release cadence (e.g., one lesson every 2 days) and justify it.
5 short lesson‑release emails
Each includes:
• Subject line
• 60–100-word body
• One CTA back to the course
1 completion email
Subject line + 80–120 word body
Congratulate the learner and offer a soft next step.
---
6. SEO & Discovery
• 5 keyword phrases
• Meta description (155 characters max)
• 3 social post variants (LinkedIn, X, Substack) in the tone defined in <course_inputs>
---
Phase 3: Quality Bar (Self‑Check Before You Finish)
After drafting, review your output against this checklist inside <self_check> tags.
If any item fails, revise before delivering the final version.
Checklist:
• Every lesson includes at least one fully worked Copilot prompt example with a sample response.
• The same core prompt pattern from Phase 1 is named and reinforced in every lesson.
• No lesson assumes coding, API access, or prior prompt‑engineering knowledge.
• Jargon is near zero; any unavoidable term is defined plainly.
• Every exercise is doable in under 10 minutes inside Copilot.
• The capstone produces the exact <learner_outcome>.
• Marketing copy avoids hype words (“unlock,” “supercharge,” “game‑changer,” “revolutionize”).
• The course could be published on Teachable today with no additional editing.
---
END OF COPILOT COURSE‑BUILDER PROMPT
