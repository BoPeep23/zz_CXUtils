import argparse
import json
import os
import random
import re
import shutil
from datetime import datetime

from monsterStatBlock import MonsterStatBlock


class discoverFields:
    """Applies Modification and Information field updates to blocks, using
    the Identifiers sanitizeFields.py has already built out as the filter
    criteria, and the Block Controls (Lock* fields) to decide whether a block
    is even eligible for a given kind of update. Never touches Identifiers -
    that's sanitizeFields.py's job."""

    # Maps guid_mapper_master.json / profile_to_modifications_improvements_map.json field names to the
    # corresponding MonsterStatBlock attribute names.
    FIELD_ATTR_MAP = {
        "Handle": "handle",
        "FullGuid": "full_guid",
        "Act": "act",
        "Location": "location",
        "Type": "type",
        "SubType": "subtype",
        "ClassArchetype": "classArchetype",
        "SubclassArchetype": "subclassArchetype",
        "MonsterArchetype": "monsterArchetype",
        "Corpse": "corpse",
        "Notes": "notes",
        "Level": "level",
        "ArmorClass": "armor_class",
        "OriginalHealth": "original_health",
        "HealthOverride": "health_override",
        "PassivesToAdd": "passives_to_add",
        "SpellsToAdd": "spells_to_add",
        "CloneDisplayName": "clone_display_name",
        "CloneTemplateGuid": "clone_template_guid",
        "LockStaticModifications": "lock_static_modifications",
        "LockRandomModifications": "lock_random_modifications",
        "LockInformation": "lock_information",
        "LockBlock": "lock_block",
    }

    # Modification fields (see MonsterStatBlock's field categories): always
    # dynamic, gathered/transformed by generateCombatExtenderBlocks.py.
    MODIFICATION_FIELDS = {
        "HealthOverride",
        "PassivesToAdd",
        "SpellsToAdd",
        "CloneTemplateGuid",
        "CloneDisplayName",
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
        "SubclassArchetype": "update_by_subclass_archetype",
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
        return discoverFields._matches_phrase(
            block.classArchetype, class_archetype_phrase
        )

    @staticmethod
    def update_by_subclass_archetype(block, subclass_archetype_phrase):
        return discoverFields._matches_phrase(
            block.subclassArchetype, subclass_archetype_phrase
        )

    @staticmethod
    def update_by_monster_archetype(block, monster_archetype):
        if not block.monsterArchetype or not monster_archetype:
            return False
        return (
            block.monsterArchetype.strip().lower()
            == str(monster_archetype).strip().lower()
        )

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
    def _split_package(value):
        """Splits a RandomPassives/RandomSpells pool entry on ';' into its
        individual pieces, letting one pool entry "package" multiple
        passives/spells together so a single roll adds all of them. Blank
        pieces are dropped; non-string values pass through unchanged."""
        if not isinstance(value, str):
            return [value]
        return [piece.strip() for piece in value.split(";") if piece.strip()]

    @staticmethod
    def _pick_new_random_values(pool, count, already_present):
        """Randomly selects up to `count` values from pool whose package (see
        _split_package) isn't already fully present, without repeats -
        equivalent to re-rolling a duplicate pick until a new one turns up or
        the pool of unused options runs out. Returns the raw (unsplit) pool
        entries - callers that add the result to a block must expand each via
        _split_package first."""
        already = set(already_present or [])
        candidates = [
            v for v in pool if not set(discoverFields._split_package(v)) <= already
        ]
        return random.sample(candidates, min(count, len(candidates)))

    @staticmethod
    def _apply_random_list_field(block, attr, pool, count):
        """Picks up to `count` new entries from pool and merges their
        expanded pieces into block.<attr> (passives_to_add/spells_to_add),
        deduplicated against what's already there."""
        if not pool or count <= 0:
            return
        existing = getattr(block, attr)
        chosen = discoverFields._pick_new_random_values(pool, count, existing)
        expanded = [
            piece for value in chosen for piece in discoverFields._split_package(value)
        ]
        setattr(block, attr, sorted(set(existing) | set(expanded)))

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
        predicate = getattr(
            discoverFields, discoverFields._FILTER_METHOD_NAMES[filter_field]
        )

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
                    if (
                        block.corpse
                        and field in MonsterStatBlock.CORPSE_EXCLUDED_FIELDS
                    ):
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
        predicate = getattr(
            discoverFields, discoverFields._FILTER_METHOD_NAMES[filter_field]
        )

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

                discoverFields._apply_random_list_field(
                    block, "passives_to_add", random_passives, random_passive_count
                )
                discoverFields._apply_random_list_field(
                    block, "spells_to_add", random_spells, random_spell_count
                )

        return blocks

    # ── Tier 1-2: ClassArchetype ────────────────────────────────────────────

    @staticmethod
    def class_archetype_to_static_modifications(blocks):
        """Tier 1 (highest priority): maps/class_archetype_static_modifications_map.json,
        keyed by ClassArchetype phrase -> ApplyStats. Does not set
        LockStaticModifications - a block can still pick up SubType/Type
        matches later in the same run."""
        map_data = discoverFields._load_map(
            "class_archetype_static_modifications_map.json"
        )
        return discoverFields._run_static_modification_tier(
            blocks, map_data, "ClassArchetype"
        )

    @staticmethod
    def class_archetype_to_random_modifications(blocks):
        """Tier 2: maps/class_archetype_random_modifications_map.json, keyed by
        ClassArchetype phrase -> RandomPassives/RandomSpells/HealthOverrideRange.
        Does not set LockRandomModifications."""
        map_data = discoverFields._load_map(
            "class_archetype_random_modifications_map.json"
        )
        return discoverFields._run_random_modification_tier(
            blocks, map_data, "ClassArchetype"
        )

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

    # ── MatchCombo helpers (Tier 6-7, discovery maps) ───────────────────────

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
        match every block.

        A field name prefixed with '!' (e.g. "!Act": "1") negates the check:
        the combo requires that field NOT contain the given value. A block
        with no value at all for a negated field trivially satisfies it."""
        valid_pairs = 0
        for raw_field, expected_value in combo.items():
            negate = raw_field.startswith("!")
            field = raw_field[1:] if negate else raw_field
            if not field or field in discoverFields.INVALID_COMBO_FIELDS:
                continue
            if not discoverFields._is_valid_combo_value(expected_value):
                continue
            valid_pairs += 1

            attr = discoverFields.FIELD_ATTR_MAP.get(field, field)
            actual_value = getattr(block, attr, None)
            if negate:
                if actual_value is not None and str(expected_value).lower() in str(
                    actual_value
                ).lower():
                    return False
            else:
                if actual_value is None:
                    return False
                if str(expected_value).lower() not in str(actual_value).lower():
                    return False
        return valid_pairs > 0

    # ── Tier 6-7: MonsterArchetype (discovery maps) ──────────────────────────

    @staticmethod
    def monster_archetype_to_static_modifications_and_info(blocks, map_data):
        """Tier 6: applies a discovery map's ApplyStaticStats to blocks
        matching a MatchCombos entry. `map_data` is a discovery map already
        loaded from maps/discovery_maps/ (see apply_discovery_map) - this
        method itself never touches the filesystem. The only tier allowed to
        write Information fields (ArmorClass/OriginalHealth/Level/Notes)
        alongside Modification fields - Information sub-fields are
        additionally gated per-field by LockInformation, independent of the
        block-level LockStaticModifications gate. LockBlock is always
        respected. LockStaticModifications gates whether a block is even
        attempted (corpse blocks are always attempted, since their excluded
        fields are filtered out per-field anyway, but never get the lock
        set). Sets LockStaticModifications on a match unless
        ApplyStaticStats.SetStaticLock is False. ApplyStaticStats.OverrideStaticLock
        ignores LockStaticModifications for that entry, forcing a full
        re-application."""
        matched_guids = set()

        for entry_key, entry in map_data.items():
            if entry_key == "dateApplied":
                continue
            match_combos = entry.get("MatchCombos", [])
            if not match_combos:
                continue
            static_stats = entry.get("ApplyStaticStats") or {}
            if not static_stats:
                continue
            override_static_lock = static_stats.get("OverrideStaticLock", False)
            set_static_lock = static_stats.get("SetStaticLock", True)

            for block in blocks:
                if block.lock_block:
                    continue
                if (
                    not block.corpse
                    and block.lock_static_modifications
                    and not override_static_lock
                ):
                    continue
                if not any(
                    discoverFields._combo_matches_block(combo, block)
                    for combo in match_combos
                ):
                    continue

                applied_anything = False
                for field, value in static_stats.items():
                    is_modification = field in discoverFields.MODIFICATION_FIELDS
                    is_information = field in discoverFields.INFORMATION_FIELDS
                    if not is_modification and not is_information:
                        continue
                    if (
                        block.corpse
                        and field in MonsterStatBlock.CORPSE_EXCLUDED_FIELDS
                    ):
                        continue
                    if is_information and block.lock_information:
                        continue
                    discoverFields._set_field(block, field, value)
                    applied_anything = True

                if applied_anything and set_static_lock and not block.corpse:
                    matched_guids.add(block.full_guid)

        for block in blocks:
            if block.full_guid in matched_guids:
                block.lock_static_modifications = True

        return blocks

    @staticmethod
    def monster_archetype_to_random_modifications(blocks, map_data):
        """Tier 7: applies a discovery map's ApplyRandomStats
        (RandomPassives/RandomSpells/HealthOverrideRange) to blocks matching a
        MatchCombos entry. Same data/`map_data` as tier 6, but a separate pass
        gated by LockRandomModifications, and never touches corpse blocks
        (every randomization output field is corpse-excluded). Sets
        LockRandomModifications on a match unless ApplyRandomStats.SetRandomLock
        is False. ApplyRandomStats.OverrideRandomLock ignores
        LockRandomModifications for that entry, forcing a full re-application."""
        matched_guids = set()

        for entry_key, entry in map_data.items():
            if entry_key == "dateApplied":
                continue
            match_combos = entry.get("MatchCombos", [])
            if not match_combos:
                continue
            random_stats = entry.get("ApplyRandomStats") or {}
            random_passives = random_stats.get("RandomPassives") or []
            random_passive_count = random_stats.get("RandomPassiveCount", 0) or 0
            random_spells = random_stats.get("RandomSpells") or []
            random_spell_count = random_stats.get("RandomSpellCount", 0) or 0
            health_override_range = discoverFields._resolve_health_override_range(
                random_stats.get("HealthOverrideRange")
            )
            has_randomization = bool(
                (random_passives and random_passive_count > 0)
                or (random_spells and random_spell_count > 0)
                or health_override_range is not None
            )
            if not has_randomization:
                continue
            override_random_lock = random_stats.get("OverrideRandomLock", False)
            set_random_lock = random_stats.get("SetRandomLock", True)

            for block in blocks:
                if block.lock_block or block.corpse:
                    continue
                if block.lock_random_modifications and not override_random_lock:
                    continue
                if not any(
                    discoverFields._combo_matches_block(combo, block)
                    for combo in match_combos
                ):
                    continue

                if health_override_range is not None:
                    low, high = health_override_range
                    resolved = low if low == high else random.randint(low, high)
                    block.health_override = resolved
                    if not block.original_health:
                        block.original_health = resolved

                discoverFields._apply_random_list_field(
                    block, "passives_to_add", random_passives, random_passive_count
                )
                discoverFields._apply_random_list_field(
                    block, "spells_to_add", random_spells, random_spell_count
                )

                if set_random_lock:
                    matched_guids.add(block.full_guid)

        for block in blocks:
            if block.full_guid in matched_guids:
                block.lock_random_modifications = True

        return blocks

    # ── Discovery maps (Tier 6-7 driver) ─────────────────────────────────────

    DISCOVERY_MAPS_DIR = "discovery_maps"
    ARCHIVE_DISCOVERY_MAPS_DIR = "archive_discovery_maps"

    @staticmethod
    def _stamp_date_applied(map_data):
        """Returns a copy of map_data with a 'dateApplied' key inserted first
        (dict insertion order = JSON key order, so it lands at the top of the
        written file), formatted as 'Weekday MM/DD/YY HH:MM'."""
        now = datetime.now()
        stamp = now.strftime("%a %m/%d/%y %H:%M")
        return {"dateApplied": stamp, **map_data}

    @staticmethod
    def apply_discovery_map(blocks, filename, dry_run=False):
        """Loads a MatchCombos map (any .json file shaped like the old
        profile_to_modifications_improvements_map.json) and runs it through
        tiers 6-7 against `blocks` - the same engine that used to be
        hardcoded to always read that one file. A bare filename (no path
        separators) resolves against maps/discovery_maps/; anything else
        (relative or absolute) is used as given, so this works on any .json
        map regardless of where it lives - it doesn't have to already be in
        discovery_maps/. This is meant for one-off application: once run,
        the map is stamped with a top-level dateApplied (Weekday MM/DD/YY
        HH:MM), written back to its original location, then moved into
        maps/archive_discovery_maps/ under its own filename, so a glance at
        that folder shows what's already been applied and when. In
        --dry-run mode the map's effects still apply to `blocks` in memory
        (so the diff/summary reflects them), but the source file is left
        untouched - nothing is stamped, moved, or archived."""
        if not filename.lower().endswith(".json"):
            raise ValueError(
                f"apply_discovery_map only accepts .json files, got: {filename}"
            )

        base_dir = os.path.dirname(__file__)
        if os.path.basename(filename) == filename:
            map_path = os.path.join(
                base_dir, "maps", discoverFields.DISCOVERY_MAPS_DIR, filename
            )
        else:
            map_path = filename

        with open(map_path, "r") as f:
            map_data = json.load(f)

        discoverFields.monster_archetype_to_static_modifications_and_info(
            blocks, map_data
        )
        discoverFields.monster_archetype_to_random_modifications(blocks, map_data)

        if dry_run:
            return blocks

        stamped = discoverFields._stamp_date_applied(map_data)
        with open(map_path, "w") as f:
            json.dump(stamped, f, indent=4)

        archive_dir = os.path.join(
            base_dir, "maps", discoverFields.ARCHIVE_DISCOVERY_MAPS_DIR
        )
        os.makedirs(archive_dir, exist_ok=True)
        stem, ext = os.path.splitext(os.path.basename(map_path))
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        shutil.move(
            map_path, os.path.join(archive_dir, f"{stem}_{timestamp}{ext}")
        )

        return blocks

    # ── Orchestrator ─────────────────────────────────────────────────────────

    @staticmethod
    def update_modifications_and_information(blocks):
        """Runs the five permanent, automatic Modification/Information tiers
        against `blocks`, most specific to least specific (ClassArchetype ->
        SubType -> Type). Each tier only touches blocks still unlocked for
        that tier's update type (LockBlock always wins). These tiers are
        driven by the maps/ folder's static identifier maps, which are always
        in effect. One-off MonsterArchetype/MatchCombo updates - including
        race traits (maps/discovery_maps/races.json) - are no longer part of
        this automatic pass; see apply_discovery_map for applying
        maps/discovery_maps/ entries explicitly."""
        discoverFields.class_archetype_to_static_modifications(blocks)
        discoverFields.class_archetype_to_random_modifications(blocks)
        discoverFields.subtype_to_static_modifications(blocks)
        discoverFields.subtype_to_random_modifications(blocks)
        discoverFields.type_to_static_modifications(blocks)
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
        "dryrun/guid_mapper_master_dryrun.json instead and prints a summary. Any "
        "--discover map is also left untouched in maps/discovery_maps/ (not "
        "stamped or archived).",
    )
    parser.add_argument(
        "--discover",
        nargs="*",
        default=[],
        metavar="FILENAME",
        help="One or more MatchCombos map filenames in maps/discovery_maps/ to "
        "apply after the automatic tiers. Each is stamped with dateApplied and "
        "moved to maps/archive_discovery_maps/ once applied (skipped in --dry-run).",
    )
    args = parser.parse_args()

    base_dir = os.path.dirname(__file__)
    blocks = MonsterStatBlock.load_from_json_file(
        os.path.join(base_dir, "guid_mapper_master.json")
    )
    blocks = MonsterStatBlock.deduplicate(blocks)
    before_snapshot = MonsterStatBlock.snapshot(blocks)

    discoverFields.update_modifications_and_information(blocks)

    for filename in args.discover:
        discoverFields.apply_discovery_map(blocks, filename, dry_run=args.dry_run)

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
