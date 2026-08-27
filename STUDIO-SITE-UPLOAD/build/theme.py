"""Bailiwick Venture Studio — shared design system, chrome, and page shell.

Inherits the Bailiwick Ventures system verbatim (navy / ivory / bronze,
Source Serif 4 + Inter, 1200px shell) so the Studio site reads as the same
company. One deliberate divergence: COBALT replaces vermilion as the color of
the terminal node in the Trajectory mark, and carries every primary action.
That is the division signal — Studio is cobalt, BailiwickVibe is signal
orange, the parent is vermilion. Everything else is shared structure.

Base CSS is loaded from _css_base.txt, which is a byte-for-byte copy of
theme.CSS in the fohboh/bailiwickventures repo. Studio-specific rules are
appended in CSS_STUDIO below, so a future upstream theme change can be
re-copied without losing the Studio layer.
"""

import pathlib

HERE = pathlib.Path(__file__).resolve().parent

BRAND = {
    "navy": "#12304F",
    "navy_deep": "#0C2138",
    "ink": "#14181D",
    "bronze": "#A8763E",
    "bronze_lt": "#C08D4E",
    "cobalt": "#1F5FD0",
    "cobalt_lt": "#5B8DE8",
    "signal": "#E2551F",
    "steel": "#6B8AA6",
    "ivory": "#FAF8F4",
    "warm": "#FFFDF9",
    "sand": "#EDE6DA",
    "line": "#E0D8CB",
    "body": "#4A5560",
}

# ---------------------------------------------------------------- mark
# TRAJECTORY — the Bailiwick Ventures identity, unchanged in geometry.
# Four nodes climbing left to right with one branch peeling off; the terminal
# node is oversized because that is where the venture ends up. On the Studio
# site that terminal node is COBALT rather than vermilion.
LINKS = "M10 52 L30 38 M30 38 L52 14 M30 38 L50 50"
NODES = ((10, 52), (30, 38), (52, 14), (50, 50))
TERMINAL = 2
COBALT = "#1F5FD0"


def mark(size=34, c="#12304F", label="Bailiwick Venture Studio", cls="mark",
         decorative=False, accent=COBALT):
    small = size <= 30
    sw = 4.5 if small else 3.5
    r = (7.5, 7.5, 9.5, 6.0) if small else (7.0, 7.0, 9.0, 5.5)
    circles = "".join(
        f'<circle cx="{x}" cy="{y}" r="{rr}" fill="{accent if (accent and i == TERMINAL) else c}"/>'
        for i, ((x, y), rr) in enumerate(zip(NODES, r)))
    a11y = ('aria-hidden="true"' if decorative
            else f'role="img" aria-label="{label}"')
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 64 64" {a11y}>'
            f'<g stroke="{c}" stroke-width="{sw}" stroke-linecap="round" fill="none">'
            f'<path d="{LINKS}"/></g>'
            f'{circles}</svg>')


CSS_BASE = (HERE / "_css_base.txt").read_text(encoding="utf-8")

