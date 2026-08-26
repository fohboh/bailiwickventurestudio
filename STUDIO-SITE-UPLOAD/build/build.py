"""Build the Bailiwick Venture Studio site.

    python3 build/build.py

Writes flat, self-contained HTML into the repo root — every page carries its
own CSS, JS and SVG inline, so there is nothing to bundle and nothing that can
fall out of sync at deploy time. Also emits sitemap.xml, robots.txt and
site.webmanifest so the whole property is regenerable from source.
"""

import os
import sys
import pathlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from theme import page, SITE          # noqa: E402
import pages as P                     # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
S = "Bailiwick Venture Studio"

PAGES = [
    ("index.html",
     f"{S} — From Idea to Usable Proof",
     "Bailiwick Venture Studio is the venture architecture division of Bailiwick Ventures, Inc. "
     "A day-zero co-founder, not a check: from consequential idea to usable proof of concept in "
     "60 days or less.",
     P.home()),

    ("model.html",
     f"The Venture Studio Model — {S}",
     "What a venture studio is, how it differs from an incubator, an accelerator and a venture "
     "fund, what the performance data actually supports — and the four widely quoted figures we "
     "decline to publish.",
     P.model()),

    ("process.html",
     f"The Six Phases — {S}",
     "Diagnose, Map, Architect, Build, Validate, Prepare. Every phase has a question it answers, a "
     "deliverable it produces, and a condition that must be met before the venture advances.",
     P.process()),

    ("ventures.html",
     f"Ventures — {S}",
     "FohBoh.ai, BailiwickQuikFix and StarBar · SnapCount — three structural diagnoses, one method, "
     "and the five conditions the Studio requires before taking a venture on.",
     P.ventures()),

    ("engage.html",
     f"Engage the Studio — {S}",
     "The Triage at $2,500 and Plan A Blueprint at $25,000 for four weeks: published scope, "
     "published price, published exclusions. No free diagnostics, and no plan below $25,000.",
     P.engage()),

    ("404.html",
     f"Page not found — {S}",
     "That page is outside our bailiwick.",
     P.notfound()),
]

ROBOTS = f"""User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
"""

MANIFEST = """{
  "name": "Bailiwick Venture Studio",
  "short_name": "BW Studio",
  "description": "The venture architecture division of Bailiwick Ventures, Inc.",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#FAF8F4",
  "theme_color": "#12304F",
  "icons": [
    { "src": "/brand/png/tile-navy-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/brand/png/tile-navy-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "/brand/svg/tile-navy.svg", "sizes": "any", "type": "image/svg+xml" }
  ]
}
"""


def sitemap(names):
    urls = ""
    for fn in names:
        if fn == "404.html":
            continue
        loc = SITE + ("/" if fn == "index.html" else "/" + fn)
        pri = "1.0" if fn == "index.html" else "0.8"
        urls += (f"  <url><loc>{loc}</loc><changefreq>monthly</changefreq>"
                 f"<priority>{pri}</priority></url>\n")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}</urlset>\n")


if __name__ == "__main__":
    total = 0
    for fn, title, desc, body in PAGES:
        html = page(title, desc, fn, body)
        (ROOT / fn).write_text(html, encoding="utf-8")
        kb = len(html.encode("utf-8")) / 1024
        total += kb
        print(f"  {fn:16} {kb:7.1f} KB")

    (ROOT / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    (ROOT / "site.webmanifest").write_text(MANIFEST, encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap([p[0] for p in PAGES]), encoding="utf-8")

    print(f"\n  wrote {len(PAGES)} pages ({total:.1f} KB) + robots.txt, "
          f"site.webmanifest, sitemap.xml to {ROOT}")
