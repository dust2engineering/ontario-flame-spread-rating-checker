# Ontario Flame-Spread Rating Checker (OBC 3.1.13)

Maximum flame-spread ratings (and, in high buildings, smoke developed classifications) for interior finishes under OBC 2024 Subsection 3.1.13: Table 3.1.13.2 for walls and ceilings, Article 3.1.13.6 for corridors, and Table 3.1.13.7 for high buildings — plus the relief rules (doors, the 10% allowance, light diffusers) that decide real specifications.

**Live web tool:** https://dust2engineering.github.io/ontario-flame-spread-rating-checker/web/

## How it works

- Pick the location or element and the sprinkler status; the checker returns the governing maximum from the correct table — they are not interchangeable.
- Exits, 3.4.4.2.(2) lobbies, covered vehicular passageways and vertical service spaces are capped at FSR 25 whether or not the building is sprinklered.
- Corridors have their own article (3.1.13.6): unsprinklered walls 75 (or 25 upper / 150 lower), ceilings 25; sprinklered, both rise to 150.
- In high buildings, Table 3.1.13.7 adds smoke developed classifications — but Sentence (2) waives the table for sprinklered buildings, except Group B and elevator cars.

## Data in this repository

- `flame-spread-data.json` — Table 3.1.13.2, the corridor article values, Table 3.1.13.7 and all related relief rules as machine-readable JSON.
- Values verified from the full text of Subsection 3.1.13 (harmonized NBC-lineage text Ontario adopts); table structure and row list confirmed identical in OBC 2024 sources, and the exit FSR 25 value cross-checked in an Ontario consultant report.

## Command line

```bash
python3 flame_spread_checker.py --location corridor-wall --sprinklered no
```

## Worked examples

- [example-exit-and-corridor.txt](examples/example-exit-and-corridor.txt)
- [example-high-building.txt](examples/example-high-building.txt)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Fire and life safety. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
