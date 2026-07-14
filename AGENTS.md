# AGENTS.md — Kochab maintainer standing orders

These are the standing orders for any agent (or person) working in this repo. They mirror the Cowork project Instructions and travel with the code, so the rules hold in Claude Code and for anyone who forks Kochab. Read this, `ETHICS.md`, and `ROADMAP.md` before proposing changes.

## What Kochab is

A job-search assistant shipped as a set of Claude skills. This repo is the product's source and maintainer workspace, **not anyone's live job search.** Personal data never lives here.

## What lives where

- `README.md` — what the product is and how to install it.
- `ETHICS.md` — the non-negotiables. The reason the project exists.
- `ROADMAP.md` — scope, version order, and what is permanently out of scope.
- `CHANGELOG.md` — the record of what changed, per version.
- `skills/` — the source for each skill (a folder with `SKILL.md` at its root).
- `*.skill` — packaged ZIP bundles, built from the folders in `skills/`.
- `docs/BACKLOG.md` — candidate features and the need under each; where roadmap-interview intake lands.
- `docs/` — design brief, walkthrough, deck, getting-started, backlog, release checklist.
- `fixtures/` — synthetic test data. The only "user data" allowed in the repo.

## Non-negotiables (from ETHICS.md; never violate, reject changes that would)

1. The tool drafts; a human applies. No auto-submit, form-filling, or bulk submission, ever.
2. Respect every site's terms: no scraping behind logins, no CAPTCHA or rate-limit evasion. Prefer public postings, official search, and the user pasting a job description in.
3. Never fabricate. Resume and cover material is reorganized truth only, and obeys the user's honesty guardrails even when overstating would score better.
4. Fit is shown as justified sub-scores with a named gap, never a bare number or percentage presented as objective.
5. Report thin days honestly. Do not manufacture matches.

## Working conventions

- Build one version at a time. Respect items marked DECIDED in the roadmap. Surface OPEN ones for a decision instead of guessing. Treat "Deliberately out of scope" as a hard wall.
- Every skill is a folder with `SKILL.md` at its root. Keep the description trigger-focused so it loads on the right tasks. Package a skill as a ZIP of its folder to install.
- Test against `fixtures/`, never against real personal data. No profiles, resumes, trackers, or real employer names get committed here.
- When behavior changes: update the relevant `SKILL.md`/references, add a `CHANGELOG.md` entry, repackage the `.skill` bundle (see `docs/RELEASING.md`), and say what changed and where.
- Voice: plain and direct. No em dashes. No AI-cliche filler.
- Em-dash convention (decided 2026-07-14): no em dashes in content the tool generates for a user (profiles, resumes, drafts, trackers, scan notes) or in templates the tool writes into a user's folder (for example the `Application_Tracker.md` header in `references/pipeline.md`), since those inherit the user's own voice rules; the synthetic fixtures follow the same rule. The repo's own narrative docs (README, walkthrough, CHANGELOG, ROADMAP) keep the author's existing em-dash style. When in doubt in generated content, use a hyphen.

## Ask before

Expanding scope beyond the roadmap, adding a dependency, or anything touching a non-negotiable.
