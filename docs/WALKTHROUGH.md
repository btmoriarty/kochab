# Walkthrough: a full session, start to finish

This is the tool in use, shown with a made-up person so you can see the actual inputs and outputs, not just descriptions. Everything below is illustrative. Your own run will differ, but the shape is real.

Meet **Sam Rivera**, a marketing analyst in Austin who wants to move into product analytics. Sam has installed the `kochab` skill and made an empty folder called `Sam Job Search`.

Format of this doc: **You** is what Sam types or does. **Tool** is what comes back, trimmed to the parts that matter.

---

## 1. Setup

**You:** *set up my job scan* (with `sam_resume.pdf` attached)

**Tool** reads the resume and reflects it back before asking anything:

> I read your resume. A few things I want to get right before we go further:
> - You've been a "Marketing Analyst" at Brightline for four years, but three of the bullets are about building dashboards and running SQL against the warehouse. That reads more like analytics than marketing. Which is it, mostly?
> - You list "led the attribution model rebuild." Did you own that, or were you on the team that did it?
> - Tableau, dbt, and "Python" are all listed flat. Which do you actually build in, versus have touched?

Sam answers, and the interview continues through what a normal week looks like, what Sam is moving toward (product analytics) and away from (campaign reporting), commute and remote tolerance, a compensation floor, and the ranking question:

> **When compensation and mission conflict, which wins?**
> *Sam: comp matters, but I'd take a real product-analytics role over a better-paid marketing one.*

Then the part that makes the drafts trustworthy:

> For each thing on your resume that sounds more impressive than it was, tell me the honest version.
> *Sam: I didn't "lead" the attribution rebuild, I built the data pipeline feeding it. And "Python" is really pandas scripts, not software engineering.*

The tool records these as rules:

> Guardrails saved:
> - Say "built the data pipeline for the attribution rebuild," never "led the attribution rebuild."
> - Say "analysis scripting in Python (pandas)," never imply software engineering.

### What gets written

`Master_Profile.md` (canonical, tailored down from, never rebuilt):

```
## Honesty guardrails
- "built the data pipeline for the attribution rebuild," never "led" it
- "analysis scripting in Python (pandas)," not software engineering
## Search priorities
- Target: product analytics / data analyst (product). Moving away from campaign reporting.
- Comp floor: $95k. Ranking: a real product-analytics role beats a better-paid marketing one.
- Austin metro; hybrid ok; remote preferred; no relocation.
## Hours for upskilling: ~5/week
```

`Story_Bank.md` is seeded from the resume, then filled in by a short interview:

```
### The dashboard nobody would give up
Demonstrates: turning a messy ask into a tool a team relies on
Situation: Sales kept asking analytics for the same three numbers weekly...
Task: Sam's to own end to end.
Action: Built a self-serve Tableau dashboard on a dbt model...
Result: Killed ~4 hours of weekly manual pulls; still in daily use.
Honest framing: Sam owned this one fully.
Best for: impact, self-serve tooling, stakeholder questions
```

`Target_Employers.md`, `Application_Tracker.md`, and `Discovered_Employers.md` are created. Setup ends by handing Sam a filled-in scheduled-task prompt to paste. Sam schedules it daily.

---

## 2. A morning scan (the ordinary case)

Most mornings, `job_scan_2026-04-14.md` looks like this:

> **No new matches today.**
> Checked: role-first searches (product analyst, data analyst product) across LinkedIn, Greenhouse, Ashby, Built In Austin; location-first (Austin, remote); two VC portfolio boards. Everything in-lane today was already in your tracker.
> Standing item: the Chorus "Analytics Engineer" role from Tuesday is still your top open Stretch.

That is the tool working. It did not manufacture a match to look busy.

---

## 3. A morning scan (a real match)

`job_scan_2026-04-17.md`:

> ### New this morning
>
> **Vessel (Series B, Austin + remote) — Product Analyst** — Strong (15/18)
> skill 3 · level 2 · domain 2 · location 3 · mission 3 · screens 2
> **Why you fit:** this is the self-serve-analytics job you've been doing at Brightline, named as product analytics. Your dashboard story lands directly.
> **The gap:** they mention experiment analysis (A/B testing) and you have little formal experimentation on your resume. Real, but learnable, and not a hard screen.
> **Legitimacy:** real company, posted 3 days ago, direct hire, comp band $100–130k (above your floor).
> [posting link, verified live]
>
> **Halcyon (Series A, remote) — Marketing Data Analyst** — Skip
> skill 3 · level 2 · domain 1 · location 3 · mission 1 · screens 3
> **Why it's a Skip:** you'd clear it easily, but it's campaign reporting, the exact work you said you're leaving. Level-sideways into the wrong lane.
>
> **Recurring gap forming:** experiment/A-B analysis has now shown up in 3 of your last 5 Strong or Stretch roles. Worth a plan; I'll surface one in the weekly summary.

Notice the tool argued *against* a role Sam would get, because it's the wrong direction. That is the honesty doing its job.

---

## 4. Drafting a note (Draft mode)

**You:** *draft a note for the Vessel product analyst role*

The tool does a short research pass for one true hook, pulls the dashboard story, and returns a short email. Note what it does **not** do: restate the posting.

> Subject: Product Analyst — Sam Rivera
>
> Hi [name],
>
> Your changelog note about moving self-serve metrics out of the data team and into the hands of PMs is the exact problem I spent the last two years on at Brightline. Sales there kept pinging analytics for the same three numbers every week; I built a dbt model and a Tableau dashboard that let them answer it themselves, which ended about four hours of manual pulls a week and is still the thing they open first every morning.
>
> I'm looking to do that kind of work full-time in a product context rather than a marketing one, which is why Vessel caught my eye. I'd bring the pipeline-and-self-serve instinct; I'd be learning your experimentation stack, which I'll be honest is newer to me than the modeling side.
>
> Happy to share the dashboard as a case study if useful.
>
> Sam

The line "which I'll be honest is newer to me" is the honesty guardrail at work, not a bug. It reads as candor, and it means Sam is not walking into the screen having oversold experimentation. There is also a longer formal-letter version if the application wants one.

---

## 5. A study plan (Plan mode)

The next weekly summary surfaces the offer:

> Experiment/A-B analysis has capped three roles you wanted this month. It's not a hard screen anywhere, but closing it turns those Stretches into Strongs. Roughly 6–8 weeks at your ~5 hours a week. Want a study plan?

**You:** *yes*

`Study_Plan_experimentation_2026-04-24.md`:

> **Target:** be able to say, truthfully, "I designed and analyzed an A/B test end to end," with something to show for it.
> **Why this gap:** it's the one requirement standing between you and the product-analyst roles you're already 80% qualified for.
> **Weeks 1–2:** Trustworthy Online Controlled Experiments (Kohavi), chapters 1–4. ~4 hrs.
> **Weeks 3–5:** a free experimentation course [named], plus reproduce one analysis in your own pandas. ~9 hrs.
> **Weeks 6–8:** run a small real experiment on a side project or a volunteer org's signup page; write it up. ~12 hrs.
> **The artifact:** a short public writeup of that experiment. "Here is an A/B test I ran" beats "I studied A/B testing."
> **Checkpoint (June 20):** re-run the Vessel-type roles against your updated profile and confirm the gap closed.

It did not tell Sam to go buy a $600 certificate. It pointed at a book, a free course, and a thing to build.

---

## 6. Interview prep (Interview mode)

Vessel invites Sam to a first call.

**You:** *prep me for my Vessel screen — it's a 30-minute call with the hiring manager*

`Interview_Prep_Vessel_2026-04-30.md`:

