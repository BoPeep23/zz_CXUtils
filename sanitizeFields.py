import json
import os

from monsterStatBlock import MonsterStatBlock

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
    def populate_original_health_override(blocks):
        """Migration helper: copies HealthOverride → OriginalHealthOverride for all blocks.
        Only writes to blocks where OriginalHealthOverride is currently 0.
        Run once on existing data; safe to re-run (never overwrites a set value)."""
        for block in blocks:
            if not block.original_health_override and block.health_override:
                block.original_health_override = block.health_override

    @staticmethod
    def populate_act_field(blocks):
        act_markers = {
            "1": ["S_FirstFight_", "S_FOR_", "S_CRA_", "S_UND_", "S_GOB", "S_CHA_", "S_ORI_", "S_HAG_",
                      "S_GOB_", "S_PLA_", "S_Skeleton_", "MMM_ITSCOMPLICATED_", "MMM_BUGBEARCHALLENGER_",
                      "S_DEN_", "EO_Minotaur_", "EO_WoodWoad_", "MMM_BUGBEARMURDER_", "MMM_BRIDGETROLL_",
                      "EO_Bugbear_Ranger_", "MMM_LOG"],
            "2": ["S_CRE_"],
            "3": ["S_TWN_", "S_MOO_", "S_SCL_", "S_SHA_", "S_SCE_", "S_COL_", "S_LOW_", "S_WYR_", "S_END_"],
            "Global": ["S_GLO_", "S_Player_", "S_VO_"],
            "Camp": ["S_CAMP"],
            "Unknown": ["S_CAMP_", "S_HAV_", "S_TUT_"]
        }
        
        for block in blocks:
            if hasattr(block, 'Act') and (block.act is None or block.act == "" or block.act == "Act 1" or block.act == "Act 2" or block.act == "Act 3"):
                block.act = ""  # default
                for act, markers in act_markers.items():
                    if block.full_guid and any(marker in block.full_guid for marker in markers):
                        block.act = act
                        break

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    clean_blocks = MonsterStatBlock.load_from_json_file(os.path.join(base_dir, 'guid_mapper_master.json'))

    # ── deduplicate ─────────────────────────────────────────────────────────
    # Always run first. Merges duplicate FullGuids, unions lists, keeps non-blank field values.
    clean_blocks = MonsterStatBlock.deduplicate(clean_blocks)

    # ── add_new_field ───────────────────────────────────────────────────────
    # Adds a field with a default only if the block doesn't already have it.
    # Use when onboarding new fields to the schema.
    # sanitizeFields.add_new_field(clean_blocks, 'FieldName', default_value="")

    # ── populate_original_health_override ──────────────────────────────────
    # ONE-TIME MIGRATION: copies HealthOverride → OriginalHealthOverride for all blocks.
    # Safe to re-run; never overwrites a value already set above 0.
    sanitizeFields.populate_original_health_override(clean_blocks)

    # ── populate_act_field ──────────────────────────────────────────────────
    # Derives Act (1/2/3/Global/Camp/Unknown) from FullGuid scene prefixes.
    # Safe to re-run; only fills blank/stale Act values.
    sanitizeFields.populate_act_field(clean_blocks)

    # ── remove_fields ───────────────────────────────────────────────────────
    # Removes obsolete fields that no longer belong in the schema.
    sanitizeFields.remove_fields(clean_blocks, ['Class', 'Distance', 'Entity', 'Guid'])

    MonsterStatBlock.save_to_json_file(clean_blocks, os.path.join(base_dir, 'guid_mapper_master_sanitizedFields.json'))
    print("Saved to guid_mapper_master_sanitizedFields.json")
