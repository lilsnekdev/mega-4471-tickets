# Parser reads dates month-first for day-first tenants — 379 reports from #4471

**Covers 379 reports** merged into #4471 (the desk's view, as exported) (of 412 unique; the export's 427 rows contain 15 duplicate ids).

## Problem

The shared date parser reads every date **month first**. Every tenant whose locale writes the day
first gets month and day flipped, on every channel (app, email, form). Example report:

> Our 7 April reminder went out on 4 July. Is this a joke. It is not April Fools where we are.

## Evidence

- 379 unique reports, 11 tenants, first seen 2026-04-01, last seen 2026-10-04.
- All 11 tenants are day-first locales (en-GB, nl-NL, cs-CZ, it-IT, fr-FR, pl-PT, es-ES, de-DE, da-DK, en-IE — per `src/lib/kb/locales.ts`).
- Channels: app 204, email 150, form 25 — every channel, so it is the shared parser, not one form.
- Report ids: `analysis/report-ids-by-problem.json` → `parser` (this repo).

Per the desk's own counting (`src/lib/kb/causes.ts`, `desk-notes.json`), the 5 reports the desk
reads as a **one-day move** are counted here, filed under parser by tenant — they are footnoted
under this ticket and get their own ticket for the fix (see the one-day-move issue).

## Not covered by this ticket

- 33 reports that are the booking-v3 **form hint** bug — separate issue.

This is the problem the desk knows and the queued fix covers — but only this one.
