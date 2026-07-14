# Scan Protocol

## The dedup rule, first

A role is a duplicate if the **same employer and same role family** already appear in `Application_Tracker.md`, in any of its three tables (Active, Watching, Closed), even when the posting ID, title wording, or location differs. "Program Manager, Safety" and "Technical Program Manager, Safety Systems" at the same company are the same family. Schema in `references/pipeline.md`.

When unsure, treat it as a duplicate. List it under "already tracked, skipped," so she can see the source was checked. Genuinely new finds are added to the **Watching** table; never pad it with roles already in the pipeline.

## Discovery, before the seed sweep

The target-employer list is a seed and a priority order. It is not the universe. The value of this tool is finding employers she has not named. Every run should try to surface at least one, unless the week is genuinely thin.

### 1. Role-first

Build queries from her target titles crossed with qualifiers and the current month and year.

Qualifiers worth rotating: `remote`, her metro, her state, her industry, seniority words (`senior`, `director`, `lead`, `principal`), and any word her field uses that outsiders do not.

Boards to name explicitly in searches or fetch directly: LinkedIn Jobs, Indeed, Glassdoor, Greenhouse (`job-boards.greenhouse.io`), Lever (`jobs.lever.co`), Ashby (`jobs.ashbyhq.com`), Workday, Built In (metro-specific), Welcome to the Jungle, and whatever vertical board exists for her field. Every field has one. Find it during setup and record it in `Target_Employers.md`.

### 2. Location-first

Run her titles against her metro, her state, and the neighboring metro, as literal searches. This is the single highest-yield channel for surfacing employers no list would have named, because it finds companies headquartered where she lives rather than where her industry is famous.

### 3. Aggregators and VC portfolio boards

Portfolio boards aggregate hundreds of companies at once: `jobs.accel.com`, `jobs.menlovc.com`, `jobs.bvp.com`, a16z, Greylock, Sequoia, Lightspeed, Index, Y Combinator's Work at a Startup. Filter to her titles.

### 4. Funding and news

Search funding rounds from the last one to three months in her sector. Newly funded organizations hire operations, program, and generalist staff early, and their boards are thin enough that a good applicant is visible.

Search for organizations founded in the current year in her field. They did not exist when the seed list was written.

### 5. Rotate

Note which channels you led with. Lead with different ones next run. Coverage broadens over time; a scan that runs the same four searches every day finds the same four things.

## Then sweep the seed list

Take a rotating subset of `Target_Employers.md`, not the whole thing. Prioritize by her stated lane order. If she has designated a single top employer, check it first every single run and surface its matches at the top.

## Scoring: rank honestly, never manufacture precision

Every new role gets a fit score built from six dimensions, each 0 to 3, with every point traceable to a stated reason. The score orders the list and shows its work. It does not replace the named gap, and it is never presented as a percentage or a bare number.

| # | Dimension | 0 | 1 | 2 | 3 |
|---|-----------|---|---|---|---|
| 1 | Core-skill match | Missing the central skill | Adjacent, would have to argue it | Clear match on most | Direct, demonstrable |
| 2 | Seniority / level fit | Two or more levels off | One level off | Right band, minor stretch | Squarely her level |
| 3 | Domain / industry fit | New domain, steep | Transferable with a story | Adjacent domain | Her domain |
| 4 | Location / logistics | Breaks a hard constraint | Workable with friction | Fine | Ideal / no relocation |
| 5 | Mission / values | Against her stated values | Neutral | Aligned | Strongly aligned |
| 6 | Screen-clearance | Fails a hard filter | Clears most, one real risk | Clears all real filters | Clears filters and preferred quals |

Read the weighting from `Master_Profile.md`, never hard-code it. If her profile ranks mission over compensation, dimension 5 breaks ties upward; if it ranks compensation first, carry that in a comp-band note instead.

**Roll-up to the existing bands** (out of 18):

- **Strong** = 14 to 18, and no zero on dimensions 1, 2, or 6. A zero on core-skill, level, or screen-clearance caps the role at Stretch no matter how high the total. A role she loves but cannot do is not a Strong.
- **Stretch** = 9 to 13, or higher with one capping zero.
- **Skip** = 8 or below, or anything that breaks a hard no.

The raw /18 orders roles **within** a band, so the ranked list is finer than three buckets. Ties break on dimension 1, then dimension 6.

**Presentation, per role.** Show the six sub-scores and the total together, always. Never the total alone, never a percentage, never a decimal.

