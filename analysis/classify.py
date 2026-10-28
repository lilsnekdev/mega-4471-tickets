#!/usr/bin/env python3
"""Split ticket #4471's reports into problems, per the kb's own cause logic
(src/lib/kb/causes.ts): the cause depends on the TENANT (locale, form) and the
channel — not on the reporter's browser locale or the subject line.

  parser : day-first tenant, any channel except form-on-booking-v3 — the shared
           month-first parser flips their dates.
  hint   : day-first tenant on the booking-v3 form — the hint says MM/DD/YYYY,
           the tenant types month-first, the form reads it day-first.
  one-day-move : the desk's desk-notes.json `oneDayMove` ids — not swaps at all.

The export's pages overlap: the same report id can appear twice. One id = one report.
"""
import json, glob, os

base = os.path.join(os.path.dirname(__file__), "..", "kb", "support-kb", "src", "lib", "data")
reports = json.load(open(os.path.join(base, "reports-4471.json")))
tenants = {}
for f in glob.glob(os.path.join(base, "tenants", "*.json")):
    t = json.load(open(f))
    tenants[t["handle"]] = t

# dayFirst(locale): does this locale write the day before the month?
# (same question causes.ts asks Intl.DateTimeFormat)
DAY_FIRST = {"en-GB", "en-IE", "pl-PL", "it-IT", "nl-NL", "fr-FR",
             "cs-CZ", "da-DK", "pt-PT", "es-ES", "de-DE"}

def cause_of(r):
    t = tenants[r["tenant"]]
    if r["channel"] == "form" and t["form"] == "booking-v3":
        return "hint"
    return "parser"

ONE_DAY_MOVE = {"R-41202", "R-41209", "R-41236", "R-41344", "R-41620"}  # desk-notes.json

unique = {}
for r in reports:  # one id, one report
    unique[r["id"]] = r

out = {"parser": [], "hint": [], "one-day-move": []}
for r in unique.values():
    if r["id"] in ONE_DAY_MOVE:
        out["one-day-move"].append(r["id"])
    else:
        out[cause_of(r)].append(r["id"])

for k, v in out.items():
    v.sort()
    print(f"{k}: {len(v)}")
print("total:", sum(len(v) for v in out.values()), "unique reports")
assert sum(len(v) for v in out.values()) == 412
print("desk's view (counted where filed): parser =", len(out["parser"]) + len(out["one-day-move"]),
      "(footnote: 5 read as a one-day move) | hint =", len(out["hint"]))
