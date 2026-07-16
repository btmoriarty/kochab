# Changelog

## Unreleased — 2026-07-11

Maintainer tooling and backlog.

- Added a **release-readiness** reminder to `ROADMAP.md` (cleanup pass, git infra for sharing, free socialization, generalizability validation, thorough user instructions): supporting activities that gate sharing Kochab widely as it approaches 1.0. Not features; recorded so they are not lost.
- Sliced the single v1.0 batch into five sequenced releases (v0.6 through v1.0) in `ROADMAP.md`, ordered by dependency: v0.6 pipeline spine, v0.7 momentum, v0.8 stage guidance, v0.9 offer and process health, v1.0 network. Re-sequences committed work only; adds no scope. Resolved two open questions in the process: the intervention dial now lands in v0.9 (with the funnel diagnosis and nudge it governs), and the tracker-overlap question is DECIDED: v0.6 builds pipeline state into kochab rather than extending the standalone `job-application-tracker` skill, so the whole search stays in one spine with one source of truth. `docs/BACKLOG.md` row statuses updated from `Planned (v1.0)` to the specific release each beat now lands in.
- Added `docs/BACKLOG.md`, the canonical feature backlog, seeded from the v1.0 and post-1.0 roadmap candidates with the need under each want, plus intake steps for folding in `roadmap-interview` output.
- `roadmap-interview` now targets `docs/BACKLOG.md` (previously an unspecified `Feature_Backlog.md` in the working folder); `SKILL.md`, `references/output_template.md`, `ROADMAP.md`, and `AGENTS.md` updated to match. Repackage `roadmap-interview.skill` on next release.
- Added `AGENTS.md` (maintainer standing orders) and `docs/RELEASING.md` (release checklist).
- Added `fixtures/kochab-test/` synthetic test data for testing without real personal data.

## v1.0 — 2026-07-13

Network, bounded. The capstone that closes the loop from discovery to offer, carrying the sensitive contact-data handling that earns the 1.0 stamp. MVP through 1.0 is feature-complete.

- New **Network mode** (Step K) and `references/network.md`. A warm introduction beats a cold application; when she is genuinely going to apply somewhere, the tool surfaces whether she already knows someone there and helps her reach out well.
- **Contacts are her own data, never a scrape.** Intake is from her own LinkedIn data export (`Connections.csv`) or a paste, parsed locally into `Contacts.md` in her folder. The tool never scrapes LinkedIn and never reads a network behind a login (ETHICS principle 2); if asked to, it explains it cannot and points her to the export. `Contacts.md` and `Connections.csv` were added to `.gitignore`; the contact data never leaves her folder and is never committed (ETHICS principle 5).
- **Intent-gated matching.** Matching runs only for a specific employer she has signaled she wants to apply to, never a blanket scan across all roles, and the daily scan never touches the contact list. It surfaces real overlaps (who, title, how she knows them) or says plainly there is no one; it never invents or inflates a tie. A guardrail in `SKILL.md` enforces that the scan does no network matching.
- **How and when to engage.** Warm framing tied to real intent: ask for insight or a conversation, not a job, and respect that a referral is the contact's to offer. The tool drafts a short note in her voice, honest about the relationship's real closeness; she sends it. It never messages anyone (ETHICS principle 1).
- **Encouragement nudge (optional, honest, dial-governed).** Off at the light default; where the dial permits or she opts in, and only on a role her own assessment rates Strong or that clearly clears the screens, it names a warm contact to lower the barrier for someone who chronically feels under-qualified. Never on a role she does not qualify for, never a badger, a door not a push. `references/intervention_dial.md` updated from pre-registered to shipped.
- Added a clearly-synthetic `fixtures/kochab-test/Contacts.md` to test matching. Updated `skills/kochab/SKILL.md` (description, mode detection, new Step K, network guardrail) and `references/intervention_dial.md`. Repackaged `kochab.skill`.
- **Release readiness remains open** (not a feature build): the cleanup pass, git infrastructure and per-release tags, free socialization, generalizability validation against a non-Brian persona, and a final user-instructions check are the gate before Kochab goes wide. Recorded in `ROADMAP.md`.

## v0.9 — 2026-07-13

Offer and process health. The highest-stakes moments, plus the tool learning from the user's own search, and a dial for how present it is.