> **Acme, Program Manager, Risk** — Stretch (11/18)
> skill 2 · level 3 · domain 1 · location 3 · mission 1 · screens 1
> **Gap:** domain is healthcare, which she has not worked; level and logistics are ideal, so this is a domain-story problem, not a qualification problem.
> **Toward Strong:** no course changes this. The gaps are healthcare domain, which is experience rather than a class, and mission fit, which is structural; neither is a skill to study, so there is no study lift to offer here.

Each sub-score carries a clause of justification, or it is not recorded. Do not store the total and trend it across runs as if it were measured data; recompute it from the profile each time.

## The directional line: what would move a role up

On every Stretch role, after the gap, add one line that names what would move it toward Strong, tied to the specific dimension holding it down. It points at the study machinery; it does not run it. A Skip that breaks a hard no gets no such line.

- **Only nominate a lift that is a concrete, studiable skill.** The line exists to name something she can go learn and get demonstrably good at in bounded time: a language or tool (a Python crash course, SQL, a named framework), a specific body of technical knowledge, or a real certification that shows up as an actual screen. "A focused Python course and one small shipped project" is a directional line. "Build ad-tech exposure" or "get more years at this level" is not, because those are experience, not study.
- **Sort the gap into one of three kinds, and handle each honestly.**
  - *A studiable skill or credential* → name it specifically and point at a plan.
  - *Experience or exposure* (domain seasoning, tenure, having owned something at scale) → say plainly it is an experience gap, not a course, so she does not chase a class that will not move it.
  - *A structural limiter she cannot change by effort* (a location that breaks a hard constraint, a level below or above her, a mission mismatch) → name it as the ceiling, never as homework.
- **Do the arithmetic, and claim only what it supports.** A role reaches Strong only at 14 or more with no zero on dimensions 1, 2, or 6. Raising one dimension from 1 to 3 adds two points; confirm that actually crosses 14 and clears any cap before saying it does. When one studiable lift crosses the line, say so plainly. When nothing studiable reaches Strong, say that instead and name why (experience, mission, or level), so the line never sends her to study something that will not change the rating.
- **A pointer, not a plan.** No curriculum, resources, or time estimates here; those live in the study plan (`study_plan.md`), on demand and in the weekly summary. The daily note still does not offer or generate a plan. Close by noting she can ask for a plan if the skill is worth building.
- **Honest about what the rating is.** The rating is this scan's ranking of fit, not a verdict from the employer. "Closing this clears the stated screen" is fair; "study this and you are in" is not.

A case where a studiable skill is the lift:

> **Meridian Labs, TPM, Model Evaluations** — Stretch (12/18)
> skill 1 · level 3 · domain 2 · location 3 · mission 2 · screens 1
> **Gap:** the role wants hands-on evaluation tooling and Python fluency she has used adjacent to but not owned.
> **Toward Strong:** core-skill (1 of 3) is the single lift, and it is studiable. A focused Python-for-evals course plus one small eval harness she ships would take it to a demonstrable 3, which crosses the total to 14 and moves this from Stretch to Strong. Ask for a plan and it will be paced to her hours.

The Acme example above is the other case: its gaps are domain experience and mission, so the honest line is that no course moves it. Name that rather than inventing a study target.

## Verification

Before sharing any posting link, confirm it is live. Career pages are frequently JavaScript-rendered and return an empty shell to a plain fetch. Confirm through a job-board mirror, a search result, or a rendering browser tool. If you cannot confirm, label it **UNVERIFIED** and say so. Do not guess.

Watch for reposts. A req that has been live for four months is telling you something.

Run the **legitimacy check** in `references/legitimacy_check.md` on each new posting as part of verification: is the employer real and operating, is the req live and recent, does the comp band make sense, is it a direct hire or a staffing-firm repost, are there scam signals. Attach a short caution to anything that is not a clean, live, direct role. A clear scam does not enter the ranked list; it goes in a short "screened out as likely not real" note so she sees it was checked. A legitimacy flag is a caution, not a verdict, except for clear scams.

## Honest reporting

Most days produce nothing new. This is the normal case, not a failure of the scan.

A scan note that says "no new matches today, here is what I checked" is a good scan note. A scan note that manufactures three Stretches to fill space trains her to stop reading. When the real match arrives, she has to be able to see it.

Report:

- Channels used, by name.
- Genuinely new roles, by lane, with ratings and real gaps.
- Already tracked and skipped, so she knows the source was covered.
- New employers appended to the ledger.
- The recurring gap, if one is emerging across runs.
