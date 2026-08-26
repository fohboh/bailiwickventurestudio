"""Page bodies for the Bailiwick Venture Studio site."""

from theme import PARENT, VIBE, FORM_ACTION, SITE
from content import PHASES, EVIDENCE, STRUCK, SOURCES

FN = '<sup class="fn">{}</sup>'


def _phase_strip():
    return '<div class="phases p6">' + "".join(
        f'<div class="phase"><div class="pn">{p["n"]}</div><h4>{p["name"]}</h4>'
        f'<p>{p["short"]}</p></div>' for p in PHASES) + "</div>"


def _evidence_grid():
    out = '<div class="ev">'
    for e in EVIDENCE:
        out += (f'<div><div class="v">{e["v"]}</div><div class="l">{e["l"]}'
                f'{FN.format(e["note"])}</div>'
                f'<div class="src">{e["src"]}</div></div>')
    return out + "</div>"


# ==================================================================== home
def home():
    return f"""
<div class="hero" style="background:linear-gradient(180deg,#FFFDF9 0%,#FFFDF9 58%,#F5F2ED 100%)">
  <div class="shell hero-in">
    <p class="eyebrow k">Bailiwick Venture Studio · An operating division of Bailiwick Ventures,&nbsp;Inc.</p>
    <h1>From consequential idea to usable proof of concept. In 60 days or less.<span style="color:var(--cobalt)">*</span></h1>
    <p class="lede">We are a day-zero co-founder, not a check. The Studio applies Enterprise Venture
      Architecture to turn a consequential problem into a coherent venture — strategy, product,
      technology, economics, governance, commercialization and capital designed together, then
      proven with something a real operator can actually use.</p>
    <div class="tagline"><span>Diagnose</span><i></i><span>Architect</span><i></i><span>Prove</span></div>
    <div class="btns">
      <a class="btn btn-p" href="engage.html#triage">Bring Us an Idea <span class="arrow">→</span></a>
      <a class="btn btn-s" href="process.html">See the Six Phases <span class="arrow">→</span></a>
    </div>
    <p class="fine" style="margin-top:24px;max-width:64ch"><span style="color:var(--cobalt)">*</span>
      The 60-day objective applies to appropriately scoped engagements with available
      decision-makers, defined access to the necessary subject-matter expertise, and timely
      validation. It is an objective we have met, not a guarantee we sell.</p>
  </div>
</div>

<section class="on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">The premise</p>
      <h2>Speed is not the thesis. Coherence is.</h2>
    </div>
    <div>
      <p class="lede" style="margin-bottom:24px">Venture development used to be slow because it was
        sequential — research, then strategy, then design, then engineering, then modeling, then
        market testing, each handoff introducing delay and rework. AI has collapsed the cost of
        several of those steps. It has not made the judgment any easier.</p>
      <p class="body">That is the whole shift. When building becomes cheap, building the wrong thing
        becomes the expensive mistake, and the scarce discipline moves upstream: deciding what should
        exist, why it should exist, and what evidence is required before anyone commits capital to it.
        The Studio uses AI to compress the work. Experienced human judgment decides what the work is.</p>
      <p class="pull">A venture that is fast and internally contradictory is not a venture. It is an
        expensive prototype with a pitch deck attached.</p>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow k">The Bailiwick process</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(28px,3.5vw,44px)">Six phases, run in parallel, not in sequence.</h2>
    {_phase_strip()}
    <p class="fine" style="margin-top:18px">Architecture is iterative. Stress-testing in phases 04–06
      routinely loops back into phase 03 — and it is supposed to. A process that never returns to the
      architecture is not testing it.</p>
    <div class="btns" style="margin-top:26px">
      <a class="btn btn-s" href="process.html">What happens in each phase <span class="arrow">→</span></a>
    </div>
  </div>
</section>

<section class="on-ink">
  <div class="shell">
    <p class="eyebrow">What leaves the Studio</p>
    <h2 style="max-width:22ch;margin-bottom:clamp(26px,3vw,42px)">Four artifacts. Not just an MVP.</h2>
    <div class="grid g4">
      <div><h4 style="margin-bottom:10px">Venture architecture</h4><p class="body" style="font-size:14.4px">
        Thesis, customer, category, economics, governance and operating model — designed as one
        system, written down as one document.</p></div>
      <div><h4 style="margin-bottom:10px">Usable proof</h4><p class="body" style="font-size:14.4px">
        A product with enough real surface to test the most consequential assumption against a person
        who has the problem.</p></div>
      <div><h4 style="margin-bottom:10px">Capital architecture</h4><p class="body" style="font-size:14.4px">
        Unit economics, funding requirement, milestone structure and an investor narrative built to
        survive diligence.</p></div>
      <div><h4 style="margin-bottom:10px">Production blueprint</h4><p class="body" style="font-size:14.4px">
        The engineering and go-to-market specification for what comes next — executable by us or by
        anyone competent.</p></div>
    </div>
    <hr class="rule" style="margin:clamp(34px,4vw,52px) 0 26px">
    <div style="display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap">
      <p class="body" style="margin:0;max-width:54ch">The Studio's work ends at the proof. Production
        engineering, enterprise readiness and market entry are BailiwickVibe's eight phases — a defined
        handoff rather than a hazy one.</p>
      <a class="btn btn-g" href="{VIBE}" target="_blank" rel="noopener">Visit BailiwickVibe <span class="arrow">→</span></a>
    </div>
  </div>
</section>

<section class="bord on-warm">
  <div class="shell">
    <div class="split" style="margin-bottom:clamp(30px,3.6vw,46px)">
      <div>
        <p class="eyebrow">The evidence</p>
        <h2>What the data actually supports.</h2>
      </div>
      <div>
        <p class="body">Venture studios are sold with statistics that mostly do not survive being
          looked up. We publish the figures that trace to a named, dated source — and on the model
          page we name the ones we refuse to publish, and why. If we would not put a number in front
          of an investor, we will not put it in front of you.</p>
        <a class="tlink" href="model.html#criticism">The numbers we struck, and why <span class="arrow">→</span></a>
      </div>
    </div>
    {_evidence_grid()}
    <p class="fine" style="margin-top:16px">Numbered notes resolve to named sources on
      <a href="model.html#sources" style="color:inherit;text-decoration:underline">the model page</a>.</p>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow k">Studio-born</p>
    <h2 style="max-width:26ch;margin-bottom:16px">The method has produced companies, not case studies.</h2>
    <p class="body" style="margin-bottom:clamp(28px,3.4vw,44px);max-width:66ch">Three ventures, three
      different problems, one method. Each began as a structural diagnosis rather than a product idea —
      and in each case the architecture is what made the business possible.</p>
    <div class="grid g3">
      <a class="card k-studio" href="ventures.html#fohboh">
        <div class="swatch"></div>
        <div class="kicker">Certified infrastructure</div>
        <h3>FohBoh.ai</h3>
        <p>A deterministic certification layer between operational systems and every system of record.
          Data is sealed on arrival, reconciled across authoritative sources, and issued as a certified
          operational fact — before AI ever sees it.</p>
        <span class="tlink">Read the architecture <span class="arrow">→</span></span>
      </a>
      <a class="card k-studio" href="ventures.html#quikfix">
        <div class="swatch"></div>
        <div class="kicker">Venture architecture</div>
        <h3>BailiwickQuikFix</h3>
        <p>On-demand home and commercial repair with a 60-minute commitment set by drive-time geofence
          rather than optimism. Six weeks from consequential idea to a complete investor package — with
          no production backend paid for.</p>
        <span class="tlink">Read the architecture <span class="arrow">→</span></span>
      </a>
      <a class="card k-studio" href="ventures.html#starbar">
        <div class="swatch"></div>
        <div class="kicker">Operating company</div>
        <h3>StarBar · SnapCount</h3>
        <p>Per-shift, voice-driven inventory counting that certifies against six deterministic
          conditions and anchors the result to an immutable ledger. The count stops being an estimate
          somebody typed in.</p>
        <span class="tlink">Read the architecture <span class="arrow">→</span></span>
      </a>
    </div>
  </div>
</section>

<section class="bord on-sand tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:22ch;margin:0 auto">Have an idea that deserves to be architected?</h2>
    <p class="body" style="margin:18px auto 0;max-width:56ch">Studio work is sold as
      <b>Plan A — Blueprint</b>: four weeks, fixed price, published. Every engagement begins with the
      Triage — ninety minutes, a written memo, and an honest answer including the one nobody wants.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="engage.html#triage">Start the Triage — $2,500 <span class="arrow">→</span></a>
      <a class="btn btn-s" href="engage.html#blueprint">What Blueprint delivers <span class="arrow">→</span></a>
    </div>
    <p class="fine" style="margin-top:18px">No free diagnostics. No plan below $25,000. If the honest
      answer is that you should not build this, the memo says so.</p>
  </div>
</section>
"""