- New **Offer mode** (Step I) and `references/offer.md`. Slows the moment down (get the whole offer in writing, a day or two to consider is normal), evaluates the full package against her stated priorities and floor rather than a generic ideal (mission-first stays mission-first; the two-year test for grant-funded roles), and helps her negotiate: anchor only on something real, ask for the one or two things that matter, know the walk-away. Drafts the counter in her voice; she sends it. Never fabricates leverage, never negotiates for her, and defers legal or tax questions to a professional.
- New **Process-health mode** (Step J) and `references/process_health.md`, three beats:
  - *Recovering from a rejection.* Acknowledge it plainly and briefly, keep the framing accurate (a fit decision at one moment, not a verdict on her worth), never agree with or amplify harsh self-talk, capture real feedback but do not invent a lesson. If she signals more than ordinary disappointment, drop the mechanics and point to real support.
  - *Rescinding cleanly.* Withdraw early and directly instead of ghosting; a short, warm note with no grievances aired. Drafts it; she sends it; the role moves to Closed (Withdrawn).
  - *Light funnel diagnosis.* Reads her own tracker (Active and Closed) for where she stalls and what converts, counting self-declines and withdrawals separately from rejections. Honest about thin samples (no false precision, per ETHICS 4), names a real pattern without preaching, ends in at most one lever. Never grades her or predicts odds.
- New **adjustable intervention dial** (`references/intervention_dial.md`), the spine theme that governs how present the tool is. A Master_Profile **Intervention level** setting (light default / standard / high), captured at setup (question 11c) and changeable on request ("dial the coaching up/down"). It governs momentum nudge intensity and funnel-diagnosis proactivity, and pre-registers the v1.0 encouragement nudge. Light preserves prior behavior exactly, so nothing changes for anyone who does not touch it. The dial changes how much the tool speaks, never whether it tells the truth: no setting softens a gap, inflates a fit, or overrides an honesty guardrail, a nudge cap, an off switch, or the ETHICS floor.
- Wired the dial through existing behavior: `references/momentum.md` (follow-up intensity now dial-governed, caps and off switch hold at every setting), `references/scheduled_task_template.md` (weekly-summary run keeps the follow-ups line at every level, matching the interactive path, and adds a funnel read only at high), and the Master_Profile section list in `SKILL.md` (A5). Added an Intervention level to `fixtures/kochab-test/Master_Profile.md` and enriched the tracker's Closed rows so funnel diagnosis has signal.
- **Boundary held:** network matching and the encouragement nudge remain v1.0; the dial only pre-registers the latter. ETHICS principle 1 holds throughout: the tool drafts offer counters, rejection responses, and withdrawal notes; a human sends them.
- Updated `skills/kochab/SKILL.md` (description, mode detection, A5, Step G dial reference, new Steps I and J), plus `references/momentum.md`, `references/setup_interview.md`, `references/scheduled_task_template.md`. Repackaged `kochab.skill`.

## v0.8 — 2026-07-13

Stage guidance. Orienting her in the process: what each stage expects and how to be ready for it.

- New **Stage-guidance mode** (Step H) and `references/stage_guidance.md`. A phase-by-phase map keyed to the pipeline Stage vocabulary (Applied, Screen, Interview, Final, Offer): each stage's purpose, what it expects of her, how to be ready, and a one-line look at what comes next, so nothing surprises her. Answers "I am at X, what now."
- **Prep for the first call.** The recruiter and hiring-manager screen are called out as the cheapest filter, the one that cuts good candidates on avoidable things: weight the crisp why-this-role, a comp range tied to her floor, and a clean account of where she is coming from.
- **Interview prep across formats.** Extended the v0.5 interview reference (Step E, `references/interview_prep.md`) with a "Prep by format" section covering recruiter screen, hiring-manager screen, panel or sequential one-on-ones, and onsite/final, each with its own emphasis and logistics. The question-to-story mapping is the same at every stage; what changes is weight and stamina.
- **References handling.** Who to ask (people who genuinely saw her work, chosen for relevance, never anyone who would have to inflate), when (before they are needed, at the final-round signal), how many, how to brief them truthfully, and closing the loop. Short best and bad practices list. Kept distinct from v1.0 network outreach, which draws on different data.
- **Design decision:** formats extend the existing interview reference; the phase map and references land in a new stage-guidance reference, rather than a second interview-prep file. Avoids duplication and keeps Step E about preparing a specific interview while Step H orients around it.
- **Boundaries held for v0.9:** the Offer stage slows her down and hands off; offer negotiation, funnel diagnosis, rejection recovery, and clean rescinding are v0.9. No bluff coached at any stage; the honesty guardrails apply to how she talks about her record throughout.
- Updated `skills/kochab/SKILL.md` (description, mode detection, Step E format point, new Step H), `references/interview_prep.md` (Prep by format section). No tracker schema change, so `fixtures/` are unchanged. Repackaged `kochab.skill`.

## v0.7 — 2026-07-13

Momentum. Acting on the v0.6 pipeline to close the quiet gaps where a search stalls.

