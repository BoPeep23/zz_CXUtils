import argparse
import json
import os
import random
import re

from monsterStatBlock import MonsterStatBlock


class discoverFields:

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
        "ArmorClass": "armor_class",
        "HealthOverride": "health_override",
        "OriginalHealth": "original_health",
        "Level": "level",
        "PassivesToAdd": "passives_to_add",
        "SpellsToAdd": "spells_to_add",
        "CloneTemplateGuid": "clone_template_guid",
        "CloneDisplayName": "clone_display_name",
        "Corpse": "corpse",
        "Notes": "notes",
        "MapApplied": "map_applied",
        "LockBlock": "lock_block",
        "RandomizationApplied": "randomization_applied",
    }

    # ApplyStats fields that should be merged into the block's existing list
    # (deduplicated) instead of overwriting it outright.
    LIST_MERGE_FIELDS = {"PassivesToAdd", "SpellsToAdd"}

    # Fields that can never be used in a MatchCombo: list-valued fields can't be
    # meaningfully substring-matched, and HealthOverride is too easy to match
    # unintended blocks by accident (e.g. "10" inside "100").
    INVALID_COMBO_FIELDS = LIST_MERGE_FIELDS | {"HealthOverride"}

    @staticmethod
    def _flatten_mapping_values(substring_mapping):
        return [
            sub.lower()
            for substrings in substring_mapping.values()
            for sub in substrings
        ]

    @staticmethod
    def _matches_with_rules(target, sub):
        """Match a substring against target using rules:
        - If the substring ends with '!', require a whole-word exact match for the phrase (word boundaries).
        - Otherwise, use simple containment (substring in target).
        Both inputs are expected to be lowercase when called from the callers below.
        """
        if not target or not sub:
            return False

        s = sub.lower()
        if s.endswith("!"):
            phrase = re.escape(s[:-1])
            pattern = r"(?<!\w)" + phrase + r"(?!\w)"
            return re.search(pattern, target) is not None
        return s in target

    @staticmethod
    def update_class_archetype_based_on_notes(blocks):
        base_dir = os.path.dirname(__file__)
        map_dir = os.path.join(base_dir, "maps")
        with open(os.path.join(map_dir, "class_archetype_map.json"), "r") as f:
            substring_mapping = json.load(f)
        mapped_substrings = discoverFields._flatten_mapping_values(substring_mapping)

        for block in blocks:
            if block.lock_block:
                continue
            if not block.classArchetype or block.classArchetype == "":
                notes_lower = block.notes.lower() if block.notes else ""
                handle = block.handle.lower() if block.handle else ""
                type = block.type.lower() if block.type else ""
                subtype = block.subtype.lower() if block.subtype else ""
                full_guid = block.full_guid.lower() if block.full_guid else ""

                notes_lower_match = False
                type_match = False
                subtype_match = False
                handle_match = False
                full_guid_match = False

                if any(
                    discoverFields._matches_with_rules(notes_lower, sub)
                    for sub in mapped_substrings
                ):
                    notes_lower_match = True
                if any(
                    discoverFields._matches_with_rules(handle, sub)
                    for sub in mapped_substrings
                ):
                    handle_match = True
                if any(
                    discoverFields._matches_with_rules(type, sub)
                    for sub in mapped_substrings
                ):
                    type_match = True
                if any(
                    discoverFields._matches_with_rules(subtype, sub)
                    for sub in mapped_substrings
                ):
                    subtype_match = True
                if any(
                    discoverFields._matches_with_rules(full_guid, sub)
                    for sub in mapped_substrings
                ):
                    full_guid_match = True

                matched_class_archetypes = []

                if type_match:
                    for archetype, substrings in substring_mapping.items():
                        if any(
                            discoverFields._matches_with_rules(type, sub)
                            for sub in substrings
                        ):
                            matched_class_archetypes.append(archetype.title())

                if full_guid_match:
                    for archetype, substrings in substring_mapping.items():
                        if any(
                            discoverFields._matches_with_rules(full_guid, sub)
                            for sub in substrings
                        ):
                            matched_class_archetypes.append(archetype.title())

                if subtype_match:
                    for archetype, substrings in substring_mapping.items():
                        if any(
                            discoverFields._matches_with_rules(subtype, sub)
                            for sub in substrings
                        ):
                            matched_class_archetypes.append(archetype.title())

                if handle_match:
                    for archetype, substrings in substring_mapping.items():
                        if any(
                            discoverFields._matches_with_rules(handle, sub)
                            for sub in substrings
                        ):
                            matched_class_archetypes.append(archetype.title())

                if notes_lower_match:
                    for archetype, substrings in substring_mapping.items():
                        if any(
                            discoverFields._matches_with_rules(notes_lower, sub)
                            for sub in substrings
                        ):
                            matched_class_archetypes.append(archetype.title())

                matched_class_archetypes = list(
                    set(matched_class_archetypes)
                )  # Remove duplicates

                if len(matched_class_archetypes) == 0:
                    continue
                elif len(matched_class_archetypes) == 1:
                    block.classArchetype = matched_class_archetypes[0]
                else:
                    print(
                        f"Multiple class archetype matches found for {block.full_guid}: {matched_class_archetypes}. Setting archetype to 'Multiple'."
                    )
                    block.classArchetype = (
                        f"Multiple: {', '.join(matched_class_archetypes)}"
                    )

    @staticmethod
    def update_monster_archetype_based_on_handle(blocks):
        base_dir = os.path.dirname(__file__)
        map_dir = os.path.join(base_dir, "maps")
        with open(os.path.join(map_dir, "monster_archetype_map.json"), "r") as f:
            object_mapping = json.load(f)

        with open(os.path.join(base_dir, "output.txt"), "w", encoding="utf-8") as of:
            of.write("Starting output file.")

            for block in blocks:
                if block.lock_block:
                    continue
                if not block.monsterArchetype or block.monsterArchetype == "":
                    handle = block.handle.lower() if block.handle else ""
                    of.write(f"\n\nCurrent handle = {handle}")
                    matched_archetypes = []

                    for archetype in object_mapping.keys():
                        of.write(f"\nCurrent archetype = {archetype.lower()}")
                        of.write(
                            f"\n{archetype.lower()} in {handle.lower()}? = {archetype.lower() in handle.lower()}"
                        )
                        if archetype.lower() in handle.lower():
                            # For single-word archetypes with oneWordMatch=True
                            if object_mapping[archetype].get("oneWordMatch", False):
                                matched_archetypes.append(archetype)
                                of.write(
                                    f"\nAppending {archetype} to matched_archetypes (oneWordMatch)."
                                )
                            # For multi-word archetypes (contain space or underscore) - match as substring
                            elif " " in archetype or "_" in archetype:
                                matched_archetypes.append(archetype)
                                of.write(
                                    f"\nAppending {archetype} to matched_archetypes (multi-word substring)."
                                )
                            # For word-boundary matching when useLongerMatches=True
                            elif object_mapping[archetype].get(
                                "useLongerMatches", False
                            ):
                                eachWordOfHandle = re.split(r"[_\s]+", handle)
                                if any(
                                    word == archetype.lower()
                                    for word in eachWordOfHandle
                                ):
                                    matched_archetypes.append(archetype)
                                    of.write(
                                        f"\nAppending {archetype} to matched_archetypes (useLongerMatches)."
                                    )

                    if len(matched_archetypes) > 1:
                        of.write(
                            f"\nMultiple monster archetype matches found for {block.full_guid}: {matched_archetypes}."
                        )
                        for archetype in matched_archetypes:
                            useLongerMatches = object_mapping[archetype].get(
                                "useLongerMatches", False
                            )
                            if useLongerMatches:
                                continue
                            else:
                                block.monsterArchetype = archetype.title()
                                break

                    elif len(matched_archetypes) == 1:
                        block.monsterArchetype = matched_archetypes[0]

            of.close()

    @staticmethod
    def update_subtype_based_on_notes(blocks):
        base_dir = os.path.dirname(__file__)
        map_dir = os.path.join(base_dir, "maps")
        with open(os.path.join(map_dir, "subtype_map.json"), "r") as f:
            substring_mapping = json.load(f)
        mapped_substrings = discoverFields._flatten_mapping_values(substring_mapping)

        for block in blocks:
            if block.lock_block:
                continue
            if not block.subtype or block.subtype == "":
                notes_lower = block.notes.lower() if block.notes else ""
                handle = block.handle.lower() if block.handle else ""
                full_guid = block.full_guid.lower() if block.full_guid else ""

                notes_lower_match = False
                handle_match = False
                full_guid_match = False

                if any(
                    discoverFields._matches_with_rules(notes_lower, sub)
                    for sub in mapped_substrings
                ):
                    notes_lower_match = True
                if any(
                    discoverFields._matches_with_rules(handle, sub)
                    for sub in mapped_substrings
                ):
                    handle_match = True
                if any(
                    discoverFields._matches_with_rules(full_guid, sub)
                    for sub in mapped_substrings
                ):
                    full_guid_match = True

                matched_subtypes = []

                if handle_match:
                    for subtype, substrings in substring_mapping.items():
                        if any(
                            discoverFields._matches_with_rules(handle, sub)
                            for sub in substrings
                        ):
                            matched_subtypes.append(subtype.title())

                elif notes_lower_match:
                    for subtype, substrings in substring_mapping.items():
                        if any(
                            discoverFields._matches_with_rules(notes_lower, sub)
                            for sub in substrings
                        ):
                            matched_subtypes.append(subtype.title())

                elif full_guid_match:
                    for subtype, substrings in substring_mapping.items():
                        if any(
                            discoverFields._matches_with_rules(full_guid, sub)
                            for sub in substrings
                        ):
                            matched_subtypes.append(subtype.title())

                matched_subtypes = list(set(matched_subtypes))  # Remove duplicates

                if len(matched_subtypes) == 0:
                    continue
                elif len(matched_subtypes) == 1:
                    block.subtype = matched_subtypes[0]
                else:
                    print(
                        f"Multiple subtype matches found for {block.full_guid}: {matched_subtypes}. Setting subtype to 'Multiple'."
                    )
                    block.subtype = f"Multiple: {', '.join(matched_subtypes)}"

    @staticmethod
    def update_type_based_on_notes(blocks):
        base_dir = os.path.dirname(__file__)
        map_dir = os.path.join(base_dir, "maps")
        with open(os.path.join(map_dir, "type_map.json"), "r") as f:
            substring_mapping = json.load(f)
        mapped_substrings = discoverFields._flatten_mapping_values(substring_mapping)

        for block in blocks:
            if block.lock_block:
                continue
            if hasattr(block, "type") and block.type not in [
                "Aberration",
                "Beast",
                "Celestial",
                "Construct",
                "Dragon",
                "Elemental",
                "Fey",
                "Fiend",
                "Giant",
                "Humanoid",
                "Monstrosity",
                "Object",
                "Ooze",
                "Plant",
                "Undead",
            ]:
                block.type = ""

        for block in blocks:
            if block.lock_block:
                continue
            if not block.type or block.type == "":
                notes_lower = block.notes.lower() if block.notes else ""
                handle = block.handle.lower() if block.handle else ""
                subtype = block.subtype.lower() if block.subtype else ""

                notes_lower_match = False
                handle_match = False
                subtype_match = False

                if any(
                    discoverFields._matches_with_rules(notes_lower, sub)
                    for sub in mapped_substrings
                ):
                    notes_lower_match = True
                if any(
                    discoverFields._matches_with_rules(handle, sub)
                    for sub in mapped_substrings
                ):
                    handle_match = True
                if any(
                    discoverFields._matches_with_rules(subtype, sub)
                    for sub in mapped_substrings
                ):
                    subtype_match = True

                matched_types = []

                if handle_match:
                    for type_, substrings in substring_mapping.items():
                        if any(
                            discoverFields._matches_with_rules(handle, sub)
                            for sub in substrings
                        ):
                            matched_types.append(type_.title())

                if notes_lower_match:
                    for type_, substrings in substring_mapping.items():
                        if any(
                            discoverFields._matches_with_rules(notes_lower, sub)
                            for sub in substrings
                        ):
                            matched_types.append(type_.title())

                if subtype_match:
                    for type_, substrings in substring_mapping.items():
                        if any(
                            discoverFields._matches_with_rules(subtype, sub)
                            for sub in substrings
                        ):
                            matched_types.append(type_.title())

                matched_types = list(set(matched_types))  # Remove duplicates

                if len(matched_types) == 0:
                    continue
                elif len(matched_types) == 1:
                    block.type = matched_types[0]
                else:
                    print(
                        f"Multiple type matches found for {block.full_guid}: {matched_types}. Setting type to 'Multiple'."
                    )
                    block.type = f"Multiple: {', '.join(matched_types)}"

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
    def apply_handle_map(blocks, override_maps=None):
        """Applies handle_map.json's ApplyStats and randomization to matching
        blocks. LockBlock is always respected.

        MapApplied and RandomizationApplied are independent gates covering
        independent parts of an entry:
          - MapApplied gates/tracks ApplyStats (the fixed, non-random fields).
          - RandomizationApplied gates/tracks RandomPassives/RandomSpells/
            HealthOverrideRange (see below).
        A block already flagged for one is skipped only for that part; the
        other still applies if the entry defines it and the block matches.
        E.g. an entry with only RandomPassives (no ApplyStats) will set
        RandomizationApplied=True on a match but leave MapApplied False.
        Listing an entry's key in override_maps ignores BOTH flags for that
        entry, forcing a full re-application (including a fresh reroll of any
        randomization) even on blocks already marked for it.

        Each entry may define, alongside ApplyStats/MatchCombos:
          RandomPassives / RandomPassiveCount - a pool of passives and how
            many to randomly draw (independently per matched block).
          RandomSpells / RandomSpellCount - same, for spells.
          HealthOverrideRange - [low, high]; when valid (see
            _resolve_health_override_range), overrides ApplyStats.HealthOverride
            entirely for this entry - applying the exact value if low == high,
            or an independent random int in [low, high] per matched block.
          SetApplied - defaults to True (normal behavior: whatever this entry
            actually applies to a block sets that part's flag, same as
            always). Set to False for mass/universal entries (e.g. "give
            every Humanoid Projectile_Jump") that should never mark a block
            as done - a match still applies normally, but MapApplied/
            RandomizationApplied are left exactly as they were, so later
            entries in this same run (and this same entry, on future runs)
            are still free to match and apply to that block.

        Corpse=True blocks are static scenery: any field in
        MonsterStatBlock.CORPSE_EXCLUDED_FIELDS (ClassArchetype, ArmorClass,
        HealthOverride, OriginalHealth, Level, PassivesToAdd, SpellsToAdd,
        MapApplied, RandomizationApplied) is skipped even if a matched
        entry's ApplyStats includes it, and randomization never applies to
        them at all. Type/SubType/MonsterArchetype/Location/Notes/etc. still
        apply normally - and since MapApplied never commits for a corpse
        block, it stays open to hard-stat matching on every run."""
        override_maps = override_maps or []
        base_dir = os.path.dirname(__file__)
        map_dir = os.path.join(base_dir, "maps")
        with open(os.path.join(map_dir, "handle_map.json"), "r") as f:
            handle_map = json.load(f)

        matched_hard_stats_guids = set()
        matched_randomization_guids = set()

        for entry_key, entry in handle_map.items():
            match_combos = entry.get("MatchCombos", [])
            if not match_combos:
                # No MatchCombos means this entry can never match a block -
                # skip it entirely rather than doing a no-op pass over blocks.
                continue

            apply_stats = entry.get("ApplyStats", {})
            entry_overridden = entry_key in override_maps
            set_applied = entry.get("SetApplied", True)

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

            for block in blocks:
                if block.lock_block:
                    continue
                if block.corpse:
                    # Corpse blocks are static scenery: they're always open to
                    # (non-excluded) hard-stat matching - MapApplied must never
                    # commit for them - and never receive randomization at all,
                    # since every randomization output field is corpse-excluded.
                    apply_hard_stats = True
                    apply_randomization = False
                else:
                    apply_hard_stats = entry_overridden or not block.map_applied
                    apply_randomization = entry_overridden or not block.randomization_applied
                if not apply_hard_stats and not apply_randomization:
                    continue

                for combo in match_combos:
                    if discoverFields._combo_matches_block(combo, block):
                        if apply_hard_stats and apply_stats:
                            for field, value in apply_stats.items():
                                if block.corpse and field in MonsterStatBlock.CORPSE_EXCLUDED_FIELDS:
                                    continue
                                if field == "HealthOverride" and health_override_range is not None:
                                    continue
                                attr = discoverFields.FIELD_ATTR_MAP.get(field, field)
                                if field in discoverFields.LIST_MERGE_FIELDS:
                                    incoming = value if isinstance(value, list) else [value]
                                    existing = getattr(block, attr, None) or []
                                    setattr(
                                        block, attr, sorted(set(existing) | set(incoming))
                                    )
                                else:
                                    setattr(block, attr, value)
                            if set_applied and not block.corpse:
                                matched_hard_stats_guids.add(block.full_guid)

                        if apply_randomization and has_randomization:
                            if health_override_range is not None:
                                low, high = health_override_range
                                resolved = low if low == high else random.randint(low, high)
                                block.health_override = resolved
                                if not block.original_health:
                                    block.original_health = resolved

                            if random_passives and random_passive_count > 0:
                                chosen = random.sample(
                                    random_passives, min(random_passive_count, len(random_passives))
                                )
                                block.passives_to_add = sorted(set(block.passives_to_add) | set(chosen))

                            if random_spells and random_spell_count > 0:
                                chosen = random.sample(
                                    random_spells, min(random_spell_count, len(random_spells))
                                )
                                block.spells_to_add = sorted(set(block.spells_to_add) | set(chosen))

                            if set_applied:
                                matched_randomization_guids.add(block.full_guid)

                        break

        for block in blocks:
            if block.full_guid in matched_hard_stats_guids:
                block.map_applied = True
            if block.full_guid in matched_randomization_guids:
                block.randomization_applied = True

        return blocks

    @staticmethod
    def extract_armor_class_from_notes(blocks):
        # Matches: XX AC, AC XX, Armor Class XX, XX Armor Class (no comma in phrase)
        patterns = [
            r"\b(\d+)\s+AC\b",
            r"\bAC\s+(\d+)\b",
            r"\bArmor\s+Class\s+(\d+)\b",
            r"\b(\d+)\s+Armor\s+Class\b",
        ]

        for block in blocks:
            if block.lock_block:
                continue
            if not block.notes:
                continue
            for pattern in patterns:
                match = re.search(pattern, block.notes, re.IGNORECASE)
                if match:
                    block.armor_class = int(match.group(1))
                    break

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

        map_applied_count = field_counts.pop("MapApplied", 0)
        randomization_applied_count = field_counts.pop("RandomizationApplied", 0)

        print("---- Dry Run Summary (discoverFields) ----")
        print(f"Blocks loaded: {len(blocks)}")
        print(f"Blocks skipped (LockBlock): {locked_count}")
        print(f"Blocks with at least one field changed: {len(diffs)}")
        print(
            f"Blocks newly matched for hard stats (MapApplied set): {map_applied_count}"
        )
        print(
            f"Blocks newly matched for randomization (RandomizationApplied set): {randomization_applied_count}"
        )
        print(f"Blocks with an ambiguous 'Multiple:' match: {multiple_count}")
        if field_counts:
            print("Changes by field:")
            for field, count in sorted(field_counts.items(), key=lambda kv: -kv[1]):
                print(f"  {field}: {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Auto-populate ClassArchetype/MonsterArchetype/SubType/Type/ArmorClass "
        "from maps + notes, and apply handle_map.json ApplyStats."
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

    # Toggle on if you want to quickly populate new fields based on existing notes
    # discoverFields.update_type_based_on_notes(blocks)
    # discoverFields.update_subtype_based_on_notes(blocks)
    # discoverFields.update_class_archetype_based_on_notes(blocks)
    # discoverFields.update_monster_archetype_based_on_handle(blocks)
    # discoverFields.extract_armor_class_from_notes(blocks)

    # List handle_map.json entry keys here (e.g. ["Mind Flayer"]) to force
    # them to re-apply to blocks that already have MapApplied=True. Leave
    # blank for the normal, safe behavior of skipping already-mapped blocks.
    override_maps = []
    discoverFields.apply_handle_map(blocks, override_maps=override_maps)

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