# =================================================================== model
def model():
    struck = "".join(
        f'<div class="struck"><p class="c">{s["c"]}</p><p class="w">{s["w"]}</p></div>'
        for s in STRUCK)

    srcs = ""
    for i, (text, url, label) in enumerate(SOURCES, 1):
        link = (f' <a href="{url}" target="_blank" rel="noopener">{label} ↗</a>'
                if url else "")
        srcs += f"<li>{text}{link}</li>"

    return f"""
<div class="hero">
  <div class="shell hero-in">
    <p class="eyebrow k">The model</p>
    <h1>A venture studio is a co-founder, not an investor.</h1>
    <p class="lede">The category is young enough that the words are still used loosely and the
      statistics are still mostly borrowed. This page says plainly what the model is, what the
      evidence supports, what it does not, and where the honest criticisms land.</p>
  </div>
</div>

<section class="on-warm">
  <div class="shell split">
    <div>
      <p class="eyebrow">Definition</p>
      <h2>What a venture studio actually is.</h2>
    </div>
    <div>
      <p class="lede" style="margin-bottom:22px">An organization that routinely creates startups from
        the ground up. It generates and tests its own ideas, commits its own capital and people,
        allocates a shared team across several ventures at once, and brings in operating founders to
        run what survives.</p>
      <p class="body">A venture capital firm evaluates companies other people started. An accelerator
        improves companies that already exist. A venture studio is present before there is anything to
        evaluate — it originates the idea, designs the business, builds the first version, and holds a
        meaningful stake because it did the founding work rather than funded it.</p>
      <p class="body">The consequence is a different relationship to risk. A fund manages risk by
        diversifying across founders. A studio manages risk by killing ideas early, cheaply, and in
        volume — before they become companies with payrolls attached.</p>
    </div>
  </div>
</section>

<section class="bord">
  <div class="shell">
    <p class="eyebrow">Where it sits</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(26px,3vw,40px)">Studio, incubator, accelerator, fund.</h2>
    <div class="cmp-wrap">
    <table class="cmp">
      <caption>Stage boundaries are conventional rather than regulated; individual firms blur them.</caption>
      <thead><tr><th scope="col">Model</th><th scope="col">Engages at</th><th scope="col">What it contributes</th><th scope="col">Typical stake</th></tr></thead>
      <tbody>
        <tr class="us"><th scope="row">Venture studio</th>
          <td>Before the company exists. Day zero, and often before the idea.</td>
          <td>The idea, the architecture, the first team, early capital, and daily operating work until spin-out.</td>
          <td>Substantial. Measured medians run 17–43% depending on dataset and on whether the studio supplied the idea.{FN.format(3)}</td></tr>
        <tr><th scope="row">Incubator</th>
          <td>An early idea and a founding team that already exist.</td>
          <td>Space, mentorship, and help refining the idea and assembling the team.</td>
          <td>Small or none; sometimes fee-based.</td></tr>
        <tr><th scope="row">Accelerator</th>
          <td>A prototype or MVP, sometimes first revenue.</td>
          <td>A fixed 3–6 month program, mentorship, a demo day, and a small standardized check.</td>
          <td>Typically a single-digit percentage on standard terms.</td></tr>
        <tr><th scope="row">Venture fund</th>
          <td>Demonstrated traction and a case for growth.</td>
          <td>Capital, governance, network, and follow-on capacity.</td>
          <td>A negotiated minority position, priced by round.</td></tr>
      </tbody>
    </table>
    </div>
    <p class="body" style="margin-top:clamp(24px,3vw,34px);max-width:72ch">The other distinction worth
      making is a funding one. A <b>venture studio</b> raises outside capital to invest in and support
      the companies it builds; a <b>startup studio</b> works from its partners' own capital. Bailiwick
      Venture Studio is a wholly owned operating division of Bailiwick Ventures,&nbsp;Inc. — a single-entity
      holding structure — and is funded from the parent rather than from an external fund vehicle.</p>
  </div>
</section>

<section class="on-ink" id="evidence">
  <div class="shell">
    <p class="eyebrow">The evidence</p>
    <h2 style="max-width:26ch;margin-bottom:20px">What the data supports, stated at the confidence it deserves.</h2>
    <p class="body" style="max-width:70ch;margin-bottom:clamp(28px,3.4vw,44px)">Each figure below traces
      to a named, dated source, and each one carries its methodology in the same breath — sample size,
      who collected it, and whether it was self-reported. Where a number is a survey finding rather than
      an industry fact, it says so.</p>
    {_evidence_grid()}
  </div>
</section>

<section class="bord" id="criticism">
  <div class="shell split">
    <div>
      <p class="eyebrow k">What we will not publish</p>
      <h2>Four numbers you will see on other studio websites.</h2>
      <p class="body" style="margin-top:20px">We checked them. They do not hold, and we are not going
        to put them in front of you and hope you do not look. Trust is the product; that starts with
        the footnotes.</p>
    </div>
    <div>{struck}</div>
  </div>
</section>

<section class="on-warm bord">
  <div class="shell">
    <p class="eyebrow">The honest criticisms</p>
    <h2 style="max-width:26ch;margin-bottom:clamp(26px,3vw,40px)">The four real objections to the model — and our answers.</h2>
    <div class="qa">
      <div>
        <p class="q">“Good founders will not hand a studio 30–40% of their company.”</p>
        <p class="a">Correct, and they should not — <b>if all they are getting is money and advice.</b>
          The stake is defensible only where the studio supplied the origin: the diagnosis, the
          architecture, the first build and the capital plan. Where a founder arrives with the idea
          already formed, the honest structure is a fee, not a founding stake. We price both, we publish
          both, and we say which one applies before an engagement starts.</p>
      </div>
      <div>
        <p class="q">“Studios spread themselves across too many ventures and do none of them well.”</p>
        <p class="a">A real failure mode, and the peer-reviewed literature names it — the
          <i>heterogenesis of ends</i>, where short-term studio economics and long-term venture health
          pull in opposite directions.{FN.format(5)} Our answer is structural rather than aspirational:
          the Studio stops at the proof. Production engineering, enterprise readiness and market entry
          belong to BailiwickVibe under a defined handoff, so the Studio is never carrying an operating
          business and a new diagnosis at the same time.</p>
      </div>
      <div>
        <p class="q">“The performance data is self-reported by the studios that survived.”</p>
        <p class="a">Also correct. Studios kill upwards of 95% of concepts before they become companies,
          so any published “success rate” is measuring the filter as much as the method — and the
          surveys behind the widely quoted return figures under-count studios that closed and are no
          longer around to answer. <b>That is why the evidence section above leads with market
          structure rather than with returns,</b> and why we publish the sample size next to every
          number.</p>
      </div>
      <div>
        <p class="q">“Studios without a defined niche cannot attract founders or investors.”</p>
        <p class="a">The clearest criticism of the model, and the easiest to fail. Ours is narrow on
          purpose: consequential problems in food, beverage, restaurants, CPG and fintech, where the
          structural failure is one of trust in operational data — and where forty years of operating
          domain expertise is the reason we can tell an irritation from an inefficiency in the first
          conversation rather than the fourth.</p>
      </div>
    </div>
  </div>
</section>

<section class="bord" id="sources">
  <div class="shell">
    <p class="eyebrow">Sources &amp; notes</p>
    <h2 style="max-width:24ch;margin-bottom:24px">Every figure on this site, and where it came from.</h2>
    <ol class="notes" style="max-width:88ch">{srcs}</ol>
    <p class="fine" style="margin-top:24px;max-width:82ch">Nothing on this page is an offer to sell or a
      solicitation of an offer to buy any security. Third-party figures are reproduced as published by
      their sources and are not independently verified by Bailiwick Ventures,&nbsp;Inc.</p>
  </div>
</section>

<section class="bord on-sand tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:24ch;margin:0 auto">The method matters more than the category.</h2>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="process.html">See the Six Phases <span class="arrow">→</span></a>
      <a class="btn btn-s" href="ventures.html">See What It Built <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""


# ================================================================= process
def process():
    blocks = ""
    for i, p in enumerate(PHASES):
        tone = ' on-warm' if i % 2 else ''
        bord = ' bord' if i else ''
        blocks += f"""
