# Contributing to Kochab

Thanks for considering a contribution. Kochab is a job-search assistant shipped as a set of Claude skills, built on one bet: it is an honest decision aid for one person running a real search, not a mass-apply tool. Please read this file and `ETHICS.md` before you start.

## The hard wall (read `ETHICS.md` first)

`ETHICS.md` is not a disclaimer. It is the set of constraints the tool actually follows, and it is the reason the project exists. Contributions that break it will not be merged. In particular, the project will not accept:

- Auto-submission, form-filling, or bulk application. The tool drafts; a human sends.
- Scraping behind logins, evading rate limits, or circumventing CAPTCHAs or bot detection.
- Numeric fit scores presented as objective measurements.
- Any resume or cover material that fabricates, or that overrides the user's honesty guardrails.
- Anything that ships personal data in the repo (see Fixtures below).

If an idea needs one of those to work, it is out of scope by design. `ROADMAP.md` has a "Deliberately out of scope, permanently" section; treat it as a wall.

## How the skills are laid out

Each skill is a folder under `skills/` with a `SKILL.md` at its root and a `references/` directory of supporting method files:

```
skills/kochab/
  SKILL.md            # modes, mode detection, and the short version of each method
  references/*.md      # the full method for each mode
  assets/              # the optional resume builder and its example profile
```

`SKILL.md` stays trigger-focused and points into `references/` for detail. The packaged `*.skill` files at the repo root are ZIPs of these folders (see Building below).

## Adding or changing a mode

A mode is wired in four places. Change all of them together:

1. A line in the `SKILL.md` **mode-detection** list.
2. A trigger phrase in the `SKILL.md` **description** frontmatter, so the skill loads on the right tasks and only those.
3. A `references/<mode>.md` file with the full method, including explicit hand-offs to later releases so a mode does not silently do another mode's job.
4. A dated `CHANGELOG.md` entry, and a repackaged `*.skill` bundle.

Respect items marked DECIDED in `ROADMAP.md`; surface OPEN ones for a decision instead of guessing. `AGENTS.md` has the full maintainer standing orders.

## The resume builder

`skills/kochab/assets/resume_builder.py` renders a profile JSON to a PDF. One security invariant: **every value interpolated into the HTML must pass through `html.escape`.** All content lands in element text, so default escaping is enough, but any new field you add to the template must be escaped too, or it is an injection hole in the generated PDF. See the comment above the render functions.

Run the tests (no native dependencies needed; they do not import WeasyPrint):

```
python3 -m unittest discover -s tests
```

To run the builder itself, see its file header for the WeasyPrint native libraries and the virtualenv install. Requires Python 3.9+.

## Building the bundles

When a skill's source changes, repackage before committing or tagging:

```
./build.sh
```

This rebuilds each `*.skill` from `skills/`. On Windows, use the `Compress-Archive` commands noted at the top of `build.sh`. `docs/RELEASING.md` has the full release checklist.

## Fixtures and personal data

The repo ships **no personal data**. The only sample data allowed is the clearly-synthetic persona under `fixtures/kochab-test/` (a fictional person and fictional employers). Test against those, never against a real search, and never commit a real profile, resume, tracker, contact list, or real employer name.

## Voice

Plain and direct. No em dashes in user-facing or user-generated content (maintainer-doc headings may keep them; see the note in `AGENTS.md`). No AI-cliche filler. Write in the user's voice, not the tool's.
