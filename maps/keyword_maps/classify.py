import json, re, os
from collections import defaultdict, OrderedDict

SCR = os.path.dirname(os.path.abspath(__file__))
ZZ = r"C:\Users\Tyler\GitHub\zz_CXUtils"
OUT_JSON = os.path.join(ZZ, "maps", "keyword_maps", "keyword_to_passives.json")
OUT_LOG = os.path.join(ZZ, "maps", "keyword_maps", "keyword_passives_log.md")

# ---------- keyword vocab (token-level matching) ----------
DAMAGE = ["Acid","Bludgeoning","Cold","Fire","Force","Lightning","Necrotic","Piercing",
          "Poison","Psychic","Radiant","Slashing","Thunder"]
SCHOOLS = ["Abjuration","Conjuration","Divination","Enchantment","Evocation",
           "Illusion","Necromancy","Transmutation","Chronurgy","Graviturgy"]
CLASSES = ["Artificer","Barbarian","Bard","Cleric","Druid","Fighter","Monk","Ranger",
           "Rogue","Sorcerer","Warlock","Wizard"]
# Subclass / archetype group: key -> token aliases (lowercase)
SUBCLASS = OrderedDict([
    ("Paladin", ["paladin"]), ("Oathbreaker", ["oathbreaker"]),
    ("Ancients", ["ancients"]), ("Devotion", ["devotion"]), ("Vengeance", ["vengeance"]),
    ("Berserker", ["berserker"]), ("WildHeart", ["wildheart"]), ("WildMagic", ["wildmagic"]),
    ("Lore", ["lore"]), ("Swords", ["swords"]), ("Valor", ["valor"]),
    ("Knowledge", ["knowledge"]), ("Life", ["life"]), ("Light", ["light"]),
    ("Nature", ["nature"]), ("Trickery", ["trickery"]), ("Tempest", ["tempest"]),
    ("War", ["war"]), ("Land", ["land"]), ("Moon", ["moon"]), ("Spores", ["spores"]),
    ("Champion", ["champion"]), ("BattleMaster", ["battlemaster"]),
    ("EldritchKnight", ["eldritch"]), ("FourElements", ["fourelements"]),
    ("OpenHand", ["openhand"]), ("Shadow", ["shadow"]), ("BeastMaster", ["beastmaster"]),
    ("GloomStalker", ["gloomstalker"]), ("Hunter", ["hunter"]),
    ("ArcaneTrickster", ["arcanetrickster"]), ("Assassin", ["assassin"]), ("Thief", ["thief"]),
    ("DraconicBloodline", ["draconicbloodline", "draconic"]), ("StormSorcery", ["stormsorcery"]),
    ("Archfey", ["archfey"]), ("Fiend", ["fiend"]), ("GreatOldOne", ["greatoldone"]),
])
RACES = OrderedDict([
    ("Halfling", ["halfling"]), ("Gnome", ["gnome", "gnomish"]), ("Dwarf", ["dwarf", "dwarven"]),
    ("Elf", ["elf", "elven"]), ("Drow", ["drow"]), ("Human", ["human"]),
    ("Dragonborn", ["dragonborn"]), ("Tiefling", ["tiefling"]), ("Orc", ["orc"]),
    ("Tabaxi", ["tabaxi"]), ("Githyanki", ["githyanki"]), ("Githzerai", ["githzerai"]),
    ("Goliath", ["goliath"]), ("Aasimar", ["aasimar"]), ("Genasi", ["genasi"]),
])
ENEMY = ["Aberration","Beast","Celestial","Construct","Dragon","Elemental","Fey","Fiend",
         "Giant","Humanoid","Monstrosity","Plant","Ooze","Undead"]
