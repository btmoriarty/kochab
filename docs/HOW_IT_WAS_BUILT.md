# How Kochab Was Built

Kochab is a job-search assistant with a single stubborn opinion: an honest "no" is worth more than a flattering "yes." Most automated job tools optimize for volume. They scrape everything, score each listing with a confident number, and fill the form for you. That produces spam for employers, terms-of-service violations for the user, and resumes that slowly stop being true. Kochab is built on the opposite bet. This is the story of how it got made, because the method is part of the point.

## One version at a time

Kochab was built in small, reviewable steps, not one big push. Version 0.1 did two things only: it scored how well a role fits you, shown as a handful of justified sub-scores instead of one confident number, and it packaged the tool as installable Claude skills. Each version after that added one capability and was reviewed before the next began: a story bank and cover notes, study plans, a legitimacy screen that flags ghost jobs and scams, interview prep, then a pipeline that holds the state of every application, follow-up timing, stage-by-stage guidance, offer handling, and finally, at 1.0, network matching that surfaces who you already know at a company you are about to apply to.

Every version's reasoning is written down rather than assumed. `ROADMAP.md` records what each release would deliver and why, `CHANGELOG.md` records what actually shipped, and decisions that were settled are marked so they do not get relitigated. If you want to see how a feature came to exist, the history is there to be read.

## The ethics are rules, not a disclaimer

The constraints in `ETHICS.md` are not marketing copy, and they are not there to cover anyone. They are rules the tool follows, and the build was not allowed to break them. A human applies, the tool never does. It respects every site's terms and does not scrape behind logins. It never fabricates, and it obeys the user's own honesty guardrails even when overstating would make the application look stronger. Fit is shown as justified sub-scores with a named gap, never a bare number passed off as objective. Thin days are reported as thin, not padded with manufactured matches.

Those rules are restated, in concrete terms, at every point in the instructions where a feature could otherwise drift. The follow-up nudge has a hard cap and an off switch. The offer helper will not invent a competing offer, or any other advantage you do not actually have. The network match only runs for a company you are actually applying to, from contacts you export yourself, never scraped. The honesty is not a promise on the label. It is enforced in the instructions.

## Built as Claude skills

Kochab ships as a set of Claude skills: folders of Markdown that tell the model how to run each part of the search, plus one small Python script that renders a resume to PDF. There is no server and no account. The tool reads and writes only inside a folder you point it at, so your profile, tracker, and contacts stay on your machine.

## Built with Claude, requirements first

Kochab was built collaboratively with Claude, working through Claude Code and the Cowork desktop tool. The collaboration was requirements-driven, not hands-off. The direction, the constraints, and the decisions came first and stayed with a human. Each version started from a stated requirement and a defined scope. The rules in `ETHICS.md` were set as hard boundaries the build was not allowed to cross. Every version was reviewed before the next began, and choices that were settled were written down as decisions so they held.

Claude did much of the drafting and the mechanical work. The requirements, the judgment calls, and the sign-off on each step were the author's. The incremental method above is what that looks like in practice: specify, build, review, record, repeat. That discipline is what let a fast collaboration stay honest and clear, and it is the same discipline that makes the tool trustworthy to use.

## Proving it was not just built for one person

A tool shaped by its author's own job search can end up hard-coding that person's assumptions without anyone noticing. To check, Kochab is tested against a fully synthetic persona who is nothing like the author: a different field, a different level, a different city, different constraints. The whole search runs against that persona, from the first scan through the offer, to confirm nothing is secretly wired to one case. That test data is entirely invented, and the repository ships no personal data at all.

## What it is not

Kochab is not a spam cannon, and it is not trying to become one. It will tell you a role is a Skip, tell you when you do not clear a screen, and tell you when a day turned up nothing. It is a sharp assistant to a person who is still doing their own thinking. That is the whole design.

If that is the kind of tool you want to use or help build, the [README](../README.md) has setup, `ETHICS.md` has the hard wall, and `CONTRIBUTING.md` has the way in.
