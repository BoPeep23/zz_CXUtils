import os
import random

from monsterStatBlock import MonsterStatBlock


class alterStatistics:

    @staticmethod
    def _apply_additions(
        block,
        passives_per_block,
        passives_to_add,
        spells_per_block,
        spells_to_add,
        health_override=0,
        ac_boost=0,
    ):
        if passives_to_add and passives_per_block == 0:
            for passive in passives_to_add:
                for p in passive.split(";"):
                    if p.endswith(":spell:") and p not in block.spells_to_add:
                        block.spells_to_add.append(p.rstrip(":spell:"))
                    elif p not in block.passives_to_add:
                        block.passives_to_add.append(p)
            block.passives_to_add.sort()
        elif passives_to_add and passives_per_block > 0:
            chosen = random.sample(
                passives_to_add, min(passives_per_block, len(passives_to_add))
            )
            for passive in chosen:
                for p in passive.split(";"):
                    if p.endswith(":spell:") and p not in block.spells_to_add:
                        block.spells_to_add.append(p.rstrip(":spell:"))
                    elif p not in block.passives_to_add:
                        block.passives_to_add.append(p)
            block.passives_to_add.sort()
        if spells_to_add and spells_per_block == 0:
            for spell in spells_to_add:
                for s in spell.split(";"):
                    if s.endswith(":passive:") and s not in block.passives_to_add:
                        block.passives_to_add.append(s.rstrip(":passive:"))
                    if s not in block.spells_to_add:
                        block.spells_to_add.append(s)
            block.spells_to_add.sort()
        elif spells_to_add and spells_per_block > 0:
            chosen = random.sample(
                spells_to_add, min(spells_per_block, len(spells_to_add))
            )
            for spell in chosen:
                for s in spell.split(";"):
                    if s.endswith(":passive:") and s not in block.passives_to_add:
                        block.passives_to_add.append(s.rstrip(":passive:"))
                    if s not in block.spells_to_add:
                        block.spells_to_add.append(s)
            block.spells_to_add.sort()
        if health_override:
            if not block.health_override:
                # First assignment: set directly and record as original.
                block.health_override = health_override
                if not block.original_health_override:
                    block.original_health_override = health_override
            else:
                # Already has a value: nudge by 10% of the new input.
                block.health_override += round(health_override * 0.10)
        if 1 <= ac_boost <= 5:
            passive_name = f"Goon_AC_Buff_{ac_boost}"
            if not any("Goon_AC_Buff_" in p for p in block.passives_to_add):
                block.passives_to_add.append(passive_name)
                block.passives_to_add.sort()

    @staticmethod
    def apply_ac_boost(blocks, ac_boost):
        if ac_boost == 0 or ac_boost >= 6:
            return blocks
        passive_name = f"Goon_AC_Buff_{ac_boost}"
        for block in blocks:
            already_has = any("Goon_AC_Buff_" in p for p in block.passives_to_add)
            if not already_has:
                block.passives_to_add.append(passive_name)
                block.passives_to_add.sort()
        return blocks

    @staticmethod
    def add_location_by_guid(blocks, guid_match_phrase, location):
        for block in blocks:
            if block.full_guid and guid_match_phrase in block.full_guid:
                block.location = location

    @staticmethod
    def replace_location_by_phrase(blocks, location_match_phrase, new_location):
        for block in blocks:
            if block.location and location_match_phrase in block.location:
                block.location = new_location

    @staticmethod
    def update_locations_from_map(blocks, location_map):
        for block in blocks:
            if block.location:
                for key, values in location_map.items():
                    if block.location in values:
                        block.location = key
                        break

    @staticmethod
    def alter_stats_by_field_combo(
        blocks,
        handle_match_phrase,
        full_guid_match_phrase,
        act_match_phrase,
        location_match_phrase,
        type_match_phrase,
        subtype_match_phrase,
        class_archetype_match_phrase,
        monster_archetype_match_phrase,
        corpse_boolean,
        passives_per_block=0,
        passives_to_add=[],
        spells_per_block=0,
        spells_to_add=[],
        health_override=0,
        ac_boost=0,
    ):
        for block in blocks:
            if alterStatistics.passes_match_phrases(
                block,
                handle_match_phrase,
                full_guid_match_phrase,
                act_match_phrase,
                location_match_phrase,
                type_match_phrase,
                subtype_match_phrase,
                class_archetype_match_phrase,
                monster_archetype_match_phrase,
                corpse_boolean,
            ):
                alterStatistics._apply_additions(
                    block,
                    passives_per_block,
                    passives_to_add,
                    spells_per_block,
                    spells_to_add,
                    health_override,
                    ac_boost,
                )
        return blocks

    @staticmethod
    def clear_stats_by_field_combo(
        blocks,
        handle_match_phrase,
        full_guid_match_phrase,
        act_match_phrase,
        location_match_phrase,
        type_match_phrase,
        subtype_match_phrase,
        class_archetype_match_phrase,
        monster_archetype_match_phrase,
        corpse_boolean,
        clear_passives=False,
        clear_spells=False,
        clear_health=False,
    ):
        for block in blocks:
            if alterStatistics.passes_match_phrases(
                block,
                handle_match_phrase,
                full_guid_match_phrase,
                act_match_phrase,
                location_match_phrase,
                type_match_phrase,
                subtype_match_phrase,
                class_archetype_match_phrase,
                monster_archetype_match_phrase,
                corpse_boolean,
            ):
                if clear_passives:
                    block.passives_to_add = []
                if clear_spells:
                    block.spells_to_add = []
                if clear_health:
                    block.health_override = 0
        return blocks

    @staticmethod
    def passes_match_phrases(
        block,
        handle_match_phrase,
        full_guid_match_phrase,
        act_match_phrase,
        location_match_phrase,
        type_match_phrase,
        subtype_match_phrase,
        class_archetype_match_phrase,
        monster_archetype_match_phrase,
        corpse_boolean,
    ):
        if handle_match_phrase:
            if not block.handle:
                return False
            if not any(p in block.handle for p in handle_match_phrase.split(";")):
                return False

        if full_guid_match_phrase:
            if not block.full_guid:
                return False
            if not any(p in block.full_guid for p in full_guid_match_phrase.split(";")):
                return False

        if act_match_phrase:
            if not block.act:
                return False
            if not any(p in block.act for p in act_match_phrase.split(";")):
                return False

        if location_match_phrase:
            if not block.location:
                return False
            if not any(p in block.location for p in location_match_phrase.split(";")):
                return False

        if type_match_phrase:
            if not block.type:
                return False
            if not any(p in block.type for p in type_match_phrase.split(";")):
                return False

        if subtype_match_phrase:
            if not block.subtype:
                return False
            if not any(p in block.subtype for p in subtype_match_phrase.split(";")):
                return False

        if class_archetype_match_phrase:
            if not block.classArchetype:
                return False
            if not any(
                p in block.classArchetype
                for p in class_archetype_match_phrase.split(";")
            ):
                return False

        if monster_archetype_match_phrase:
            if not block.monsterArchetype:
                return False
            if not any(
                p in block.monsterArchetype
                for p in monster_archetype_match_phrase.split(";")
            ):
                return False

        if corpse_boolean is not None:
            if block.corpse != corpse_boolean:
                return False

        return True


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    blocks = MonsterStatBlock.load_from_json_file(
        os.path.join(base_dir, "guid_mapper_master.json")
    )

    # ── alter_stats_by_field_combo ──────────────────────────────────────────
    # Adds passives/spells/health override to all blocks matching every non-empty filter.
    # All match phrases support semicolon-delimited OR (e.g. "2;3" = Act 2 or Act 3).
    # Pass "" to skip any filter. corpse_boolean: None=ignore, True=corpses only, False=non-corpses.

    # 1st update: Skeleton damage type changes by Act
    # blocks = alterStatistics.alter_stats_by_field_combo(
    #     blocks,
    #     handle_match_phrase="",
    #     full_guid_match_phrase="",
    #     act_match_phrase="3",
    #     location_match_phrase="",
    #     type_match_phrase="",
    #     subtype_match_phrase="",
    #     class_archetype_match_phrase="",
    #     monster_archetype_match_phrase="Flaming Fist Protector",
    #     corpse_boolean=False,
    #     passives_per_block=3,
    #     passives_to_add=[
    #         "Sentinel_OpportunityAdvantage;Sentinel_Attack",
    #         "Sentinel_ZeroSpeed",
    #         "ImprovedCombatSuperiority",
    #         "ARP_ChannelOath_2;TouchOfDeath;Shout_RadianceOfTheDawn:spell:",
    #         "Goon_Summon_Potion_Healing_Greater_x3",
    #         "DampenElements",
    #         "ARP_Reaction_2",
    #     ],
    #     spells_per_block=3,
    #     spells_to_add=[
    #         "Target_Rally",
    #         "Target_DisarmingAttack",
    #         "Target_ManoeuvringAttack",
    #         "Target_PushingAttack",
    #         "Target_DistractingStrike",
    #         "Target_CommandersStrike",
    #     ],
    #     health_override=0,
    # )

    # 2nd update: Clear fields
    # blocks = alterStatistics.clear_stats_by_field_combo(
    #     blocks,
    #     handle_match_phrase="Fist ",
    #     full_guid_match_phrase="",
    #     act_match_phrase="3",
    #     location_match_phrase="",
    #     type_match_phrase="",
    #     subtype_match_phrase="",
    #     class_archetype_match_phrase="",
    #     monster_archetype_match_phrase="",
    #     corpse_boolean=None,
    #     clear_passives=True,
    #     clear_spells=False,
    #     clear_health=True,
    # )

    # ── set_health_override_by_monster_archetype ────────────────────────────
    # alterStatistics.set_health_override_by_monster_archetype(blocks, "", 0, exact_match=False)

    # ── set_health_override_by_class_archetype ──────────────────────────────
    # alterStatistics.set_health_override_by_class_archetype(blocks, "", 0, exact_match=False)

    # ── set_health_override_by_full_guid ────────────────────────────────────
    # alterStatistics.set_health_override_by_full_guid(blocks, "", 0)

    # ── set_health_override_by_handle ───────────────────────────────────────
    # alterStatistics.set_health_override_by_handle(blocks, "", 0)

    MonsterStatBlock.save_to_json_file(
        blocks, os.path.join(base_dir, "guid_mapper_master_alteredStats.json")
    )
