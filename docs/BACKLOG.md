# Kochab Backlog

The maintainer's working list of candidate features, each tied to the **need underneath** the stated want. The roadmap decides order and commits to versions; this backlog holds the fuller set of candidates and the reasons they matter, so decisions are made against real needs rather than a wish list.

How items flow:

- **In:** a `roadmap-interview` run ends with a "New candidate for the backlog" line. That candidate lands here as a row, with the need under the want and how strongly it was felt.
- **Out:** when a candidate is committed to a release, it moves into `ROADMAP.md` under its version and is marked Planned here. When it ships, `CHANGELOG.md` records it and the row is marked Shipped.

Status values: **Candidate** (recorded, not committed) · **Planned** (committed to a roadmap version) · **Shipped** (in a released version) · **Out of scope** (declined; see the wall in `ROADMAP.md` / `ETHICS.md`).

Signal is how strongly and how often the need has surfaced. Rows seeded from the roadmap are marked `roadmap` until real interview signal is attached.

> Seeded 2026-07-11 from the v1.0 and post-1.0 candidates already written in `ROADMAP.md` (themselves distilled from product-discovery interviews). No new features invented here; this is consolidation. Raw interview notes, when captured, live alongside this file and feed the rows below.

---

## Spine themes (cross-cutting, govern many rows)

| Theme | The need underneath | Status | Signal |
|---|---|---|---|
| Pipeline orchestration as working-memory offload | A person cannot hold more than a few applications in their head; the tool holding the whole search (state of each application, the next action for each, timing across competing processes, capacity) is a core job, not a convenience | Shipped (v0.6) | roadmap |
| Adjustable intervention dial | How much the tool coaches, nudges, and diagnoses should be the user's setting, light-touch by default, tunable up or down; over-coaching erodes trust, under-coaching leaves people stuck | Shipped (v0.9) | roadmap |

## Near-term — Scan enrichment (pre-1.0)

| Candidate | The need underneath | Status | Signal |
|---|---|---|---|
| Directional gap line in the scan | She sees a fit rating and a named gap, but not what closing the gap would do; making the gap forward-looking turns a static rating into a next step. Directional pointer only, not a curriculum pitch (see v0.5.1 in `ROADMAP.md`) | Shipped | maintainer, direct |
| Tunable study plans | A recommendation is only useful if she can act on it at her real pace; the same skill needs a different plan at 15 minutes a day than at 4 hours a day, so time budget must reshape the plan, not just its length (see v0.5.2 in `ROADMAP.md`) | Shipped | maintainer, direct |

## Road to 1.0 — External, employer-facing beats

| Candidate | The need underneath | Status | Signal |
|---|---|---|---|
| Follow-up timing | Knowing when to nudge after applying or interviewing, without pestering or going silent | Shipped (v0.7) | roadmap |
| Prep for the first call (recruiter or hiring-manager screen) | The screen is where good candidates get cut on avoidable things; walk in ready | Shipped (v0.8) | roadmap |
| Post-call next actions | Momentum is lost in the gap after a call when it is unclear what to do next | Shipped (v0.7) | roadmap |
| Interview prep across formats (extends v0.5) | A search runs from one-off screens to a panel battery to an onsite; prep has to scale to the format | Shipped (v0.8) | roadmap |
| Phase-by-phase guidance | People do not know what a given stage expects of them or what comes after | Shipped (v0.8) | roadmap |
| References: best and bad practices | References are handled late and clumsily; who to ask, when, and how to brief them | Shipped (v0.8) | roadmap |
| Offer handling and negotiation | The highest-stakes, least-practiced moment of the search, where leaving money and terms on the table is common | Shipped (v0.9) | roadmap |

## Road to 1.0 — Internal, the user's own process and state