CSS_STUDIO = """
/* ============================================================
   STUDIO LAYER — appended to the inherited Bailiwick system.
   Only additions and overrides live here.
   ============================================================ */
:root{ --cobalt-lt:#5B8DE8; --accent:#1F5FD0; }

/* primary action is cobalt on this property */
.btn-p{background:var(--cobalt);border-color:var(--cobalt)}
.btn-p:hover{background:#1A4FAF;border-color:#1A4FAF}
.nav-cta{border-color:var(--cobalt);color:var(--cobalt)}
.nav-cta:hover{background:var(--cobalt);color:var(--warm);border-color:var(--cobalt)}
.menu a.on::after{background:var(--cobalt)}

/* the parent-company link sits apart from the section nav */
.menu .up a{color:var(--steel);font-size:12.5px}
.menu .up a:hover{color:var(--navy)}
.menu .up{margin-left:6px;padding-left:10px;border-left:1px solid var(--line)}

/* eyebrow variant that marks Studio-owned material */
.eyebrow.k{color:var(--cobalt)}
.phase .pn{color:var(--cobalt)}

/* ---- comparison table ---- */
.cmp{width:100%;border-collapse:collapse;font-size:14.2px;line-height:1.5;
  border:1px solid var(--line);background:var(--warm);border-radius:3px}
.cmp caption{caption-side:bottom;text-align:left;font-size:12.5px;color:#7A858F;padding-top:14px}
.cmp th,.cmp td{text-align:left;padding:15px 16px;border-bottom:1px solid var(--line);vertical-align:top}
.cmp thead th{font-family:var(--sans);font-size:10.5px;font-weight:700;letter-spacing:.16em;
  text-transform:uppercase;color:var(--steel);background:var(--sand);border-bottom:1px solid var(--line)}
.cmp tbody th{font-family:var(--serif);font-weight:400;font-size:16px;color:var(--ink);width:20%}
.cmp td{color:var(--body)}
.cmp tr:last-child th,.cmp tr:last-child td{border-bottom:0}
.cmp .us{background:rgba(31,95,208,.05)}
.cmp .us th{color:var(--cobalt)}
.cmp-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
@media (max-width:760px){.cmp{min-width:660px}}

/* ---- evidence / citation blocks ---- */
.ev{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);
  border:1px solid var(--line);border-radius:3px;overflow:hidden}
.ev>div{background:var(--warm);padding:26px 22px;display:flex;flex-direction:column}
.ev .v{font-family:var(--serif);font-size:clamp(24px,2.6vw,32px);line-height:1.05;
  color:var(--navy);letter-spacing:-.02em;margin-bottom:10px}
.ev .l{font-size:13.8px;line-height:1.5;color:var(--body);margin-bottom:14px}
.ev .src{margin-top:auto;font-size:11px;line-height:1.45;color:#7A858F;
  padding-top:12px;border-top:1px solid var(--line)}
.ev .src a{color:#7A858F}
.ev .src a:hover{color:var(--cobalt)}
@media (max-width:860px){.ev{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.ev{grid-template-columns:1fr}}

/* a claim we deliberately refuse to publish */
.struck{border:1px solid var(--line);border-left:3px solid var(--signal);border-radius:2px;
  background:var(--warm);padding:18px 20px;margin-bottom:14px}
.struck .c{font-family:var(--serif);font-size:16.5px;line-height:1.4;color:#8A8078;
  text-decoration:line-through;text-decoration-color:rgba(226,85,31,.5);margin:0 0 9px}
.struck .w{font-size:13.6px;line-height:1.6;color:var(--body);margin:0}
.struck .w b{color:var(--ink);font-weight:600}

/* ---- deliverable ledger ---- */
.led{border-top:1px solid var(--line)}
.led .row{display:grid;grid-template-columns:44px 1fr 1.5fr;gap:18px;align-items:baseline;
  padding:17px 0;border-bottom:1px solid var(--line)}
.led .n{font-family:var(--serif);font-size:12.5px;color:var(--cobalt);letter-spacing:.08em}
.led .t{font-family:var(--serif);font-size:17px;line-height:1.3;color:var(--ink)}
.led .d{font-size:14px;line-height:1.6;color:var(--body)}
@media (max-width:760px){.led .row{grid-template-columns:36px 1fr;gap:12px}
  .led .d{grid-column:2}}

/* ---- price header ---- */
.price{display:flex;align-items:baseline;gap:16px;flex-wrap:wrap;margin:0 0 8px}
.price .amt{font-family:var(--serif);font-size:clamp(34px,4.2vw,52px);line-height:1;
  color:var(--navy);letter-spacing:-.025em}
.price .terms{font-size:12.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--steel)}

/* ---- venture entry ---- */
.vent{border-top:1px solid var(--line);padding-top:clamp(28px,3.4vw,42px);
  margin-top:clamp(28px,3.4vw,42px)}
.vent:first-of-type{border-top:0;padding-top:0;margin-top:0}
.vent .hd{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:6px}
.vent .hd h3{font-size:clamp(21px,2.3vw,27px)}
.vent .badge{font-size:10px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  color:var(--cobalt);border:1px solid rgba(31,95,208,.35);border-radius:2px;padding:3px 8px;
  background:rgba(31,95,208,.06)}
.vent .badge.q{color:var(--steel);border-color:var(--line);background:transparent}

/* ---- honest-answer pairs ---- */
.qa{border:1px solid var(--line);border-radius:3px;background:var(--warm);overflow:hidden}
.qa>div{padding:clamp(20px,2.4vw,28px);border-bottom:1px solid var(--line)}
.qa>div:last-child{border-bottom:0}
.qa .q{font-family:var(--serif);font-size:clamp(17px,1.8vw,20px);line-height:1.36;
  color:var(--ink);margin:0 0 12px;letter-spacing:-.01em}
.qa .a{font-size:14.8px;line-height:1.68;color:var(--body);margin:0;max-width:74ch}
.qa .a b{color:var(--ink);font-weight:600}
.on-ink .qa{background:transparent;border-color:#274259}
.on-ink .qa>div{border-color:#274259}
.on-ink .qa .q{color:var(--warm)}
.on-ink .qa .a{color:#AEBDCA}

/* footnote list */
.notes{list-style:none;margin:0;padding:0;counter-reset:n}
.notes li{counter-increment:n;position:relative;padding:10px 0 10px 30px;
  font-size:12.4px;line-height:1.6;color:#7A858F;border-top:1px solid var(--line)}
.notes li::before{content:counter(n);position:absolute;left:0;top:11px;
  font-family:var(--serif);font-size:11px;color:var(--cobalt)}
.notes a{color:#7A858F;text-decoration:underline;text-underline-offset:2px}
.notes a:hover{color:var(--cobalt)}
sup.fn{font-size:10px;font-weight:700;color:var(--cobalt);vertical-align:super;margin-left:2px}

/* dark-section variants of the Studio pieces */
.on-ink .led{border-color:#274259}
.on-ink .led .row{border-color:#274259}
.on-ink .led .t{color:var(--warm)}
.on-ink .led .d{color:#AEBDCA}
.on-ink .led .n{color:var(--cobalt-lt)}
.on-ink .ev{background:#274259;border-color:#274259}
.on-ink .ev>div{background:var(--navy-deep)}
.on-ink .ev .v{color:var(--warm)}
.on-ink .ev .l{color:#AEBDCA}
.on-ink .ev .src{color:#8195A6;border-color:#274259}
.on-ink .btn-p{background:var(--cobalt);border-color:var(--cobalt)}
.on-ink .price .amt{color:var(--warm)}

/* the six-phase strip needs six columns at width */
.phases.p6{grid-template-columns:repeat(6,1fr)}
@media (max-width:1080px){.phases.p6{grid-template-columns:repeat(3,1fr)}}
@media (max-width:620px){.phases.p6{grid-template-columns:1fr}}
"""