- New **Momentum mode** (Step G) and `references/momentum.md`, covering four beats that all read and write the one tracker. Everything is a suggestion she acts on; the tool never sends, submits, or contacts anyone. Light-touch by default, since the adjustable intensity dial is v0.9.
- **Getting applications out the door.** Surfaces drafted-not-sent roles: what is left, the real posting deadline if any, and an offer to finish the draft. A **Notes column** was added to the Watching table to carry that between-scan-and-send state ("cover note drafted, not sent").
- **Follow-up timing.** Suggests when to reach out and offers to draft the note. Conservative default cadence: a light check-in about a week after applying and at most one more, then rest; a thank-you within a day after a call, then a status check on the employer's stated timeline or about a week if none was given. An employer-stated timeline always wins. Capped at two nudges per waiting period, honors "no follow-ups on this one," never guilt-trips a passed date.
- **Post-call next actions.** A short capture right after she reports a call: advance the stage, set a thank-you as the immediate next action, schedule the next touch from their timeline, note one line on how it went. Captures and schedules only; how to run the next round is stage prep (v0.8).
- **Triage a role she is not interested in.** "I'm not interested in X" moves the row to Closed with outcome Declined in one step, optionally with a one-line reason for the search history, no arguing a high fit back at her. Declining frees capacity.
- **Cadence discipline held.** Follow-ups surface in Momentum and Pipeline status on request, and once a week on the weekly-summary run as a "follow-ups coming due" line, never in the daily note (v0.3 anti-nag cadence). ETHICS principle 1 holds throughout: the tool drafts and suggests; a human sends.
- **Scope boundaries kept for later releases:** no stage coaching (v0.8), no funnel diagnosis, no rejection recovery, no clean rescinding, and no intensity dial (all v0.9).
- Updated `skills/kochab/SKILL.md` (description, mode detection, B5 weekly line, B6 Watching columns, new Step G), `references/pipeline.md` (follow-up cross-references, Watching Notes column). Updated `fixtures/kochab-test/Application_Tracker.md` to exercise a drafted-not-sent row and an applied-no-response row. Repackaged `kochab.skill`.

## v0.6 — 2026-07-13

Pipeline spine. The working-memory offload the rest of the road to 1.0 depends on.

- **One tracker holds the whole search.** `Application_Tracker.md` becomes three tables: **Active** (applications sent and everything live after them), **Watching** (scored but not yet sent, where scan finds land), and **Closed** (the archive, never deleted). Every role across all three is already known to the scan; dedup reads all of them. Replaces the old Applied plus New Finds pair.
- **Stage, next action, and due date per application.** Active rows carry a Stage from one ordered vocabulary (Applied, Screen, Interview, Final, Offer), the single next action she has decided on in her own words, and an optional due date. The tool records what she reports; it never invents a status or a follow-up date.
- **Timing view across competing processes.** A status read lays the search out at once: counts by stage, next actions sorted soonest-first, and any week where two or more live processes collide. A mirror of recorded state, not a coach.
- **Capacity as a target she sets.** One setup question (Part 3, 9b) captures how many live applications she can attend to at once, stored in the tracker header. The view reflects it back once as a fact when she crosses it, never as a cap or a nag.
- New **Pipeline mode** (Step F) and `references/pipeline.md`. Triggers on application events ("I applied to," "I heard back from," "I withdrew") and status questions ("where does my search stand," "what's my next step").
- DECIDED (2026-07-11) honored: pipeline state is built into kochab, not the standalone `job-application-tracker` skill, so scan finds and pipeline state share one source of truth. Trigger overlap with that separate skill is expected; folding it in or retiring it stays a later question.
- **Deliberately bounded to holding and showing state.** No follow-up timing (v0.7), no stage coaching (v0.8), no funnel diagnosis (v0.9). The Closed archive is built to support that diagnosis later. ETHICS principle 1 holds: the tool records what a human did, and applies or advances nothing on its own.
- Updated `skills/kochab/SKILL.md` (description, mode detection, Step A6, B1, B6, B7, new Step F), `references/setup_interview.md` (question 9b), `references/scheduled_task_template.md`, and `references/scan_protocol.md`. Rewrote `fixtures/kochab-test/Application_Tracker.md` to the new schema. Repackaged `kochab.skill`.

## v0.5.2 — 2026-07-11

Tunable study plans.

- Study plans now take a **time budget** as the primary tuning input. The hours from setup are the default, but any in-the-moment figure overrides it (15 minutes a day, four hours a day), normalized to hours per week. If none is known, the plan asks once rather than guessing.
- **Budget changes the plan's composition, not just its length.** Three bands: lean (under ~3 hr/wk) gets one thread and the smallest demonstrable artifact over an honest, longer horizon; steady (~3 to 10) gets the standard month-by-month path; immersive (over ~10) gets a project-first, parallel, compressed plan with a more ambitious artifact. Re-tunable: a new budget recomposes the plan rather than rescaling the dates.
- Completes the v0.5.1 handoff: after a scan's directional line, "what do you recommend" or "make a plan" targets the specific skill that line named.
- Updated `skills/kochab/references/study_plan.md` and `skills/kochab/SKILL.md` (Step D). Repackaged `kochab.skill`.

