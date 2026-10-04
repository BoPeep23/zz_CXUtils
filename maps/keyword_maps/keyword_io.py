"""Shared writer for keyword_to_passives.json / keyword_to_spells.json.

Never replaces a keyword file. The existing file is read first, and the new
output is merged into it: existing groups, keys and entries are always kept,
and only missing groups, keys and entries are added.
"""
import json, os
from collections import OrderedDict


def merge_keyword_map(path, new, sort_key=lambda s: s.lower()):
    """Merge `new` into the JSON at `path` and write it back. Returns (added_count, path)."""
    existing = OrderedDict()
    if os.path.exists(path):
        existing = json.load(open(path, encoding="utf-8"), object_pairs_hook=OrderedDict)

    added = 0
    for group, keys in new.items():
        if group not in existing:
            existing[group] = OrderedDict()
        for key, entries in keys.items():
            if key not in existing[group]:
                existing[group][key] = []
            current = existing[group][key]
            for e in entries:
                if e not in current:
                    current.append(e)
                    added += 1
            existing[group][key] = sorted(set(current), key=sort_key)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=4, ensure_ascii=False)
        f.write("\n")
    return added, path