CSS = CSS_BASE + CSS_STUDIO

JS = """
document.querySelectorAll('.drop').forEach(function(d){
  var t;
  d.addEventListener('mouseenter',function(){clearTimeout(t);d.open=true});
  d.addEventListener('mouseleave',function(){t=setTimeout(function(){d.open=false},140)});
});
document.addEventListener('click',function(e){
  document.querySelectorAll('.drop[open]').forEach(function(d){ if(!d.contains(e.target)) d.open=false; });
});
var bg=document.querySelector('.burger'), mo=document.querySelector('.mobile');
if(bg){bg.addEventListener('click',function(){
  var o=mo.classList.toggle('open'); bg.setAttribute('aria-expanded',o?'true':'false');
});}
"""

# ---------------------------------------------------------------- config
#
# SITE is the one place the domain is declared. The parent site's
# portfolio.html currently states the Studio was "confirmed as a subdomain of
# the corporate site" — that copy contradicts this build and needs a patch on
# the parent before launch. Changing the line below is the only edit required
# here if the subdomain is chosen instead.
SITE = "https://bailiwickventurestudio.com"
PARENT = "https://bailiwickventures.com"
VIBE = "https://bailiwickvibe.com"
FORM_ACTION = "https://formsubmit.co/michael@bailiwickventures.com"