<section class="{tone}{bord}" id="p{p['n']}">
  <div class="shell split">
    <div>
      <p class="eyebrow k">Phase {p['n']}</p>
      <h2>{p['name']}</h2>
      <p class="pull" style="margin-top:22px">{p['ask']}</p>
    </div>
    <div>
      <p class="body" style="margin-bottom:22px">{p['do']}</p>
      <h4 style="margin-bottom:10px">What you get</h4>
      <p class="body" style="margin-bottom:22px">{p['out']}</p>
      <div class="gate" style="margin:0">
        <div class="lbl">What advances it</div>
        <p style="font-size:clamp(16px,1.6vw,18px);margin:0">{p['gate']}</p>
      </div>
    </div>
  </div>
</section>"""

    return f"""
<div class="hero">
  <div class="shell hero-in">
    <p class="eyebrow k">The process</p>
    <h1>Six phases. Run in parallel, and revisited on purpose.</h1>
    <p class="lede">Every phase has a question it exists to answer, a deliverable it produces, and a
      condition that has to be met before the venture advances. Nothing moves forward because time
      passed.</p>
    <div class="btns">
      <a class="btn btn-p" href="engage.html#triage">Start the Triage <span class="arrow">→</span></a>
      <a class="btn btn-s" href="#gate">Where the Studio stops <span class="arrow">→</span></a>
    </div>
  </div>
