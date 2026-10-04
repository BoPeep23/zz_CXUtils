import os, re, json, sys
from collections import defaultdict
ROOT = r"C:\Users\Tyler\source\repos\bg3-mod-extraction-utils"
SRC = {
    "BASE": [os.path.join(ROOT, "scratch_vanilla_extract", "allstats_hunt")],
    "DTHM": [os.path.join(ROOT, "mods", "DeathMarch")],
    "INVX": [os.path.join(ROOT, "mods", "InvocationsExpanded")],
    "RAN":  [os.path.join(ROOT, "mods", "RangerSubclasses5eCombined")],
    "DEGR": [os.path.join(ROOT, "mods", "DeGreaser")],
    "ENCO": [os.path.join(ROOT, "mods", "EncountersOverhaul")],
    "EXEP": [os.path.join(ROOT, "mods", "Extra_encounters_plus")],
    "FEAT": [os.path.join(ROOT, "mods", "featsextra")],
    "SWTE": [os.path.join(ROOT, "mods", "StormWardensTomeOfEncounters")],
    "UTUT": [os.path.join(ROOT, "mods", "UtutsCoreLibrary")],
    # FADE: Fade's Equipment Distribution per-class packs (7 of 10 folders; Ranger/Bard/Warlock excluded)
    "FADE": [os.path.join(ROOT, "mods", f) for f in [
        "FADE_CC_Sorcerer_Equipment", "FADE_FF_Cleric_Equipment", "FADE_GG_Druid_Equipment",
        "FADE_OO_Paladin_Equipment", "FADE_UU_Monk_Equipment", "FADE_VV_Rogue_Equipment",
        "FADE_WW_Wizard_Equipment"]],
}
ENTRY = re.compile(r'^new entry "([^"]+)"', re.M)
DATA = re.compile(r'^data "([^"]+)" "(.*)"\s*$', re.M)
TYPE = re.compile(r'^type "([^"]+)"', re.M)
USING = re.compile(r'^using "([^"]+)"', re.M)

def parse_file(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    parts = re.split(r'(?=^new entry ")', text, flags=re.M)
    out = []
    for p in parts:
        m = ENTRY.match(p)
        if not m: continue
        t = TYPE.search(p)
        if not t or t.group(1) != "PassiveData": continue
        d = defaultdict(list)
        for k, v in DATA.findall(p):
            d[k].append(v)
        u = USING.search(p)
        out.append({"name": m.group(1), "using": u.group(1) if u else None,
                    "file": os.path.relpath(path, ROOT), "data": {k: v[0] if len(v)==1 else v for k, v in d.items()}})
    return out

def walk(dirs):
    for d in dirs:
        for dp, _, fns in os.walk(d):
            for fn in fns:
                if fn.lower().endswith(".txt") and os.sep + "Stats" + os.sep in dp:
                    yield os.path.join(dp, fn)

if __name__ == "__main__":
    result = {}
    for code, dirs in SRC.items():
        entries = []
        for f in walk(dirs):
            entries += parse_file(f)
        result[code] = entries
        print(code, len(entries), "unique names:", len({e["name"] for e in entries}), file=sys.stderr)
    json.dump(result, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "passives_raw.json"), "w", encoding="utf-8"), indent=1)
