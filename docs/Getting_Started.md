# Getting Started

This is a job scan that runs itself. Once it is set up, it looks for roles on a schedule, tells you honestly whether any are worth your time, and drafts the materials for the ones that are.

Setup takes about twenty minutes, most of it you talking. You do it once.

---

## What you need

- Your resume, in any format.
- A folder on your computer where the job search will live. It can be empty. **This is where your data stays. Nothing personal is ever sent to the repository or anywhere else.**
- The `kochab` skill installed.

## Step 1: Install the skill

A skill is just a folder with a `SKILL.md` at its root. Install it wherever you run Claude:

- **Cowork (desktop):** open the `kochab.skill` file from the repo and choose **Save skill**. It shows up under Settings → Capabilities. Done.
- **Claude Code:** clone the repo, then link the skill into your skills directory so Claude Code discovers it:

  ```bash
  git clone <repo-url> kochab
  ln -s "$PWD/kochab/skills/kochab" ~/.claude/skills/kochab
  ```

  `~/.claude/skills/` makes it available in every project; a project's own `.claude/skills/` scopes it to that repo. The `SKILL.md` has to sit directly at `kochab/SKILL.md`. Check it loaded with `/skills`.

There's no "enable" toggle and nothing to configure. The skill triggers when you describe a job-search task. The companion skills (`opportunity-brief`, `roadmap-interview`) install the same way.

## Step 2: Point Claude at your folder and say the words

Connect the folder you made and say:

> set up my job scan

Then give it your resume when it asks. The exact phrase matters less than the intent, but "set up my job scan" reliably starts the setup.

## Step 3: The interview

This is the part that matters, and the part it is tempting to rush.

It reads your resume back to you and asks about the parts that look compressed or inflated. Then it asks what you actually want next, what you are trying to get away from, how far you would really commute, your compensation floor, and one question that decides how everything gets ranked afterward: **when compensation and mission conflict, which one wins?**

Answer that one honestly. Every recommendation depends on it.

It also asks how hands-on you want the tool to be, from just holding things until you ask, to actively coaching you along. Light is the default, and you can change it any time by saying so ("be more hands-on," "dial the coaching back").

### The honesty questions

Near the end it asks something unusual:

> For each thing on your resume that sounds more impressive than it was, tell me the honest version.

It follows up. Where were you the owner, and where were you next to the owner? Which tool do people assume you built that you actually used? Which title overstates the scope?

This is not a trap and it is not false modesty. Your answers become hard rules that every future draft obeys. If you say you were adjacent to a system rather than the person who built it, the tool will never write a line that implies otherwise, no matter how much a posting would reward the overclaim. That is what makes the output safe to send: it will not put a sentence in your mouth that you would have to walk back in an interview.

Five uncomfortable minutes buys you the ability to trust everything it writes.

## Step 4: Let it build your target list

It researches the organizations that hire people like you, in your field and your geography, and writes them into a file. This is a starting point, not a fence. Every run it looks for employers not on the list and adds the ones it finds.

## Step 5: Schedule it

Setup ends by handing you a block of text: your scan prompt, with your folder path and your search already filled in. You do not run it by hand every day. You hand it to a schedule once.

**In Cowork (desktop):** start a new message, paste that block in, and add a line like *run this every weekday morning at 8am.* Claude creates the recurring task and lists it under your scheduled tasks, where you can pause, edit, or delete it later. Make sure your search folder is connected so each run can read your profile and update your tracker.

**In Claude Code:** there is no built-in scheduler, so run that same prompt from your own (cron on macOS or Linux, Task Scheduler on Windows), or just paste it in whenever you want a fresh scan.

Daily is the right cadence. A scan that honestly says "nothing new" most mornings is doing its job; a weekly one misses roles that close in five days. **Do not schedule it before setup finishes** — a scan with no profile has nothing to compare roles against.

---

## What you will get

Most mornings, a short note that says some version of *nothing new today, here is what I checked.*

**That is the tool working correctly.** Real matches are rare. A scan that finds three exciting roles every day is one you stop reading by week two, and then the real one shows up and you skim past it. This one is built to be boring most days so it is worth reading on the day it is not.

When something real turns up, you get:

- An honest rating: **Strong**, **Stretch**, or **Skip**, with a fit score shown as six justified sub-scores and a total, and the actual gap named. Not "may require additional experience." Something like: *the posting asks for five years running a regulated compliance program; you have three in an adjacent function; open with the audit work and expect to be tested on it in the screen.*
- A tailored resume for the top matches, built from your profile by cutting, never by inventing.
- A short "why this organization" paragraph in your voice.
- A note on any screen you might not clear, so you decide rather than find out from a rejection.

## The part people find most useful

For every Strong or Stretch role you also get:

**Emphasize** — what to lead with for this posting, and what to cut. Tailoring is mostly subtraction.

**Build** — what you would need to learn or earn to close the gap, sorted into a quarter, a year, and not-soon, with honest time estimates and a warning when a certification is oversold.

**The recurring gap** — if the same requirement blocks several roles you want and you do not have it, the scan tells you so without being asked. That sentence is usually worth more than any single application.

---

## Once you start applying

The scan is the front door; the tool follows the whole search from there. You do not set any of this up separately. You tell it what happened, and it keeps the state:

- **When you apply** ("I applied to X"), it holds your whole pipeline: every application's stage, the next action for each, how their timing collides, and your capacity. Ask "where does my search stand" any time.
- **Momentum.** It suggests when to follow up without pestering, helps get a drafted application actually sent, and captures the next step right after a call. How much it nudges follows your coaching dial.
- **Stage guidance and interview prep.** What each stage expects and what comes next, prep for a recruiter screen through a panel or onsite, and how to line up references.
- **Offers.** When you get one, it weighs the whole package against your priorities and floor and drafts a counter for you to send. It never negotiates for you.
- **Rejections and process health.** An honest way to metabolize a no and keep moving, a clean way to withdraw from a process, and a light read of where your own search stalls.
- **Your network.** From contacts you export or paste (never scraped), who you already know at a company you are about to apply to.

All of it drafts; you send. The one-page [cheat sheet](CHEATSHEET.pdf) lists the phrase that triggers each.

---

## If something feels off

Tell it. The profile is a file, not a contract. If it writes something that does not sound like you, say so and it updates the voice rules. If it keeps surfacing roles you would never take, say what you dislike and it adds a hard no. If it rates something Strong and you disagree, push back; it is calibrated to be blunt, not to be right.