NAV_ITEMS = [
    ("model.html", "The Model"),
    ("process.html", "Process"),
    ("ventures.html", "Ventures"),
    ("engage.html", "Engage"),
]


def nav(active):
    items = ""
    for href, label in NAV_ITEMS:
        on = ' class="on"' if href == active else ""
        items += f'<li><a href="{href}"{on}>{label}</a></li>'
    items += (f'<li class="up"><a href="{PARENT}" target="_blank" rel="noopener">'
              f'Bailiwick Ventures <span class="ext" aria-hidden="true">↗</span></a></li>')

    mob = "".join(f'<a href="{h}">{l}</a>' for h, l in NAV_ITEMS)
    mob += '<a href="engage.html#triage">Start the Triage — $2,500</a>'
    mob += f'<a href="{PARENT}" target="_blank" rel="noopener">Bailiwick Ventures ↗</a>'
    mob += f'<a href="{VIBE}" target="_blank" rel="noopener">BailiwickVibe ↗</a>'

    return f"""<header class="nav">
  <div class="nav-in">
    <a class="brand" href="index.html" aria-label="Bailiwick Venture Studio home">
      {mark(32)}
      <span><span class="bn">Bailiwick&nbsp;Venture&nbsp;Studio</span><span class="bs">Diagnose · Architect · Prove</span></span>
    </a>
    <nav aria-label="Primary"><ul class="menu">{items}</ul></nav>
    <a class="nav-cta" href="engage.html#triage">Start the Triage</a>
    <button class="burger" aria-label="Menu" aria-expanded="false"><span></span></button>
  </div>
  <div class="mobile">{mob}</div>
</header>"""


FOOTER = f"""<footer class="site">
  <div class="shell">
    <div class="eyebrow" style="color:#7F93A6">Where the work goes next</div>
    <div class="handoff">
      <div><div class="hw">Bring us an idea</div><p>A consequential problem you keep running into, and no defensible answer yet to what it costs or whether it works.</p></div>
      <div><div class="hw">Bring us a venture</div><p>Something already begun that was never designed as a whole system, and now cannot be explained to an investor.</p></div>
      <div><div class="hw">Take it to production</div><p>The proof holds and the architecture is settled. BailiwickVibe carries it from proof to deployed and commercial.</p></div>
      <div><div class="hw">Talk to the parent</div><p>Investment, ownership, portfolio-level relationships and Michael's personal advisory sit with Bailiwick Ventures, Inc.</p></div>
    </div>

    <div class="f-grid" style="margin-top:clamp(44px,5vw,66px)">
      <div class="f-brand">
        <div style="display:flex;align-items:center;gap:12px">
          {mark(28, "#FFFDF9", "Bailiwick Venture Studio")}
          <span class="bn">Bailiwick&nbsp;Venture&nbsp;Studio</span>
        </div>
        <p>The venture architecture division of Bailiwick Ventures,&nbsp;Inc. From consequential idea to usable proof.</p>
        <div class="social">
          <a href="https://www.linkedin.com/in/mlatkinson1/" target="_blank" rel="noopener" aria-label="Michael L. Atkinson on LinkedIn" title="Michael on LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3V9zm7 0h3.8v1.7h.05a4.2 4.2 0 0 1 3.77-2.07c4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.5c0-1.31-.02-3-1.83-3-1.83 0-2.11 1.43-2.11 2.9V21h-4V9z"/></svg></a>
          <a href="https://x.com/Michaelatkinson" target="_blank" rel="noopener" aria-label="Michael L. Atkinson on X" title="@Michaelatkinson on X"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.53 3H20.5l-6.49 7.42L21.64 21h-5.97l-4.68-6.12L5.62 21H2.65l6.94-7.93L2.36 3h6.12l4.23 5.59L17.53 3zm-1.04 16.2h1.65L7.6 4.71H5.83L16.49 19.2z"/></svg></a>
          <a href="https://substack.com/@michaellatkinson1" target="_blank" rel="noopener" aria-label="Michael L. Atkinson on Substack" title="Substack"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3.5 3h17v2.3h-17V3zm0 4.3h17v2.3h-17V7.3zM3.5 11.6 12 16.4l8.5-4.8V21L12 16.2 3.5 21v-9.4z"/></svg></a>
        </div>
      </div>
      <div>
        <h4>The Studio</h4>
        <a href="index.html">Overview</a>
        <a href="model.html">The Model</a>
        <a href="process.html">The Six Phases</a>
        <a href="ventures.html">Ventures</a>
        <a href="engage.html">Engage</a>
      </div>
      <div>
        <h4>Engagements</h4>
        <a href="engage.html#triage">The Triage — $2,500</a>
        <a href="engage.html#blueprint">Plan A · Blueprint — $25,000</a>
        <a href="{PARENT}/plans.html" target="_blank" rel="noopener">Plan B · Buildout <span class="ext">↗</span></a>
        <a href="{PARENT}/plans.html" target="_blank" rel="noopener">Plan C · Venture <span class="ext">↗</span></a>
      </div>
      <div>
        <h4>Evidence</h4>
        <a href="model.html#evidence">What the data shows</a>
        <a href="model.html#criticism">What it does not</a>
        <a href="model.html#sources">Sources &amp; notes</a>
        <a href="process.html#gate">Where the Studio stops</a>
      </div>
      <div>
        <h4>Elsewhere</h4>
        <a href="{PARENT}" target="_blank" rel="noopener">Bailiwick Ventures, Inc. <span class="ext">↗</span></a>
        <a href="{VIBE}" target="_blank" rel="noopener">BailiwickVibe <span class="ext">↗</span></a>
        <a href="https://fohboh.ai" target="_blank" rel="noopener">FohBoh.ai <span class="ext">↗</span></a>
        <a href="https://michaelatkinson.me" target="_blank" rel="noopener">MichaelAtkinson.me <span class="ext">↗</span></a>
        <a href="mailto:info@bailiwickventures.com">info@bailiwickventures.com</a>
      </div>
    </div>

    <div class="f-quote">
      <p>&ldquo;The best way to predict the future is to invent it.&rdquo;</p>
      <cite>Alan Kay</cite>
    </div>

    <div class="f-bot">
      <p>&copy; 2026 Bailiwick Ventures, Inc. All rights reserved. &nbsp;·&nbsp; <a href="{PARENT}/privacy.html" style="display:inline;padding:0">Privacy</a></p>
      <p>Bailiwick Venture Studio is a wholly owned operating division of Bailiwick Ventures, Inc.</p>
    </div>
  </div>
</footer>"""


