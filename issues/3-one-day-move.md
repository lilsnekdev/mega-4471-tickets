# One-day move (suspected timezone handling) — 5 reports from #4471

**Covers 5 reports** merged into #4471. The desk's own notes (`desk-notes.json`, `oneDayMove`)
already read these separately; they are filed here so they stop hiding under the parser.

## Problem

These reports are not month/day swaps at all. Dates move by **one day**, weekdays shift, and one
meeting shows on different days in different timezones — a smell of timezone or DST handling
around all-day dates or invite rendering.

The five reports:

- `R-41202` (kettle.books): invite said Tuesday 12 May, calendar showed Monday 11 May; client turned up on the Monday.
- `R-41209` (alder.physio): every booking in June one day off — only June.
- `R-41236` (nine.lanterns): the invite arrived before the booking was made.
- `R-41344` (pale.harbour): client in Lisbon got Tuesday, client in Toronto got Monday — same meeting, held twice.
- `R-41620` (lantern.row): Tuesday 6 October showed as Monday.

## Evidence

- Report ids: `analysis/report-ids-by-problem.json` → `one-day-move` (this repo).
- All five were mechanically classified `parser` by tenant, but their bodies describe one-day
  shifts, not flips — which is exactly why the desk notes them apart.

## Fix direction

Investigate timezone/DST handling in invite generation and all-day date rendering (the Lisbon vs
Toronto pair is the cleanest reproduction). The queued month-first fix will not touch these.
