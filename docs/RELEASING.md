# Releasing Kochab

Kochab ships as skill folders under `skills/`, each also distributed as a packaged `.skill` ZIP at the repo root. This checklist keeps a release consistent across the three skills (`kochab`, `opportunity-brief`, `roadmap-interview`).

## Before you package

- The change is within scope. Check `ROADMAP.md`; if it touches a non-negotiable in `ETHICS.md`, stop.
- The skill's `SKILL.md` and `references/` are updated, and the description still triggers on the right tasks and only those.
- You ran the behavior against `fixtures/` (not real data) and the output looks right.

## Package each changed skill

A `.skill` file is just a ZIP of the skill folder with `SKILL.md` at its root.

```bash
# from the repo root, for each changed skill:
cd skills && zip -r ../kochab.skill kochab -x '*/.*' && cd ..
# repeat for opportunity-brief, roadmap-interview as needed
```

Verify the bundle's top-level entry is the skill folder with its `SKILL.md` inside it (that is, `kochab/SKILL.md`), not a bare `SKILL.md` at the zip root. This layout is correct; do not "flatten" it.

```bash
unzip -l kochab.skill | head
```

## Record and tag

- Add a `CHANGELOG.md` entry: version, date, what changed, and which skills were repackaged.
- If versioning with git, commit and tag (for example `v0.5.1`). Note: run git from a normal terminal; some sandboxed filesystems block the file operations git needs.

## Install / verify

- Install the updated `.skill` via **Settings → Capabilities**, toggle it on, and confirm it loads on a matching task.
- Do a smoke run against `fixtures/` to confirm nothing regressed.

## Reminder

Never commit personal data. Profiles, resumes, trackers, and real employer names stay out of this repo; only synthetic `fixtures/` data belongs here.
