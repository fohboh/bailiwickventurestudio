"""Shared content objects — phases, evidence, and sources.

Every published figure carries a numbered note that resolves to a named
source on model.html#sources. Figures that could not be traced to an
inspectable primary source are not published; the ones the industry repeats
anyway are named and struck on model.html#criticism, which is the point.
"""

# ---------------------------------------------------------------- phases
#
# The six Studio phases. Sequence is nominal — 04-06 routinely loop back
# into 03, and the site says so rather than pretending to a waterfall.
PHASES = [
    dict(
        n="01", name="Diagnose",
        short="Is the problem consequential? Market forces, constraints, and structural inefficiency.",
        ask="What is actually broken, for whom, and what does it cost them today?",
        do=("We separate the irritation from the inefficiency. Most ideas are a "
            "reaction to an annoyance; a venture needs a structural failure — something "
            "the current arrangement of an industry cannot fix without changing shape. "
            "We size that failure in money, not adjectives, and we look for who is "
            "already paying for it in a form they have stopped noticing."),
        out=("A written diagnosis of the problem, its cost, the forces holding the "
             "broken arrangement in place, and an explicit statement of what would "
             "have to be true for it to be worth solving."),
        gate="The problem is expensive, structural, and currently unowned.",
    ),
    dict(
        n="02", name="Map",
        short="Where are the risks and asymmetries? Leverage points and structural advantage.",
        ask="What kills this, and where does a small input produce a disproportionate result?",
        do=("We map the terrain before committing to a route: incumbents and what they "
            "are structurally unable to do, the regulatory and data constraints, the "
            "distribution paths that already exist, and the two or three assumptions "
            "on which the whole venture rests. Risks get ranked by what they would cost "
            "to be wrong about, not by how likely they feel."),
        out=("A risk and asymmetry map — ranked kill risks, identified leverage points, "
             "and a named first assumption to test."),
        gate="There is at least one asymmetry we can hold, and the kill risks are testable.",
    ),
    dict(
        n="03", name="Architect",
        short="What complete venture should exist? Product, capital structure, and operating model.",
        ask="What is the whole system — not the product, the whole system?",
        do=("This is the phase the name of the discipline comes from. Strategy, product, "
            "technology, unit economics, governance, commercialization and capital plan "
            "are designed together, because a decision in any one of them constrains the "
            "other five. A pricing model implies an architecture. An architecture implies "
            "a cost floor. A cost floor implies who can be sold to. Designing them in "
            "sequence is how ventures end up internally contradictory and unfundable."),
        out=("The venture architecture: thesis, category, customer, product definition, "
             "data model, unit economics, operating model, governance posture, and "
             "capital shape — as one coherent document."),
        gate="The system is internally consistent and the economics survive their own model.",
    ),
    dict(
        n="04", name="Build",
        short="Can we create a usable proof? Experience, workflows, data model, demonstrable product.",
        ask="Can someone who has the problem use this and tell us something true?",
        do=("We build the smallest artifact capable of testing the most consequential "
            "assumption — not a demo, and not a product. AI has collapsed the cost of "
            "this step, which is exactly why the discipline has to move upstream: when "
            "building is cheap, building the wrong thing is the expensive mistake."),
        out=("A usable proof of concept: real workflows, a real data model, and enough "
             "surface for a practitioner to work in it rather than watch it."),
        gate="A person with the problem can complete the core task unaided.",
    ),
    dict(
        n="05", name="Validate",
        short="Will customers care enough to act? Technical, product, and commercial evidence.",
        ask="Does anyone change their behavior — and would they pay?",
        do=("Evidence, gathered in the open. We put the proof in front of operators and "
            "buyers and record what they do, not what they say. Enthusiasm is not "
            "evidence. A pilot commitment, a signed letter of intent, a purchase order, "
            "or a refusal with a stated reason all count; a compliment does not."),
        out=("A validation record: what was tested, with whom, what happened, what it "
             "falsified, and what it left standing."),
        gate="The consequential assumption survived contact, or the architecture changed.",
    ),
    dict(
        n="06", name="Prepare",
        short="Should capital be committed? Production scope, GTM, capital plan, investor narrative.",
        ask="What does the next stage cost, and is the case strong enough to fund it?",
        do=("We convert the architecture and the evidence into the package the next "
            "stage requires: the production build specification, the go-to-market motion, "
            "the capital plan tied to milestones rather than to a round size, and an "
            "investor narrative that will survive diligence because it is describing "
            "something that already exists."),
        out=("Production blueprint, go-to-market plan, capital plan, and investor "
             "narrative — plus an honest recommendation on whether to proceed."),
        gate="Either the case for capital is defensible, or we say so and stop.",
    ),
]

