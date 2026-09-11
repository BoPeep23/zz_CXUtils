"""Build research/cx_passive_options.md - candidate ExtraPassives / Spells for
every CX_*_Boost passive, harvested from bg3.norbyte.dev.

Run from anywhere; writes into the zz_CXUtils repo.
"""
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
from scrape import search, summarize  # noqa: E402
from terms import TERMS  # noqa: E402

REPO = r"C:\Users\Tyler\GitHub\zz_CXUtils"
MANAGER = os.path.join(REPO, "cx_passive_manager.json")
OUT = os.path.join(REPO, "research", "cx_passive_options.md")

CLASS_ORDER = [
    ("Generic", ["CX_Boss_Boost", "CX_MiniBoss_Boost", "CX_Magic_Boost", "CX_Martial_Boost"]),
    ("Barbarian", ["CX_Barbarian_Boost", "CX_Barbarian_Berserker_Boost",
                   "CX_Barbarian_WildMagic_Boost", "CX_Barbarian_Wildheart_Boost"]),
    ("Bard", ["CX_Bard_Boost", "CX_Bard_Lore_Boost", "CX_Bard_Swords_Boost",
              "CX_Bard_Valor_Boost"]),
    ("Cleric", ["CX_Cleric_Boost", "CX_Cleric_Knowledge_Boost", "CX_Cleric_Life_Boost",
                "CX_Cleric_Light_Boost", "CX_Cleric_Nature_Boost", "CX_Cleric_Trickery_Boost",
                "CX_Cleric_Tempest_Boost", "CX_Cleric_War_Boost"]),
    ("Druid", ["CX_Druid_Boost", "CX_Druid_Land_Boost", "CX_Druid_Moon_Boost",
               "CX_Druid_Spores_Boost"]),
    ("Fighter", ["CX_Fighter_Boost", "CX_Fighter_BattleMaster_Boost",
                 "CX_Fighter_Champion_Boost", "CX_Fighter_EldritchKnight_Boost"]),
    ("Monk", ["CX_Monk_Boost", "CX_Monk_FourElements_Boost", "CX_Monk_OpenHand_Boost",
              "CX_Monk_Shadow_Boost"]),
    ("Paladin", ["CX_Paladin_Boost", "CX_Paladin_Ancients_Boost", "CX_Paladin_Devotion_Boost",
                 "CX_Paladin_Vengeance_Boost", "CX_Paladin_Oathbreaker_Boost"]),
    ("Ranger", ["CX_Ranger_Boost", "CX_Ranger_BeastMaster_Boost",
                "CX_Ranger_GloomStalker_Boost", "CX_Ranger_Hunter_Boost"]),
    ("Rogue", ["CX_Rogue_Boost", "CX_Rogue_ArcaneTrickster_Boost", "CX_Rogue_Assassin_Boost",
               "CX_Rogue_Thief_Boost"]),
    ("Sorcerer", ["CX_Sorcerer_Boost", "CX_Sorcerer_DraconicBloodline_Boost",
                  "CX_Sorcerer_WildMagic_Boost", "CX_Sorcerer_StormSorcery_Boost"]),
    ("Warlock", ["CX_Warlock_Boost", "CX_Warlock_Archfey_Boost", "CX_Warlock_Fiend_Boost",
                 "CX_Warlock_GreatOldOne_Boost"]),
    ("Wizard", ["CX_Wizard_Boost", "CX_Wizard_Abjuration_Boost", "CX_Wizard_Conjuration_Boost",
                "CX_Wizard_Divination_Boost", "CX_Wizard_Enchantment_Boost",
                "CX_Wizard_Evocation_Boost", "CX_Wizard_Illusion_Boost",
                "CX_Wizard_Necromancy_Boost", "CX_Wizard_Transmutation_Boost"]),
]

