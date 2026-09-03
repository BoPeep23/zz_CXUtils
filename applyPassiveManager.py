import argparse
import json
import os

COMBAT_EXTENDER_PATH = (
    r"C:\Users\Tyler\AppData\Local\Larian Studios\Baldur's Gate 3"
    r"\Script Extender\CombatExtender.json"
)


def apply_passive_manager(passive_manager_path, combat_extender_path, dry_run=False):
    """Overwrites CombatExtender.json's top-level Passives list with the
    contents of cx_passive_manager.json. Every other top-level key (Health,
    Damage, ArmourClass, Clones, Overrides, ...) is left untouched."""
    with open(passive_manager_path, "r", encoding="utf-8") as f:
        passives = json.load(f)

    with open(combat_extender_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    previous_count = len(data.get("Passives", []))

    if dry_run:
        print(
            f"[Dry run] Would replace {previous_count} existing Passives entries "
            f"with {len(passives)} from {passive_manager_path}."
        )
        return

    data["Passives"] = passives
    with open(combat_extender_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(
        f"Replaced {previous_count} Passives entries with {len(passives)} from "
        f"{passive_manager_path} in {combat_extender_path}"
    )


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    parser = argparse.ArgumentParser(
        description="Overwrite CombatExtender.json's top-level Passives list with "
        "the contents of cx_passive_manager.json."
    )
    parser.add_argument(
        "--passive-manager",
        default=os.path.join(base_dir, "cx_passive_manager.json"),
        help="Path to the passive manager JSON file (a list of PassiveName/Act entries).",
    )
    parser.add_argument(
        "--combat-extender-path",
        default=COMBAT_EXTENDER_PATH,
        help="Path to the live CombatExtender.json to write into.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the change without writing to CombatExtender.json.",
    )
    args = parser.parse_args()

    apply_passive_manager(
        args.passive_manager, args.combat_extender_path, dry_run=args.dry_run
    )
