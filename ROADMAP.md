# Roadmap

Built one version at a time so each piece can be reviewed before the next begins. Decisions marked DECIDED are settled; OPEN ones need an answer before that version starts.

## v0.1 — Packaging and honest scoring (this version)

- Repository skeleton: README, LICENSE (MIT), ETHICS, this roadmap, changelog.
- Personal data separated from tool: the repo ships no profiles, resumes, or trackers.
- **Transparent match score and ranked list.** Six dimensions (core-skill, level, domain, location, mission, screen-clearance), 0-3 each, rolling to an /18 that ranks within the existing Strong / Stretch / Skip bands. A zero on core-skill, level, or screen-clearance caps a role at Stretch. DECIDED: show the six sub-scores and the /18 total always together, never a bare number or a percentage.

## v0.2 — Story bank and anti-boilerplate cover notes (SHIPPED)

Notes that are personal and specific because the personal material is captured once and reused, and easy because only the employer hook is researched fresh each time.

- **The hard rule:** a draft never restates the job description. About the candidate and this specific employer, not a mirror of the requirements. No "I am writing to express my interest," no walking the five bullets.
- **Story bank** (`references/story_bank.md`): DECIDED as **seeded from the resume, then filled out through a short interview**, and grown as she applies. Three to five situation-task-action-result stories, each with its honest owner-vs-adjacent framing. Same bank feeds interview prep in v0.5.
- **Cover note generator** (`references/cover_note.md`): a researched true hook, one story that proves the central requirement, one tailored claim, a close. Two lengths from the same inputs (short application email and a formal letter). New Draft mode (Step C) plus a Step A5b seeding step.
- **Honesty guardrails:** the hook must be real, the story must respect its framing, and if the candidate has no genuine reason to want the job the tool says so rather than manufacturing enthusiasm.

## v0.3 — Gap study plans (SHIPPED)

- The scan offers a study plan only when a gap is both **recurring** (caps two or more wanted roles) and **bounded** (closes in a quarter or a year).
- The offer surfaces in the **weekly-summary run** (default Monday, or first run of a new week), not the daily note. Callable **on demand** any time.
- On demand it infers the target from what she gives it: a named skill, a specific role, or nothing (then it picks the highest-leverage recurring gap from her scan history). Natural-language triggers ("what should I study," "make me a study plan," "how do I qualify for [role]"). New Plan mode (Step D).
- `references/study_plan.md`: target as a demonstrable artifact, why-this-gap, month-by-month real resources with time costs paced to her available hours, a portfolio artifact as the endpoint, and a re-assessment checkpoint. Skeptical of certifications by default.
- Setup interview gained one question: realistic hours per week available for upskilling.

## v0.4 — Legitimacy screen and consistent fit rationale (SHIPPED)

- **Ghost-job and scam check** on each new posting (`references/legitimacy_check.md`): is the company real and operating, is the req live and recent, does the comp band make sense, is it a direct hire or a staffing-firm repost, are there scam signals. Runs as part of link verification; a caution is attached to anything not clean, and a clear scam stays out of the ranked list.
- A consistent one-line **why-you-fit** rationale on every ranked role, paired with the gap, so the picture is honest in both directions.

## v0.5 — Interview preparation (SHIPPED)

- New Interview mode (Step E) and `references/interview_prep.md`. Grounded in the profile, the story bank, and the specific job description.
- Maps likely questions to the real stories that answer them, gives her specific questions to ask, names the thin spots with an honest way to handle each, and adds logistics for the format (screen, panel, onsite). Flags a likely question with no story as a gap, not a blank to bluff.

## v0.5.1 — Directional gap line in the scan (SHIPPED)

A small enrichment of the already-shipped scan, not part of the discovery-to-offer loop below, so it slots ahead of v0.6 without disturbing that sequence.

- The scan already shows a fit score and a named gap per role (v0.4). This turns the gap forward: a one-line pointer on a sub-Strong role that names what closing the gap would do, tied to the dimension holding the role back. Example: "close the healthcare-domain gap and this moves from Stretch to Strong."
- DECIDED (2026-07-11): **directional line only.** The line points, it does not pitch a curriculum. It states what would raise the fit rating using the gap the scan already computed. The full study plan stays on demand and in the weekly summary, exactly as v0.3 set it up.
- Guardrails carry over unchanged: the line appears only where the gap is real and nameable, never as a course pitch (ETHICS principle 6), and the daily note still does not offer or generate a plan. The rating it points at is this scan's ranking, not a promise from the employer, so the wording stays honest ("closing this clears the screen," not "study this and you are hired").

## v0.5.2 — Tunable study plans (SHIPPED)

A refinement of the v0.3 study plan surfaced while testing v0.5.1: the directional line points at a specific studiable skill, and "what do you recommend" turns it into a plan whose shape is set by a tunable time budget.

- Time budget is the primary input: default from setup, overridable on the spot (15 minutes a day, four hours a day), asked once if unknown.
- The budget changes the plan's composition, not just its length. Lean, steady, and immersive bands assemble differently. Re-tuning recomposes rather than rescales.

