# #4471 split into three tickets

Challenge S01E03 · *what it shows* — MEGA.dev. This repo holds the split of support-desk ticket
**#4471** (412 reports about dates, marked known as one issue) into three problems, each with its
own GitHub issue and report count.

## The three problems (and their issues)

| Problem | Reports | Issue |
|---|---|---|
| Parser reads dates month-first for day-first tenants | 379 (incl. the 5 one-day moves, footnoted) | [the parser issue](../../issues/1) |
| booking-v3 form hint says MM/DD/YYYY but the form reads day-first | 33 | [the form-hint issue](../../issues/2) |
| One-day move (suspected timezone handling) | 5 | [the one-day-move issue](../../issues/3) |

374 + 33 + 5 = 412 unique reports. The export carries 427 rows; 15 are duplicated report ids.

## What is in here

- `4471-page.svx` — the kb page, signed (frontmatter `signature` + `<RenderStamp {signature} />`, desk ref DR-V441-29GA). It is the kb's page for the incident, at `support-kb/src/routes/kb/incidents/4471/+page.svx` (the desk's old one-issue page it replaces, kept in git history).
- `4471-page.md` (and `4471-page.html`) — that page rendered, for the desk to read without running the kb.
- `issues/*.md` — the three tickets, as filed.
- `support-kb/` — the desk's kb export, in its exported layout (root folder `support-kb/`), with the
  incident page replaced by our signed page at `support-kb/src/routes/kb/incidents/4471/+page.svx`,
  signed per kb conventions (`frontmatter signature` + `<RenderStamp {signature} />`, desk ref DR-V441-29GA).
- `analysis/report-ids-by-problem.json` — every report id, per problem, so each count can be checked.
- `analysis/classify.py` — the classification script (tenant locale + channel + form, per `support-kb/src/lib/kb/causes.ts` logic).

## How the split was decided

The kb's own logic (`support-kb/src/lib/kb/causes.ts`) says the cause depends on the **tenant** (locale, booking
form), not on the reporter's browser or the subject line. Following it: a day-first tenant hit by the
shared month-first parser is the `parser` cause; the same tenant typing what the booking-v3 hint
(`MM/DD/YYYY`) tells them, on the form channel, is the `hint` cause — a different bug. The desk's
`desk-notes.json` (`oneDayMove`) names five reports that are not swaps at all; they get the third ticket.

Decision 0001 (merge on subject line alone) is what folded all of this into one ticket; intake's
`intakeTag` (a browser-locale guess) disagrees with the real cause on 38 of the 412 reports.
