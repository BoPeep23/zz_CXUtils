import argparse
import json
import os

from monsterStatBlock import MonsterStatBlock
from organizeBlocks import organizeBlocks


# Storm Warden's Tome (SWTE_) creatures are fully statted in their own Stats
# entries, so these three override fields are never set on them. Flip to False
# to let SWTE_ blocks carry them again.
STRIP_SWTE_OVERRIDE_FIELDS = True
SWTE_PREFIX = "SWTE_"


class sanitizeFields:

    @staticmethod
    def add_new_field(blocks, field_name, default_value=""):
        for block in blocks:
            if not hasattr(block, field_name):
                setattr(block, field_name, default_value)

    @staticmethod
    def remove_fields(blocks, fields_to_remove):
        for block in blocks:
            for field in fields_to_remove:
                if hasattr(block, field):
                    delattr(block, field)

    @staticmethod
    def rename_field(blocks, old_field, new_field):
        """Migration helper: copies a legacy field's value (kept as a raw attribute
        once it drops out of the schema) into its renamed replacement, then removes
        the legacy field. Only overwrites the new field when it's still blank/zero.
        Safe to re-run; a no-op once the legacy field is gone."""
        for block in blocks:
            if not hasattr(block, old_field):
                continue
            legacy_value = getattr(block, old_field)
            if legacy_value and not getattr(block, new_field, None):
                setattr(block, new_field, legacy_value)
            delattr(block, old_field)

    @staticmethod
    def clamp_level_field(blocks, max_level=30):
        """Keeps Level within its valid 0-30 range (0 = unknown level).
        Blocks missing a Level already default to 0 via MonsterStatBlock.from_dict;
        this only clamps values that exceed max_level. Safe to re-run."""
        for block in blocks:
            if block.level and block.level > max_level:
                block.level = max_level

    @staticmethod
    def normalize_todo_field(blocks):
        """TODO is always a list of strings, blank as []. A missing/None/blank
        value becomes [], a lone string becomes a one-item list, and blank
        entries inside a list are dropped. Safe to re-run."""
        for block in blocks:
            value = block.todo
            if value is None or value == "":
                block.todo = []
            elif isinstance(value, str):
                block.todo = [value]
            elif isinstance(value, list):
                block.todo = [str(task) for task in value if str(task).strip()]

    @staticmethod
    def strip_corpse_only_fields(blocks):
        """Corpse=True blocks are static scenery, not fighters - ClassArchetype,
        SubclassArchetype, ArmorClass, HealthOverride, OriginalHealth, Level,
        PassivesToAdd, and SpellsToAdd (see MonsterStatBlock.CORPSE_EXCLUDED_FIELDS)
        are never relevant for them. Resets each to its blank/zero default. The lock
        fields are left False/open (not excluded) so corpse blocks stay open
        to non-excluded-field matching on every discoverFields run, same as
        before. Safe to re-run."""
        for block in blocks:
            if not block.corpse:
                continue
            block.classArchetype = ""
            block.subclassArchetype = ""
            block.armor_class = 0
            block.health_override = 0
            block.original_health = 0
            block.level = 0
            block.passives_to_add = []
            block.spells_to_add = []
            block.lock_static_modifications = False
            block.lock_random_modifications = False

    @staticmethod
    def strip_swte_override_fields(blocks):
        """SWTE_ FullGuids (Storm Warden's Tome creatures) get HealthOverride,
        PassivesToAdd and SpellsToAdd reset to blank/zero, whatever they hold.
        Gated by STRIP_SWTE_OVERRIDE_FIELDS. Safe to re-run."""
        if not STRIP_SWTE_OVERRIDE_FIELDS:
            return
        for block in blocks:
            if not (block.full_guid or "").startswith(SWTE_PREFIX):
                continue
            block.health_override = 0
            block.passives_to_add = []
            block.spells_to_add = []

    @staticmethod
    def populate_act_field(blocks):
        """Derives Act from the FullGuid's scene prefix, using
        maps/location_to_act_map.json (prefix -> Act), checked in file order.
        A FullGuid whose prefix isn't listed there is set to "Unknown" for
        manual triage. Safe to re-run; only fills blank/stale Act values."""
        base_dir = os.path.dirname(__file__)
        map_path = os.path.join(base_dir, "maps", "location_to_act_map.json")
        with open(map_path, "r") as f:
            location_to_act_map = json.load(f)

        for block in blocks:
            if block.act not in (None, "", "Unknown"):
                continue
            block.act = "Unknown"
            if not block.full_guid:
                continue
            for prefix, act in location_to_act_map.items():
                if block.full_guid.startswith(prefix):
                    block.act = act
                    break

    @staticmethod
    def populate_type_subtype_from_guid(blocks):
        """Derives Type/SubType from phrases found anywhere in FullGuid, using
        maps/guid_to_type_subtype_map.json - a tiered, ordered list of
        key -> "Type" or "Type, SubType" entries (SubType is never applied
        without a Type from the same entry). Fill-only: a Type/SubType already
        set on the block (by hand or by an earlier run) is never replaced -
        the map only fills blank fields. Within a single run the search still
        tiers: a later, more specific match overrides an earlier, broader one
        for the same block, and a key ending in '!' stops the search right
        there. Matching is a case-sensitive substring check (not just a
        prefix), consistent with how these key phrases are authored as
        literal fragments of the game's FullGuid naming. Safe to re-run."""
        base_dir = os.path.dirname(__file__)
        map_path = os.path.join(base_dir, "maps", "guid_to_type_subtype_map.json")
        with open(map_path, "r") as f:
            guid_to_type_subtype_map = json.load(f)

        for block in blocks:
            if not block.full_guid:
                continue
            # Matches are gathered for the whole pass and written once at the
            # end, so the fill-only check sees the block's pre-run values.
            type_found = None
            subtype_found = None
            for raw_key, value in guid_to_type_subtype_map.items():
                stop = raw_key.endswith("!")
                phrase = raw_key[:-1] if stop else raw_key
                if not phrase or phrase not in block.full_guid:
                    continue

                parts = [p.strip() for p in value.split(",")]
                type_value = parts[0] if parts and parts[0] else None
                subtype_value = parts[1] if len(parts) > 1 and parts[1] else None

                if type_value:
                    type_found = type_value
                    if subtype_value:
                        subtype_found = subtype_value

                if stop:
                    break

            if type_found and not block.type:
                block.type = type_found
            if subtype_found and not block.subtype:
                block.subtype = subtype_found

    @staticmethod
    def populate_class_archetype_from_guid(blocks):
        """Derives ClassArchetype from phrases found anywhere in FullGuid,
        using maps/guid_to_class_archetype_map.json - a tiered, ordered list
        of key -> ClassArchetype entries, same shape/matching rules as
        populate_type_subtype_from_guid (case-sensitive substring anywhere
        in FullGuid; a match applies and the search continues to later keys
        by default, so a later, more specific entry can still override an
        earlier one; a key ending in '!' stops the search right there
        instead). Unlike the other populate_*_from_guid functions, this one
        treats ClassArchetype as a static, set-once value: it only fills in
        a block that's still blank, and never overwrites one that's already
        set - whether set by this function on an earlier run or by hand -
        so a manual correction always sticks. Safe to re-run."""
        base_dir = os.path.dirname(__file__)
        map_path = os.path.join(
            base_dir, "maps", "guid_to_class_archetype_map.json"
        )
        with open(map_path, "r") as f:
            guid_to_class_archetype_map = json.load(f)

        for block in blocks:
            if block.classArchetype:
                continue
            if not block.full_guid:
                continue
            for raw_key, value in guid_to_class_archetype_map.items():
                stop = raw_key.endswith("!")
                phrase = raw_key[:-1] if stop else raw_key
                if not phrase or phrase not in block.full_guid:
                    continue

                if value:
                    block.classArchetype = value

                if stop:
                    break

    @staticmethod
    def populate_subclass_archetype_from_guid(blocks):
        """Derives SubclassArchetype from phrases found anywhere in FullGuid,
        using maps/guid_to_subclass_archetype_map.json - same shape/matching
        rules and set-once behavior as populate_class_archetype_from_guid
        (case-sensitive substring anywhere in FullGuid; a match applies and
        the search continues to later keys by default, so a later, more
        specific entry can still override an earlier one; a key ending in
        '!' stops the search right there instead). Only fills in a block
        that's still blank - never overwrites one already set, whether set
        by this function on an earlier run or by hand. Safe to re-run."""
        base_dir = os.path.dirname(__file__)
        map_path = os.path.join(
            base_dir, "maps", "guid_to_subclass_archetype_map.json"
        )
        with open(map_path, "r") as f:
            guid_to_subclass_archetype_map = json.load(f)

        for block in blocks:
            if block.subclassArchetype:
                continue
            if not block.full_guid:
                continue
            for raw_key, value in guid_to_subclass_archetype_map.items():
                stop = raw_key.endswith("!")
                phrase = raw_key[:-1] if stop else raw_key
                if not phrase or phrase not in block.full_guid:
                    continue

                if value:
                    block.subclassArchetype = value

                if stop:
                    break

    @staticmethod
    def populate_location_field(blocks):
        """Derives Location from the FullGuid's prefix, using
        maps/guid_to_location_map.json. Prefixes are checked in file order, so
        a more specific key listed earlier wins over a more generic key listed
        later. Fill-only: a block that already has a Location keeps it, and a
        block whose FullGuid doesn't match any prefix stays blank. Safe to re-run."""
        base_dir = os.path.dirname(__file__)
        map_path = os.path.join(base_dir, "maps", "guid_to_location_map.json")
        with open(map_path, "r") as f:
            guid_to_location_map = json.load(f)

        for block in blocks:
            if not block.full_guid or block.location:
                continue
            for prefix, location in guid_to_location_map.items():
                if block.full_guid.startswith(prefix):
                    block.location = location
                    break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Normalize/populate schema fields (Act, Location, Type, SubType, "
        "Level, ...) on guid_mapper_master.json."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing to guid_mapper_master.json. Writes "
        "dryrun/guid_mapper_master_dryrun.json instead and prints a change summary.",
    )
    args = parser.parse_args()

    base_dir = os.path.dirname(__file__)
    clean_blocks = MonsterStatBlock.load_from_json_file(
        os.path.join(base_dir, "guid_mapper_master.json")
    )

    # ── deduplicate ─────────────────────────────────────────────────────────
    # Always run first. Merges duplicate FullGuids, unions lists, keeps non-blank field values.
    clean_blocks = MonsterStatBlock.deduplicate(clean_blocks)
    before_snapshot = MonsterStatBlock.snapshot(clean_blocks)

    # ── add_new_field ───────────────────────────────────────────────────────
    # Adds a field with a default only if the block doesn't already have it.
    # Use when onboarding new fields to the schema.
    # sanitizeFields.add_new_field(clean_blocks, 'FieldName', default_value="")

    # ── rename_field ────────────────────────────────────────────────────────
    # ONE-TIME MIGRATION: carries the old 'OriginalHealthOverride' JSON key's value
    # into the renamed OriginalHealth field. Safe to re-run; a no-op once migrated.
    sanitizeFields.rename_field(
        clean_blocks, "OriginalHealthOverride", "original_health"
    )

    # ── rename_field ────────────────────────────────────────────────────────
    # ONE-TIME MIGRATION: carries the old 'MapApplied'/'RandomizationApplied' JSON
    # keys into the renamed lock_static_modifications/lock_random_modifications
    # fields (True keeps its "already applied" meaning as "locked"). Safe to
    # re-run; a no-op once migrated.
    sanitizeFields.rename_field(clean_blocks, "MapApplied", "lock_static_modifications")
    sanitizeFields.rename_field(
        clean_blocks, "RandomizationApplied", "lock_random_modifications"
    )

    # ── populate_act_field ──────────────────────────────────────────────────
    # Derives Act from FullGuid scene prefixes via maps/location_to_act_map.json;
    # unmapped prefixes become "Unknown". Safe to re-run; only fills blank/stale Act values.
    sanitizeFields.populate_act_field(clean_blocks)

    # ── populate_location_field ──────────────────────────────────────────────
    # Derives Location from FullGuid prefixes via maps/guid_to_location_map.json.
    # Fill-only: a Location already on the block is kept.
    sanitizeFields.populate_location_field(clean_blocks)

    # ── populate_type_subtype_from_guid ──────────────────────────────────────
    # Derives Type/SubType from phrases anywhere in FullGuid via
    # maps/guid_to_type_subtype_map.json. Fill-only: only blank Type/SubType
    # are written, so a value set by hand is never overwritten. Tiered within
    # a run so later entries catch edge cases.
    sanitizeFields.populate_type_subtype_from_guid(clean_blocks)

    # ── populate_class_archetype_from_guid ───────────────────────────────────
    # Derives ClassArchetype from phrases anywhere in FullGuid via
    # maps/guid_to_class_archetype_map.json. Static/set-once: only fills a
    # blank ClassArchetype, never overwrites one already set (by hand or by
    # a prior run).
    sanitizeFields.populate_class_archetype_from_guid(clean_blocks)

    # ── populate_subclass_archetype_from_guid ────────────────────────────────
    # Derives SubclassArchetype from phrases anywhere in FullGuid via
    # maps/guid_to_subclass_archetype_map.json. Static/set-once: only fills a
    # blank SubclassArchetype, never overwrites one already set (by hand or
    # by a prior run).
    sanitizeFields.populate_subclass_archetype_from_guid(clean_blocks)

    # ── clamp_level_field ─────────────────────────────────────────────────
    # Level is 0-30 (0 = unknown); blocks without one already default to 0
    # on load. This clamps any value above 30 down to 30. Safe to re-run.
    sanitizeFields.clamp_level_field(clean_blocks)

    # ── normalize_todo_field ─────────────────────────────────────────────────
    # TODO (Claude Prompt) is always a list of strings, blank as []. Safe to re-run.
    sanitizeFields.normalize_todo_field(clean_blocks)

    # ── strip_corpse_only_fields ─────────────────────────────────────────────
    # Corpse=True blocks never carry combat-relevant fields. Safe to re-run.
    sanitizeFields.strip_corpse_only_fields(clean_blocks)

    # ── strip_swte_override_fields ───────────────────────────────────────────
    # SWTE_ creatures are statted in their own Stats entries, so HealthOverride,
    # PassivesToAdd and SpellsToAdd are reset on them. Toggle with
    # STRIP_SWTE_OVERRIDE_FIELDS at the top of this file.
    sanitizeFields.strip_swte_override_fields(clean_blocks)

    # ── remove_fields ───────────────────────────────────────────────────────
    # Removes obsolete fields that no longer belong in the schema.
    sanitizeFields.remove_fields(
        clean_blocks, ["Class", "Distance", "Entity", "Guid", "Profiles"]
    )

    # ── reorder_blocks ───────────────────────────────────────────────────────
    # Orders blocks by scene, following the key order in maps/location_to_act_map.json
    # (Unknown/unmapped FullGuids sort last).
    clean_blocks = organizeBlocks.reorder_blocks(clean_blocks)

    diffs = MonsterStatBlock.diff_from_snapshot(before_snapshot, clean_blocks)

    if args.dry_run:
        type_subtype_changed = sum(
            1
            for changes in diffs.values()
            if "Type" in changes or "SubType" in changes
        )
        print("---- Dry Run Summary (sanitizeFields) ----")
        print(f"Blocks loaded: {len(clean_blocks)}")
        print(f"Blocks with at least one field changed: {len(diffs)}")
        print(f"Blocks with Type and/or SubType changed: {type_subtype_changed}")
        dryrun_dir = os.path.join(base_dir, "dryrun")
        os.makedirs(dryrun_dir, exist_ok=True)
        dryrun_path = os.path.join(dryrun_dir, "guid_mapper_master_dryrun.json")
        MonsterStatBlock.save_to_json_file(clean_blocks, dryrun_path, archive=False)
        print(f"Dry run preview written to {dryrun_path}")
    else:
        MonsterStatBlock.save_to_json_file(
            clean_blocks, os.path.join(base_dir, "guid_mapper_master.json")
        )
        print("Saved to guid_mapper_master.json")
