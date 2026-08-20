import argparse
import json
import os
import random

from monsterStatBlock import MonsterStatBlock

BASE_DIR = os.path.dirname(__file__)
DEFAULT_TEMPLATE = os.path.join(BASE_DIR, "block_filter.json")
DEFAULT_MASTER = os.path.join(BASE_DIR, "guid_mapper_master.json")
TEMPLATES_DIR = os.path.join(BASE_DIR, "filter_templates")

DAMAGE_TYPES = {
    "Acid", "Bludgeoning", "Cold", "Fire", "Force", "Lightning",
    "Necrotic", "Piercing", "Poison", "Psychic", "Radiant", "Slashing", "Thunder",
}
DICE = {"d4", "d6", "d8", "d10", "d12", "d20"}

# key -> (list field name, "apply one random" flag name, Goon_ passive suffix)
_RES_IMM_VULN_CFG = {
    "Resistance": ("Resistances", "ApplyOneRandomResFromList", "Resistant"),
    "Immunity": ("Immunities", "ApplyOneRandomImmFromList", "Immune"),
    "Vulnerability": ("Vulnerabilities", "ApplyOneRandomVulFromList", "Vulnerable"),
}

_FILTER_FIELD_GETTERS = {
    "Type": lambda b: b.type,
    "SubType": lambda b: b.subtype,
    "ClassArchetype": lambda b: b.classArchetype,
    "MonsterArchetype": lambda b: b.monsterArchetype,
    "FullGuid": lambda b: b.full_guid,
    "Act": lambda b: b.act,
    "Location": lambda b: b.location,
}


def _clean_list(values):
    return [v.strip() for v in (values or []) if v and v.strip()]


def _entry_matches(value, entry, exact_match):
    if exact_match:
        return value == entry
    return entry in value


def block_passes_filters(block, filters):
    for field_name, getter in _FILTER_FIELD_GETTERS.items():
        rule = filters.get(field_name)
        if not rule:
            continue
        value = getter(block) or ""
        exact_match = rule.get("ExactMatch", True)
        include = _clean_list(rule.get("Include"))
        exclude = _clean_list(rule.get("Exclude"))

        if exclude and any(_entry_matches(value, e, exact_match) for e in exclude):
            return False
        if include and not any(_entry_matches(value, i, exact_match) for i in include):
            return False

    for bool_field, attr in (("LockBlock", "lock_block"), ("MapApplied", "map_applied")):
        rule = filters.get(bool_field)
        if rule is not None and getattr(block, attr) != rule:
            return False

    return True


# ── Passives / Spells ────────────────────────────────────────────────────────

def _apply_full_and_random(target_list, full_list, random_list, random_select):
    changed = False
    for item in _clean_list(full_list):
        if item not in target_list:
            target_list.append(item)
            changed = True

    random_list = _clean_list(random_list)
    if random_list and 0 < random_select <= len(random_list):
        for item in random.sample(random_list, random_select):
            if item not in target_list:
                target_list.append(item)
                changed = True

    if changed:
        target_list.sort()


def _apply_passives(block, cfg):
    _apply_full_and_random(
        block.passives_to_add,
        cfg.get("FullPassiveList"), cfg.get("RandomPassiveList"), cfg.get("RandomPassiveSelect", 0),
    )


def _apply_spells(block, cfg):
    _apply_full_and_random(
        block.spells_to_add,
        cfg.get("FullSpellList"), cfg.get("RandomSpellList"), cfg.get("RandomSpellSelect", 0),
    )


# ── HealthOverride ────────────────────────────────────────────────────────────

def _apply_health_override(block, cfg):
    lo = cfg.get("HealthOverrideMin", 0) or 0
    hi = cfg.get("HealthOverrideMax", 0) or 0
    if not lo or not hi:
        return
    if block.health_override and not cfg.get("OverrideExisting", False):
        return
    value = lo if lo == hi else random.randint(min(lo, hi), max(lo, hi))
    block.health_override = value
    if not block.original_health:
        block.original_health = value


# ── Tiered stat passives: AC, AttackRolls, Movement, Scale ──────────────────
# Each family is a single passive naming a signed tier, e.g. Goon_AC_Buff_3 /
# Goon_AC_Debuff_2. AddToExisting=true combines the new value with whatever
# tier is already present (clamped, removed if it nets to 0). AddToExisting=
# false does a direct/absolute set instead, and only touches a block that
# already carries a tier passive when OverrideExisting=true.

def _extract_tier(passives, prefix):
    for p in passives:
        if p.startswith(prefix):
            suffix = p[len(prefix):]
            if suffix.isdigit():
                return p, int(suffix)
    return None, 0


def _apply_tiered_stat(block, buff_prefix, debuff_prefix, max_tier, value, add_to_existing, override_existing, allow_negative):
    if value == 0 or (not allow_negative and value < 0):
        return

    passives = block.passives_to_add
    buff_name, buff_tier = _extract_tier(passives, buff_prefix)
    debuff_name, debuff_tier = (None, 0)
    if debuff_prefix:
        debuff_name, debuff_tier = _extract_tier(passives, debuff_prefix)
    existing_name = buff_name or debuff_name
    existing_signed = buff_tier - debuff_tier

    if add_to_existing:
        new_signed = existing_signed + value
    else:
        if existing_name is not None and not override_existing:
            return
        new_signed = value

    min_bound = -max_tier if debuff_prefix else 0
    new_signed = max(min_bound, min(max_tier, new_signed))

    if existing_name and existing_name in passives:
        passives.remove(existing_name)

    if new_signed > 0:
        passives.append(f"{buff_prefix}{new_signed}")
    elif new_signed < 0:
        passives.append(f"{debuff_prefix}{-new_signed}")

    passives.sort()