# hits that add nothing as an NPC combat buff - drop from candidate lists
NOISE_SUBSTR = ("_DEBUG", "DEBUG_", "_TUT_", "TUT_", "_QUEST", "Cinematic", "_CIN_",
                "Placeholder", "PLACEHOLDER", "_UNUSED", "Deprecated", "GENERIC_",
                "_Trap", "TRAP_", "_Technical", "_TECHNICAL", "_Container", "_Interrupt_",
                "_Hardcore", "_HONOUR", "_Honour")

_FAMILY_RE = re.compile(r"_\d+(_Passive)?$")

# spell reskins that pollute broad English searches: creature/area-scoped
# copies (_LOW_ _DEN_ _MAG_ ...), delivery-method copies, cosmetic race/sex
# disguise variants, and technical helpers.
_SPELL_NOISE_RE = re.compile(
    r"_[A-Z]{2,5}_"
    r"|_(MOMF|NPC|Cancel|Dummy|Fake|Preview|Explosion|Turret|Trap|Container|Technical"
    r"|FromScroll|FromWand|FromWeapon|FromItem|FromShield|FromLute|FromPipe|Reaction"
    r"|Dragonborn|Drow|Elf|HalfElf|Human|Gith|Githyanki|Halfling|Gnome|Tiefling|Dwarf"
    r"|HalfOrc|Female|Male|Femme|Masc|Djinni|FleshGolem|AI)(_|$)"
)


def family_key(name):
    """Collapse numbered tiers: ARM_MagicalPlate_1_Passive -> ARM_MagicalPlate."""
    return _FAMILY_RE.sub("", name)


def spell_is_noise(name, cx):
    if _SPELL_NOISE_RE.search(name):
        return True
    if "_Monk" in name and "Monk" not in cx:
        return True
    return False

_UPCAST_RE = re.compile(r"_([2-9]|1[0-2])$")  # spell upcast variants: NPCs auto-upcast


def is_upcast(name):
    return bool(_UPCAST_RE.search(name))


MAX_PASSIVE = 18
MAX_SPELL = 14


def load_manager_index():
    with open(MANAGER, encoding="utf-8") as f:
        data = json.load(f)
    idx = {}
    for e in data:
        have_p, have_s = set(), set()
        for act in ("1", "2", "3"):
            a = e.get("Act", {}).get(act, {})
            have_p.update(x for x in a.get("ExtraPassives", []) if x)
            have_s.update(x for x in a.get("Spells", []) if x)
        idx[e["PassiveName"]] = {"passives": have_p, "spells": have_s}
    return idx


def is_noise(name):
    return any(s in name for s in NOISE_SUBSTR)


def gather(kind, terms, want_type, have_set, cx_name):
    """kind: 'passive'|'spell'. Returns ordered list of candidate dicts."""
    seen = {}
    for term in terms:
        q = f"type:{want_type} & {term}"
        try:
            res = search(q)
        except Exception as e:  # noqa: BLE001
            print(f"    ! {q}: {e}")
            continue
        tag = "CAPPED" if res["capped"] else str(res["total"])
        print(f"    {q}  -> {tag}")
        for row in res["rows"]:
            nm = row["name"]
            if nm in seen or is_noise(nm):
                continue
            if kind == "spell" and nm not in have_set:
                if is_upcast(nm) or spell_is_noise(nm, cx_name):
                    continue
            if row["type"].lower() != want_type:
                continue
            s = summarize(row["body"])
            seen[nm] = {
                "name": nm,
                "type": row["type"],
                "have": nm in have_set,
                "term": term,
                "display": s["display"],
                "desc": s["desc"],
                "mech": s["mech"],
                "using": s["using"],
            }
    # order: not-yet-owned first, then by whether the search term is literally
    # in the name (tighter match), then alphabetical
    def key(c):
        return (c["have"], c["term"].lower() not in c["name"].lower(), c["name"].lower())

    ordered = sorted(seen.values(), key=key)
    # collapse numbered tiers (ARM_*_1_Passive / _2_Passive / _3 ...): keep the
    # first (best-ranked) of each family, note how many siblings were folded in.
    out, fam_seen = [], {}
    for c in ordered:
        fk = family_key(c["name"])
        if fk == c["name"]:
            out.append(c)
            continue
        if fk in fam_seen:
            fam_seen[fk]["_folded"] = fam_seen[fk].get("_folded", 1) + 1
            continue
        fam_seen[fk] = c
        out.append(c)
    return out


