# How Kochab Was Built

Kochab is a job-search assistant with a single stubborn opinion: an honest "no" is worth more than a flattering "yes." Most automated job tools optimize for volume. They scrape everything, score each listing with a confident number, and fill the form for you. That produces spam for employers, terms-of-service violations for the user, and resumes that slowly stop being true. Kochab is built on the opposite bet. This is the story of how it got made, because the method is part of the point.

## One version at a time

Kochab was built in small, reviewable steps, not one big push. Version 0.1 was just the honest scoring and the packaging. Each version after that added one theme and was reviewed before the next began: the story bank and cover notes, study plans, a legitimacy screen, interview prep, then the pipeline that tracks every application, follow-up timing, stage guidance, offer handling, and finally bounded network matching at 1.0.

Every version's reasoning is written down rather than assumed. `ROADMAP.md` records what each release would deliver and why, `CHANGELOG.md` records what actually shipped, and decisions that were settled are marked so they do not get relitigated. If you want to see how a feature came to exist, the history is legible on purpose.

## Ethics as the architecture, not the disclaimer

The constraints in `ETHICS.md` are not a footer. They are the load-bearing walls. A human applies, the tool never does. It respects every site's terms and does not scrape behind logins. It never fabricates, and it obeys the user's own honesty guardrails even when overstating would score better. Fit is shown as justified sub-scores with a named gap, never a bare number dressed up as objective truth. Thin days are reported honestly rather than padded with manufactured matches.

Those rules are restated, in operational language, at every point in the code where a feature could drift. The follow-up nudge has a hard cap and an off switch. The offer helper refuses to invent leverage. The network match only runs for a company you are actually applying to, from contacts you export yourself, never scraped. The honesty is not a promise on the label. It is enforced in the instructions.

## Built as Claude skills

Kochab ships as a set of Claude skills: folders of Markdown that tell the model how to run each part of the search, plus one small Python script that renders a resume to PDF. There is no server and no account. The tool reads and writes only inside a folder you point it at, so your profile, tracker, and contacts stay on your machine.

## Built with Claude, requirements first

Kochab was built collaboratively with Claude, working through Claude Code and the Cowork desktop tool. The collaboration was requirements-driven, not hands-off. The direction, the constraints, and the decisions came first and stayed with a human. Each version started from a stated requirement and a defined scope. The rules in `ETHICS.md` were set as hard boundaries the build was not allowed to cross. Every version was reviewed before the next began, and choices that were settled were written down as decisions so they held.

Claude did much of the drafting and the mechanical work. The requirements, the judgment calls, and the sign-off on each step were the author's. The incremental method above is what that looks like in practice: specify, build, review, record, repeat. That discipline is what let a fast collaboration stay honest and legible, and it is the same discipline that makes the tool trustworthy to use.

## Proving it was not just built for one person

A tool shaped by its author's own job search can quietly hard-code that person's assumptions. To check, Kochab is tested against a fully synthetic persona who is nothing like the author: a different field, a different level, a different city, different constraints. The whole loop runs against that fixture, from the first scan through the offer, to confirm nothing is secretly wired to one case. The test data in `fixtures/` is entirely invented, and the repository ships no personal data at all.

## What it is not

Kochab is not a spam cannon, and it is not trying to become one. It will tell you a role is a Skip, tell you when you do not clear a screen, and tell you when a day turned up nothing. It is a sharp assistant to a person who is still doing their own thinking. That is the whole design.

If that is the kind of tool you want to use or help build, the [README](../README.md) has setup, `ETHICS.md` has the hard wall, and `CONTRIBUTING.md` has the way in.
