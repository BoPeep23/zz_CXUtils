import json
import os

# Define file paths
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, "spell_map.json")
output_file = os.path.join(current_dir, "spell_map_updated.json")

# Read the JSON file
with open(input_file, 'r', encoding='utf-8') as f:
    spell_map = json.load(f)

def spell_sort_key(entry):
    # Sort by the spell name after the first underscore (e.g. "ArmorOfAgathys" from "Shout_ArmorOfAgathys")
    parts = entry.split('_', 1)
    return parts[1].lower() if len(parts) > 1 else parts[0].lower()

# Sort A-Z and deduplicate (if it's a dict, sort by keys and sort/dedupe each list value; if it's a list, sort by name field)
if isinstance(spell_map, dict):
    sorted_map = {
        k: sorted(dict.fromkeys(v), key=spell_sort_key) if isinstance(v, list) else v
        for k, v in sorted(spell_map.items())
    }
elif isinstance(spell_map, list):
    sorted_map = sorted(spell_map, key=lambda x: x.get('name', '').lower() if isinstance(x, dict) else str(x).lower())
else:
    sorted_map = spell_map

# Write to new file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(sorted_map, f, indent=2, ensure_ascii=False)

print(f"Sorted spell map saved to: {output_file}")