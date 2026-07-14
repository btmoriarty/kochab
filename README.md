# Kochab

*A personalized job search assistant.*

An honest, human-in-the-loop job search that runs inside Claude. It finds roles that actually fit, tells you the truth about the ones that do not, tailors your materials without inventing anything, and leaves every send in your hands.

Built as a set of Claude skills. No auto-apply, no scraping behind logins, no fake confidence scores. See [ETHICS.md](ETHICS.md) for why that matters and what this project will not do.

> **The name.** Before Polaris, there was Kochab — the star sailors and caravans steered by for roughly two thousand years, the one they trusted to find their way when they were lost. That is the job.

## Why this exists

The popular automated job tools optimize for volume: apply to a thousand jobs in two days, score every listing 0-100, let a bot fill the form. Hiring managers can smell it, the user's name ends up on spam, and the resume slowly stops being true.

This suite makes the opposite bet. It is a decision aid for one person running a real search. Its one durable advantage over the mass-apply crowd is that **it is willing to tell you a role is a Skip, that you do not clear a screen, and that today there is nothing new.** That honesty is the product.

## What's inside

### `skills/kochab`
Set up a personalized, recurring job scan from your resume, and everything downstream of it. First run interviews you, writes a canonical profile including your honesty guardrails, seeds a story bank, researches a target-employer list for your field, and asks how hands-on you want it. Then it works across the whole search:

- **Scan** — reads your tracker so it never repeats a role, discovers new employers, screens each posting for legitimacy (real employer, live req, not a ghost job or scam), and rates each new role with a transparent fit score plus a named gap and a why-you-fit line.
- **Draft** — anti-boilerplate cover notes and application emails that never restate the job description, built from a researched hook and your story bank.
- **Plan** — a study plan when a recurring, closable gap keeps blocking roles you want, paced to your real weekly hours.
- **Interview** — prep grounded in your profile, story bank, and the specific posting, across formats from recruiter screen to panel to onsite.
- **Pipeline** — one tracker holding the state of every parallel application, its next action, how their timing collides, and your capacity.
- **Momentum** — follow-up timing that never pesters, nudges to get drafted applications sent, post-call capture, and a one-step way to pass on a role.
- **Stage guidance** — what each stage of the process expects and what comes next, plus how to handle references well.
- **Offer** — the whole offer weighed against your priorities and floor, and an honestly-anchored counter drafted for you to send.
- **Process health** — honest rejection recovery, a clean withdrawal note, and a light read of your own funnel with no false precision.
- **Network** — from your own contacts (exported or pasted, never scraped), who you already know at an employer you are about to apply to.
- Plus tailored **resume** variants built by subtraction from your profile, and an adjustable **coaching dial** that sets how hands-on the tool is, light by default.

All of it drafts; you send. Nothing auto-applies.

### `skills/opportunity-brief`
Point it at a company, a posting, or a recruiter message and get a grounded brief: what the organization actually is, whether it is credible and stable, what the role really asks, where your honest gaps are, and the decisions that are yours to make. Built for the moment a recruiter reaches out or a friend mentions a job.

### `skills/roadmap-interview` (for maintainers)
Run a short, non-leading product-discovery interview with a user and turn it into structured roadmap input. Requests that recur across many interviews rise to the top of a shared feature backlog. This is how the tool's own roadmap stays driven by real needs rather than guesses.

## Install

A skill is a folder with a `SKILL.md` at its root; the agent reads the description and loads it when it's relevant. Two ways to install, depending on where you run Claude.

**Claude Code.** Skills live in `~/.claude/skills/<name>/SKILL.md` (personal, available in every project) or `.claude/skills/<name>/` (scoped to one repo). Clone this repo and link or copy the skill folders in:

```bash
git clone https://github.com/btmoriarty/kochab.git
cd kochab

# personal install, all projects (symlink so `git pull` keeps them current):
ln -s "$PWD/skills/kochab"          ~/.claude/skills/kochab
ln -s "$PWD/skills/opportunity-brief" ~/.claude/skills/opportunity-brief
# or copy instead of symlink:  cp -r skills/* ~/.claude/skills/
```

The `SKILL.md` must sit directly at `<name>/SKILL.md`, not nested a level deeper. No manual "enable" step; skills trigger from their description. Confirm with `/skills` in a Claude Code session.

**Cowork (Claude desktop).** Each skill is also packaged as a `.skill` file at the repo root (`kochab.skill`, `opportunity-brief.skill`, `roadmap-interview.skill`). Open one and choose **Save skill**, or re-zip a `skills/<name>/` folder with a `.skill` extension and do the same. It appears under Settings → Capabilities.

## Quick start

1. **Install** a skill (above).
2. **Make a folder** for your search and connect it. Your data lives there, not in this repo.
3. **Say "set up my job scan"** and hand over your resume — or **"look into this company"** with a posting.
4. **Schedule it.** Setup ends by handing you a filled-in scheduled-task prompt to paste; run it daily.

New here? Read [docs/Getting_Started.md](docs/Getting_Started.md) for orientation, then the worked walkthrough (a full session with example outputs) as a styled page ([WALKTHROUGH.html](docs/WALKTHROUGH.html)), a [PDF](docs/WALKTHROUGH.pdf), or [Markdown](docs/WALKTHROUGH.md). A one-page [cheat sheet](docs/CHEATSHEET.pdf) lists every mode and how to trigger it, and a slide overview is in [docs/Kochab_Deck.pptx](docs/Kochab_Deck.pptx).

## Design principles

- **Honesty over encouragement.** An accurate "Skip" beats a flattering "Strong."
- **Reorganize the truth, never invent it.** Resumes are tailored by subtraction.
- **A number may rank; it may never be the verdict.** Fit is shown as justified sub-scores with a named gap, not a lab-coat percentage.
- **A human applies. The tool never does.**
- **Thin days are reported honestly.** Most days there is nothing new, and the tool says so.

## Status and roadmap

**Feature-complete through v1.0.** The whole search is in, from discovery to offer to network: scan and scoring, story bank and cover notes, study plans, legitimacy screen, interview prep across formats, the application pipeline, follow-up momentum, stage guidance, offer negotiation, process health, and bounded network matching, with an adjustable coaching dial over all of it. See [ROADMAP.md](ROADMAP.md) for the version-by-version scope and [CHANGELOG.md](CHANGELOG.md) for what shipped when.

Built one version at a time; each version's rationale is recorded rather than assumed.

## License

[MIT](LICENSE). Fork it, run your own search, own your data end to end.