## Road to 1.0 — Close the loop through the offer

The target for 1.0 is to touch the whole search from discovery to accepting an offer, so the tool goes quiet nowhere in the middle. Rather than ship that as one batch, it is sliced into five reviewable releases (v0.6 through v1.0), each a tight theme that can be built and reviewed before the next begins. Ordering follows dependency: the pipeline spine comes first because most other beats hang off knowing application state, and the bounded network feature closes the loop as 1.0. This re-sequences the committed v1.0 work; it adds no scope.

Candidates come from product-discovery interviews; a full backlog with underlying needs is maintained in [docs/BACKLOG.md](docs/BACKLOG.md).

Two spine themes underpin the releases below:

- **Pipeline orchestration as working-memory offload.** A person cannot hold more than a few applications in their head, so the tool holding the whole search (state of every application, the next action for each, timing across competing processes, capacity) is a core job, not a convenience. Lands in v0.6.
- **An adjustable intervention dial.** How much the tool coaches, nudges, and diagnoses is a user setting, light-touch by default, tunable up or down. It governs the funnel diagnosis and the encouragement nudge, so it lands with them in v0.9.

### v0.6 — Pipeline spine (SHIPPED)

The working-memory offload everything downstream depends on.

- **Application tracking across many:** hold the state of every parallel application, the next action for each, timing across competing processes, and capacity.
- DECIDED (2026-07-11): build pipeline state into kochab rather than extend the standalone `job-application-tracker` skill. The road to 1.0 keeps the whole search inside one spine so state stays consistent and the downstream beats (follow-up timing, post-call actions, funnel diagnosis) read and write one source of truth. Whether the standalone `job-application-tracker` skill is later folded in or deprecated is a separate question, not a blocker for v0.6.
- Shipped as a three-table `Application_Tracker.md` (Active / Watching / Closed), a Stage vocabulary (Applied, Screen, Interview, Final, Offer), a per-row next action and due date, a capacity target set at setup, a timing view that surfaces collisions across live processes, and a new Pipeline mode (Step F). Deliberately bounded to holding and showing state: follow-up timing is v0.7, stage guidance v0.8, funnel diagnosis v0.9. Full model in `references/pipeline.md`.

### v0.7 — Momentum (SHIPPED)

Keeping the search moving once applications are in flight. Sits directly on the v0.6 tracker.

- Getting applications out the door (closing the gap between drafted and sent).
- Follow-up timing (when to nudge after applying or interviewing, without pestering or going silent).
- Post-call next actions.
- Triage a high-fit role the user is not interested in, declined without friction or guilt.
- Shipped as a new Momentum mode (Step G) and `references/momentum.md`: drafted-not-sent surfacing (with a Notes column added to the Watching table), a conservative default follow-up cadence (about a week after applying, capped at two nudges, employer timelines always win, easy off switch), a short post-call capture routine, and one-step triage to a Declined close. Suggestions only; the tool never sends or submits. Light-touch by default, since the adjustable intensity dial is v0.9. Follow-ups surface on request and on the weekly-summary run, never in the daily note.

### v0.8 — Stage guidance (SHIPPED)

What each stage expects and how to be ready for it.

- Prep for the first call (recruiter or hiring-manager screen).
- Phase-by-phase guidance (what a given stage expects and what comes after).
- Interview prep across formats, extending v0.5 (one-off screen to panel battery to onsite).
- References: best and bad practices (who to ask, when, how to brief them).
- Shipped as a new Stage-guidance mode (Step H) and `references/stage_guidance.md`: a phase-by-phase map keyed to the pipeline Stage vocabulary (Applied, Screen, Interview, Final, Offer) giving each stage's purpose, what it expects, how to be ready, and what comes next, plus a references section (who to ask, when, how many, how to brief truthfully, best and bad practices). Interview prep (Step E, `references/interview_prep.md`) was extended to be format-aware across recruiter screen, hiring-manager screen, panel, and onsite. Decision: formats extend the v0.5 interview reference; the phase map and references land in a new stage-guidance reference, rather than a second interview file. Boundaries held: the Offer stage slows her down and hands off to v0.9 (negotiation, funnel diagnosis, rejection recovery, rescinding), and references stay distinct from v1.0 network outreach. No bluff coached at any stage.

### v0.9 — Offer and process health (SHIPPED)

The highest-stakes moments, plus the tool learning from the user's own search.

