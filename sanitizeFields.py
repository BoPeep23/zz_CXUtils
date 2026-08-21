import json
import os

from monsterStatBlock import MonsterStatBlock
from organizeBlocks import organizeBlocks


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
    def strip_corpse_only_fields(blocks):
        """Corpse=True blocks are static scenery, not fighters - ClassArchetype,
        ArmorClass, HealthOverride, OriginalHealth, Level, PassivesToAdd, and
        SpellsToAdd (see MonsterStatBlock.CORPSE_EXCLUDED_FIELDS) are never
        relevant for them. Resets each to its blank/zero default. The lock
        fields are left False/open (not excluded) so corpse blocks stay open
        to non-excluded-field matching on every discoverFields run, same as
        before. Safe to re-run."""
        for block in blocks:
            if not block.corpse:
                continue
            block.classArchetype = ""
            block.armor_class = 0
            block.health_override = 0
            block.original_health = 0
            block.level = 0
            block.passives_to_add = []
            block.spells_to_add = []
            block.lock_static_modifications = False
            block.lock_random_modifications = False

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
            if block.act not in (None, "", "Act 1", "Act 2", "Act 3"):
                continue
            block.act = "Unknown"
            if not block.full_guid:
                continue
            for prefix, act in location_to_act_map.items():
                if block.full_guid.startswith(prefix):
                    block.act = act
                    break

    @staticmethod
    def populate_location_field(blocks):
        """Derives Location from the FullGuid's prefix, using
        maps/guid_to_location_map.json as the definitive source. Prefixes are
        checked in file order, so a more specific key listed earlier wins over
        a more generic key listed later. A block whose FullGuid doesn't match
        any prefix keeps its existing Location untouched. Safe to re-run;
        always re-applies the mapped value on a match."""
        base_dir = os.path.dirname(__file__)
        map_path = os.path.join(base_dir, "maps", "guid_to_location_map.json")
        with open(map_path, "r") as f:
            guid_to_location_map = json.load(f)

        for block in blocks:
            if not block.full_guid:
                continue
            for prefix, location in guid_to_location_map.items():
                if block.full_guid.startswith(prefix):
                    block.location = location
                    break


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    clean_blocks = MonsterStatBlock.load_from_json_file(
        os.path.join(base_dir, "guid_mapper_master.json")
    )

    # ── deduplicate ─────────────────────────────────────────────────────────
    # Always run first. Merges duplicate FullGuids, unions lists, keeps non-blank field values.
    clean_blocks = MonsterStatBlock.deduplicate(clean_blocks)

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
    # Derives Location from FullGuid prefixes via maps/guid_to_location_map.json,
    # the definitive source. Unmatched FullGuids keep their existing Location.
    sanitizeFields.populate_location_field(clean_blocks)

    # ── clamp_level_field ─────────────────────────────────────────────────
    # Level is 0-30 (0 = unknown); blocks without one already default to 0
    # on load. This clamps any value above 30 down to 30. Safe to re-run.
    sanitizeFields.clamp_level_field(clean_blocks)

    # ── strip_corpse_only_fields ─────────────────────────────────────────────
    # Corpse=True blocks never carry combat-relevant fields. Safe to re-run.
    sanitizeFields.strip_corpse_only_fields(clean_blocks)

    # ── remove_fields ───────────────────────────────────────────────────────
    # Removes obsolete fields that no longer belong in the schema.
    sanitizeFields.remove_fields(
        clean_blocks, ["Class", "Distance", "Entity", "Guid", "Profiles"]
    )

    # ── reorder_blocks ───────────────────────────────────────────────────────
    # Orders blocks by scene, following the key order in maps/location_to_act_map.json
    # (Unknown/unmapped FullGuids sort last).
    clean_blocks = organizeBlocks.reorder_blocks(clean_blocks)

    MonsterStatBlock.save_to_json_file(
        clean_blocks, os.path.join(base_dir, "guid_mapper_master.json")
    )
    print("Saved to guid_mapper_master.json")
