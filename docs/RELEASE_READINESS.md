# Release Readiness — Kochab 1.0 goes wide

The features are done. v0.6 through v1.0 shipped, and the MVP-to-1.0 loop is complete. What remains before Kochab is shared widely is not feature work; it is the five supporting activities named in `ROADMAP.md`. This document turns that gate into a concrete plan, split two ways:

- **Artifacts to build:** things the tool or a maintainer session can produce (docs, drafts, a synthetic persona, checklists).
- **On Brian's side:** things only a human can do (anything touching git history, a public host, personal accounts, or a judgment call that is yours).

State captured 2026-07-14, read from the repo. Decisions still open are marked OPEN and collected at the end.

## Snapshot of what the repo needs

- The whole road-to-1.0 (v0.6 through v1.0) is **uncommitted**. Only `v0.5.1` and `v0.5.2` are tagged; `v0.6` through `v1.0` have no commits and no tags.
- Every user-facing doc (`README.md`, `docs/Getting_Started.md`, `docs/WALKTHROUGH.*`, `docs/Demo_Script.md`, `docs/Kochab_Deck.pptx`) predates v0.6. The README still says the tool "works in five modes"; there are now eleven plus the intervention dial.
- There is no `CONTRIBUTING.md`, so the contribution path that should point at `ETHICS.md` does not exist yet.
- The test fixtures carry real personal data (phone, email, home city, real employers and patents in `fixtures/kochab-test/Master_Profile.md`). This bends the no-personal-data rule for a public repo.
- Two stray temp files (`zivpuKb2`, `ziwU4LJU`, leftovers from packaging) sit in the repo root and cannot be unlinked from the sandbox.

## Readiness build completed 2026-07-14

Most of the buildable gate is done in this pass:

- **Synthetic persona (hard gate met).** The Brian-shaped fixtures are replaced with a fully fictional persona, Dana Whitfield, a mid-career teacher pivoting to instructional design in Columbus, with invented employers and contacts throughout. All seven fixture files rewritten; no real names.
- **Generalizability validated.** Grepped the skill for hard-coded Brian-isms (found and genericized one example guardrail in `SKILL.md`) and ran the pipeline, funnel, and network smoke tests against the new persona. All pass; nothing is hard-coded to the author's case.
- **Portability minimums.** `requirements.txt`, a shebang and Python 3.9+ note on `resume_builder.py`, and the `--break-system-packages` line replaced with virtualenv plus per-platform native-dependency notes (in the script and `resume_builder_notes.md`).
- **Contributor readiness.** `CONTRIBUTING.md`, three passing unit tests in `tests/` (no native deps needed), and `build.sh` (one-command repackaging, with a Windows note).
- **Docs refreshed.** README (full mode set, fixed a broken deck link, current status), `Getting_Started.md` (the dial and the post-application modes), and the walkthrough in all three formats (`.md`, regenerated `.html` and 7-page `.pdf`) extended through pipeline, momentum, offer, and network. The cheat sheet already covers every mode.
- **Consistency.** Em-dash convention applied to the persona fixture and scoped in `AGENTS.md`; `__pycache__` git-ignored.

### Still open

- **Slide deck** (`docs/Kochab_Deck.pptx`): not refreshed here. Lower priority now that README, Getting Started, walkthrough, and the cheat sheet cover the feature set. A follow-up if you want the deck current.
- **Socialization** (section 3): deferred by the suggested sequence until the repo is public.
- **Packaging decision:** the prebuilt `kochab.skill` stays committed, since Cowork users install that file directly; drift is mitigated by `build.sh` and the RELEASING checklist rather than git-ignoring it. Moving it to GitHub Releases is a future option once hosting is set.
- **Your terminal:** remove the two stray temp files and the stale `.git/index.lock`, then commit v0.6 through v1.0 (one commit per release) and tag each. The repackaged `kochab.skill` is current.
- **Open decisions:** hosting (repo home) and socialization channels.

---

## 1. Cleanup pass

**Artifacts to build**