ORG_JSONLD = """{
  "@context":"https://schema.org",
  "@type":"Organization",
  "name":"Bailiwick Venture Studio",
  "url":"SITE_URL",
  "logo":"SITE_URL/brand/png/tile-navy-512.png",
  "description":"The venture architecture division of Bailiwick Ventures, Inc. From consequential idea to usable proof of concept in 60 days or less.",
  "email":"info@bailiwickventures.com",
  "parentOrganization":{"@type":"Organization","name":"Bailiwick Ventures, Inc.","url":"PARENT_URL"},
  "founder":{"@type":"Person","name":"Michael L. Atkinson","jobTitle":"Founder & Chief Executive Officer","url":"https://michaelatkinson.me"},
  "sameAs":["https://www.linkedin.com/in/mlatkinson1/","https://x.com/Michaelatkinson"]
}""".replace("SITE_URL", SITE).replace("PARENT_URL", PARENT)


def page(title, desc, active, body, og_extra=""):
    canonical = SITE + ("/" if active == "index.html" else "/" + active)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:site_name" content="Bailiwick Venture Studio">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Bailiwick Venture Studio — from consequential idea to usable proof.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/og-image.png">
<meta name="theme-color" content="#12304F">
{og_extra}
<link rel="icon" type="image/svg+xml" href="/brand/svg/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/brand/png/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/brand/png/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/brand/png/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<script type="application/ld+json">{ORG_JSONLD}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,300;8..60,400;8..60,600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<a class="sr" href="#main">Skip to content</a>
{nav(active)}
<main id="main">
{body}
</main>
{FOOTER}
<script>{JS}</script>
</body>
</html>
"""
