# Design Notes: Scoring, Study Plans, and What We Borrowed

Rationale behind the v0.1 scoring model and the v0.2 study-plan design, plus the survey of existing tools that informed them. Written to explain the *why* to anyone forking this.

---

## The principle these features have to survive

The suite's one durable advantage over the popular job-search agents is that it will say "nothing today" and "you do not clear this screen." Every tool in the field slaps a confident number on a job; this one tells the truth about fit. A scoring feature that manufactures false confidence would trade the moat for a gimmick.

The rule for everything here: **a number may rank, but it may never be the verdict.** The named-gap sentence stays. The score orders a list and shows its work; it does not replace judgment with arithmetic.

## The match score (v0.1)

Six dimensions, 0-3 each, every point traceable to a reason: core-skill match, seniority/level fit, domain fit, location/logistics, mission/values, screen-clearance. Full rubric in `skills/kochab/references/scan_protocol.md`.

Roll-up out of 18 into the existing Strong / Stretch / Skip bands, with a capping rule: a zero on core-skill, level, or screen-clearance holds a role at Stretch no matter how high the total. A role someone loves but cannot do is not a Strong. The raw /18 orders roles within a band, so the ranked list is finer than three buckets without inventing precision.

Presentation shows the six sub-scores and the total together, always. No 0-100, no percentage, no decimal, because those read as measurements when they are language-model judgments.

## The study plan (v0.2)

The gap analysis (`skills/kochab/references/gap_analysis.md`) already produces Emphasize, Build, and a recurring-gap watch. The study plan sits on top: when a gap is both **recurring** (blocks two or more wanted roles) and **bounded** (closes in a quarter or a year), the scan offers a plan. A one-off gap is named and left alone; a pattern earns the offer.

The offer surfaces in the weekly summary, not the daily note, and can be requested on demand. The plan itself names the target as a demonstrable artifact rather than a certificate, lists real web-searched resources with time costs, and ends with a re-assessment checkpoint. It is skeptical of certifications by default.

## What we surveyed, and what we took

The leading open-source job tools as of mid-2026:

- **ai-job-search** (Claude Code framework): setup, scrape, evaluate, draft, a second reviewer agent, revise, compile-and-inspect the PDF. Its `/upskill` gap heatmap with a learning plan and time estimates directly informed the study-plan design.
- **career-ops** (agent-skill CLI): A-F evaluation across weighted dimensions, an explicit "recommend against applying below threshold," a posting-legitimacy and ghost-job check, a persistent story bank, a single-source-of-truth tracker.
- **Resume-Matcher** (web app): keyword/ATS match highlighting, interview-prep generation, a master-resume concept.
- **ApplyPilot** (autonomous browser agent): multi-source discovery across boards and career sites; also the clearest anti-pattern, marketed on "applied to 1,000 jobs in 2 days," with auto-submit and CAPTCHA-solving.
- **autopilot-jobhunt** (nightly cron): 0-100 LLM scoring, push alerts with a one-line rationale per job.

**Adopted or planned:** the weighted-dimensions idea (rebuilt honestly as the six sub-scores), the `/upskill` learning plan (v0.2), the legitimacy/ghost-job screen and a consistent "why you fit" line (v0.4), the story bank and interview prep (v0.3 and v0.5).

**Deliberately refused:** auto-submission, scraping behind logins or around bot detection, CAPTCHA circumvention, numeric scores presented as objective, and any tailoring that fabricates. These are the patterns the project defines itself against; see `../ETHICS.md`.