# ---------------------------------------------------------------- evidence
#
# Only figures with a named, dated, inspectable-or-attributable source.
# `note` indexes into SOURCES below.
EVIDENCE = [
    dict(v="1,107", l="active venture studios catalogued worldwide in 2024, against 154 "
                      "recorded as closed — up from roughly 560 identified in 2020.",
         src="Big Venture Studio Research 2024; GSSN, <i>Disrupting the Venture Landscape</i>, 2020", note=1),
    dict(v="17 vs. 20", l="new studio registrations against closures in Q3 2024. Studio "
                          "formation peaked in 2020 at 114 founded against 10 closed. The "
                          "model is consolidating, not compounding.",
         src="Big Venture Studio Research 2024", note=1),
    dict(v="10.7 months", l="average time from day zero to a seed round across 258 "
                            "studio-created startups surveyed in 2020, against a roughly "
                            "three-year industry average. Self-reported by participating studios.",
         src="GSSN, <i>Disrupting the Venture Landscape</i>, 2020", note=2),
    dict(v="24%", l="exit rate for venture studio portfolio companies across 2,246 "
                    "PitchBook deals — ahead of accelerators at 14%, behind pre-seed "
                    "venture funds at 38%. The author notes the difference is not "
                    "statistically significant.",
         src="Big Venture Studio Research 2024, PitchBook data", note=1),
    dict(v="17–43%", l="the measured range of studio equity in the companies they create, "
                       "depending on dataset and on whether the studio supplied the "
                       "original idea. The conventional “20–40%” is a convention, not a measurement.",
         src="Big Venture Studio Research 2024; Vault Fund, 2023; Forum Ventures, 2024", note=3),
    dict(v="No benchmark", l="exists. The Venture Studio Forum — working with MIT, Harvard "
                             "and Stanford — states the field “still lacks shared benchmarks, "
                             "consistent definitions, and an authoritative global view of how "
                             "studios operate.” Its first global report is expected in 2026.",
         src="Venture Studio Forum, Global Venture Studio Survey, 2025", note=4),
]

# Claims in wide circulation that we decline to publish, and why.
STRUCK = [
    dict(c="“Studio startups exit 33% faster — five years to acquisition, based on "
           "182 acquisitions and 22 IPOs.”",
         w="One researcher's uncontrolled Crunchbase pull, published in the first person, "
           "with no described comparison group. <b>The same author's 2024 work, using "
           "PitchBook, reports 4.5 years on a 38-deal sample and states plainly that the "
           "result does not reach statistical significance.</b> Twenty-two IPOs cannot "
           "support a percentage comparison."),
    dict(c="“Venture studios return a 53% IRR, against 21.3% for traditional venture.”",
         w="Self-reported, largely unrealized, from roughly twenty to forty studios that "
           "chose to answer a survey — and benchmarked against traditional venture's "
           "<i>top quartile</i>. <b>The industry's own Venture Studio Forum has publicly "
           "disowned the comparison</b>, noting the sample under-counts failed studios "
           "that are no longer around to report."),
    dict(c="“Studio startups have a 30% higher success rate.”",
         w="No stated denominator. Studios kill upwards of 95% of concepts before they "
           "become companies, so a “success rate” measured on survivors is measuring the "
           "filter, not the method. <b>2024 exit-rate data puts studios below pre-seed "
           "venture funds.</b>"),
    dict(c="“625% growth in the number of venture studios over seven years.”",
         w="A 2020 figure, now six years old and <b>directionally wrong</b>: the sector has "
           "been in net contraction since 2020."),
]

SOURCES = [
    ('Global Startup Studio Network, <i>Disrupting the Venture Landscape</i> (2020). Survey of 258 '
     'startups created by roughly 40 studios; comparison data from CB Insights. Widely mis-cited '
     'online as a 2022 report — the speed, IRR and success-rate figures attributed to “GSSN 2022” '
     'are from this 2020 paper.',
     'https://insightstudios.s3.amazonaws.com/Disrupting-the-Venture-Landscape_GSSN-White-Paper-1.pdf',
     'GSSN white paper (PDF)'),
    ('Max Pog, <i>Big Venture Studio Research 2024</i>. PitchBook data across 2,246 deals; studio '
     'sub-sample of 38 deals from 23 studios. Supersedes the same author’s 2023 Crunchbase study.',
     'https://inniches.com/big-venture-studio-research', 'inniches.com'),
    ('Vault Fund, <i>2023 Company Creator Insights</i>. Note that only 13% of surveyed firms '
     'maintained a firm-level track record, and only 20 reported an IRR.',
     'https://vaultfund.com/wp-content/uploads/2023/11/2023-Company-Creator-Insights-by-Vault-Fund.pdf',
     'Vault Fund (PDF)'),
    ('Venture Studio Forum, <i>Global Venture Studio Survey</i> (2025, in collection with MIT, Harvard '
     'and Stanford); and M. Burris, “Venture Studios and the Pursuit of Truth” (January 2026).',
     'https://venturestudioforum.org/ecosystem-survey', 'venturestudioforum.org'),
    ('C. Moiana, A. Ghezzi and A. Rangone, “Venture studios beyond the hype: Key challenges and a '
     'way forward,” <i>Business Horizons</i> 69(4), 575–589 (2026). Peer-reviewed; studies eight '
     'global exemplars and fourteen Italian studios.',
     'https://ideas.repec.org/a/eee/bushor/v69y2026i4p575-589.html', 'Business Horizons'),
    ('The GSSN Data Report 2022, source of the frequently cited $1.36M median / $2.49M average studio '
     'operating budget, is not publicly available for inspection. We have not published those figures '
     'for that reason.', None, None),
]
