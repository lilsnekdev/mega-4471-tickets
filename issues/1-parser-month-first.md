# Parser reads dates month-first for day-first tenants — 374 reports from #4471

**Covers 374 reports** merged into #4471 (of 412 unique; the export's 427 rows contain 15 duplicate ids).

## Problem

The shared date parser reads every date **month first**. Every tenant whose locale writes the day
first gets month and day flipped, on every channel (app, email, form). Example report:

> Our 7 April reminder went out on 4 July. Is this a joke. It is not April Fools where we are.

## Evidence

- 374 unique reports, 11 tenants, first seen 2026-04-01, last seen 2026-10-04.
- All 11 tenants are day-first locales (en-GB, nl-NL, cs-CZ, it-IT, fr-FR, pl-PT, es-ES, de-DE, da-DK, en-IE — per `src/lib/kb/locales.ts`).
- Channels: app 204, email 150, form 25 — every channel, so it is the shared parser, not one form.
- Report ids: `analysis/report-ids-by-problem.json` → `parser` (this repo).

## Not covered by this ticket

- 33 reports that are the booking-v3 **form hint** bug — separate issue.
- 5 reports that are **one-day moves**, not swaps — separate issue.

This is the problem the desk knows and the queued fix covers — but only this one.
