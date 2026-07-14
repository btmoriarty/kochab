# Study Plans

A study plan turns a gap into a bounded, honest path to closing it. It exists because a job she does not get today can still tell her what to go learn, and the scan is already watching for the requirement that keeps blocking roles she wants.

The plan is a decision aid, not a curriculum she is enrolled in. It ends by returning the choice to her.

## When it surfaces on its own

The scan offers a plan only when a gap is **both**:

1. **Recurring.** The same missing qualification caps two or more roles she has rated Strong-if-only or Stretch, across the current run or the recent scan history.
2. **Bounded.** It lives in the "closes in a quarter" or "closes in a year" bucket from `gap_analysis.md`, not "not closing soon."

A one-off gap is named in the Build section and left alone. Only a pattern earns the offer. This is the guard against sending her to chase a certificate for a single posting.

**The auto-offer surfaces in the weekly summary, not the daily note.** The daily scan may detect a recurring gap, but it does not pitch a curriculum every morning. See "Weekly cadence" below.

## Calling it on demand

She can ask any time, in natural language: "make me a study plan," "what should I study," "what do you recommend," "how do I qualify for [role]." Infer the target from what she gives you:

- **She names a skill or topic** → plan for that.
- **She points at a specific job or role** → plan to clear that role's real screens.
- **She asks "what do you recommend" right after a scan** → the target is the specific skill the role's directional line named. That line exists to seed exactly this plan, so carry its named skill straight in rather than re-deriving it.
- **She says nothing specific** → pick the **highest-leverage recurring gap**: the requirement blocking the most roles she wants, read from her recent scan notes and tracker.

If there is no scan history yet and she names nothing, do not guess. Infer likely recurring requirements from her `Master_Profile.md` and `Target_Employers.md`, name them, and ask which one to plan for. Better to ask than to plan for the wrong gap.

## Time budget: the primary tuning input

How much time she has is the input that shapes the plan most, so establish it before assembling anything.

- **Default to setup, override on the spot.** Use the hours per week captured at setup as the default, but always take an in-the-moment figure when she gives one ("I have 15 minutes a day," "four hours a day," "maybe six hours a week"). The latest thing she says wins.
- **Normalize to hours per week** so the math is consistent: 15 minutes a day is about 1.75 hours a week; one hour a day is 7; four hours a day is about 28. State the weekly figure you are planning against so she can correct it.
- **If no budget is known and she gives none, ask once.** A plan paced to the wrong budget is worse than a short pause to get it right. This is the one thing not to guess.

## Pace changes the plan, not just its length

A bigger budget is not the same plan finished sooner. The budget changes what the plan is made of. Assemble differently across three bands, and always show the calendar horizon the chosen budget implies to reach the artifact.

- **Lean, under about 3 hours a week (for example 15 minutes a day).** One resource at a time, never parallel. The smallest artifact that still demonstrates the skill. Micro-sessions with spaced repetition, built to survive interruption. Cut all breadth to the single highest-leverage thread. Be honest that this is a months-long trickle, not a sprint, and give the real horizon rather than a flattering one.
- **Steady, about 3 to 10 hours a week.** The standard month-by-month path: one primary resource carried to completion, the demonstrable artifact alongside it, a little breadth where it genuinely helps.
- **Immersive, over about 10 hours a week (for example 4 hours a day).** Project-first: start building early and let the resources serve the build. A more ambitious artifact worth showing. Parallel threads in the same week (learn, build, read), a compressed calendar, and an earlier re-assessment checkpoint.

**Re-tunable.** If she changes the budget ("what if I only get 15 minutes?"), recompose the plan for the new band; do not just stretch or compress the dates. Show the new horizon and the new running total.

## The plan (structure)

Save as `Study_Plan_<topic>_<YYYY-MM-DD>.md`. Sections:

### The target
The specific gap, and the concrete claim she will be able to make when done, phrased the way a resume bullet would carry it. The endpoint is a **demonstrable artifact**, not a certificate of attendance. "A working X she can show" beats "completed a course in X."

### Why this gap, over the others
One paragraph on why this is the highest-leverage thing for her actual target list right now. Tie it to the specific roles it unblocks.

### The path, month by month
Real, web-searched resources: named courses, books, docs, projects, each with a rough time cost. Pace and shape it to the weekly budget established above, following the band it falls in, and give a running total she can sanity-check against her life. Prefer free or low-cost and reputable over expensive and branded.

### The artifact
The portfolio piece, talk, open-source contribution, or small public project that **demonstrates** the skill. This is the part most study plans skip and the part that actually moves a resume, because "I studied X" loses to "here is X I built." Name a specific, achievable artifact.

### The checkpoint
A re-assessment date, and the instruction to re-run the relevant roles against her updated profile then, to confirm the gap actually closed rather than assume it did. If it did, the plan worked; if not, adjust.

## Weekly cadence (for the scheduled scan)

The scheduled scan runs daily and is memoryless, so "weekly" is determined by file state and the calendar, not by remembering last week:

- On the configured weekly-summary day (default Monday, or the first run of a new calendar week), read the last roughly seven `job_scan_*.md` notes plus the tracker and aggregate which gaps recurred.
- If a gap is recurring and bounded, surface the **offer** (not the full plan) in that day's note: name the gap, the roles it blocked, a rough time-to-close, and ask if she wants a plan.
- On other days, detect and log gaps as usual, but do not surface the offer.
- Generate the full plan only when she says yes, or when she asks on demand.

## Guardrails

- **Be skeptical of certifications.** Recommend one only when it appears as a real screen in multiple roles she wants, never because it exists. The field is full of paid credentials employers do not actually check for.
- **Honest time estimates**, hers to live, not optimistic marketing. "Roughly three months at five hours a week" beats "fast-track in 30 days."
- **Real resources only.** Verify a course or book actually exists and is current before listing it. Do not invent a syllabus.
- **Never imply the gap makes her a weaker person.** It is a nameable, closable gap, which is the only kind there is.
- **Return the decision to her.** The plan ends with a choice, not an enrollment.
