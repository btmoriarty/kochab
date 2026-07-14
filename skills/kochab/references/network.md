# Network, Bounded

A warm introduction beats a cold application, and the person applying often already knows someone who could help, but cannot hold the overlap between hundreds of contacts and dozens of employers in their head. This closes the loop from discovery to offer: when she is genuinely going to apply somewhere, surface whether she already knows someone there, and help her reach out well.

It is the capstone, and it carries the most sensitive data in the whole tool. The constraints below are not optional polish; they are the reason this feature is allowed to exist at all. Build and run it exactly this way.

## The hard rules (ETHICS principles 2 and 5)

- **Contacts come from her own data, never a scrape.** The only two sources are her own LinkedIn data export (LinkedIn, Settings, Get a copy of your data, Connections, which produces a `Connections.csv`) or contacts she pastes in. The tool never scrapes LinkedIn, never reads connections behind a login, and never automates the export. If she asks it to pull her network directly, explain that it cannot and will not, and point her to the export.
- **It stays in her folder.** The export is parsed locally into `Contacts.md` in her working folder and stays there. It is personal data: never committed to any repo (the `.gitignore` excludes it), never transmitted anywhere beyond the model calls she herself initiates, and owned by her end to end.
- **Intent-gated, never a blanket scan.** Matching runs only for a specific employer she has signaled she wants to apply to. It never runs across all open roles, and the daily scan never touches the contact list. No "here is everyone you know at every company that is hiring." The gate is her stated intent to apply, one employer at a time.
- **Honest, never manufactured.** A match is a real overlap between a real contact and the employer, or it is nothing. The tool never invents a connection, never inflates a loose tie into a strong one, and never suggests she imply a closer relationship than she has.

## Intake

Optional, and available any time, not required at setup. When she wants to bring her network in:

- **From the export.** She downloads `Connections.csv` from LinkedIn and drops it in her folder. Parse it locally. The columns are First Name, Last Name, URL, Email Address, Company, Position, Connected On. Build `Contacts.md`: Name, Current employer, Title, How she knows them (if known), Last contact, Notes. Do not fabricate the relationship strength; leave it blank until she says.
- **From a paste.** She pastes a few names and where they work. Same ledger.
- Tell her plainly, once, where the file lives and that it stays local. It is her data.

`Contacts.md` grows and is corrected over time the way the other ledgers do. Never delete a row silently; mark it stale.

## Matching: you know someone here

When she signals intent to apply to a specific employer ("I'm applying to X," or she is drafting for a specific role she is pursuing), and only then:

- Match that employer against the Current-employer field in `Contacts.md`, including obvious variants (the same company under a slightly different name).
- Surface the real overlaps: who she knows there, their title, and how she knows them if recorded. If there is no one, say so plainly; a manufactured "maybe you know someone" helps no one.
- Keep it to the employer at hand. Do not volunteer matches for other companies she did not ask about.

## How and when to engage

People freeze on outreach. The help is in the timing and the framing, not in doing it for her.

- **When.** When she is genuinely pursuing the role, not as a blanket networking campaign. A note tied to a real, current intent reads as sincere; a mass reconnect does not.
- **Framing.** Ask for insight or a conversation, not a job. "I'm looking at a role on your team and wanted your read on it" lands better than "can you refer me." Respect the contact's position; a referral is theirs to offer, not hers to demand.
- **Draft, do not send.** Offer to draft a short, warm outreach note in her voice, obeying the voice rules and honesty guardrails, honest about the relationship's real closeness. She reads it, edits it, and sends it herself. The tool never messages anyone. (ETHICS principle 1.)
- Log the outreach in `Contacts.md` (last contact) so she does not double-reach or lose track.

## The encouragement nudge (optional, honest, dial-governed)

Some people who are genuinely qualified skip roles anyway because they chronically feel under-qualified. For them, and only for them, naming a warm contact can lower the barrier enough to apply. This is the one place the tool leans in, and it is fenced hard.

- **Off by default.** It follows the intervention dial (`references/intervention_dial.md`): silent at the light default, available at standard or high, or when she opts in. It never fires at the light setting.
- **Only where she genuinely qualifies.** The nudge fires only on a role her own fit assessment rates Strong, or that clearly clears the real screens. Never on a Stretch, never on a role she does not qualify for. Lowering the barrier to a role she cannot do is a disservice, and it violates the honesty line; naming a contact to get her into a losing application is exactly the dark pattern this tool refuses.
- **A door, not a push.** It names the warm contact and notes she is genuinely qualified, then returns the decision to her. It does not badger, does not repeat, and does not guilt her for passing.

## What this does not do

- It never scrapes LinkedIn or reads any network behind a login. Export or paste only.
- It never runs a blanket match across all jobs; only for an employer she has signaled intent to apply to.
- It never messages a contact, requests a referral, or acts on the network on her behalf. It drafts; she sends.
- It never invents a connection or inflates a tie, and it never nudges her toward a role she does not qualify for.
- The contact data never leaves her folder and is never committed to the repo.
