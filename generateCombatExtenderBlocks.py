import argparse
import json
import os

from monsterStatBlock import MonsterStatBlock


class CombatExtenderBlockGenerator:

    @staticmethod
    def load_blocks(input_path):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        return MonsterStatBlock.load_from_json_file(input_path)

    @staticmethod
    def generate_clones_by_location(blocks, location_match_phrase):
        clones = {}
        for block in blocks:
            if block.clone_display_name and block.clone_display_name != "":
                clone_definition = {"DisplayName": block.clone_display_name}
                if block.clone_template_guid and block.clone_template_guid != "":
                    clone_definition["Template"] = block.clone_template_guid
                clones[block.full_guid] = clone_definition
        return clones

    @staticmethod
    def generate_overrides_by_location(blocks, location_match_phrase):
        overrides = {}
        for block in blocks:
            override_definition = {}
            if (
                block.passives_to_add
                and len(block.passives_to_add) > 0
                and block.location
                and location_match_phrase in block.location
            ):
                override_definition["Passives"] = block.passives_to_add
            if (
                block.spells_to_add
                and len(block.spells_to_add) > 0
                and block.location
                and location_match_phrase in block.location
            ):
                override_definition["Spells"] = block.spells_to_add
            if (
                block.health_override is not None
                and block.health_override != 0
                and block.location
                and location_match_phrase in block.location
            ):
                override_definition["HealthOverride"] = block.health_override
            if override_definition:
                overrides[block.full_guid] = override_definition
        return overrides

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
    return parser.parse_args()


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    metadata_dir = os.path.join(base_dir, "metadata")
    clean_blocks = MonsterStatBlock.load_from_json_file(
        os.path.join(base_dir, "guid_mapper_master.json")
    )
    deduped_blocks = MonsterStatBlock.deduplicate(clean_blocks)

    clones = CombatExtenderBlockGenerator.generate_clones_by_location(
        deduped_blocks, "RIVINGTON_FIELDS_GUR"
    )
    overrides = CombatExtenderBlockGenerator.generate_overrides_by_location(
        deduped_blocks, "RIVINGTON_FIELDS_GUR"
    )

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
