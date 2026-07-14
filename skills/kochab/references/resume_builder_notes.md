# Resume Builder Notes

## Install and run

WeasyPrint needs native libraries first (Pango, Cairo, GDK-PixBuf): `brew install pango` on macOS, `apt-get install libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0` on Debian/Ubuntu, or the WeasyPrint install docs on Windows. Then, inside a virtualenv (not `--break-system-packages`):

```
python3 -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python3 assets/resume_builder.py profile.json "Acme Program Manager" /path/to/folder
```

Writes `Acme_Program_Manager.pdf`. Requires Python 3.9+.

## How variants work

`profile.json` holds the content. A variant is a copy of that file with material **cut and reordered** for a specific target, not rewritten.

To build a variant:

1. Copy `profile.json` to `profile_<target>.json`.
2. Rewrite the `summary` for this employer. It is the only section written fresh each time.
3. Reorder `skills` groups so the ones this posting names come first. Delete groups it will not care about.
4. Within each `experience` entry, cut bullets that do not serve this target and promote the ones that do. Keep bullets factual; never add an accomplishment that was not already true in `Master_Profile.md`.
5. Leave `publications`, `patents`, and `education` alone unless the target has a reason to see them differently.

Set a key to `[]` or `""` and its section disappears.

## Filling two pages honestly

The layout is tuned so that a genuine two pages of content fills two pages. If a variant lands at 1.3 pages, do not pad it. Either:

- Break a long tenure into its real sub-roles, which usually recovers a third of a page of true content, or
- Ship a focused one-page version.

A near-empty second page reads worse than a full single page. For a teaching, adjunct, or specialist application, a focused one-pager is often the better document.

## Guardrails

- Every bullet must trace to something in `Master_Profile.md`.
- Every bullet must obey the honesty guardrails. If a posting rewards a claim the guardrails forbid, the answer is to name the gap in the cover note, not to soften the guardrail.
- Scale belongs in the bullet. "Coordinated 300+ programs a year across 10+ engineering organizations" beats "coordinated many programs."
- One accomplishment per bullet. Two accomplishments in one bullet halves the value of both.
- Avoid words that could describe anyone: dynamic, results-driven, proven track record, passionate.

## Fonts

The CSS asks for Carlito, then Calibri. Carlito is metric-compatible with Calibri and ships with most Linux distributions. On a machine with neither, the fallback is the generic sans-serif and line breaks will shift. Check the page count after any font change.