# ── Damage ────────────────────────────────────────────────────────────────────

def _apply_damage_category(block, cfg, suffix, override_key):
    damage_types = _clean_list(cfg.get("DamageTypes"))
    die = (cfg.get("die") or "").strip()

    if not damage_types or die not in DICE or any(dt not in DAMAGE_TYPES for dt in damage_types):
        return

    if cfg.get("ApplyOneRandomDamageTypeFromList", False) and len(damage_types) > 1:
        damage_types = [random.choice(damage_types)]

    passives = block.passives_to_add
    existing = [p for p in passives if p.startswith("Goon_Damage_") and p.rsplit("_", 1)[-1] == suffix]

    if existing:
        if not cfg.get(override_key, False):
            return
        for p in existing:
            passives.remove(p)

    for dt in damage_types:
        name = f"Goon_Damage_{dt}_{die}_{suffix}"
        if name not in passives:
            passives.append(name)

    passives.sort()


# ── Resistance / Immunity / Vulnerability ────────────────────────────────────

def _apply_res_imm_vuln(block, cluster):
    passives = block.passives_to_add
    changed = False
    for key, (list_field, random_field, suffix) in _RES_IMM_VULN_CFG.items():
        cfg = cluster.get(key, {})
        values = [dt for dt in _clean_list(cfg.get(list_field)) if dt in DAMAGE_TYPES]
        if not values:
            continue
        if cfg.get(random_field, False) and len(values) > 1:
            values = [random.choice(values)]
        for dt in values:
            name = f"Goon_{dt}_{suffix}"
            if name not in passives:
                passives.append(name)
                changed = True
    if changed:
        passives.sort()


# ── Cluster / top-level driver ───────────────────────────────────────────────

def apply_cluster(block, cluster):
    _apply_passives(block, cluster.get("Passives", {}))
    _apply_spells(block, cluster.get("Spells", {}))
    _apply_health_override(block, cluster.get("HealthOverride", {}))

    ac = cluster.get("AC", {})
    _apply_tiered_stat(
        block, "Goon_AC_Buff_", "Goon_AC_Debuff_", 5,
        ac.get("ACBonus", 0), ac.get("AddToExisting", True), ac.get("OverrideExisting", False),
        allow_negative=True,
    )

    atk = cluster.get("AttackRolls", {})
    _apply_tiered_stat(
        block, "Goon_AttackRoll_", None, 5,
        atk.get("AttackBonus", 0), atk.get("AddToExisting", True), atk.get("OverrideExisting", False),
        allow_negative=False,
    )

    mv = cluster.get("Movement", {})
    _apply_tiered_stat(
        block, "Goon_Increased_Movement_", "Goon_Impeded_Movement_", 9,
        mv.get("MovementBonus", 0), mv.get("AddToExisting", False), mv.get("OverrideExisting", False),
        allow_negative=True,
    )

    sc = cluster.get("Scale", {})
    _apply_tiered_stat(
        block, "Goon_Increased_Scale_", None, 6,
        sc.get("ScaleBonus", 0), sc.get("AddToExisting", False), sc.get("OverrideExisting", False),
        allow_negative=False,
    )

    dmg = cluster.get("Damage", {})
    _apply_damage_category(block, dmg.get("Attacks", {}), "Attacks", "OverrideExistingAttackPassive")
    _apply_damage_category(block, dmg.get("SpellAttacks", {}), "SpellAttacks", "OverrideExistingSpellAttackPassive")
    _apply_damage_category(block, dmg.get("Spells", {}), "Spells", "OverrideExistingSpellPassive")

    _apply_res_imm_vuln(block, cluster)


def apply_block_filter(blocks, config):
    filters = config.get("Filters", {})
    apply_cfg = config.get("Apply", {})
    clusters = apply_cfg.get("Clusters", [])
    random_cluster_select = apply_cfg.get("RandomClusterSelect", 0)

    matched = 0
    for block in blocks:
        if block.lock_block:
            continue
        if not block_passes_filters(block, filters):
            continue
        matched += 1
        if not clusters:
            continue

        if random_cluster_select <= 0 or random_cluster_select >= len(clusters):
            chosen_clusters = clusters
        else:
            chosen_clusters = random.sample(clusters, random_cluster_select)

        for cluster in chosen_clusters:
            apply_cluster(block, cluster)

    return blocks, matched


def load_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Apply a block_filter template's Filters/Apply rules to guid_mapper_master.json."
    )
    parser.add_argument(
        "--template",
        default=DEFAULT_TEMPLATE,
        help="Path to a block_filter JSON template (see filter_templates/). Default: block_filter.json (blank template).",
    )
    parser.add_argument(
        "--input",
        default=DEFAULT_MASTER,
        help="Path to the guid_mapper master JSON file to read. Default: guid_mapper_master.json.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Where to write results. Default: overwrite --input.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    output_path = args.output or args.input

    config = load_template(args.template)
    blocks = MonsterStatBlock.load_from_json_file(args.input)

    blocks, matched = apply_block_filter(blocks, config)

    MonsterStatBlock.save_to_json_file(blocks, output_path)
    print(f"Template: {args.template}")
    print(f"Matched {matched} block(s); saved to {output_path}")


if __name__ == "__main__":
    main()