</div>

<section class="on-sand tight">
  <div class="shell">
    {_phase_strip()}
    <p class="fine" style="margin-top:18px">The numbering is nominal. Phases 04–06 routinely send work
      back into phase 03, because that is what stress-testing an architecture is for. A process that
      never returns to the design is not testing it — it is decorating it.</p>
  </div>
</section>
{blocks}

<section class="bord on-ink" id="gate">
  <div class="shell">
    <p class="eyebrow">The handoff</p>
    <h2 style="max-width:24ch;margin-bottom:22px">The Studio's work ends at the proof. Deliberately.</h2>
    <div class="split">
      <div>
        <p class="body">These six phases are pre-proof work: deciding what should exist, designing it
          as a whole system, and producing enough evidence to justify building it for real. That is a
          different discipline from making software survive real users, real data and real money — and
          a studio that pretends otherwise ends up doing both badly.</p>
      </div>
      <div>
        <p class="body">Everything after the proof — refactoring for production, security and data
          integrity, governance and IP structure, economic simulation at scale, cap table and control
          calibration, launch, and investor and acquisition readiness — is <b>BailiwickVibe's 8-Phase
          Venture Architecture</b>. Same company, same discipline, later stage, and a defined handoff
          rather than a hazy one.</p>
        <a class="btn btn-g" href="{VIBE}" target="_blank" rel="noopener" style="margin-top:8px">See the eight phases <span class="arrow">→</span></a>
      </div>
    </div>
  </div>
