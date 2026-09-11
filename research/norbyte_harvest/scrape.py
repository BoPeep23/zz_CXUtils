"""Minimal scraper for bg3.norbyte.dev server-rendered search results.

The search page renders the first 30 hits server-side (alphabetical, no
pagination), so queries must be narrow enough to return < 30 rows. Each hit
carries the full stat-entry text in a <code> block, including the //-comment
lines Norbyte injects with the localized DisplayName / Description.
"""
import hashlib
import html
import os
import re
import time
import urllib.parse
import urllib.request

BASE = "https://bg3.norbyte.dev/search"
CACHE = os.path.join(os.path.dirname(__file__), "cache")
os.makedirs(CACHE, exist_ok=True)
DELAY = 0.35  # politeness between live fetches

_RESULT_SPLIT = re.compile(r'<div class="d-flex flex-column highlighted search-result p-2"')
_NAME_RE = re.compile(
    r'</a>\s*([A-Za-z0-9_]+)\s*<span class="badge[^"]*">([^<]+)</span>', re.S
)
_CODE_RE = re.compile(r'<code class="c"[^>]*>(.*?)</code>', re.S)
_COUNT_RE = re.compile(r'Showing results 1 - (\d+) of (\d+)')


def fetch(query, force=False):
    key = hashlib.sha1(query.encode("utf-8")).hexdigest()
    path = os.path.join(CACHE, key + ".html")
    if not force and os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return f.read()
    url = BASE + "?q=" + urllib.parse.quote(query)
    req = urllib.request.Request(
        url, headers={"User-Agent": "cx-passive-manager research script (personal modding)"}
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                body = r.read().decode("utf-8", "replace")
            break
        except Exception as e:  # noqa: BLE001
            if attempt == 3:
                raise
            time.sleep(1.5 * (attempt + 1))
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    time.sleep(DELAY)
    return body


def parse(page_html):
    shown = total = 0
    m = _COUNT_RE.search(page_html)
    if m:
        shown, total = int(m.group(1)), int(m.group(2))
    rows = []
    chunks = _RESULT_SPLIT.split(page_html)[1:]  # drop preamble
    for chunk in chunks:
        nm = _NAME_RE.search(chunk)
        code = _CODE_RE.search(chunk)
        if not nm or not code:
            continue
        rows.append(
            {
                "name": nm.group(1),
                "type": nm.group(2).strip(),
                "body": html.unescape(code.group(1)).strip(),
            }
        )
    return {"shown": shown, "total": total, "capped": total > shown, "rows": rows}


def search(query, force=False):
    return parse(fetch(query, force=force))


# ---- field extraction from a stat-entry body ------------------------------

_DATA_RE = re.compile(r'^data "([^"]+)" "(.*)"$', re.M)


def entry_fields(body):
    lines = body.splitlines()
    out = {"_comments": [], "name": None, "entry_type": None, "using": None}
    for i, ln in enumerate(lines):
        ln = ln.strip()
        if ln.startswith('new entry "'):
            out["name"] = ln.split('"')[1]
        elif ln.startswith('type "'):
            out["entry_type"] = ln.split('"')[1]
        elif ln.startswith('using "'):
            out["using"] = ln.split('"')[1]
        elif ln.startswith("// "):
            out["_comments"].append(ln[3:].strip())
    for k, v in _DATA_RE.findall(body):
        out.setdefault(k, v)
    return out


def _clean_text(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    s = s.replace("&quot;", '"').replace("&#039;", "'").replace("&amp;", "&")
    return re.sub(r"\s+", " ", s).strip()


def _looks_like_handle(s):
    return (not s) or s.startswith("%%%") or bool(
        re.fullmatch(r"h[0-9a-f]{8}[0-9a-fg]{20,};?\d*", s)
    )


def summarize(body, max_desc=240):
    """Human-readable one-liner(s) for a candidate: localized name + effect."""
    f = entry_fields(body)
    comments = [c for c in f["_comments"] if c and not c.startswith("h")]
    disp = _clean_text(comments[0]) if comments else ""
    if _looks_like_handle(disp):
        disp = ""
    # Norbyte puts the description text as the comment right before data "Description"
    desc = ""
    lines = body.splitlines()
    for i, ln in enumerate(lines):
        if ln.strip().startswith('data "Description"') and i > 0:
            prev = lines[i - 1].strip()
            if prev.startswith("// "):
                desc = prev[3:].strip()
    if not desc and len(comments) > 1:
        desc = comments[1]
    desc = _clean_text(desc)
    if _looks_like_handle(desc):
        desc = ""
    if len(desc) > max_desc:
        desc = desc[:max_desc].rstrip() + "…"
    mech = []
    for key in ("Boosts", "SpellType", "SpellSuccess", "SpellProperties", "Level",
                "UseCosts", "Cooldown", "StatusPropertyFlags"):
        if f.get(key):
            val = re.sub(r"\s+", " ", f[key]).strip()
            if len(val) > 180:
                val = val[:180].rstrip() + "…"
            mech.append(f"{key}={val}")
    return {"display": disp, "desc": desc, "mech": mech, "using": f["using"],
            "entry_type": f["entry_type"]}


if __name__ == "__main__":
    import json
    import sys

    q = sys.argv[1] if len(sys.argv) > 1 else "type:passive & Portent"
    res = search(q, force="--force" in sys.argv)
    print(f"# {q}  ->  shown {res['shown']} / total {res['total']}"
          + ("  [CAPPED]" if res["capped"] else ""))
    for row in res["rows"]:
        s = summarize(row["body"])
        print(f"\n## {row['name']}  ({row['type']})")
        if s["display"]:
            print(f"   name: {s['display']}")
        if s["desc"]:
            print(f"   desc: {s['desc']}")
        for m in s["mech"]:
            print(f"   {m}")