def fmt_candidate(c):
    flag = " _(already in manager)_" if c["have"] else ""
    if c.get("_folded"):
        flag += f" _(+{c['_folded']} numbered tiers)_"
    head = f"- `{c['name']}`{flag}"
    bits = []
    if c["display"]:
        bits.append(f"**{c['display']}**")
    if c["desc"]:
        bits.append(c["desc"])
    line = head
    if bits:
        line += " - " + " | ".join(bits)
    extra = []
    for m in c["mech"]:
        if m.startswith(("Boosts=", "SpellSuccess=", "SpellType=", "SpellProperties=")):
            extra.append(m)
    if extra:
        line += "\n  <br>`" + "`  `".join(extra) + "`"
    return line


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    mgr = load_manager_index()
    started = time.time()
    parts = [
        "# CX passive-manager candidate options",
        "",
        "Auto-harvested from <https://bg3.norbyte.dev> for every `CX_*_Boost` passive "
        "tracked in `cx_passive_manager.json`. Each list is *candidates to consider*, "
        "not a recommendation - skim and cherry-pick into the Act buckets.",
        "",
        f"_Generated {time.strftime('%Y-%m-%d %H:%M')} - "
        "Norbyte search returns the first 30 hits only; very broad terms are truncated._",
        "",
        "**Legend** - `already in manager` means the name is already present in some Act "
        "bucket for this passive. Candidates you do not own yet are listed first, and "
        "names that literally contain the search term rank above thematic-only matches. "
        "Spell upcast variants (`_2` .. `_6`) are collapsed to the base name.",
        "",
        "---",
        "",
    ]

    for class_name, cx_names in CLASS_ORDER:
        parts.append(f"## {class_name}")
        parts.append("")
        for cx in cx_names:
            spec = TERMS.get(cx)
            if not spec:
                continue
            print(f"[{cx}]  ({spec['role']})")
            have = mgr.get(cx, {"passives": set(), "spells": set()})
            parts.append(f"### `{cx}`  -  _{spec['role']}_")
            if have["passives"] or have["spells"]:
                cur = []
                if have["passives"]:
                    cur.append("passives: " + ", ".join(f"`{p}`" for p in sorted(have["passives"])))
                if have["spells"]:
                    cur.append("spells: " + ", ".join(f"`{p}`" for p in sorted(have["spells"])))
                parts.append("_Currently in manager_ - " + "; ".join(cur))
            parts.append("")

            pcands = gather("passive", spec["passive"], "passive", have["passives"], cx)
            parts.append(f"**Passive candidates** ({len(pcands)} found"
                         + (f", showing {MAX_PASSIVE}" if len(pcands) > MAX_PASSIVE else "")
                         + ")")
            if pcands:
                parts.extend(fmt_candidate(c) for c in pcands[:MAX_PASSIVE])
            else:
                parts.append("- _(no hits - adjust search terms in terms.py)_")
            parts.append("")

            scands = gather("spell", spec["spell"], "spell", have["spells"], cx)
            parts.append(f"**Spell candidates** ({len(scands)} found"
                         + (f", showing {MAX_SPELL}" if len(scands) > MAX_SPELL else "")
                         + ")")
            if scands:
                parts.extend(fmt_candidate(c) for c in scands[:MAX_SPELL])
            else:
                parts.append("- _(no hits - adjust search terms in terms.py)_")
            parts.append("")
        parts.append("---")
        parts.append("")

    parts.append(f"_Done in {time.time() - started:.0f}s._")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(parts) + "\n")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
