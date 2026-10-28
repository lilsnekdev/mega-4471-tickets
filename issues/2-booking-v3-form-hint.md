# booking-v3 form hint says MM/DD/YYYY but the form reads day-first — 33 reports from #4471

**Covers 33 reports** merged into #4471.

## Problem

On the **booking-v3** form, the hint under the date field says `MM/DD/YYYY`, so the tenant's people
type the month first — and the form then reads it **the tenant's day-first way**. Month and day come
out flipped. This is a different bug from the shared parser: the parser did nothing wrong here; the
**hint contradicts the form's own reading order**.

Per `src/lib/kb/causes.ts`: `hint` — "Through booking-v3's form the tenant's people type what the
hint tells them, month first, and the form reads it the tenant's way: that is `hint`, a different bug."

## Evidence

- 33 unique reports, all channel `form`, all booking-v3 tenants:
  **alder.physio** (12), **copper.studio** (11), **pale.harbour** (10).
- First seen 2026-04-17, last seen 2026-09-22.
- Intake tagged 15 of them `parser` and 18 `hint` — the browser-locale guess disagrees with the
  real cause; the tenant's locale + form decides it.
- These reports share subject lines with the parser reports, so decision 0001
  (merge on subject alone) folded them into #4471.
- Report ids: `analysis/report-ids-by-problem.json` → `hint` (this repo).

## Fix direction

booking-v3's date hint must match the reading order the form actually applies (day-first for these
tenants), or the form must parse what the hint says. Either way, it is not the shared parser's fix.
