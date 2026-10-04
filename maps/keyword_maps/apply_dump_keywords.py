"""Additive pass: propagate keywords from SE stat dump records onto passives and spells.

Reads the current keyword_to_passives.json / keyword_to_spells.json, and for every
item or creature in the dump that references a passive or spell, adds the keywords
that record's structured fields imply to that passive or spell's buckets.

Rules (structured fields only):
  Weapon/Armor Slot          -> MagicItemType (Helmet=Headwear, Breast=Armor/Clothing, ...)
  Armor Proficiency Group    -> MagicItemType Shield (contains 'Shields')
  Weapon Group Martial*      -> MagicItemType Martial Weapon
  Weapon Slot Ranged / *Ranged* group -> MagicItemType Ranged Weapon
  Weapon Damage Type         -> DamageTypes, non-physical only (physical is the default on every weapon)
  Character Class            -> Class, or Subclass when the value is a subclass name

Edges:
  Weapon/Armor PassivesOnEquip / PassivesMainHand / PassivesOffHand -> passives
  Weapon/Armor UnlockSpell(...) in Boosts / DefaultBoosts / BoostsOnEquip* -> spells
  Character Passives -> passives (inherit Class/Subclass only)

Additive and idempotent: existing entries are kept, only new memberships are added.
Passives and spells that appear in the dump but are not already indexed are reported,
not added (no source code is known for them).
"""
import json, os, re
from keyword_io import merge_keyword_map
from collections import OrderedDict, defaultdict, Counter

DUMP = r"C:\Users\Tyler\source\repos\bg3-mod-extraction-utils\resources\se_stat_dump"
KM = os.path.dirname(os.path.abspath(__file__))
P_JSON = os.path.join(KM, "keyword_to_passives.json")
S_JSON = os.path.join(KM, "keyword_to_spells.json")
P_LOG = os.path.join(KM, "keyword_passives_log.md")
S_LOG = os.path.join(KM, "keyword_spells_log.md")

SLOT_TO_ITEM = {
    "Helmet": "Headwear",
    "Cloak": "Cloak",
    "Breast": "Armor/Clothing",
    "Gloves": "Gloves",
    "Boots": "Boots",
    "Amulet": "Necklace",
    "Ring": "Ring",
}
PHYSICAL = {"Bludgeoning", "Piercing", "Slashing", "None", ""}
CLASSES = {"Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
           "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"}


def load(name):
    return json.load(open(os.path.join(DUMP, name + ".json"), encoding="utf-8"))


def split(v):
    return [p.strip() for p in str(v or "").split(";") if p.strip()]


def item_profile(rec, is_weapon):
    """Set of (group, key) implied by an item's structured fields."""
    out = set()
    slot = rec.get("Slot", "")
    if slot in SLOT_TO_ITEM:
        out.add(("MagicItemType", SLOT_TO_ITEM[slot]))
    if "Shields" in (rec.get("Proficiency Group") or []):
        out.add(("MagicItemType", "Shield"))
    if is_weapon:
        wg = rec.get("Weapon Group", "")
        if wg.startswith("Martial"):
            out.add(("MagicItemType", "Martial Weapon"))
        if slot == "Ranged Main Weapon" or wg.endswith("RangedWeapon"):
            out.add(("MagicItemType", "Ranged Weapon"))
        dt = rec.get("Damage Type", "")
        if dt not in PHYSICAL:
            out.add(("DamageTypes", dt))
    return out


def char_profile(rec):
    out = set()
    cls = rec.get("Class", "")
    if cls in CLASSES:
        out.add(("Class", cls))
    return out


def index_names(data):
    """name -> list of (group, key, entry_string) already present in a map."""
    idx = defaultdict(set)
    for g, keys in data.items():
        for k, entries in keys.items():
            for e in entries:
                m = re.match(r"^(.*) \[([A-Z0-9]+)\]$", e)
                idx[m.group(1)].add(m.group(2))
    return idx


