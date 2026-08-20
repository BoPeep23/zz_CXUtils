import argparse
import json
import os

from monsterStatBlock import MonsterStatBlock

COMBAT_EXTENDER_PATH = (
    r"C:\Users\Tyler\AppData\Local\Larian Studios\Baldur's Gate 3"
    r"\Script Extender\CombatExtender.json"
)


class CombatExtenderBlockGenerator:

    @staticmethod
    def load_blocks(input_path):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        return MonsterStatBlock.load_from_json_file(input_path)

    @staticmethod
    def generate_clones(blocks):
        clones = {}
        for block in blocks:
            if block.clone_display_name and block.clone_display_name != "":
                clone_definition = {"DisplayName": block.clone_display_name}
                if block.clone_template_guid and block.clone_template_guid != "":
                    clone_definition["Template"] = block.clone_template_guid
                clones[block.full_guid] = clone_definition
        return clones

    @staticmethod
    def generate_overrides(blocks):
        overrides = {}
        for block in blocks:
            override_definition = {}
            if block.passives_to_add and len(block.passives_to_add) > 0:
                override_definition["Passives"] = block.passives_to_add
            if block.spells_to_add and len(block.spells_to_add) > 0:
                override_definition["Spells"] = block.spells_to_add
            if block.health_override is not None and block.health_override != 0:
                override_definition["HealthOverride"] = block.health_override
            if override_definition:
                overrides[block.full_guid] = override_definition
        return overrides

    @staticmethod
    def _passes_field_combo(
        block,
        location_match_phrase,
        class_archetype_match_phrase,
        monster_archetype_match_phrase,
        handle_match_phrase,
    ):
        """A filter is skipped when its phrase is empty; a block must satisfy
        every non-empty filter via case-insensitive substring containment
        (e.g. "Booyahg" matches a MonsterArchetype of "Booyahg Foobar")."""
        if location_match_phrase:
            if not block.location or location_match_phrase.lower() not in block.location.lower():
                return False
        if class_archetype_match_phrase:
            if not block.classArchetype or class_archetype_match_phrase.lower() not in block.classArchetype.lower():
                return False
        if monster_archetype_match_phrase:
            if not block.monsterArchetype or monster_archetype_match_phrase.lower() not in block.monsterArchetype.lower():
                return False
        if handle_match_phrase:
            if not block.handle or handle_match_phrase.lower() not in block.handle.lower():
                return False
        return True

    @staticmethod
    def generate_clones_by_field_combo(
        blocks,
        location_match_phrase="",
        class_archetype_match_phrase="",
        monster_archetype_match_phrase="",
        handle_match_phrase="",
    ):
        clones = {}
        for block in blocks:
            if not CombatExtenderBlockGenerator._passes_field_combo(
                block,
                location_match_phrase,
                class_archetype_match_phrase,
                monster_archetype_match_phrase,
                handle_match_phrase,
            ):
                continue
            if block.clone_display_name and block.clone_display_name != "":
                clone_definition = {"DisplayName": block.clone_display_name}
                if block.clone_template_guid and block.clone_template_guid != "":
                    clone_definition["Template"] = block.clone_template_guid
                clones[block.full_guid] = clone_definition
        return clones

    @staticmethod
    def generate_overrides_by_field_combo(
        blocks,
        location_match_phrase="",
        class_archetype_match_phrase="",
        monster_archetype_match_phrase="",
        handle_match_phrase="",
    ):
        overrides = {}
        for block in blocks:
            if not CombatExtenderBlockGenerator._passes_field_combo(
                block,
                location_match_phrase,
                class_archetype_match_phrase,
                monster_archetype_match_phrase,
                handle_match_phrase,
            ):
                continue
            override_definition = {}
            if block.passives_to_add and len(block.passives_to_add) > 0:
                override_definition["Passives"] = block.passives_to_add
            if block.spells_to_add and len(block.spells_to_add) > 0:
                override_definition["Spells"] = block.spells_to_add
            if block.health_override is not None and block.health_override != 0:
                override_definition["HealthOverride"] = block.health_override
            if override_definition:
                overrides[block.full_guid] = override_definition
        return overrides

    @staticmethod
    def merge_into_combat_extender(clones, overrides, combat_extender_path):
        """Merge generated Clones/Overrides into the live CombatExtender.json,
        overwriting any existing entry with the same FullGuid key. Every other
        top-level key (Health, Damage, ArmourClass, ...) is left untouched."""
        with open(combat_extender_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        data.setdefault("Clones", {}).update(clones)
        data.setdefault("Overrides", {}).update(overrides)

        with open(combat_extender_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(
            f"Merged {len(clones)} clone(s) and {len(overrides)} override(s) into {combat_extender_path}"
        )

    @staticmethod
    def save_json(data, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Saved {output_path}")


def parse_args():
    base_dir = os.path.dirname(__file__)
    parser = argparse.ArgumentParser(
        description="Generate CombatExtender-ready Clones and Overrides JSON from a guid_mapper input file."
    )
    parser.add_argument(
        "--input",
        default=os.path.join(base_dir, "guid_mapper_input.json"),
        help="Path to the guid_mapper input JSON file. Default: guid_mapper_input.json in this folder.",
    )
    parser.add_argument(
        "--clones-output",
        default=os.path.join(base_dir, "combat_extender_clones.json"),
        help="Output file path for the Clones JSON block.",
    )
    parser.add_argument(
        "--overrides-output",
        default=os.path.join(base_dir, "combat_extender_overrides.json"),
        help="Output file path for the Overrides JSON block.",
    )
    parser.add_argument(
        "--print-only",
        action="store_true",
        help="Print the generated JSON blocks to stdout instead of writing files.",
    )
    parser.add_argument(
        "--combat-extender-path",
        default=COMBAT_EXTENDER_PATH,
        help="Path to the live CombatExtender.json to merge Clones/Overrides into.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    metadata_dir = os.path.join(base_dir, "metadata")
    clean_blocks = MonsterStatBlock.load_from_json_file(
        os.path.join(base_dir, "guid_mapper_master.json")
    )
    deduped_blocks = MonsterStatBlock.deduplicate(clean_blocks)

    clones = CombatExtenderBlockGenerator.generate_clones(deduped_blocks)
    overrides = CombatExtenderBlockGenerator.generate_overrides(deduped_blocks)

    clones_payload = {"Clones": clones}
    overrides_payload = {"Overrides": overrides}

    CombatExtenderBlockGenerator.save_json(
        clones_payload,
        os.path.join(base_dir, "clonesAndOverrides/combat_extender_clones.json"),
    )
    CombatExtenderBlockGenerator.save_json(
        overrides_payload,
        os.path.join(base_dir, "clonesAndOverrides/combat_extender_overrides.json"),
    )

    # Toggle on when ready to write these Clones/Overrides into the live CombatExtender.json.
    # CombatExtenderBlockGenerator.merge_into_combat_extender(
    #     clones, overrides, COMBAT_EXTENDER_PATH
    # )