</section>

<section class="bord tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:24ch;margin:0 auto">Sixty days is the objective. The gates are the guarantee.</h2>
    <p class="body" style="margin:18px auto 0;max-width:58ch">We would rather tell you in week two that
      the problem is not consequential than deliver a beautiful architecture for a business that should
      not exist.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="engage.html#blueprint">What Blueprint delivers <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""


# ================================================================ ventures
def ventures():
    return f"""
<div class="hero">
  <div class="shell hero-in">
    <p class="eyebrow k">Ventures</p>
    <h1>What the method actually produced.</h1>
    <p class="lede">Each of these began as a structural diagnosis rather than a product idea. In every
      case the architecture is what made the business possible — and in one case it is the reason no
      production backend was ever paid for.</p>
  </div>
</div>

<section class="on-warm">
  <div class="shell">

    <div class="vent" id="fohboh">
      <div class="hd"><span class="badge">Studio-born · Operating</span><span class="badge q">Certified infrastructure</span></div>
      <h3>FohBoh.ai</h3>
      <div class="split" style="margin-top:20px">
        <div>
          <h4 style="margin-bottom:10px">The problem</h4>
          <p class="body" style="font-size:14.8px">A restaurant group runs point-of-sale, inventory,
            labor, payroll and accounting on separate systems, each producing its own version of
            “sales” and “cost.” Nobody can say which number is authoritative — and AI trained on those
            numbers inherits the contradiction rather than resolving it.</p>
          <dl class="meta">
            <div><dt>Role</dt><dd>Founded and architected</dd></div>
            <div><dt>Sector</dt><dd>Restaurant infrastructure</dd></div>
            <div><dt>Status</dt><dd>Operating · raising</dd></div>
          </dl>
        </div>
        <div>
          <h4 style="margin-bottom:10px">What was architected</h4>
          <p class="body" style="font-size:14.8px">The Metrics Governance Engine — a deterministic
            certification layer between operational systems and every system of record. Data is sealed
            on arrival, normalized, reconciled across authoritative sources, scored against trust gates,
            and issued as a certified operational fact rather than a raw number.</p>
          <h4 style="margin:20px 0 10px">What changed</h4>
          <p class="body" style="font-size:14.8px">Certification happens <i>before</i> data reaches the
            system of record, so neither the source system nor the destination can influence the
            outcome. Sentry™ and Cortex™ are the first applications built on that foundation — proof
            that the engine works, not the reason it exists.</p>
          <a class="tlink" href="https://fohboh.ai" target="_blank" rel="noopener">fohboh.ai <span class="arrow">↗</span></a>
        </div>
      </div>
    </div>

    <div class="vent" id="quikfix">
      <div class="hd"><span class="badge">Studio-born · In development</span><span class="badge q">Venture architecture</span></div>
      <h3>BailiwickQuikFix</h3>
      <div class="split" style="margin-top:20px">
        <div>
          <h4 style="margin-bottom:10px">The problem</h4>
          <p class="body" style="font-size:14.8px">On-demand home and commercial repair is a large,
            fragmented market with no dependable promise attached to it. Response times are estimates,
            dispatch is manual, and margin leaks everywhere between the customer and the tradesperson.</p>
          <dl class="meta">
            <div><dt>Role</dt><dd>Originated in the Studio</dd></div>
            <div><dt>Sector</dt><dd>Home &amp; commercial services</dd></div>
            <div><dt>Elapsed</dt><dd>Six weeks to package</dd></div>
          </dl>
        </div>
        <div>
          <h4 style="margin-bottom:10px">What was architected</h4>
          <p class="body" style="font-size:14.8px">Three applications, a licensed governance engine, and
            a 60-minute service commitment set by drive-time geofence rather than optimism — combined
            with voice and AI into an intelligence stack no competitor has assembled.</p>
          <h4 style="margin:20px 0 10px">What changed</h4>
          <p class="body" style="font-size:14.8px">No production backend was ever paid for. The venture
            was architected, modeled, governed and packaged — fifteen documents from pitch deck to
            engineering handoff, and three viable exit paths — before the expensive part began.
            <b>That sequencing is the whole argument.</b></p>
        </div>
      </div>
    </div>

    <div class="vent" id="starbar">
      <div class="hd"><span class="badge">Operating company</span><span class="badge q">Majority owned</span></div>
      <h3>StarBar · SnapCount™</h3>
      <div class="split" style="margin-top:20px">
        <div>
          <h4 style="margin-bottom:10px">The problem</h4>
          <p class="body" style="font-size:14.8px">Periodic inventory is still done on a clipboard and
            typed in afterward. It is slow, error-prone, and because it is unpleasant it gets done late
            or approximated — which corrupts every cost metric downstream of it.</p>
          <dl class="meta">
            <div><dt>Role</dt><dd>Majority owned</dd></div>
            <div><dt>Sector</dt><dd>ResTech</dd></div>
            <div><dt>Trust layer</dt><dd>MGE licensee</dd></div>
          </dl>
        </div>
        <div>
          <h4 style="margin-bottom:10px">What was architected</h4>
          <p class="body" style="font-size:14.8px">Per-shift, voice-driven counting against a locked
            watchlist — one item at a time, spoken, with tenthing for partial bottles. Mid-shift
            breakage and transfers are captured with a photo, so the variance math stays clean and
            custody is never inferred.</p>
          <h4 style="margin:20px 0 10px">What changed</h4>
          <p class="body" style="font-size:14.8px">The count stops being an estimate. Certification is
            deterministic — named opening count, named closing count, both inside the shift window,
            variance within threshold, trust score at or above 85, and no open exception. All six, or
            it is not certified.</p>
          <a class="tlink" href="https://starbar.ai" target="_blank" rel="noopener">starbar.ai <span class="arrow">↗</span></a>
        </div>
      </div>
    </div>

  </div>
</section>

<section class="bord on-ink">
  <div class="shell">
    <p class="eyebrow">What we take on</p>
    <h2 style="max-width:24ch;margin-bottom:clamp(26px,3vw,40px)">Five conditions. All of them, or we decline.</h2>
    <ul class="crit" style="max-width:82ch">
      <li><b>The problem is structural.</b> Not an irritation, and not a feature somebody's incumbent
        forgot to ship. Something the current arrangement of an industry cannot fix without changing
        shape.</li>
      <li><b>Somebody is already paying for it.</b> In money, in labor, or in losses they have stopped
        noticing. A problem nobody is currently funding is a hobby.</li>
      <li><b>Architecture is what changes the value.</b> If the outcome turns on capital, timing or
        salesmanship rather than on how the thing is designed, we are the wrong partner and will say so.</li>
      <li><b>The decision-maker is available.</b> One person who can decide, in the room. Not a
        committee tour, and not a proxy relaying answers.</li>
      <li><b>The evidence can be gathered.</b> There is a reachable population of people with the
        problem who will tell us the truth by what they do.</li>
    </ul>
    <p class="body" style="margin-top:clamp(28px,3.2vw,40px);max-width:64ch">Investment, ownership and
      portfolio-level relationships sit with the parent company rather than with the Studio.</p>
    <a class="btn btn-g" href="{PARENT}/portfolio.html" target="_blank" rel="noopener">See the full Bailiwick portfolio <span class="arrow">→</span></a>
  </div>
</section>

<section class="bord tight">
  <div class="shell" style="text-align:center">
    <h2 style="max-width:24ch;margin:0 auto">Bring us the problem, not the pitch.</h2>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="engage.html#triage">Start the Triage — $2,500 <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""


# ================================================================== engage
BLUEPRINT = [
    ("01", "Venture architecture",
     "Thesis, customer, category, and the value exchange. What this is — and the adjacent things it is deliberately not."),
    ("02", "Risk &amp; asymmetry map",
     "What kills it, ranked. Where a small investment produces a disproportionate result. Which assumption to test first."),
    ("03", "Unit economics",
     "A working model, not a slide. Cost to serve, price, margin, and the honest breakeven — including AI inference cost."),
    ("04", "Product definition",
     "The workflows, the data model, and the ruthless first cut of what does not get built in version one."),
    ("05", "Build specification",
     "Scoped work, architecture direction, stack recommendation, and acceptance criteria. Executable by us or by anyone else."),
    ("06", "Capital shape",
     "What reaching proof costs, what it should be funded with, and whether it needs outside money at all."),
    ("07", "Walkthrough",
     "A recorded 60-minute session on the whole package, with your engineers or advisors in the room if you want them."),
    ("08", "Thirty days after",
     "Email access to Michael for thirty days following delivery, for the questions that only surface once you start."),
]


def engage():
    led = '<div class="led">' + "".join(
        f'<div class="row"><div class="n">{n}</div><div class="t">{t}</div><div class="d">{d}</div></div>'
        for n, t, d in BLUEPRINT) + "</div>"

    return f"""
