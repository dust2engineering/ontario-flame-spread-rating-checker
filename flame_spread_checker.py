#!/usr/bin/env python3
"""Ontario flame-spread rating checker (OBC 2024, Subsection 3.1.13).
Usage:
  python3 flame_spread_checker.py --location exit
  python3 flame_spread_checker.py --location corridor-wall --sprinklered no
  python3 flame_spread_checker.py --location high-exit-stair
Locations: a1, group-b, exit, lobby, vehicular-passageway, vertical-service, other,
           corridor-wall, corridor-ceiling, high-exit-stair, high-corridor,
           high-elevator-car, high-elevator-vestibule, high-service, high-other
"""
import argparse, json, os
D = json.load(open(os.path.join(os.path.dirname(__file__), "flame-spread-data.json")))
BASE = {r["location"]: r for r in D["table_3_1_13_2_wall_ceiling_finishes"]}
KEYS = {"a1": 0, "group-b": 1, "exit": 2, "lobby": 3, "vehicular-passageway": 4, "vertical-service": 5, "other": 6}
HIGH = {r["location"]: r for r in D["high_building_table_3_1_13_7"]}
HKEYS = {"high-exit-stair": 0, "high-corridor": 1, "high-elevator-car": 2, "high-elevator-vestibule": 3, "high-service": 4, "high-other": 5}
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--location", required=True)
    ap.add_argument("--sprinklered", choices=["yes", "no"], default="no")
    a = ap.parse_args()
    loc = a.location
    if loc in ("corridor-wall", "corridor-ceiling"):
        el = "wall" if loc.endswith("wall") else "ceiling"
        v = D["corridor_article_3_1_13_6"][el]["sprinklered" if a.sprinklered == "yes" else "not_sprinklered"]
        print(f"Corridor {el} finish (3.1.13.6), {'sprinklered' if a.sprinklered == 'yes' else 'not sprinklered'}: maximum flame-spread rating {v}")
        return
    if loc in HKEYS:
        r = D["high_building_table_3_1_13_7"][HKEYS[loc]]
        print(f"High building (Table 3.1.13.7) - {r['location']}: FSR wall/ceiling/floor = {r['fsr_wall_ceiling_floor']}; SDC wall/ceiling/floor = {r['sdc_wall_ceiling_floor']}")
        print("Note: except for Group B buildings and elevator cars, this table need not be met if the building is sprinklered (3.1.13.7.(2)).")
        return
    r = D["table_3_1_13_2_wall_ceiling_finishes"][KEYS[loc]]
    v = r["max_fsr_sprinklered"] if a.sprinklered == "yes" else r["max_fsr_not_sprinklered"]
    print(f"{r['location']}: maximum flame-spread rating {v} ({'sprinklered' if a.sprinklered == 'yes' else 'not sprinklered'}, Table 3.1.13.2)")
if __name__ == "__main__":
    main()
