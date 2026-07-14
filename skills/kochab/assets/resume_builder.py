#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Two-page resume builder. Renders HTML to PDF with WeasyPrint. Requires Python 3.9+.

WeasyPrint needs native libraries (Pango, Cairo, GDK-PixBuf). Install those first:
  macOS:          brew install pango
  Debian/Ubuntu:  apt-get install libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0
  Windows:        see https://doc.courtbouillon.org/weasyprint/stable/first_steps.html

Then, from a virtual environment (do not use --break-system-packages):
    python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
    pip install -r requirements.txt
    python3 resume_builder.py profile.json "Acme Program Manager" ./out

Content lives in a JSON file so the same builder serves every variant.
Build a variant by copying profile.json, cutting what the target does not
care about, and reordering what it does. Tailor by subtraction.

The layout is tuned so a full two pages of genuine content fills two pages.
If your variant comes out at 1.3 pages, the answer is more real content or
a one-page layout, not padding.
"""

import json
import os
import sys
from html import escape

CSS = """
<style>
  @page { size: Letter; margin: 0.5in 0.6in; }
  body { font-family: "Carlito","Calibri",sans-serif; font-size: 10.5pt;
         color:#1a1a1a; line-height:1.34; }
  .name { font-size: 20pt; font-weight:700; letter-spacing:0.5px;
          color:#15233b; margin:0; }
  .contact { font-size: 9pt; color:#333; margin:3px 0 10px 0; }
  h2 { font-size:11pt; font-weight:700; text-transform:uppercase;
       letter-spacing:0.6px; color:#15233b; border-bottom:1.4px solid #15233b;
       padding-bottom:2px; margin:12px 0 6px 0; }
  p { margin:0 0 6px 0; text-align:justify; }
  ul { margin:3px 0 7px 0; padding-left:17px; }
  li { margin:0 0 4px 0; text-align:justify; }
  .role { font-weight:700; color:#15233b; }
  .sub { font-style:italic; color:#333; margin:0 0 3px 0; }
  .meta { float:right; font-style:italic; color:#444; font-size:9pt; }
  .entry { margin-bottom:9px; }
  .clear { clear:both; }
  .skills span { font-weight:700; color:#15233b; }
</style>
"""


# SECURITY INVARIANT: every value interpolated into HTML must pass through
# html.escape(). All content below lands in element text (no dynamic attributes),
# so default escaping is sufficient. Any new field added to the template must be
# escaped too, or it is an HTML-injection hole in the generated PDF.


def safe_filename(variant_name):
    """Sanitize a variant name into a PDF filename. Blocks path traversal (keeps
    only alphanumerics, hyphen, underscore, space), caps length, and falls back
    to a default if nothing usable remains."""
    safe = "".join(ch if ch.isalnum() or ch in "-_ " else "" for ch in variant_name)
    safe = safe.strip()[:120] or "resume_variant"
    return f"{safe.replace(' ', '_')}.pdf"


def header(p):
    c = p["contact"]
    line = " &nbsp;|&nbsp; ".join(escape(x) for x in c["line"])
    return (f'<p class="name">{escape(c["name"])}</p>'
            f'<p class="contact">{line}</p>')


def summary(p):
    if not p.get("summary"):
        return ""
    return f'<h2>Summary</h2><p>{escape(p["summary"])}</p>'


def skills(p):
    if not p.get("skills"):
        return ""
    rows = "".join(
        f'<li><span>{escape(g["label"])}:</span> {escape(" · ".join(g["items"]))}</li>'
        for g in p["skills"]
    )
    return f'<h2>Skills &amp; Expertise</h2><ul class="skills">{rows}</ul>'


def experience(p):
    out = ["<h2>Experience</h2>"]
    for e in p["experience"]:
        sub = f'<div class="sub">{escape(e["subtitle"])}</div>' if e.get("subtitle") else ""
        bullets = "".join(f"<li>{escape(b)}</li>" for b in e["bullets"])
        out.append(
            f'<div class="entry">'
            f'<span class="meta">{escape(e["dates"])}</span>'
            f'<span class="role">{escape(e["title"])}</span>, {escape(e["employer"])}'
            f'{sub}<ul>{bullets}</ul></div>'
        )
    out.append('<div class="clear"></div>')
    return "".join(out)


def simple_list(p, key, heading, numbered=False):
    if not p.get(key):
        return ""
    tag = "ol" if numbered else "ul"
    rows = "".join(f"<li>{escape(x)}</li>" for x in p[key])
    return f"<h2>{escape(heading)}</h2><{tag}>{rows}</{tag}>"


def build(profile_path, variant_name, outdir):
    with open(profile_path) as f:
        p = json.load(f)

    body = "".join([
        header(p),
        summary(p),
        skills(p),
        experience(p),
        simple_list(p, "publications", "Selected Publications"),
        simple_list(p, "patents", "U.S. Patents", numbered=True),
        simple_list(p, "education", "Education"),
    ])

    html = f"<html><head><meta charset='utf-8'>{CSS}</head><body>{body}</body></html>"

    os.makedirs(outdir, exist_ok=True)
    pdf_path = os.path.join(outdir, safe_filename(variant_name))

    from weasyprint import HTML

    # The template embeds no external resources. Block all URL fetches so an
    # untrusted profile.json can never trigger local-file disclosure or SSRF if
    # a link or image is ever added later.
    def _block_urls(url):
        raise ValueError(f"external resource blocked: {url}")

    HTML(string=html, url_fetcher=_block_urls).write_pdf(pdf_path)

    print(f"wrote {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    try:
        build(sys.argv[1], sys.argv[2], sys.argv[3])
    except KeyError as e:
        sys.exit(f"profile is missing a required field: {e}")
    except json.JSONDecodeError as e:
        sys.exit(f"profile is not valid JSON: {e}")
    except OSError as e:
        sys.exit(f"could not read or write file: {e}")