> **This stage:** hiring-manager screen, 30 min. Goal is fit and a sanity check on your background, not a deep technical grill.
>
> **Likely questions, mapped to your stories:**
> - "Walk me through a dashboard or tool you built that people actually used." → **The dashboard nobody would give up.** Lead with the four-hours-a-week result.
> - "How do you decide what to measure?" → same story, framed on how you scoped the three numbers.
> - "Tell me about a time you worked with PMs / non-analysts." → *(no story in your bank yet — let's add one before the call.)*
>
> **The thin spot:** they'll likely probe experimentation. Honest line: "I've been going deep on it recently — I'm running an A/B test on [side project] right now. My strength is the pipeline and modeling underneath; experimentation is the part I'm actively building." True, and it turns the gap into momentum.
>
> **Questions for you to ask:** how PMs currently get their numbers today; whether analysts own experiment design or just analysis; what the first 90 days looks like.

It flagged a missing story rather than inventing one, and offered to seed it.

---

## 7. Once you're in motion (Pipeline, Momentum, Offer, Network)

Sam applies to Vessel and a couple of others. From here the tool holds the whole search, so Sam does not have to keep it in their head.

**You:** *I applied to Vessel, and to Northwind and Cardinal too*

The tracker now carries all three, each with a stage and a next action. A week later:

**You:** *where does my search stand?*

> **Active: 3 of a target 4.**
> - **Vessel** — Interview. Next: prep the take-home, due Friday.
> - **Northwind** — Applied 8 days ago, no reply. A light check-in is reasonable now. Want me to draft one?
> - **Cardinal** — Screen booked Tuesday.
> Heads up: two of these land the week of the 20th, so you may want to space them.

That check-in is the **Momentum** layer. It suggests when to nudge, capped so it never pesters, respects any timeline the employer gave, and drafts the note for Sam to send. It never emails anyone itself.

Sam gets the Vessel offer.

**You:** *I got an offer from Vessel, $118k. help me think about it*

> Against your floor ($95k) and your ranking (a real product role over a better-paid marketing one), this clears both. Before you answer: base looks mid-band for the level and market, and they moved fast, so a counter to about $125k is reasonable and low-risk. Want me to draft it? Also get the equity vesting and the remote arrangement in writing.

It lays out the real decision and drafts a counter Sam sends. It does not negotiate for Sam, and it never invents a competing offer to bluff with.

And back when Sam was deciding whether to even apply to Cardinal:

**You:** *do I know anyone at Cardinal?*

> From the contacts you exported: yes. Marcus Okafor, a former Brightline colleague, is a senior analyst there. A short note asking for his read on the team beats a cold application. Want a draft? (This runs only for a company you are actually applying to, and only from your own contacts.)

How much the tool nudges and coaches through all of this follows your **coaching dial**, which Sam left on the light default. And if a rejection had come instead of an offer, **Process health** would have logged it honestly and kept the other two moving, rather than letting one no stall the search.

---

## 8. The other direction (opportunity-brief)

A week later a recruiter messages Sam about a "Growth Analyst" role at a company Sam has not heard of.

**You:** paste the message into the `opportunity-brief` skill

**Tool** returns a brief: what the company actually is (a 30-person martech startup, seed stage, one small raise 18 months ago and quiet since), what the role really is (campaign and funnel reporting under a "growth" label), the honest fit read (Skip — it's the marketing-reporting lane again, and the funding signal is a small yellow flag), and the decision left to Sam: *worth a reply to stay warm with the recruiter, not worth an application.*

---

## What this session showed

- The tool tailored down from one honest profile and never wrote a claim Sam couldn't back up.
- It argued against a role Sam would have gotten, because it was the wrong direction.
- It turned a recurring rejection reason into a bounded plan with a real artifact at the end.
- It flagged a missing interview story instead of bluffing one.
- Once Sam started applying, it held the whole pipeline, timed the follow-ups without pestering, weighed the offer, and surfaced a warm contact, all from Sam's own data.
- Every draft stopped at Sam's desk. Sam sent them.

That is the whole design: a sharp assistant to someone still doing their own thinking, from the first scan through the offer.
