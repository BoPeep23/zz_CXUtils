"""
organizeBlocks.py

Utilities for ordering block output without changing block field values.
Blocks are sorted alphabetically by FullGuid by default, which naturally
groups them by scene prefix (S_GLO_, S_CRA_, S_GOB_, S_TWN_, etc.).
"""

import os

from monsterStatBlock import MonsterStatBlock

# Maps lowercased JSON field names to MonsterStatBlock property names where they differ.
_FIELD_ATTR_MAP = {
    "fullguid":          "full_guid",
    "classarchetype":    "classArchetype",
    "monsterarchetype":  "monsterArchetype",
    "healthoverride":    "health_override",
    "passivestoadd":     "passives_to_add",
    "spellstoadd":       "spells_to_add",
    "clonetemplatguid":  "clone_template_guid",
    "clonedisplayname":  "clone_display_name",
}


class organizeBlocks:

    @staticmethod
    def _get_block_field(block, field_name):
        if isinstance(block, dict):
            return block.get(field_name) or ""
        attr = _FIELD_ATTR_MAP.get(field_name.lower(), field_name.lower())
        return getattr(block, attr, "") or ""

    @staticmethod
    def sort_blocks_by_full_guid(blocks):
        """Sort blocks alphabetically by FullGuid only."""
        return sorted(blocks, key=lambda b: organizeBlocks._get_block_field(b, "FullGuid").lower())

    @staticmethod
    def sort_blocks_by_fields(blocks, field_order=None):
        """Sort blocks by a progressive list of fields. Default: Act then FullGuid."""
        if field_order is None:
            field_order = organizeBlocks.get_field_order()

        def block_key(block):
            return tuple(
                organizeBlocks._get_block_field(block, f).lower()
                for f in field_order
            )

        return sorted(blocks, key=block_key)

    @staticmethod
    def reorder_blocks(blocks):
        """Sort blocks by the default field order (Act, FullGuid)."""
        return organizeBlocks.sort_blocks_by_fields(blocks)

    @staticmethod
    def get_field_order():
        return ["Act", "FullGuid"]


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    clean_blocks = MonsterStatBlock.load_from_json_file(os.path.join(base_dir, 'guid_mapper_master.json'))
    clean_blocks = MonsterStatBlock.deduplicate(clean_blocks)

    # ── reorder_blocks ──────────────────────────────────────────────────────
    # Sorts by Act then FullGuid. FullGuid prefixes naturally group entries by
    # scene (S_GLO_ → S_CRA_ → S_GOB_ → ... → S_TWN_ → S_END_).
    clean_blocks = organizeBlocks.reorder_blocks(clean_blocks)

    # ── sort_blocks_by_full_guid ────────────────────────────────────────────
    # Pure alphabetical sort by FullGuid only (ignores Act grouping).
    # clean_blocks = organizeBlocks.sort_blocks_by_full_guid(clean_blocks)

    # ── sort_blocks_by_fields ───────────────────────────────────────────────
    # Sort by any combination of fields, in priority order.
    # clean_blocks = organizeBlocks.sort_blocks_by_fields(clean_blocks, ["Act", "Type", "FullGuid"])

    MonsterStatBlock.save_to_json_file(clean_blocks, os.path.join(base_dir, 'guid_mapper_master_organized.json'))