## v0.5.1 — 2026-07-11

Directional gap line in the scan.

- Every Stretch role now carries a **directional line** after its gap: the single dimension holding it below Strong and what closing that gap would do to the rating. Turns the static fit rating into a next step, using the score and gap the scan already computed.
- **Points only at concrete, studiable skills.** The lift it names is something she can go learn and get demonstrably good at (a Python course, SQL, a named tool, a real cert screen). When the gap is experience (domain seasoning, tenure) or structural (mission, level, location), the line says plainly that no course moves it rather than inventing a study target.
- **Directional line only, by decision.** It points at the study machinery; it does not run it. No curriculum, resources, or time estimates in the scan. The full study plan stays on demand and in the weekly summary (v0.3), and the daily note still does not offer or generate a plan, so the v0.3 anti-nag cadence and ETHICS principle 6 hold.
- **Arithmetic-honest.** A move to Strong is claimed only when the math supports it (14 or more with no capping zero on core-skill, level, or screen-clearance); otherwise the line says plainly that no single lift reaches Strong.
- Updated `skills/kochab/references/scan_protocol.md` (new directional-line section plus a worked example each way) and `skills/kochab/SKILL.md` (Step B3). Repackaged `kochab.skill`.

## v0.5 — 2026-07-10

Interview preparation. MVP feature-complete.

- New **Interview mode** (Step E) and `references/interview_prep.md`. Grounded in the profile, story bank, and the specific job description: maps likely questions to the real stories that answer them, supplies specific questions for her to ask, names the thin spots with an honest way to handle each, and adds format logistics (screen, panel, onsite). A likely question with no story is flagged as a gap, not bluffed.

## v0.4 — 2026-07-10

Legitimacy screen and consistent fit rationale.

- **Legitimacy check** (`references/legitimacy_check.md`) on each new posting as part of verification: real employer, live/recent req, sane comp band, direct-vs-staffing-firm, scam signals. Cautions attach to anything not clean; clear scams are kept out of the ranked list and noted as screened out.
- Every ranked role now carries a one-line **why-you-fit** rationale alongside its gap.

## v0.3 — 2026-07-10

Gap study plans.

- New **Plan mode** (Step D) and `references/study_plan.md`. Turns a recurring, bounded gap into a month-by-month path: target as a demonstrable artifact, real web-searched resources with time costs paced to the user's available hours, a portfolio artifact endpoint, and a re-assessment checkpoint.
- **On-demand invocation** infers the target from input: a named skill, a specific role, or nothing (picks the highest-leverage recurring gap from scan history). Natural-language triggers.
- **Auto-offer** surfaces in the weekly-summary run only (default Monday), never the daily note, and only when a gap is both recurring and bounded. Wired into the scan step and the scheduled-task template.
- Setup interview adds one question: realistic hours per week for upskilling. Skeptical of certifications by default; real resources only.

## v0.2 — 2026-07-10

Story bank and anti-boilerplate cover notes.

- **Story bank** (`Story_Bank.md`, built via `references/story_bank.md`): seeded from the resume, then filled out through a short interview into three to five situation-task-action-result stories, each carrying its honest owner-vs-adjacent framing. Grows as the user applies. Reused by cover notes and, later, interview prep.
- **Cover note generator** (`references/cover_note.md`): produces a short application email and a formal letter from a researched, true employer hook plus one relevant story and one tailored claim. Never restates the job description. If the candidate has no genuine reason to want the role, it says so rather than manufacture enthusiasm.
- New **Draft mode** (Step C) and a setup seeding step (A5b); setup interview extended (Part 8).
- The tool drafts; a human sends. No auto-submission, consistent with ETHICS.

## v0.1 — 2026-07-10

First packaged version, prepared for public release.

- Assembled two skills into one suite: `kochab` (recurring personalized scan from a resume) and `opportunity-brief` (assess a company or posting on demand).
- Added README, MIT LICENSE, and ETHICS (responsible-use constraints: human-applies-not-the-tool, respect site terms of service, never fabricate, scores rank but do not measure, user data stays local).
- Separated tool from data: the repository ships no profiles, resumes, or trackers.
- **Transparent match score.** Six justified sub-scores (core-skill, level, domain, location, mission, screen-clearance), 0-3 each, rolling to an /18 that ranks roles within the Strong / Stretch / Skip bands. Sub-scores and total always shown together; no bare number, no percentage. A zero on core-skill, level, or screen-clearance caps a role at Stretch regardless of total.
- Roadmap published for v0.2 through v0.5.