<div class="hero">
  <div class="shell hero-in">
    <p class="eyebrow k">Engage the Studio</p>
    <h1>We publish the number. You arrive knowing what you are buying.</h1>
    <p class="lede">Most firms make you sit through discovery before they will tell you what anything
      costs. There is one way into Studio work and it is priced, and the plan it leads to is priced.
      Published scope, published price, published exclusions.</p>
    <div class="btns">
      <a class="btn btn-p" href="#triage">Start the Triage — $2,500 <span class="arrow">→</span></a>
      <a class="btn btn-s" href="#blueprint">What Blueprint delivers <span class="arrow">→</span></a>
    </div>
  </div>
</div>

<section class="on-warm" id="triage">
  <div class="shell">
    <p class="eyebrow">The front door</p>
    <div class="price"><span class="amt">$2,500</span><span class="terms">The Triage · two sessions · written memo · credited in full</span></div>
    <div class="split" style="margin-top:clamp(26px,3vw,38px)">
      <div>
        <p class="body">Ninety minutes with Michael, a written assessment of what you actually have and
          what it would take to make it real, then half an hour walking through it together.</p>
        <p class="body">It is paid because unpaid diagnostics get treated as free consulting, and
          because the memo is worth more than most people pay for a month of advice. The entire fee is
          credited against any plan booked within 30 days of delivery.</p>
        <p class="pull">If the honest answer is that you should not build this, the memo says so. That
          is a finished deliverable, not a failed sale.</p>
      </div>
      <div>
        <h4 style="margin-bottom:12px">What you bring</h4>
        <ul class="ticks">
          <li>Whatever exists — a document, a repository, a prototype URL, a deck, or nothing but the problem.</li>
          <li>Read access to the code and data, if there is code and data.</li>
          <li>The person who can actually decide. One call, not a committee tour.</li>
          <li>An honest account of what has already been tried and what it cost.</li>
        </ul>
        <h4 style="margin:24px 0 12px">What you leave with</h4>
        <ul class="ticks">
          <li><b>Findings &amp; Path</b> — a written memo, inside five business days.</li>
          <li>An unsentimental read of what you have, including the parts that only look finished.</li>
          <li>The three or four things most likely to kill it, ranked.</li>
          <li>Which plan fits, why the other two do not, and an indicative cost and elapsed time.</li>
          <li>What we would do in your position if you never hired us.</li>
          <li>A <b>30-minute walkthrough</b> with Michael — findings discussed, not emailed and abandoned.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="bord" id="blueprint">
  <div class="shell">
    <p class="eyebrow k">Plan A · Run by Bailiwick Venture Studio</p>
    <h2 style="margin-bottom:18px">Blueprint.</h2>
    <div class="price"><span class="amt">$25,000</span><span class="terms">4 weeks · fixed · 60 / 40</span></div>
    <p class="body" style="margin-top:22px;max-width:70ch">The first three phases of the Studio's
      six-phase process, plus a build specification. Blueprint answers the question that stops most
      founders before they start: <b>what exactly am I building, and is it worth building?</b> You end
      the month with a venture designed as a whole system and a specification precise enough that a
      competent engineer — or a competent engineer paired with AI — can begin on the Monday.</p>
    <p class="body" style="max-width:70ch">No code is written. That is deliberate. Building before this
      work is done is how people spend forty thousand dollars discovering that the thing they built was
      not the business.</p>

    <h3 style="margin:clamp(32px,3.8vw,48px) 0 6px">Eight named deliverables</h3>
    {led}

    <div class="gate" style="margin-top:clamp(30px,3.6vw,44px);margin-bottom:0">
      <div class="lbl">Not included in Blueprint</div>
      <p>Working software, visual design, and anything investor-facing.</p>
      <p class="sub">No code, no design comps, no prototype, no pitch deck, no incorporation, no
        fundraising. Blueprint produces the decision and the specification. Building it is Plan B;
        funding it is Plan C.</p>
      <div class="exc">
        <div class="lbl">Payment</div>
        <p><b>60% at signature, 40% on delivery.</b> Fixed at signature for the named scope. Blueprint
          credits in full against Plan B or Plan C started within ninety days — the specification is the
          input to both, so you never pay for the same discovery twice.</p>
      </div>
    </div>
  </div>
