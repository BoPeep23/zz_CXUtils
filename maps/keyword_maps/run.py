import json, os, sys
from collections import defaultdict, Counter, OrderedDict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify import *

R = json.load(open(os.path.join(SCR, "passives_raw.json"), encoding="utf-8"))
MANAGER = json.load(open(os.path.join(ZZ, "cx_passive_manager.json"), encoding="utf-8"))

# name -> data lookup across all sources (BASE wins for vanilla lookups, then mods)
LOOKUP = {}
for code in ["BASE", "DTHM", "INVX", "RAN", "DEGR", "ENCO", "EXEP", "FEAT", "SWTE", "UTUT"]:
    for e in R.get(code, []):
        LOOKUP.setdefault(e["name"], e["data"])

drops = Counter()
drop_names = defaultdict(list)
entries = []     # (name, code, tags)
seen = set()

for code in ["BASE", "DTHM", "INVX", "RAN", "DEGR", "ENCO", "EXEP", "FEAT", "SWTE", "UTUT"]:
    for e in R[code]:
        name = e["name"]
        key = (name, code)
        if key in seen:
            drops["duplicate in source"] += 1
            continue
        seen.add(key)
        d = e["data"]
        toks_name = toks(name)
        # Scope rule 2: legendary actions / monster legendary passives. MAG_Legendary* magic-item passives kept.
        if "legendary" in toks_name or "legendaryaction" in name.lower() or "legendaryresistance" in name.lower():
            if not name.startswith("MAG_"):
                drops["legendary action / legendary passive"] += 1
                drop_names["legendary action / legendary passive"].append(f"{name} [{code}]")
                continue
        tags = classify(name, mech_text(d), fx_text(d))
        # Scope rule 1: visual-FX-only. No mechanics and no name-driven tag -> drop.
        if not has_fx(d) and not tags:
            drops["no mechanics and no keyword (visual/FX-only)"] += 1
            drop_names["no mechanics and no keyword (visual/FX-only)"].append(f"{name} [{code}]")
            continue
        entries.append((name, code, tags))

# CX homebrew: classify from the vanilla/mod passives each CX_* passive grants (ExtraPassives)
for m in MANAGER:
    name = m["PassiveName"]
    refs = set()
    for act in m["Act"].values():
        refs.update(act.get("ExtraPassives", []))
    extra_mech, extra_fx = [], []
    missing = []
    for r in sorted(refs):
        if r in LOOKUP:
            extra_mech.append(mech_text(LOOKUP[r]))
            extra_fx.append(fx_text(LOOKUP[r]))
        else:
            missing.append(r)
    tags = classify(name, " ".join(extra_mech), " ".join(extra_fx))
    entries.append((name, "CXCX", tags))
    if missing:
        drop_names["_cx_missing_refs"].append(f"{name}: {', '.join(missing)}")

# build output
out = OrderedDict()
for g in GROUP_ORDER:
    out[g] = OrderedDict((k, []) for k in BASE_KEYS[g])

kept_no_tag = 0
for name, code, tags in entries:
    if not tags:
        kept_no_tag += 1
        continue
    for t in tags:
        g, k = bucket_path(t)
        out[g][k].append(f"{name} [{code}]")

for g in out:
    for k in out[g]:
        out[g][k] = sorted(set(out[g][k]), key=lambda s: s.lower())

# write JSON (4-space indent, existing style)
json.dump(out, open(OUT_JSON, "w", encoding="utf-8"), indent=4, ensure_ascii=False)
open(OUT_JSON, "a", encoding="utf-8").write("\n")

# stats
print("entries classified:", len(entries), "no-tag kept out:", kept_no_tag)
print("drops:", dict(drops))
for g in out:
    print(g, {k: len(v) for k, v in out[g].items()})
print("missing CX refs:", len(drop_names["_cx_missing_refs"]))
json.dump({"drops": dict(drops), "drop_names": {k: v for k, v in drop_names.items() if k != "_cx_missing_refs"},
           "cx_missing": drop_names["_cx_missing_refs"],
           "counts": {g: {k: len(v) for k, v in out[g].items()} for g in out},
           "total_entries": len(entries)}, open(os.path.join(SCR, "run_stats.json"), "w", encoding="utf-8"), indent=1)