ITEM = OrderedDict([
    ("Headwear", {"helmet","helm","hat","circlet","crown","headwear","headband","tiara","diadem","hood"}),
    ("Cloak", {"cloak","cape","mantle"}),
    ("Armor/Clothing", {"armor","armour","clothing","robe","breastplate","plate","leather"}),
    ("Gloves", {"gloves","gauntlets","glove","gauntlet"}),
    ("Boots", {"boots","shoes","sandals"}),
    ("Necklace", {"necklace","amulet","pendant","torc"}),
    ("Ring", {"ring"}),
    ("Martial Weapon", {"martial"}),
    ("Ranged Weapon", {"ranged","bow","crossbow","longbow","shortbow","sling"}),
    ("Shield", {"shield"}),
])
CONTROL = {"stunned","frightened","charmed","paralyzed","prone","restrained","blinded",
           "incapacitated","sleep","entangled","petrified","hold","held","knockdown","stun","fear"}
AOE_RE = re.compile(r"Radius|Sphere|Cone|Cube|Line|Area|Within|AOE|AllEnemies|AllAllies|Battlefield", re.I)


def toks(s):
    """Split camel/underscore/punctuation into lowercase word pieces (plus whole words)."""
    out = set()
    if not s:
        return out
    for w in re.findall(r"[A-Za-z]+", s):
        for p in re.findall(r"[A-Z]+(?![a-z])|[A-Z]?[a-z]+", w):
            out.add(p.lower())
        out.add(w.lower())
    return out


def fx_text(d):
    keys = ("Boosts", "StatsFunctors", "ToggleOnFunctors", "Conditions", "BoostConditions",
            "EnabledConditions", "StatsFunctorContext", "BoostContext", "Properties")
    parts = []
    for k in keys:
        v = d.get(k)
        if v is None:
            continue
        parts.append(";".join(v) if isinstance(v, list) else v)
    return " ".join(parts)


def mech_text(d):
    """Mechanics only: what the passive grants or does (Boosts, StatsFunctors, ToggleOnFunctors)."""
    parts = []
    for k in ("Boosts", "StatsFunctors", "ToggleOnFunctors"):
        v = d.get(k)
        if v is None:
            continue
        parts.append(";".join(v) if isinstance(v, list) else v)
    return " ".join(parts)


def has_fx(d):
    return bool(d.get("Boosts") or d.get("StatsFunctors") or d.get("ToggleOnFunctors"))