</section>

<section class="on-ink bord">
  <div class="shell">
    <p class="eyebrow">After the Blueprint</p>
    <h2 style="max-width:26ch;margin-bottom:clamp(24px,3vw,38px)">Two plans carry it further. Neither one is run by the Studio alone.</h2>
    <p class="body" style="max-width:62ch;margin:-14px 0 clamp(24px,3vw,38px);font-size:14.6px">Both involve
      <b>BailiwickVibe</b>, our sister division &mdash; the same company, the same discipline, a later
      stage. The Studio stops at the proof; Vibe begins at the prototype.</p>
    <div class="grid g2">
      <div>
        <h3 style="margin-bottom:10px">Plan B · Buildout</h3>
        <div class="price" style="margin-bottom:14px"><span class="amt" style="font-size:clamp(26px,2.6vw,32px)">$85,000</span><span class="terms">10–14 weeks · fixed</span></div>
        <p class="body" style="font-size:14.6px">Run by <b>BailiwickVibe</b> — phases 01 through 04 of
          its eight-phase method, carried through to a deployed system. A prototype that demos is not a
          product; Buildout is the finish carpentry.</p>
      </div>
      <div>
        <h3 style="margin-bottom:10px">Plan C · Venture</h3>
        <div class="price" style="margin-bottom:14px"><span class="amt" style="font-size:clamp(26px,2.6vw,32px)">From $250,000</span><span class="terms">6–9 months · plus 3–6% equity</span></div>
        <p class="body" style="font-size:14.6px">Run by the <b>Studio and BailiwickVibe together</b> &mdash;
          everything above, plus the entity, the economics, the launch, and an investor package built to
          survive diligence. Bailiwick materially inside the business rather than adjacent to it.</p>
      </div>
    </div>
    <a class="btn btn-g" href="{PARENT}/plans.html" target="_blank" rel="noopener" style="margin-top:clamp(26px,3vw,38px)">All three plans in full <span class="arrow">↗</span></a>
  </div>
