import os
import openpyxl
from monsterStatBlock import MonsterStatBlock
from alterStatistics import alterStatistics

BASE_DIR = os.path.dirname(__file__)
EXCEL_PATH = os.path.join(BASE_DIR, "alter_statistics_inputs.xlsx")
INPUT_JSON = os.path.join(BASE_DIR, "guid_mapper_master.json")
OUTPUT_JSON = os.path.join(BASE_DIR, "guid_mapper_master_alteredStats.json")

ALTER_SHEET = "alter_stats"
CLEAR_SHEET = "clear_stats"

STATUS_READY = "ready"
STATUS_PROCESSED = "processed"
STATUS_NOT_READY = "not ready"

# alter_stats column order (0-based index into row values):
# 0=#  1=status  2=passives_per  3=passives_to_add  4=spells_per  5=spells_to_add
# 6=health_override  7=monster_archetype_match  8=class_archetype_match
# 9=subtype_match  10=act_match  11=corpse_boolean  12=handle_match
# 13=full_guid_match  14=location_match  15=type_match

# clear_stats column order (0-based index into row values):
# 0=#  1=status  2=monster_archetype_match  3=clear_passives  4=clear_spells
# 5=clear_health  6=class_archetype_match  7=subtype_match  8=act_match
# 9=corpse_boolean  10=handle_match  11=full_guid_match  12=location_match  13=type_match

CLEAR_HEADERS = [
    "#",
    "status",
    "monster_archetype_match",
    "clear_passives",
    "clear_spells",
    "clear_health",
    "class_archetype_match",
    "subtype_match",
    "act_match",
    "corpse_boolean",
    "handle_match",
    "full_guid_match",
    "location_match",
    "type_match",
]
CLEAR_PLACEHOLDER_ROWS = 8


def _str(value):
    return "" if value is None else str(value).strip()


def _int(value, default=0):
    if value is None:
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def _bool_or_none(value):
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    s = str(value).strip().lower()
    if s in ("true", "1", "yes"):
        return True
    if s in ("false", "0", "no"):
        return False
    return None


def _list_cell(value):
    """Newline-delimited cell → list of strings."""
    if not value:
        return []
    return [item.strip() for item in str(value).split("\n") if item.strip()]


def _read_row(ws, row_idx):
    return [ws.cell(row=row_idx, column=c).value for c in range(1, ws.max_column + 1)]


def _process_alter_sheet(ws, blocks):
    for row_idx in range(2, ws.max_row + 1):
        vals = _read_row(ws, row_idx)
        status_cell = ws.cell(row=row_idx, column=2)

        has_content = bool(vals[3]) or bool(vals[5]) or bool(vals[6])

        if not has_content:
            status_cell.value = STATUS_NOT_READY
            continue

        if vals[1] != STATUS_READY:
            continue

        blocks = alterStatistics.alter_stats_by_field_combo(
            blocks,
            handle_match_phrase=_str(vals[12]),
            full_guid_match_phrase=_str(vals[13]),
            act_match_phrase=_str(vals[10]),
            location_match_phrase=_str(vals[14]),
            type_match_phrase=_str(vals[15]),
            subtype_match_phrase=_str(vals[9]),
            class_archetype_match_phrase=_str(vals[8]),
            monster_archetype_match_phrase=_str(vals[7]),
            corpse_boolean=_bool_or_none(vals[11]),
            passives_per_block=_int(vals[2]),
            passives_to_add=_list_cell(vals[3]),
            spells_per_block=_int(vals[4]),
            spells_to_add=_list_cell(vals[5]),
            health_override=_int(vals[6]),
        )

        status_cell.value = STATUS_PROCESSED
        print(f"  alter_stats row #{vals[0]}: applied")

    return blocks


def _process_clear_sheet(ws, blocks):
    for row_idx in range(2, ws.max_row + 1):
        vals = _read_row(ws, row_idx)
        status_cell = ws.cell(row=row_idx, column=2)

        # clear flags are stored as booleans in the sheet
        clear_passives = bool(vals[3])
        clear_spells = bool(vals[4])
        clear_health = bool(vals[5])
        has_content = clear_passives or clear_spells or clear_health

        if not has_content:
            status_cell.value = STATUS_NOT_READY
            continue

        if vals[1] != STATUS_READY:
            continue

        blocks = alterStatistics.clear_stats_by_field_combo(
            blocks,
            handle_match_phrase=_str(vals[10]),
            full_guid_match_phrase=_str(vals[11]),
            act_match_phrase=_str(vals[8]),
            location_match_phrase=_str(vals[12]),
            type_match_phrase=_str(vals[13]),
            subtype_match_phrase=_str(vals[7]),
            class_archetype_match_phrase=_str(vals[6]),
            monster_archetype_match_phrase=_str(vals[2]),
            corpse_boolean=_bool_or_none(vals[9]),
            clear_passives=clear_passives,
            clear_spells=clear_spells,
            clear_health=clear_health,
        )

        status_cell.value = STATUS_PROCESSED
        print(f"  clear_stats row #{vals[0]}: applied")

    return blocks


def _ensure_clear_sheet(wb):
    if CLEAR_SHEET in wb.sheetnames:
        return
    ws = wb.create_sheet(CLEAR_SHEET)
    ws.append(CLEAR_HEADERS)
    for i in range(1, CLEAR_PLACEHOLDER_ROWS + 1):
        ws.append([i, STATUS_NOT_READY] + [None] * (len(CLEAR_HEADERS) - 2))


def main():
    blocks = MonsterStatBlock.load_from_json_file(INPUT_JSON)
    wb = openpyxl.load_workbook(EXCEL_PATH)

    _ensure_clear_sheet(wb)

    print("Processing alter_stats...")
    blocks = _process_alter_sheet(wb[ALTER_SHEET], blocks)

    print("Processing clear_stats...")
    blocks = _process_clear_sheet(wb[CLEAR_SHEET], blocks)

    wb.save(EXCEL_PATH)
    print(f"Excel updated: {EXCEL_PATH}")

    MonsterStatBlock.save_to_json_file(blocks, OUTPUT_JSON)
    print(f"JSON saved: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
