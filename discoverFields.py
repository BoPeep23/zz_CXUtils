import argparse
import json
import os
import random
import re

from monsterStatBlock import MonsterStatBlock


class discoverFields:
    """Applies Modification and Information field updates to blocks, using
    the Identifiers sanitizeFields.py has already built out as the filter
    criteria, and the Block Controls (Lock* fields) to decide whether a block
    is even eligible for a given kind of update. Never touches Identifiers -
    that's sanitizeFields.py's job."""

    # Maps guid_mapper_master.json / handle_map.json field names to the
    # corresponding MonsterStatBlock attribute names.
    FIELD_ATTR_MAP = {
        "Handle": "handle",
        "FullGuid": "full_guid",
        "Act": "act",
        "Location": "location",
        "Type": "type",
        "SubType": "subtype",
        "ClassArchetype": "classArchetype",
        "MonsterArchetype": "monsterArchetype",
        "Corpse": "corpse",
        "ArmorClass": "armor_class",
        "OriginalHealth": "original_health",
        "Level": "level",
        "Notes": "notes",
        "HealthOverride": "health_override",
        "PassivesToAdd": "passives_to_add",
        "SpellsToAdd": "spells_to_add",
        "CloneTemplateGuid": "clone_template_guid",
        "CloneDisplayName": "clone_display_name",
        "LockStaticModifications": "lock_static_modifications",
        "LockRandomModifications": "lock_random_modifications",
        "LockInformation": "lock_information",
        "LockBlock": "lock_block",
    }

    # Modification fields (see MonsterStatBlock's field categories): always
    # dynamic, gathered/transformed by generateCombatExtenderBlocks.py.
    MODIFICATION_FIELDS = {
        "HealthOverride", "PassivesToAdd", "SpellsToAdd",
        "CloneTemplateGuid", "CloneDisplayName",
    }

    # Information fields: current/planned info about the creature. Only
    # monster_archetype_to_static_modifications_and_info() may write these,
    # and only when the block isn't LockInformation'd.
    INFORMATION_FIELDS = {"ArmorClass", "OriginalHealth", "Level", "Notes"}

    # ApplyStats fields that should be merged into the block's existing list
    # (deduplicated) instead of overwriting it outright.
    LIST_MERGE_FIELDS = {"PassivesToAdd", "SpellsToAdd"}

    # Fields that can never be used in a MatchCombo: list-valued fields can't be
    # meaningfully substring-matched, and HealthOverride is too easy to match
    # unintended blocks by accident (e.g. "10" inside "100").
    INVALID_COMBO_FIELDS = LIST_MERGE_FIELDS | {"HealthOverride"}

    # Dispatches an update_by_* filter method by the Identifier field it reads.
    _FILTER_METHOD_NAMES = {
        "Handle": "update_by_handle",
        "FullGuid": "update_by_full_guid",
        "Act": "update_by_act",
        "Location": "update_by_location",
        "Type": "update_by_type",
        "SubType": "update_by_sub_type",
        "ClassArchetype": "update_by_class_archetype",
        "MonsterArchetype": "update_by_monster_archetype",
    }

    # ── Identifier filters ──────────────────────────────────────────────────
    # Each is a predicate over a single block. Never invoked directly by
    # __main__ - each modification/information tier below dispatches the one
    # it needs, keyed by which Identifier field that tier's map is keyed on.

    @staticmethod
    def _matches_phrase(target, phrase):
        """Substring match (case-insensitive) by default. A trailing '*' on
        phrase forces a whole-word/whole-phrase match instead."""
        if not target or not phrase:
            return False
        phrase = str(phrase)
        if phrase.endswith("*"):
            core = re.escape(phrase[:-1].strip())
            if not core:
                return False
            pattern = r"(?<!\w)" + core + r"(?!\w)"
            return re.search(pattern, target, re.IGNORECASE) is not None
        return phrase.lower() in target.lower()

    @staticmethod
    def update_by_handle(block, handle_phrase):
        return discoverFields._matches_phrase(block.handle, handle_phrase)

    @staticmethod
    def update_by_full_guid(block, full_guid_phrase):
        return discoverFields._matches_phrase(block.full_guid, full_guid_phrase)

    @staticmethod
    def update_by_act(block, act):
        if not block.act or not act:
            return False
        return block.act.strip().lower() == str(act).strip().lower()

    @staticmethod
    def update_by_location(block, location):
        if not block.location or not location:
            return False
        return block.location.strip().lower() == str(location).strip().lower()

    @staticmethod
    def update_by_type(block, type_value):
        if not block.type or not type_value:
            return False
        return block.type.strip().lower() == str(type_value).strip().lower()

    @staticmethod
    def update_by_sub_type(block, sub_type_phrase):
        return discoverFields._matches_phrase(block.subtype, sub_type_phrase)

    @staticmethod
    def update_by_class_archetype(block, class_archetype_phrase):
        return discoverFields._matches_phrase(block.classArchetype, class_archetype_phrase)

    @staticmethod
    def update_by_monster_archetype(block, monster_archetype):
        if not block.monsterArchetype or not monster_archetype:
            return False
        return block.monsterArchetype.strip().lower() == str(monster_archetype).strip().lower()

    # ── Shared engine ────────────────────────────────────────────────────────

    @staticmethod
    def _load_map(filename):
        base_dir = os.path.dirname(__file__)
        map_path = os.path.join(base_dir, "maps", filename)
        with open(map_path, "r") as f:
            return json.load(f)

    @staticmethod
    def _set_field(block, field, value):
        attr = discoverFields.FIELD_ATTR_MAP.get(field, field)
        if field in discoverFields.LIST_MERGE_FIELDS:
            incoming = value if isinstance(value, list) else [value]
            existing = getattr(block, attr, None) or []
            setattr(block, attr, sorted(set(existing) | set(incoming)))
        else:
            setattr(block, attr, value)

    @staticmethod
    def _pick_new_random_values(pool, count, already_present):
        """Randomly selects up to `count` values from pool that the block
        doesn't already have, without repeats - equivalent to re-rolling a
        duplicate pick until a new one turns up or the pool of unused options
        runs out."""
        already = set(already_present or [])
        candidates = [v for v in pool if v not in already]
        return random.sample(candidates, min(count, len(candidates)))

    @staticmethod
    def _resolve_health_override_range(range_value):
        """Validates an entry's HealthOverrideRange [low, high]. Returns
        (low, high) as ints if usable, or None if it should be ignored:
        missing/blank, not exactly 2 values, either value is 0 or non-numeric,
        or high < low. When low == high, the caller should apply that exact
        value rather than randomizing."""
        if not range_value or len(range_value) != 2:
            return None
        low, high = range_value
        try:
            low, high = int(low), int(high)
        except (TypeError, ValueError):
            return None
        if low == 0 or high == 0:
            return None
        if high < low:
            return None
        return (low, high)

    @staticmethod
    def _run_static_modification_tier(blocks, map_data, filter_field):
        """Shared engine for the ClassArchetype/SubType/Type -> static
        modifications tiers (1, 3, 5). map_data is keyed by the filter phrase
        for filter_field (matched via that field's update_by_* predicate);
        each entry's ApplyStats (Modification fields only) is applied to
        every still-open, matching block. A block is open when LockBlock and
        LockStaticModifications are both False (corpse blocks are always
        attempted). These tiers never set LockStaticModifications themselves
        - only monster_archetype_to_static_modifications_and_info does -
        so a block can pick up a Class-, SubType-, and Type-level match all
        in the same run; they only respect a lock already set elsewhere."""
        predicate = getattr(discoverFields, discoverFields._FILTER_METHOD_NAMES[filter_field])

        for entry_key, entry in map_data.items():
            apply_stats = entry.get("ApplyStats") or {}
            if not apply_stats:
                continue

            for block in blocks:
                if block.lock_block:
                    continue
                if not block.corpse and block.lock_static_modifications:
                    continue
                if not predicate(block, entry_key):
                    continue

                for field, value in apply_stats.items():
                    if field not in discoverFields.MODIFICATION_FIELDS:
                        continue
                    if block.corpse and field in MonsterStatBlock.CORPSE_EXCLUDED_FIELDS:
                        continue
                    discoverFields._set_field(block, field, value)

        return blocks

    @staticmethod
    def _run_random_modification_tier(blocks, map_data, filter_field):
        """Shared engine for the ClassArchetype/SubType -> random modifications
        tiers (2, 4). Same shape as _run_static_modification_tier, but for
        RandomPassives/RandomSpells/HealthOverrideRange, gated by
        LockRandomModifications, and skips corpse blocks outright since every
        randomization output field is corpse-excluded. Like the static tiers,
        these never set LockRandomModifications themselves - only
        monster_archetype_to_random_modifications does."""
        predicate = getattr(discoverFields, discoverFields._FILTER_METHOD_NAMES[filter_field])

        for entry_key, entry in map_data.items():
            random_passives = entry.get("RandomPassives") or []
            random_passive_count = entry.get("RandomPassiveCount", 0) or 0
            random_spells = entry.get("RandomSpells") or []
            random_spell_count = entry.get("RandomSpellCount", 0) or 0
            health_override_range = discoverFields._resolve_health_override_range(
                entry.get("HealthOverrideRange")
            )
            has_randomization = bool(
                (random_passives and random_passive_count > 0)
                or (random_spells and random_spell_count > 0)
                or health_override_range is not None
            )
            if not has_randomization:
                continue

            for block in blocks:
                if block.lock_block or block.corpse:
                    continue
                if block.lock_random_modifications:
                    continue
                if not predicate(block, entry_key):
                    continue

                if health_override_range is not None:
                    low, high = health_override_range
                    resolved = low if low == high else random.randint(low, high)
                    block.health_override = resolved
                    if not block.original_health:
                        block.original_health = resolved

                if random_passives and random_passive_count > 0:
                    chosen = discoverFields._pick_new_random_values(
                        random_passives, random_passive_count, block.passives_to_add
                    )
                    block.passives_to_add = sorted(set(block.passives_to_add) | set(chosen))

                if random_spells and random_spell_count > 0:
                    chosen = discoverFields._pick_new_random_values(
                        random_spells, random_spell_count, block.spells_to_add
                    )
                    block.spells_to_add = sorted(set(block.spells_to_add) | set(chosen))

        return blocks

    # ── Tier 1-2: ClassArchetype ────────────────────────────────────────────

    @staticmethod
    def class_archetype_to_static_modifications(blocks):
        """Tier 1 (highest priority): maps/class_archetype_static_modifications_map.json,
        keyed by ClassArchetype phrase -> ApplyStats. Does not set
        LockStaticModifications - a block can still pick up SubType/Type
        matches later in the same run."""
        map_data = discoverFields._load_map("class_archetype_static_modifications_map.json")
        return discoverFields._run_static_modification_tier(blocks, map_data, "ClassArchetype")

    @staticmethod
    def class_archetype_to_random_modifications(blocks):
        """Tier 2: maps/class_archetype_random_modifications_map.json, keyed by
        ClassArchetype phrase -> RandomPassives/RandomSpells/HealthOverrideRange.
        Does not set LockRandomModifications."""
        map_data = discoverFields._load_map("class_archetype_random_modifications_map.json")
        return discoverFields._run_random_modification_tier(blocks, map_data, "ClassArchetype")

    # ── Tier 3-4: SubType ────────────────────────────────────────────────────

    @staticmethod
    def subtype_to_static_modifications(blocks):
        """Tier 3: maps/subtype_static_modifications_map.json, keyed by SubType
        phrase -> ApplyStats. Does not set LockStaticModifications."""
        map_data = discoverFields._load_map("subtype_static_modifications_map.json")
        return discoverFields._run_static_modification_tier(blocks, map_data, "SubType")

    @staticmethod
    def subtype_to_random_modifications(blocks):
        """Tier 4: maps/subtype_random_modifications_map.json, keyed by SubType
        phrase -> RandomPassives/RandomSpells/HealthOverrideRange. Does not
        set LockRandomModifications."""
        map_data = discoverFields._load_map("subtype_random_modifications_map.json")
        return discoverFields._run_random_modification_tier(blocks, map_data, "SubType")

    # ── Tier 5: Type ─────────────────────────────────────────────────────────

    @staticmethod
    def type_to_static_modifications(blocks):
        """Tier 5: maps/type_static_modifications_map.json, keyed by Type ->
        ApplyStats. No random counterpart - very limited use cases at the Type
        level, but the map exists for the rare case that needs one. Does not
        set LockStaticModifications."""
        map_data = discoverFields._load_map("type_static_modifications_map.json")
        return discoverFields._run_static_modification_tier(blocks, map_data, "Type")

    # ── MatchCombo helpers (Tier 6-7, handle_map.json) ──────────────────────

    @staticmethod
    def _is_valid_combo_value(value):
        """A MatchCombo value must be a bool, a non-blank string, or an int/float."""
        if isinstance(value, bool):
            return True
        if isinstance(value, (int, float)):
            return True
        if isinstance(value, str):
            return value.strip() != ""
        return False

    @staticmethod
    def _combo_matches_block(combo, block):
        """A MatchCombo is satisfied when every valid field/value pair in it is
        contained (case-insensitive) within the same field on the block.
        Blank field names, blank/None values, list-valued fields, and
        HealthOverride are never valid and are skipped outright. A combo left
        with zero valid pairs after filtering (e.g. an empty dict, or one made
        up entirely of blanks) never matches anything - it would otherwise
        match every block."""
        valid_pairs = 0
        for field, expected_value in combo.items():
            if not field or field in discoverFields.INVALID_COMBO_FIELDS:
                continue
            if not discoverFields._is_valid_combo_value(expected_value):
                continue
            valid_pairs += 1

            attr = discoverFields.FIELD_ATTR_MAP.get(field, field)
            actual_value = getattr(block, attr, None)
            if actual_value is None:
                return False
            if str(expected_value).lower() not in str(actual_value).lower():
                return False
        return valid_pairs > 0

    # ── Tier 6-7: MonsterArchetype ───────────────────────────────────────────

    @staticmethod
    def monster_archetype_to_static_modifications_and_info(blocks, override_maps=None):
        """Tier 6: applies handle_map.json's ApplyStats to blocks matching a
        MatchCombos entry. The only tier allowed to write Information fields
        (ArmorClass/OriginalHealth/Level/Notes) alongside Modification fields
        - Information sub-fields are additionally gated per-field by
        LockInformation, independent of the block-level LockStaticModifications
        gate. LockBlock is always respected. LockStaticModifications gates
        whether a block is even attempted (corpse blocks are always attempted,
        since their excluded fields are filtered out per-field anyway, but
        never get the lock set). Sets LockStaticModifications on a match
        unless the entry's SetApplied is False. Listing an entry's key in
        override_maps ignores LockStaticModifications for that entry, forcing
        a full re-application."""
        override_maps = override_maps or []
        handle_map = discoverFields._load_map("handle_map.json")
        matched_guids = set()

        for entry_key, entry in handle_map.items():
            match_combos = entry.get("MatchCombos", [])
            if not match_combos:
                continue
            apply_stats = entry.get("ApplyStats", {})
            if not apply_stats:
                continue
            entry_overridden = entry_key in override_maps
            set_applied = entry.get("SetApplied", True)

            for block in blocks:
                if block.lock_block:
                    continue
                if not block.corpse and block.lock_static_modifications and not entry_overridden:
                    continue
                if not any(discoverFields._combo_matches_block(combo, block) for combo in match_combos):
                    continue

                applied_anything = False
                for field, value in apply_stats.items():
                    is_modification = field in discoverFields.MODIFICATION_FIELDS
                    is_information = field in discoverFields.INFORMATION_FIELDS
                    if not is_modification and not is_information:
                        continue
                    if block.corpse and field in MonsterStatBlock.CORPSE_EXCLUDED_FIELDS:
                        continue
                    if is_information and block.lock_information:
                        continue
                    discoverFields._set_field(block, field, value)
                    applied_anything = True

                if applied_anything and set_applied and not block.corpse:
                    matched_guids.add(block.full_guid)

        for block in blocks:
            if block.full_guid in matched_guids:
                block.lock_static_modifications = True

        return blocks

    @staticmethod
    def monster_archetype_to_random_modifications(blocks, override_maps=None):
        """Tier 7: applies handle_map.json's RandomPassives/RandomSpells/
        HealthOverrideRange to blocks matching a MatchCombos entry. Same data
        as tier 6, but a separate pass gated by LockRandomModifications, and
        never touches corpse blocks (every randomization output field is
        corpse-excluded). Sets LockRandomModifications on a match unless the
        entry's SetApplied is False. override_maps behaves as in tier 6."""
        override_maps = override_maps or []
        handle_map = discoverFields._load_map("handle_map.json")
        matched_guids = set()

        for entry_key, entry in handle_map.items():
            match_combos = entry.get("MatchCombos", [])
            if not match_combos:
                continue
            random_passives = entry.get("RandomPassives") or []
            random_passive_count = entry.get("RandomPassiveCount", 0) or 0
            random_spells = entry.get("RandomSpells") or []
            random_spell_count = entry.get("RandomSpellCount", 0) or 0
            health_override_range = discoverFields._resolve_health_override_range(
                entry.get("HealthOverrideRange")
            )
            has_randomization = bool(
                (random_passives and random_passive_count > 0)
                or (random_spells and random_spell_count > 0)
                or health_override_range is not None
            )
            if not has_randomization:
                continue
            entry_overridden = entry_key in override_maps
            set_applied = entry.get("SetApplied", True)

            for block in blocks:
                if block.lock_block or block.corpse:
                    continue
                if block.lock_random_modifications and not entry_overridden:
                    continue
                if not any(discoverFields._combo_matches_block(combo, block) for combo in match_combos):
                    continue

                if health_override_range is not None:
                    low, high = health_override_range
                    resolved = low if low == high else random.randint(low, high)
                    block.health_override = resolved
                    if not block.original_health:
                        block.original_health = resolved

                if random_passives and random_passive_count > 0:
                    chosen = discoverFields._pick_new_random_values(
                        random_passives, random_passive_count, block.passives_to_add
                    )
                    block.passives_to_add = sorted(set(block.passives_to_add) | set(chosen))

                if random_spells and random_spell_count > 0:
                    chosen = discoverFields._pick_new_random_values(
                        random_spells, random_spell_count, block.spells_to_add
                    )
                    block.spells_to_add = sorted(set(block.spells_to_add) | set(chosen))

                if set_applied:
                    matched_guids.add(block.full_guid)

        for block in blocks:
            if block.full_guid in matched_guids:
                block.lock_random_modifications = True

        return blocks

    # ── Orchestrator ─────────────────────────────────────────────────────────

    @staticmethod
    def update_modifications_and_information(blocks, override_maps=None):
        """The single entry point: runs all seven Modification/Information
        tiers against `blocks`, most specific to least specific (ClassArchetype
        -> SubType -> Type -> MonsterArchetype). Each tier only touches blocks
        still unlocked for that tier's update type (LockBlock always wins);
        the MonsterArchetype tiers (6-7) additionally set their own lock on a
        match, so later runs skip a block they've already updated.
        override_maps only applies to the MonsterArchetype tiers - see
        monster_archetype_to_static_modifications_and_info."""
        discoverFields.class_archetype_to_static_modifications(blocks)
        discoverFields.class_archetype_to_random_modifications(blocks)
        discoverFields.subtype_to_static_modifications(blocks)
        discoverFields.subtype_to_random_modifications(blocks)
        discoverFields.type_to_static_modifications(blocks)
        discoverFields.monster_archetype_to_static_modifications_and_info(blocks, override_maps=override_maps)
        discoverFields.monster_archetype_to_random_modifications(blocks, override_maps=override_maps)
        return blocks

    # ── Standalone utility (not part of the tier cascade) ───────────────────

    @staticmethod
    def extract_armor_class_from_notes(blocks):
        """Parses an explicit AC out of Notes text and writes it to ArmorClass.
        Not part of the tier cascade above (it isn't Identifier-driven), but
        still an Information-field write, so it respects LockBlock/
        LockInformation like any other Information update."""
        # Matches: XX AC, AC XX, Armor Class XX, XX Armor Class (no comma in phrase)
        patterns = [
            r"\b(\d+)\s+AC\b",
            r"\bAC\s+(\d+)\b",
            r"\bArmor\s+Class\s+(\d+)\b",
            r"\b(\d+)\s+Armor\s+Class\b",
        ]

        for block in blocks:
            if block.lock_block or block.lock_information:
                continue
            if not block.notes:
                continue
            for pattern in patterns:
                match = re.search(pattern, block.notes, re.IGNORECASE)
                if match:
                    block.armor_class = int(match.group(1))
                    break

    # ── Dry-run reporting ────────────────────────────────────────────────────

    @staticmethod
    def print_dry_run_summary(diffs, blocks):
        locked_count = sum(1 for block in blocks if block.lock_block)

        field_counts = {}
        multiple_count = 0
        for changes in diffs.values():
            has_multiple = False
            for field, (_, new_value) in changes.items():
                field_counts[field] = field_counts.get(field, 0) + 1
                if isinstance(new_value, str) and new_value.startswith("Multiple:"):
                    has_multiple = True
            if has_multiple:
                multiple_count += 1

        static_locked_count = field_counts.pop("LockStaticModifications", 0)
        random_locked_count = field_counts.pop("LockRandomModifications", 0)

        print("---- Dry Run Summary (discoverFields) ----")
        print(f"Blocks loaded: {len(blocks)}")
        print(f"Blocks skipped (LockBlock): {locked_count}")
        print(f"Blocks with at least one field changed: {len(diffs)}")
        print(
            f"Blocks newly locked for static modifications (LockStaticModifications set): {static_locked_count}"
        )
        print(
            f"Blocks newly locked for random modifications (LockRandomModifications set): {random_locked_count}"
        )
        print(f"Blocks with an ambiguous 'Multiple:' match: {multiple_count}")
        if field_counts:
            print("Changes by field:")
            for field, count in sorted(field_counts.items(), key=lambda kv: -kv[1]):
                print(f"  {field}: {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Apply Modification/Information field updates (passives, spells, "
        "health overrides, AC, level, notes) to blocks, driven by their existing "
        "Identifiers and gated by their Block Controls."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing to guid_mapper_master.json. Writes "
        "dryrun/guid_mapper_master_dryrun.json instead and prints a summary.",
    )
    args = parser.parse_args()

    base_dir = os.path.dirname(__file__)
    blocks = MonsterStatBlock.load_from_json_file(
        os.path.join(base_dir, "guid_mapper_master.json")
    )
    blocks = MonsterStatBlock.deduplicate(blocks)
    before_snapshot = MonsterStatBlock.snapshot(blocks)

    # List handle_map.json entry keys here (e.g. ["Mind Flayer"]) to force the
    # MonsterArchetype tiers to re-apply to blocks already locked for that
    # tier. Leave blank for the normal, safe behavior of skipping
    # already-updated blocks.
    override_maps = []
    discoverFields.update_modifications_and_information(blocks, override_maps=override_maps)

    diffs = MonsterStatBlock.diff_from_snapshot(before_snapshot, blocks)

    if args.dry_run:
        discoverFields.print_dry_run_summary(diffs, blocks)
        dryrun_dir = os.path.join(base_dir, "dryrun")
        os.makedirs(dryrun_dir, exist_ok=True)
        dryrun_path = os.path.join(dryrun_dir, "guid_mapper_master_dryrun.json")
        MonsterStatBlock.save_to_json_file(blocks, dryrun_path, archive=False)
        print(f"Dry run preview written to {dryrun_path}")
    elif MonsterStatBlock.confirm_large_change(diffs, blocks):
        MonsterStatBlock.save_to_json_file(
            blocks, os.path.join(base_dir, "guid_mapper_master.json")
        )
        print("Saved to guid_mapper_master.json")
    else:
        print("Aborted - guid_mapper_master.json was not modified.")