def apply(data, additions, idx, gaps, label, sort_key):
    """Add (group,key) memberships to every indexed source-code entry of each name."""
    added = Counter()
    touched = set()
    for name, profile in additions.items():
        if name not in idx:
            gaps[label][name] |= profile
            continue
        for code in idx[name]:
            entry = f"{name} [{code}]"
            for g, k in profile:
                if k not in data[g]:
                    continue  # only keys that exist in this map's structure
                if entry not in data[g][k]:
                    data[g][k].append(entry)
                    added[(g, k)] += 1
                    touched.add(entry)
    for g in data:
        for k in data[g]:
            data[g][k] = sorted(set(data[g][k]), key=sort_key)
    return added, touched


def main():
    W, A, C = load("dump_weapon"), load("dump_armor"), load("dump_character")
    passives = json.load(open(P_JSON, encoding="utf-8"), object_pairs_hook=OrderedDict)
    spells = json.load(open(S_JSON, encoding="utf-8"), object_pairs_hook=OrderedDict)
    p_idx, s_idx = index_names(passives), index_names(spells)

    p_add, s_add = defaultdict(set), defaultdict(set)
    edge_src = Counter()  # where each passive/spell gained keywords from, for the log
    gaps = {"passives": defaultdict(set), "spells": defaultdict(set)}

    for src, recs, is_weapon in (("weapon", W, True), ("armor", A, False)):
        for name, rec in recs.items():
            prof = item_profile(rec, is_weapon)
            if not prof:
                continue
            pnames = set()
            for field in ("PassivesOnEquip", "PassivesMainHand", "PassivesOffHand"):
                pnames.update(split(rec.get(field)))
            snames = set()
            for field in ("Boosts", "DefaultBoosts", "BoostsOnEquipMainHand", "BoostsOnEquipOffHand"):
                snames.update(re.findall(r"UnlockSpell\(([^,)]+)", str(rec.get(field) or "")))
            for p in pnames:
                p_add[p] |= prof
                edge_src[("passive", src)] += 1
            for s in snames:
                s_add[s] |= prof
                edge_src[("spell", src)] += 1

    for name, rec in C.items():
        prof = char_profile(rec)
        if not prof:
            continue
        for p in split(rec.get("Passives")):
            p_add[p] |= prof
            edge_src[("passive", "character")] += 1

    p_added, p_touched = apply(passives, p_add, p_idx, gaps, "passives", lambda s: s.lower())
    s_added, s_touched = apply(spells, s_add, s_idx, gaps, "spells", lambda s: s)  # spells file is plain ASCII-sorted

    # Merge, never replace. The loaded maps already hold every existing key and entry.
    merge_keyword_map(P_JSON, passives, sort_key=lambda s: s.lower())
    merge_keyword_map(S_JSON, spells, sort_key=lambda s: s)

    # ---- report ----
    print("passive names with inherited keywords:", len(p_add), "| indexed:", sum(1 for n in p_add if n in p_idx))
    print("spell names with inherited keywords:  ", len(s_add), "| indexed:", sum(1 for n in s_add if n in s_idx))
    print("edges:", dict((f"{a}/{b}", n) for (a, b), n in edge_src.items()))
    print("new memberships passives:", sum(p_added.values()), dict(Counter({f"{g}:{k}": n for (g, k), n in p_added.items()})))
    print("new memberships spells:  ", sum(s_added.values()), dict(Counter({f"{g}:{k}": n for (g, k), n in s_added.items()})))
    print("not indexed (gaps): passives", len(gaps["passives"]), "spells", len(gaps["spells"]))

    stats = {
        "passive_memberships_added": {f"{g}:{k}": n for (g, k), n in p_added.items()},
        "spell_memberships_added": {f"{g}:{k}": n for (g, k), n in s_added.items()},
        "passive_gaps": sorted(gaps["passives"].keys()),
        "spell_gaps": sorted(gaps["spells"].keys()),
        "passive_entries_touched": len(p_touched),
        "spell_entries_touched": len(s_touched),
    }
    json.dump(stats, open(os.path.join(KM, "dump_pass_stats.json"), "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
