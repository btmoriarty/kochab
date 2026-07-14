# Responsible Use

This project exists because most automated job-search tools are pointed the wrong way. They optimize for volume: scrape everything, score it with a confident number, auto-fill the form, submit at scale. That produces spam for employers, ToS violations for the user, and resumes that quietly drift from the truth.

This suite is built on the opposite bet. It is a decision aid for one person doing a real search, and it is designed to be something you would be comfortable having your name attached to. The rules below are not disclaimers. They are constraints the tools actually follow, and contributions that break them will not be merged.

## 1. A human applies. The tool never does.

The suite drafts. It does not submit. There is no auto-apply, no form-filling on the user's behalf, no bulk submission. Every application leaves the user's hands only after the user has read it and chosen to send it.

This is the single most important line in the project. It is why the tool cannot be turned into a spam cannon, and it is non-negotiable.

## 2. Respect the terms of service of every site.

- No scraping behind a login, no evading rate limits, no circumventing CAPTCHAs or bot detection.
- Prefer public postings, official job-board search, published APIs, and the oldest reliable method of all: the user pasting a job description in.
- When a career page cannot be read without violating its terms, the tool says so and asks the user to bring the posting to it. It does not find a workaround.
- Honor `robots.txt` and posted access rules.

A tool that has to break a website's rules to function is not a tool this project ships.

## 3. Never fabricate. Reorganize the truth; do not invent it.

- Resume variants are built by cutting and reordering real experience for a target. They never add a skill, a title, a date, or an accomplishment the person does not have.
- The setup interview captures explicit honesty guardrails ("say X, never say Y") for exactly the places a resume tends to overstate. Every draft obeys them, even when a posting would reward the overstatement.
- Fit assessments name the real gap. The tool is built to say "you do not clear this screen" rather than flatter the user into an application they will lose.

## 4. Scores rank. They do not pretend to measure.

The suite deliberately refuses the 0-100 and 1-10 scores that competing tools display, because those read as objective measurements when they are language-model judgments. Fit is shown as a small set of justified sub-scores with a named gap attached, so the user can see the reasoning and disagree with it. A number may order a list. It may never stand in for judgment.

## 5. The user's data stays the user's.

- This repository ships **no personal data**. Profiles, resumes, trackers, and application history live in the user's own folders and are never committed here.
- The tools read and write only within the folder the user points them at. They do not transmit personal data anywhere beyond the model calls the user themselves initiates.
- Anyone forking this to run their own search owns their data end to end.

## 6. No dark patterns toward the user, either.

- Study-plan and upskilling suggestions are offered only when a gap is real and recurring, never to sell a course or pad engagement. The tool is skeptical of certifications by default.
- The scan reports thin days honestly. It does not manufacture matches to look busy.
- Every recommendation ends by returning the decision to the user.

## 7. Know what this cannot do.

Language models make mistakes. A fit rating can be wrong, a "live" link can be stale, a company can look stable a week before it is not. Treat every output as a well-researched draft to check, not a verdict to act on blind. The tool is a sharp assistant to a person who is still doing their own thinking.

---

If you are considering a contribution that adds auto-submission, scraping that violates a site's terms, numeric fit scores presented as objective, or any form of resume fabrication, please do not. Those features are the reason this project exists as an alternative.
