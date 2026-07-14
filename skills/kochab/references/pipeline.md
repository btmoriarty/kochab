# Pipeline

The scan finds roles. The pipeline holds them once she acts. This is the working-memory offload: a person cannot keep the state of a dozen parallel applications, the next move on each, and how their timing collides in their head, so the tool keeps it instead. One file, one source of truth: `Application_Tracker.md`.

This reference defines the tracker schema, the pipeline stages, what a "next action" is, how the timing view reads, and what capacity means. It is deliberately bounded to **holding and showing state**. It does not tell her when to follow up (that is v0.7), it does not coach a stage (v0.8 and v0.9), and it does not diagnose her funnel (v0.9). It records what she did and lays it out so she can see the whole search at once.

## One tracker, not two

Pipeline state lives inside kochab, in `Application_Tracker.md`, alongside the scan that feeds it. Decided 2026-07-11: build the pipeline into kochab rather than extend the standalone `job-application-tracker` skill, so scan finds, applied state, and every downstream beat read and write one file. The standalone tracker skill is separate; whether it is later folded in or retired is its own question, not a blocker here. When both are installed and the triggers overlap, prefer the kochab tracker for anyone running the full search through kochab.

## The file: `Application_Tracker.md`

A header, then three tables. Every role the scan has ever surfaced or she has ever acted on lives in exactly one of them. A role moves between tables; it is never duplicated across them.

```
# Application Tracker - [Name]

Capacity: [N] active applications at once (target, not a cap). Updated [YYYY-MM-DD].

## Active
| Role | Org | Lane | Stage | Fit (/18) | Next action | Due | Link | Notes |

## Watching
| Role | Org | Lane | Fit (/18) | Gap | Found | Link | Notes |

## Closed
| Role | Org | Outcome | Closed | Notes |
```

The Watching **Notes** column carries the row's state between scan and send, for example "cover note drafted 07-13, not sent." Momentum mode reads it to surface drafted-not-sent roles.

**Active** holds every application she has actually sent and everything still live after it: applied, screening, interviewing, offer. This is the heart of the pipeline.

**Watching** holds roles that are scored but not yet sent: fresh scan finds, and roles she has decided to pursue but has not applied to. This is what the scan used to call "new finds." A Watching row can carry its own next action ("finish resume, send") so a drafted-but-unsent role does not vanish; closing that drafted-to-sent gap is v0.7's theme, but the row has to exist first.

**Closed** is the archive: rejected, withdrawn, declined, accepted, or gone silent. Nothing is deleted. A closed row is search history, and the funnel diagnosis in v0.9 reads from it.

Every role in any of the three tables is **already known** to the scan and off the "new" list. Dedup reads all three.

## Stages

A single ordered vocabulary for the Stage column in Active. Keep to these words so the timing view and later releases can rely on them.

`Applied` → `Screen` → `Interview` → `Final` → `Offer`

- **Applied:** she has sent it. Entry point to Active.
- **Screen:** a recruiter or hiring-manager screen is scheduled or done.
- **Interview:** one or more rounds underway.
- **Final:** onsite, panel battery, or last round.
- **Offer:** an offer is on the table.

A role leaves Active for Closed at any point, in either direction of good news or bad. The stages are a place to record where things stand, not a script the tool pushes her through. v0.6 names the stage; the guidance for each stage arrives in v0.8 and v0.9.

## Next action and Due

Each Active row carries the single next thing **she** has decided to do, in her words, plus an optional date.

- The next action is one concrete move: "reply to recruiter," "send writing sample," "prep for panel," "decide on offer." One move, not a plan.
- **Due** is a date she gives or a date tied to something real (an interview she booked, a deadline the employer set). If she has not set one, leave it blank. Pipeline mode does not invent a follow-up date; suggesting when to nudge is Momentum mode's job (see `references/momentum.md`), where the cadence is defined.
- A Watching row may also carry a next action in its Notes-adjacent sense ("draft cover note, then send"), so a role she means to apply to is not lost between scan and send. Getting that role sent is acted on in Momentum mode.

The tool records these. Pipeline mode does not nag when a Due date passes. If she asks what is overdue, the timing view shows it as a fact; suggesting a follow-up on it is Momentum mode.

## The timing view

The reason to hold all of this in one place is to see it laid out at once. When she asks where her search stands, or after a scan, produce a short status read from the tracker:

1. **Counts by stage.** How many Active, split across Applied / Screen / Interview / Final / Offer. How many Watching. How many Closed recently.
2. **Active vs capacity.** Active count against her target (see below): under, at, or over.
3. **Next actions, soonest first.** The Active rows sorted by Due, earliest first, blanks last. This is her to-do list, in her own words, pulled from state rather than reconstructed from memory.
4. **Collisions.** When two or more live processes have actions or dates in the same week, say so plainly: "three things land the week of the 20th." Naming the pileup is the whole point; she decides what to do about it.
5. **Stalled, only if she asks.** Rows whose Due has passed, or that have sat in one stage a long time, listed as a fact with no scolding. Whether and when to nudge is Momentum mode (`references/momentum.md`).

The view is a mirror, not a coach. It reflects the state she has recorded so she can act on the whole picture instead of the one application in front of her.

## Capacity

A running search has a natural ceiling: how many live applications she can give real attention to at once. Past it, quality drops and things get dropped. Capacity is her stated target for concurrent Active applications, captured once at setup (see `setup_interview.md`, Part 3) and stored in the tracker header.

- It is a target, not a cap. The tool never blocks her from adding a role or applying.
- When Active is at or over the target, the status read says so, once, as a fact: "you are running seven active against a target of five." That is information for her, not a verdict and not a nag. Whether to slow discovery, triage a role she is lukewarm on, or simply push on is her call. (Frictionless triage of a role she does not want is v0.7.)
- If no target was ever set, ask once, or treat capacity as unset and skip the line rather than guessing a number.

Capacity respects the same rule as everything else here: it returns the decision to her.

## Updating the tracker: the operations

Pipeline mode (Step F in `SKILL.md`) is a small set of read-and-write operations on this file. Each one reads the current tracker, makes the smallest change that matches what she said, and confirms it back.

- **Log an application.** "I applied to X." Move the matching Watching row into Active with Stage `Applied`, or add a new Active row if it was never watched. Ask for a next action and due only if it is natural; do not interrogate.
- **Advance a stage.** "I heard back from X," "moved to the panel." Update Stage and, if she named one, Next action and Due.
- **Set or change a next action.** "Next thing on X is the writing sample, due Friday." Update those two fields.
- **Close a role.** "Rejected from X," "I withdrew," "I accepted." Move the row to Closed with the outcome and date. Never delete.
- **Add a watch by hand.** A role she found herself, not through a scan. Add to Watching, scored if she wants a read, or unscored with a note.
- **Report status.** "Where does my search stand." Produce the timing view above. This is read-only.

Match a role she names to an existing row the same way the scan dedups: same employer and role family. When unsure which row she means, ask rather than guess. After any write, save the file and confirm the one thing that changed.

## What this does not do

- It does not submit anything, advance a stage on its own, or fill a form. She reports what she did; the tool records it. ETHICS principle 1 holds here as everywhere.
- It does not compute follow-up timing or tell her to nudge. That is Momentum mode (v0.7, `references/momentum.md`).
- It does not coach a stage or prep her for it beyond what v0.5 interview prep already does. Stage guidance is v0.8.
- It does not diagnose her funnel or read patterns across the search. The Closed archive is built to support that, but the diagnosis is v0.9.
- It does not treat capacity as a limit to enforce. It is a number she set, reflected back once when she crosses it.