| Candidate | The need underneath | Status | Signal |
|---|---|---|---|
| Triage a high-fit role they are not interested in | Not every strong match is wanted; the tool should let a person decline without friction or guilt | Shipped (v0.7) | roadmap |
| Getting applications out the door | Started applications stall; the need is closing the gap between drafted and sent | Shipped (v0.7) | roadmap |
| How and when to engage the network | People freeze on outreach; timing and framing lower the barrier | Shipped (v1.0) | roadmap |
| Application tracking across many | Holding the state of many parallel applications exceeds working memory (see spine theme) | Shipped (v0.6) | roadmap |
| Rescinding an application cleanly | Withdrawing gracefully, without burning a bridge, is unclear and stressful | Shipped (v0.9) | roadmap |
| Recovering from a rejection | A rejection can stall a whole search; the need is to metabolize it and keep moving | Shipped (v0.9) | roadmap |
| Light funnel diagnosis from the user's own data | The search itself is data; surface what it is teaching (where things stall, what converts) without preaching | Shipped (v0.9) | roadmap |

## Road to 1.0 — Network, bounded

| Candidate | The need underneath | Status | Signal |
|---|---|---|---|
| Contact-to-employer matching ("you know someone here") | A warm intro beats a cold application; surface real overlaps between contacts and targets. **Intent-gated:** fires only when the user signals they want to apply, never a blanket scan | Shipped (v1.0) | roadmap |
| Encouragement nudge (optional, honest) | Chronically under-confident users skip roles they are qualified for; naming a warm contact lowers the barrier, but only where they genuinely qualify | Shipped (v1.0) | roadmap |

**Decided approach (2026-07-11): contacts come from a download, not a scrape.** The user supplies their network as their own LinkedIn data export (LinkedIn → Settings → Get a copy of your data → Connections) or pastes contacts in. Kochab never scrapes LinkedIn or reads connections behind a login, consistent with ETHICS principle 2. The export is parsed locally, matched against `Target_Employers.md`, and stays in the user's folder. This constraint applies to both rows above, since the encouragement nudge draws on the same contact data.

## Post-1.0 — Beyond the offer

| Candidate | The need underneath | Status | Signal |
|---|---|---|---|
| First-day and onboarding prep | The search does not end at the offer; starting well is its own task | Candidate | roadmap |
| General skill and career augmentation | Ongoing growth beyond a single search | Candidate | roadmap |
| Promotions | Advancing in a role is adjacent to searching and reuses the same evidence | Candidate | roadmap |
| Moving jobs | A deliberate move while employed differs from an urgent search | Candidate | roadmap |
| Changing careers | A career change stresses the tailoring and honesty machinery hardest | Candidate | roadmap |
| People / relationship CRM | Track interviewers, referrers, what was said, and follow-ups owed; relationships outlast any one search | Candidate | roadmap |
| Search-while-employed vs. quit-and-search decision support | A high-stakes life decision the tool can inform honestly | Candidate | roadmap |
| Handling a large resume gap | Adjacent to existing tailoring and honesty guardrails, so it may pull earlier than post-1.0 | Candidate (may pull earlier) | roadmap |

## Post-1.0 — Capture and scoring refinements

| Candidate | The need underneath | Status | Signal |
|---|---|---|---|
| Comp range and comp-agnostic option in setup | Setup captures a comp **floor** and a comp-vs-mission **ranking**, but not a target range or ceiling, and "comp-agnostic" is only expressible indirectly (mission-first, no floor). Some people think in a band and want to say so plainly. Add an optional comp range and an explicit comp-agnostic setting to the setup interview and `Master_Profile.md`, feeding the location/comp handling in the scan. Small, additive; does not touch a non-negotiable | Candidate | maintainer, direct (2026-07-14) |

---

## Intake: turning a roadmap-interview into backlog rows

After a `roadmap-interview` run, take its "Requests, paired with the need underneath" table and its "New candidate for the backlog" line, and for each:

1. Add or update a row in the right section above, writing the **need**, not just the want.
2. Set **Signal** from how strongly and how often it surfaced (replace `roadmap` with real interview signal as it accumulates, for example `2 interviews, strong`).
3. If it duplicates an existing row, raise that row's signal rather than adding a new one.
4. If it falls on the permanent wall in `ROADMAP.md` / `ETHICS.md`, mark it **Out of scope** with a one-line reason instead of dropping it silently.

Recently shipped work (v0.1 through v0.5) lives in `ROADMAP.md` and `CHANGELOG.md`; it is not repeated here.