- Rewrite the `README.md` feature list: replace "five modes" with the shipped set (Scan, Draft, Plan, Interview, Pipeline, Momentum, Stage guidance, Offer, Process health, Network) plus the intervention dial and tailored resume variants.
- Audit `skills/` and `docs/` for dead files, inconsistent naming, and half-finished references; produce a short findings list and fix what is mechanical.
- Resolve the fixture PII question by building the synthetic persona (see section 4); that is the cleanup for the largest no-personal-data risk.

**On Brian's side**

- Delete the two stray temp files `zivpuKb2` and `ziwU4LJU` from a real terminal (the sandbox cannot unlink them).
- Final eyeball that nothing personal remains before anything is pushed.

## 2. Git infrastructure for sharing

**Artifacts to build**

- Write `CONTRIBUTING.md` that names `ETHICS.md` as the hard wall: what the project will not merge (auto-submit, scraping behind logins, objective numeric scores, resume fabrication) and how to propose changes.
- Confirm `.gitignore` covers every personal artifact. Current coverage: profile, tracker, story bank, employer lists, scans, study plans, resumes, and now `Contacts.md` and `Connections.csv`. Verify nothing new leaks.
- Draft the commit-and-tag plan: how to group v0.6 through v1.0 into commits, the messages, and the annotated tags to create.

**On Brian's side** (all of this needs a real terminal; the sandbox blocks the file operations git needs, per `docs/RELEASING.md`)

- Commit the v0.6 through v1.0 work, ideally one commit per release so the tags line up with `CHANGELOG.md`.
- Create annotated tags `v0.6`, `v0.7`, `v0.8`, `v0.9`, `v1.0`.
- Verify no personal data was ever committed to history (`git log`, a grep of past commits); if any exists, scrub it before the repo is public.
- Create the public remote (for example a GitHub repo), set description, license display, and visibility, and push.

## 3. Free socialization

**Artifacts to build**

- Draft a plain writeup: what Kochab is, why the honesty stance matters, and how to try it. No hype, no paid promotion. Run it through the `voice-validator` skill so it sounds like Brian.
- Draft short, channel-specific posts for the no-cost channels already in the target list: aisafety.com, the 80,000 Hours community, relevant Slacks and forums, `4dayweek.io/ai-governance-jobs` communities.
- Update `docs/Demo_Script.md` and, if wanted, a short screencast or GIF script so a reader can see it work in two minutes.

**On Brian's side**

- Choose the channels and post to them (they require your accounts and community standing).
- Word-of-mouth outreach to people who would actually use it.
- Decide timing relative to the repo going public.

## 4. Generalizability validation

**Artifacts to build**

- Build at least one clearly-synthetic persona that is not Brian: a different field, level, and constraint set. Produce a full fixture set for them (profile, story bank, target employers, tracker, contacts), all obviously fictional.
- Run the whole loop against that persona (setup through scan, draft, plan, interview, pipeline, momentum, stage guidance, offer, process health, network) and confirm nothing is secretly hard-coded to Brian's case.
- Record findings and fix anything persona-specific that surfaces.
- Retire the PII risk in the existing fixtures per the OPEN decision below.

**On Brian's side**

- Review the synthetic persona for realism and sign off that it exercises the tool fairly.

## 5. User instructions

**Artifacts to build**

- Update `docs/Getting_Started.md` to match shipped behavior: all modes, the intervention dial, contact intake, and how the scheduled scan works.
- Update `docs/WALKTHROUGH.md` and regenerate `docs/WALKTHROUGH.html` and `docs/WALKTHROUGH.pdf` from it.
- Update `docs/Kochab_Deck.pptx` to the current feature set.
- Confirm the setup-to-first-scan path is complete, honest, and tells a new user where their data lives.
- **Cheat sheet (drafted 2026-07-14).** A one-page quick reference: every mode, an example phrase to trigger it, and what it returns, plus the fit-score key and the never-bends rules, so a new user discovers features they would otherwise never invoke. Three forms: `docs/CHEATSHEET.md` (source, GitHub-viewable), `docs/CHEATSHEET.html` (designed, print-optimized landscape), and `docs/CHEATSHEET.pdf` (rendered, one page). Keep in sync with the shipped mode set; re-verify the trigger phrases against `SKILL.md` before release, and re-render the PDF from the HTML if it changes (`weasyprint docs/CHEATSHEET.html docs/CHEATSHEET.pdf`).