- Offer handling and negotiation.
- Recovering from a rejection (metabolize it and keep moving).
- Rescinding an application cleanly, without burning a bridge.
- Light funnel diagnosis from the user's own data (where things stall, what converts), without preaching.
- The **adjustable intervention dial** ships here, since it governs the funnel diagnosis and the v1.0 encouragement nudge.
- Shipped as Offer mode (Step I, `references/offer.md`) and Process-health mode (Step J, `references/process_health.md`), plus the dial (`references/intervention_dial.md`). Offer handling slows the moment down, evaluates the whole package against her stated priorities and floor, and drafts an honestly-anchored counter she sends herself (never fabricated leverage, not legal or tax advice). Process health covers rejection recovery (accurate framing, no negative-self-talk reinforcement, step back for genuine distress), clean rescinding (a gracious withdrawal note, no burned bridges), and light funnel diagnosis over her own tracker (self-declines counted separately, honest about thin samples per ETHICS 4, one lever not ten, no preaching). The intervention dial (light default / standard / high) is a Master_Profile setting, captured at setup and tunable on request, that governs momentum nudge intensity and funnel proactivity and pre-registers the v1.0 encouragement nudge; it changes how much the tool speaks, never whether it tells the truth. Boundary held: network and the encouragement nudge remain v1.0.

### v1.0 — Network, bounded (SHIPPED)

The capstone that closes discovery-to-offer, carrying the sensitive data handling that earns the 1.0 stamp.

- Match contacts against target employers to surface "you know someone here," **intent-gated** (fires when the user signals they want to apply, never a blanket scan of all jobs).
- How and when to engage the network (timing and framing that lower the barrier to outreach).
- An optional, honest **encouragement nudge** for users who chronically feel under-qualified: name a warm contact to lower the barrier, but only where they are genuinely qualified.
- DECIDED: contacts come from the user's own LinkedIn data export or are pasted in, never scraped or read behind a login (see ETHICS principle 2); the export is parsed locally and stays in the user's folder.
- Shipped as Network mode (Step K) and `references/network.md`. Contact intake from a LinkedIn `Connections.csv` export or a paste, parsed locally into `Contacts.md` (added to `.gitignore`, never committed, never transmitted). Intent-gated matching against one employer she signals intent to apply to, never a blanket scan and never in the daily scan. Warm-outreach framing (ask for insight, not a job) with a draft note she sends herself. The optional encouragement nudge is dial-governed (off at light default) and fires only on a role she genuinely qualifies for. The tool never scrapes, never messages a contact, and never invents or inflates a tie. This completes the discovery-to-offer loop; MVP through 1.0 is feature-complete.

### Release readiness (still open before going wide)

The features are done; these supporting activities (see the section below) are the remaining gate before Kochab is shared widely, and are deliberately not part of the v1.0 feature build: the cleanup pass, git infrastructure for sharing (including per-release tags, which still need a real terminal), free socialization, generalizability validation against a non-Brian persona, and a final check of the user instructions. Sequence and ownership to be set now that 1.0 is reached.

### Release readiness (supporting activities before 1.0 goes wide)

Not features, and they do not slot into a version above, but they gate sharing Kochab widely and should be tracked alongside the final releases. Recorded here as a standing reminder; sequence and ownership to be set when the road to 1.0 is close.

1. **Cleanup pass.** Find and clear anything unfit for a public repo before sharing: stray personal data, dead files, inconsistent naming, half-finished references, anything that bends the no-personal-data rule. The fixtures are a Brian-shaped dry-run and must read as clearly synthetic.
2. **Git infrastructure for sharing.** Configure the repo to be shared: license present (done), a sensible `.gitignore` that keeps personal folders out, clean history with no committed personal data, a tag per release, and a contribution path that points at `ETHICS.md` as the hard wall.
3. **Free socialization.** Decide how to get the tool in front of people with no paid promotion: the channels already in the target list (aisafety.com, 80,000 Hours community, relevant Slacks and forums), a plain writeup, word of mouth. No paid ads.
4. **Generalizability validation.** Prove it works for someone who is not Brian. The profile, fixtures, and examples are all shaped by one search; build at least one distinct synthetic persona (different field, level, and constraints) and run the whole loop against it to confirm nothing is secretly hard-coded to this case.
5. **User instructions.** Confirm thorough, honest setup-to-first-scan instructions exist for a new user: what to install, how to point it at a folder, what the setup interview covers, how the scheduled scan works, and where their data lives. `docs/Getting_Started.md` and `docs/WALKTHROUGH.md` exist; verify they are complete and match shipped behavior.

## Post-1.0 — Beyond the offer

First-day and onboarding prep; general skill and career augmentation; promotions; moving jobs; changing careers. Plus a people/relationship CRM (track interviewers, referrers, what was said, and follow-ups owed), search-while-employed vs. quit-and-search decision support, and handling a large resume gap (adjacent to existing tailoring and honesty guardrails, so it may pull earlier).

## Deliberately out of scope, permanently

Auto-submitting applications. Scraping behind logins or around bot detection. CAPTCHA circumvention. Numeric fit scores presented as objective measurements. Any resume tailoring that fabricates. These are the patterns the project defines itself against; see [ETHICS.md](ETHICS.md).

## Borrowed-from analysis

The survey of the leading open-source tools (ai-job-search, career-ops, Resume-Matcher, ApplyPilot, autopilot-jobhunt) that informed v0.3 and v0.4 lives in [docs/Design_Brief_v2_Scoring_and_StudyPlans.md](docs/Design_Brief_v2_Scoring_and_StudyPlans.md).
