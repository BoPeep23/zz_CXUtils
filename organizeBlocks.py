"""
organizeBlocks.py

Utilities for ordering block output without changing block field values.
Blocks are sorted by default according to the key order of
maps/location_to_act_map.json, which groups them by scene prefix
(S_GLO_, S_CRA_, S_GOB_, S_TWN_, etc.) in that map's order. FullGuids whose
prefix isn't in the map (Unknown) sort last.
"""

import json
import os

from monsterStatBlock import MonsterStatBlock

# Maps lowercased JSON field names to MonsterStatBlock property names where they differ.
_FIELD_ATTR_MAP = {
    "fullguid":          "full_guid",
    "classarchetype":    "classArchetype",
    "subclassarchetype": "subclassArchetype",
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
    def _load_location_order():
        base_dir = os.path.dirname(__file__)
        map_path = os.path.join(base_dir, "maps", "location_to_act_map.json")
        with open(map_path, "r") as f:
            return list(json.load(f).keys())

    @staticmethod
    def _location_rank(full_guid, location_order):
        """Index of the first location_to_act_map.json prefix that full_guid
        starts with. Unmatched FullGuids rank past every known prefix, so they
        sort last."""
        for i, prefix in enumerate(location_order):
            if full_guid.startswith(prefix):
                return i
        return len(location_order)

    @staticmethod
    def sort_blocks_by_location_order(blocks):
        """Sort blocks by the order their FullGuid's scene prefix appears as a
        key in maps/location_to_act_map.json, then alphabetically by FullGuid
        within the same prefix. FullGuids that don't match any prefix
        (Unknown) sort last."""
        location_order = organizeBlocks._load_location_order()

        def block_key(block):
            full_guid = organizeBlocks._get_block_field(block, "FullGuid")
            return (
                organizeBlocks._location_rank(full_guid, location_order),
                full_guid.lower(),
            )

        return sorted(blocks, key=block_key)

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
        """Sort blocks by scene order, per maps/location_to_act_map.json's key
        order (Unknown/unmapped FullGuids sort last)."""
        return organizeBlocks.sort_blocks_by_location_order(blocks)

    @staticmethod
    def get_field_order():
        return ["Act", "FullGuid"]


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    clean_blocks = MonsterStatBlock.load_from_json_file(os.path.join(base_dir, 'guid_mapper_master.json'))
    clean_blocks = MonsterStatBlock.deduplicate(clean_blocks)

    # ── reorder_blocks ──────────────────────────────────────────────────────
    # Sorts by scene, per maps/location_to_act_map.json's key order
    # (S_FirstFight_ → S_TUT_ → S_CAMP_ → S_GLO_ → ... → S_END_); Unknown last.
    clean_blocks = organizeBlocks.reorder_blocks(clean_blocks)

    # ── sort_blocks_by_full_guid ────────────────────────────────────────────
    # Pure alphabetical sort by FullGuid only (ignores Act grouping).
    # clean_blocks = organizeBlocks.sort_blocks_by_full_guid(clean_blocks)

    # ── sort_blocks_by_fields ───────────────────────────────────────────────
    # Sort by any combination of fields, in priority order.
    # clean_blocks = organizeBlocks.sort_blocks_by_fields(clean_blocks, ["Act", "Type", "FullGuid"])

    MonsterStatBlock.save_to_json_file(clean_blocks, os.path.join(base_dir, 'guid_mapper_master_organized.json'))