**On Brian's side**

- Read the updated Getting Started and walkthrough as a brand-new user would and confirm they match reality.

## Suggested sequence

1. Cleanup and the synthetic persona first (sections 1 and 4), because the persona work is also the fixture-PII fix and shakes out anything Brian-specific before docs are written.
2. Docs next (sections 1 README and 5), so the writeup and walkthrough describe the validated, cleaned tool.
3. `CONTRIBUTING.md` and the commit-and-tag plan (section 2 artifacts).
4. Brian commits, tags, and creates the public remote (section 2 activities).
5. Socialization last (section 3), once the public repo and docs are live.

## From the 2026-07-14 code review

A full review of the v0.6 through v1.0 change set (separate report) passed the ethics checklist and cleared the change set to commit and tag. Its concrete follow-ups, with status:

**Fixed already (folded into the pre-tag commit, `kochab.skill` repackaged):**

- The weekly follow-ups behavior fork between `scheduled_task_template.md` and the dial / `momentum.md` / SKILL.md B5. The weekly "follow-ups coming due" line now fires at every dial level, matching the interactive path.
- SKILL.md stale "Two modes" lead; `intervention_dial.md` grammar; the CHANGELOG line that described the old behavior.
- `resume_builder.py` hardening: filename empty-name and length guard, a rejecting `url_fetcher` on the WeasyPrint call, friendly errors for a missing profile key or bad JSON, and a security-invariant comment on the escaping rule.
- `docs/RELEASING.md` reworded so a contributor does not flatten the correct `kochab/`-at-top bundle.
- Em-dash convention decided and recorded in `AGENTS.md`; the one user-file-generating template (the `pipeline.md` tracker header) switched to a hyphen.

**Publication blockers (before public):**

- Synthetic-persona fixtures (the hard gate; also under Decisions).
- Portability minimums for `resume_builder.py`: replace the `--break-system-packages` install line with virtualenv plus per-platform system-dependency notes; add `requirements.txt` (pin weasyprint), a `#!/usr/bin/env python3` shebang, and a stated minimum Python (3.9+).
- Stale docs refresh (README "five modes", Getting Started, walkthrough, deck), section 5 above.

**Recommended for contributor readiness (not blockers):**

- Three unit tests on `resume_builder.py`: escaping (a `<script>` in a bullet comes out escaped), empty-key section omission, and filename sanitization including the all-symbol edge.
- `CONTRIBUTING.md` (section 2): skill layout, how to add a mode, the escaping rule, ETHICS as the hard wall.
- Git-ignore `*.skill` and generate the bundle at release via a one-command build script (Makefile or `build.sh`), with a Windows `Compress-Archive` note. The `@page` A4 option and the font-fallback caveat can be filed as issues.

**Your terminal:** delete the two stray temp files (`zivpuKb2`, `ziwU4LJU`) and the stale `.git/index.lock`, then commit v0.6 through v1.0 (one commit per release) and tag each.

## Decisions

**DECIDED (2026-07-14)**

- **Fixture PII.** Replace the Brian-shaped fixtures with a clearly-synthetic non-Brian persona as the primary fixture set. This removes the personal data from the repo and doubles as the generalizability validation (sections 1 and 4 merge into one piece of work: build the persona, run the loop, retire the old fixtures).
- **Next step.** Hand this plan back to Brian to sequence. No further artifacts are being built in this session.

**OPEN**

- **Hosting.** Where the public repo lives (GitHub is assumed above) and under what account or org.
- **Channels.** Which of the free channels you actually want to use, so the writeup and posts are drafted to fit them.