def classify(name, mech, fx=None):
    """Return a set of bucket tags for one passive.
    mech: mechanics text (Boosts/StatsFunctors). fx: full text incl. Conditions, used only for
    spell/AOE/control context. Keyword groups match on name + mech, never on conditions."""
    fx = mech if fx is None else fx
    N = toks(name)
    # Explicit tag references: Tagged('BEAST', ...) etc. Status/ID names are NOT matched here.
    tags_ref = {t.lower() for t in re.findall(r"Tagged\('([A-Za-z]+)'", mech)}
    b = set()

    # Damage type: only as a capitalised argument/enum (DamageType.Fire, DealDamage(..., Fire), Resistance(Fire))
    for d in DAMAGE:
        if re.search(r"(?<![A-Za-z_])" + d + r"(?![A-Za-z_])", mech) or ("DamageType." + d) in mech:
            b.add(d)
    # Schools, classes, subclasses, races: name tokens only
    for s in SCHOOLS:
        if s.lower() in N:
            b.add(s)
    for c in CLASSES:
        if c.lower() in N:
            b.add("Class:" + c)
    for k, al in SUBCLASS.items():
        if any(a in N for a in al):
            b.add("Subclass:" + k)
    for k, al in RACES.items():
        if any(a in N or a in tags_ref for a in al):
            b.add("Races:" + k)
    for e in ENEMY:
        if e.lower() in N or e.lower() in tags_ref:
            b.add("EnemyType:" + e)
    # Magic item type: item name tokens; ranged/martial also via weapon-attack conditions in mech
    ranged_ctx = bool(re.search(r"IsRangedWeaponAttack|IsRangedUnarmed|IsRanged", mech))
    martial_ctx = "Martial" in mech or "martial" in mech.lower() and "Weapon" in mech
    for k, words in ITEM.items():
        hit = bool(words & N)
        if k == "Ranged Weapon" and ranged_ctx:
            hit = True
        if k == "Martial Weapon" and not hit and martial_ctx:
            hit = True
        if hit:
            b.add("MagicItemType:" + k)

    # Type buckets: rough mechanic-driven heuristics
    aoe = bool(AOE_RE.search(fx))
    spell = bool(re.search(r"IsSpell|SpellDamageTypeIs|IsCantrip|IsPerformSpell|SpellAttackCheck|SpellCategory", fx))
    ctrl = bool(CONTROL & toks(mech))
    if re.search(r"DealDamage|DamageBonus|DamageReduction", mech) and spell:
        b.add("Type:SpellDamage_" + ("AOE_Small" if aoe else "Single"))
    if ctrl:
        b.add("Type:Control_" + ("AOE_Small" if aoe else "Single"))
    if re.search(r"IncreaseMaxHP|TemporaryHP|MaxHP", mech):
        b.add("Type:Defense_HitPoints")
    if re.search(r"\bAC\(", mech):
        b.add("Type:Defense_ArmorClass")
    if re.search(r"RollBonus\([^)]*SavingThrow|ModifySavingThrow|Advantage\([^)]*SavingThrow", mech):
        b.add("Type:Defense_SavingThrows")
    if re.search(r"Resistance\(|DamageReduction", mech):
        b.add("Type:Defense_DamageResistance")
    if re.search(r"StatusImmunity|IsImmuneToStatus", mech):
        b.add("Type:Defense_ConditionImmunity")
    if re.search(r"RedirectDamage|IgnoreFallDamage|Invulnerab", mech):
        b.add("Type:Defense_Special")
    if re.search(r"Heal|Regenerat|RegainHP", mech):
        b.add("Type:Healing_" + ("AOE" if aoe else "Single"))
    # negative numeric boosts only (Ability(X,-1)); ignore durations like ApplyStatus(...,-1)
    neg = re.search(r"Disadvantage\(|ModifySavingThrowDisadvantage|(Ability|RollBonus|Proficiency)\([^)]*,-\d", mech)
    pos = re.search(r"Advantage\(|ProficiencyBonus|RollBonus\([^)]*,\+?\d|Ability\([^)]*,\+?\d|ActionResource|Initiative|DamageBonus|\bAC\(", mech)
    if neg:
        b.add("Type:Debuff_" + ("Multiple" if aoe else "Single"))
    if pos and not neg:
        b.add("Type:Buff_" + ("Multiple" if aoe else "Single"))
    if re.search(r"Teleport|Jump|Blink", mech):
        b.add("Type:Teleportation")
    return b


GROUP_ORDER = ["DamageTypes", "SpellSchools", "Class", "Subclass", "Races", "EnemyType", "MagicItemType", "Type"]
BASE_KEYS = {
    "DamageTypes": DAMAGE,
    "SpellSchools": ["Abjuration","Chronurgy","Conjuration","Divination","Enchantment","Evocation","Graviturgy","Illusion","Necromancy","Transmutation"],
    "Class": CLASSES,
    "Subclass": list(SUBCLASS.keys()),
    "Races": list(RACES.keys()),
    "EnemyType": ENEMY,
    "MagicItemType": list(ITEM.keys()),
    "Type": ["SpellDamage_Single","SpellDamage_AOE_Small","SpellDamage_AOE_Large","Control_Single","Control_AOE_Small","Control_AOE_Large","Defense_HitPoints","Defense_ArmorClass","Defense_SavingThrows","Defense_DamageResistance","Defense_ConditionImmunity","Defense_Special","Healing_Single","Healing_AOE","Buff_Single","Buff_Multiple","Debuff_Single","Debuff_Multiple","Teleportation"],
}


def bucket_path(tag):
    """Map a classify() tag to (group, key)."""
    if ":" in tag:
        g, k = tag.split(":", 1)
        if g == "Class": return ("Class", k)
        if g == "Subclass": return ("Subclass", k)
        if g == "Races": return ("Races", k)
        if g == "EnemyType": return ("EnemyType", k)
        if g == "MagicItemType": return ("MagicItemType", k)
        if g == "Type": return ("Type", k)
    if tag in DAMAGE: return ("DamageTypes", tag)
    if tag in SCHOOLS: return ("SpellSchools", tag)
    raise KeyError(tag)