</section>

<section class="bord on-warm">
  <div class="shell">
    <p class="eyebrow">Standing positions</p>
    <h2 style="max-width:26ch;margin-bottom:clamp(24px,3vw,38px)">Four things that are settled before we ever talk about your venture.</h2>
    <ul class="crit" style="max-width:84ch">
      <li><b>Compensation is never contingent on a financing.</b> Cash is a fixed fee, payable whether
        or not a raise happens. Equity, where it applies, is negotiated and fixed in writing before the
        engagement begins, with time-based vesting and no acceleration. There is never a success fee, a
        percentage of proceeds, or a finder's fee.</li>
      <li><b>We are not fractional executives, and we are not recruiters.</b> Introductions and help,
        yes. Staffing and operating roles, no. Founders build their own teams — and we strongly
        encourage building them from people you have known a while, because a newly assembled team is a
        negative in diligence.</li>
      <li><b>Nothing is free.</b> Scoping calls, prototype reviews, architecture opinions and “can I
        pick your brain” all resolve to the same place: the Triage. One fee, one memo, credited if you
        proceed.</li>
      <li><b>There is a floor.</b> We do not open a plan below $25,000. Below that number there is no
        version of this work that is honest about what it can deliver, so we do not sell one. If your
        budget is under the floor, take the Triage anyway and use the memo yourself — that is a
        legitimate outcome and we will write it that way.</li>
    </ul>
  </div>
</section>

<section class="bord" id="start">
  <div class="shell split">
    <div>
      <p class="eyebrow k">Start a conversation</p>
      <h2>Tell us the situation.</h2>
      <p class="body" style="margin-top:18px">The more specific you are about the problem — and about
        what has already been tried — the more useful the first reply will be. If the Studio is the
        wrong door, we will say which one is right.</p>
      <p class="body">Prefer email? <a class="tlink" href="mailto:info@bailiwickventures.com">info@bailiwickventures.com</a></p>
    </div>
    <div>
      <form class="inquiry" method="POST" action="{FORM_ACTION}">
        <input type="hidden" name="_subject" value="Bailiwick Venture Studio — inquiry">
        <input type="hidden" name="_next" value="{PARENT}/thanks.html">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="f2">
          <div class="field"><label for="name">Name</label>
            <input id="name" name="name" type="text" required autocomplete="name"></div>
          <div class="field"><label for="email">Email</label>
            <input id="email" name="email" type="email" required autocomplete="email"></div>
        </div>
        <div class="f2">
          <div class="field"><label for="company">Company</label>
            <input id="company" name="company" type="text" autocomplete="organization"></div>
          <div class="field"><label for="stage">Where you are</label>
            <select id="stage" name="stage">
              <option>An idea, and nothing built</option>
              <option>An idea, and something built that I do not trust</option>
              <option>A venture underway that was never architected</option>
              <option>Ready for the Triage</option>
              <option>Something else</option>
            </select></div>
        </div>
        <div class="field"><label for="msg">The situation</label>
          <textarea id="msg" name="message" required placeholder="What is the problem, who has it, and what has been tried?"></textarea>
          <p class="hint">Please do not send confidential material in a first message. We will tell you
            when there is a mutual NDA in place.</p></div>
        <button class="btn btn-p" type="submit">Send <span class="arrow">→</span></button>
      </form>
    </div>
  </div>
</section>
"""


# =================================================================== extras
def notfound():
    return """
<section style="padding-top:clamp(70px,9vw,130px)">
  <div class="shell" style="text-align:center">
    <p class="eyebrow k">404</p>
    <h1 style="max-width:20ch;margin:0 auto">That page is outside our bailiwick.</h1>
    <p class="body" style="margin:20px auto 0;max-width:48ch">The link is broken or the page has moved.
      The six phases and the ventures are both a click away.</p>
    <div class="btns" style="justify-content:center">
      <a class="btn btn-p" href="index.html">Back to the Studio <span class="arrow">→</span></a>
      <a class="btn btn-s" href="process.html">The Six Phases <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""
