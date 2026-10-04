import re, os, json, glob, collections, random

ROOT = 'C:/Users/Tyler/source/repos/bg3-mod-extraction-utils'
OUT = 'C:/Users/Tyler/GitHub/zz_CXUtils/maps/keyword_maps'

# Load order from modsettings.lsx (later overrides earlier for non-collision duplicates)
LO = ['BASE', '5ESP', 'MYST', 'U5E', 'SWTS', 'INVX', 'RAN', 'DTHM']
SOURCES = {
    'BASE': [f'{ROOT}/scratch_vanilla_extract/allstats_hunt/Public/GustavDev',
             f'{ROOT}/scratch_vanilla_extract/allstats_hunt/Public/Gustav',
             f'{ROOT}/scratch_vanilla_extract/allstats_hunt/Public/Honour',
             os.environ['SCR'] + '/shared_pak/Public/Shared',
             os.environ['SCR'] + '/shared_pak/Public/SharedDev'],
    '5ESP': [f'{ROOT}/mods/5eSpells'],
    'MYST': [f'{ROOT}/mods/MystraSpells'],
    'U5E': [f'{ROOT}/mods/Use5eSpellsWithMystraSpells'],
    'SWTS': [f'{ROOT}/mods/StormWardensTomeOfSpells'],
    'INVX': [f'{ROOT}/mods/InvocationsExpanded'],
    'RAN': [f'{ROOT}/mods/RangerSubclasses5eCombined'],
    'DTHM': [f'{ROOT}/mods/DeathMarch'],
}
CODES = {'BASE': 'BASE', '5ESP': '5ESP', 'MYST': 'MYST', 'SWTS': 'SWTS',
         'INVX': 'INVX', 'RAN': 'RAN', 'DTHM': 'DTHM'}

# Use5eSpellsWithMystraSpells rules (see research/mystra_5espells_compat_report.md)
PATCHED_5E = {'Shout_BorrowedKnowledge', 'Target_DragonsBreath', 'Target_FlockOfFamiliars',
              'Target_SummonBeast', 'Shout_SpiritShroud', 'Target_SummonShadowspawn',
              'Target_SteelWindStrike'}
REMOVED = {
    'MYST': {'Target_BoomingBladeMove', 'Projectile_Infestation', 'Projectile_MindSilver',
             'Target_CreateDestroyMoldEarth', 'Target_ShapeWater_Container', 'Shout_MagicStone',
             'Shout_AbsorbElementsSpell', 'Projectile_ChaosBoltNew', 'Zone_AganazzarScorcher',
             'Shout_DustDevil', 'Target_EarthenGrasp', 'Target_SnowballStorm', 'Shout_ShadowBlade_Spell',
             'Shout_CreateFoodAndWater', 'Shout_MelfsMinuteMeteors', 'Target_ArcaneEyeNew',
             'Target_PsychicLance', 'Shout_FarStep'},
    '5ESP': {'Target_SummonFey', 'Shout_WaterWalk', 'Target_SummonBeholderkin', 'Target_SummonDraconicSpirit'},
}

NEW_RE = re.compile(r'^new entry "(.*)"')
TYPE_RE = re.compile(r'^type "(.*)"')
USING_RE = re.compile(r'^using "(.*)"')
DATA_RE = re.compile(r'^data "([^"]*)" "(.*)"\s*$')


def parse_file(path):
    out, cur = {}, None
    with open(path, encoding='utf-8', errors='replace') as f:
        for raw in f:
            line = raw.rstrip('\r\n')
            if line.startswith('new entry'):
                m = NEW_RE.match(line)
                if not m:
                    cur = None
                    continue
                cur = {'id': m.group(1), 'type': None, 'using': None, 'data': {}}
                out[cur['id']] = cur
            elif cur is None:
                continue
            elif line.startswith('type '):
                m = TYPE_RE.match(line)
                if m: cur['type'] = m.group(1)
            elif line.startswith('using '):
                m = USING_RE.match(line)
                if m: cur['using'] = m.group(1)
            elif line.startswith('data '):
                m = DATA_RE.match(line)
                if m: cur['data'][m.group(1)] = m.group(2)
    return out


def load_source(roots):
    ents = {}
    for root in roots:
        for p in sorted(glob.glob(root + '/**/Stats/Generated/Data/*.txt', recursive=True)):
            for k, v in parse_file(p).items():
                ents.setdefault(k, v)
    return ents


SRC = {c: load_source(r) for c, r in SOURCES.items()}


def find(eid, own):
    if eid in own:
        return own[eid]
    for c in LO:
        if eid in SRC[c]:
            return SRC[c][eid]
    return None


def effective(rec, own):
    chain, cur = [rec], rec
    while cur['using'] and len(chain) < 15:
        p = find(cur['using'], own)
        if p is None or any(p is c for c in chain):
            break
        chain.append(p)
        cur = p
    data, typ = {}, None
    for r in reversed(chain):
        data.update(r['data'])
        if r['type']:
            typ = r['type']
    return typ, data


# ---- spell candidates per source ----
defs = collections.defaultdict(dict)  # id -> {code: data}
for code in LO:
    own = SRC[code]
    for eid, rec in own.items():
        typ, data = effective(rec, own)
        if typ != 'SpellData':
            continue
        defs[eid][code] = data
spell_ids_by_src = {c: {i for i in defs if c in defs[i]} for c in LO}

# ---- resolve winners ----
stats = collections.Counter()
winners = {}  # id -> (code, data)
for eid, bycode in defs.items():
    if '5ESP' in bycode and 'MYST' in bycode:
        stats['collision_59_check'] += 1
        if eid in PATCHED_5E:
            data = bycode['U5E'] if 'U5E' in bycode else bycode['5ESP']
            winners[eid] = ('5ESP', data)
            stats['collision_patched_5esp'] += 1
        else:
            winners[eid] = ('MYST', bycode['MYST'])
            stats['collision_mystra'] += 1
        continue
    if 'BASE' in bycode:
        winners[eid] = ('BASE', bycode['BASE'])
        stats['vanilla_id'] += 1
        continue
    if eid in PATCHED_5E:
        winners[eid] = ('5ESP', bycode.get('U5E', bycode.get('5ESP')))
        stats['patched_not_both'] += 1
        continue
    if 'U5E' in bycode and len(bycode) == 1:
        stats['u5e_only_skipped'] += 1
        continue
    cands = [c for c in LO if c in bycode and c != 'U5E']
    if 'SWTS' in cands and len(cands) > 1:
        # Tome copies are collision pins for mods that already define the ID; attribute to the origin mod
        cands.remove('SWTS')
        stats['swts_pin_yielded_to_origin'] += 1
    if not cands:
        continue
    if len(cands) > 1:
        stats['multi_source_dup_last_in_loadorder'] += 1
    winners[eid] = (cands[-1], bycode[cands[-1]])

# Remove list-dedup losers
removed_hits = []
for eid in list(winners):
    code = winners[eid][0]
    for rcode, rset in REMOVED.items():
        if eid in rset and code == rcode:
            removed_hits.append(eid)
            del winners[eid]
            break
# Actually removed from lists even when only defined by that mod
for rcode, rset in REMOVED.items():
    for eid in rset:
        if eid in defs and eid not in removed_hits and eid in winners:
            del winners[eid]
            removed_hits.append(eid)
stats['list_dedup_removed'] = len(removed_hits)

# ---- spell list membership ----
LIST_NODE = re.compile(r'<node id="SpellList">(.*?)</node>', re.S)
NAME_RE = re.compile(r'<attribute id="Name" type="\w+" value="([^"]*)"')
SPELLS_RE = re.compile(r'<attribute id="Spells" type="\w+" value="([^"]*)"')
LIST_FILES = [(f'{ROOT}/scratch_vanilla_extract/gustavx_check/Public/GustavX/Lists/SpellLists.lsx', 'BASE'),
              (os.environ['SCR'] + '/shared_pak/Public/Shared/Lists/SpellLists.lsx', 'BASE')]
for m in ['5eSpells', 'MystraSpells', 'DeathMarch', 'RangerSubclasses5eCombined', 'InvocationsExpanded']:
    for p in glob.glob(f'{ROOT}/mods/{m}/**/Lists/SpellLists.lsx', recursive=True):
        LIST_FILES.append((p, m))

CLASSES = {'Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Ranger', 'Rogue',
           'Sorcerer', 'Warlock', 'Wizard'}
SUBS = [('eldritch knight', 'Eldritch Knight', 'Fighter'), ('arcane trick', 'Arcane Trickster', 'Rogue'),
        ('arcane archer', 'Arcane Archer', 'Fighter'), ('archfey', 'Archfey', 'Warlock'),
        ('fiend', 'Fiend', 'Warlock'), ('great old one', 'Great Old One', 'Warlock'),
        ('hexblade', 'Hexblade', 'Warlock'), ('death domain', 'Death Domain', 'Cleric'),
        ('knowledge domain', 'Knowledge Domain', 'Cleric'), ('life domain', 'Life Domain', 'Cleric'),
        ('light domain', 'Light Domain', 'Cleric'), ('nature domain', 'Nature Domain', 'Cleric'),
        ('tempest domain', 'Tempest Domain', 'Cleric'), ('trickery domain', 'Trickery Domain', 'Cleric'),
        ('war domain', 'War Domain', 'Cleric'), ('swarmkeeper', 'Swarmkeeper', 'Ranger'),
        ('bladesinging', 'Bladesinger', 'Wizard'), ('swashbuckler', 'Swashbuckler', 'Rogue'),
        ('glamour', 'Glamour Bard', 'Bard'), ('drunken master', 'Drunken Master', 'Monk'),
        ('shadow sorcerer', 'Shadow Sorcerer', 'Sorcerer'), ('druid of the stars', 'Circle of Stars', 'Druid'),
        ('starry', 'Circle of Stars', 'Druid'),
        ('beast master', 'Beast Master', 'Ranger'), ('hunter horde', 'Hunter', 'Ranger'),
        ('totem warrior', 'Totem Warrior', 'Barbarian'), ('berserker', 'Berserker', 'Barbarian'),
        ('storm sorcery', 'Storm Sorcery', 'Sorcerer'), ('stormsorcery', 'Storm Sorcery', 'Sorcerer'),
        ('lore bard', 'College of Lore', 'Bard'), ('pact of the tome', 'Pact of the Tome', 'Warlock'),
        ('oathbreaker', 'Oathbreaker', None),
        ('paladin', 'Paladin', None)]
RACE_WORDS = [('drow', 'Drow'), ('tiefling', 'Tiefling'), ('forest gnome', 'Gnome'), ('githyanki', 'Githyanki')]


def map_list(name):
    n = re.sub(r'^5eSpells\s+', '', name)
    n = re.sub(r'\s+NEW$', '', n)
    low = n.lower()
    sub, sub_cls = None, None
    for key, label, parent in SUBS:
        if key in low:
            sub, sub_cls = label, parent
            break
    m = re.search(r'\b(' + '|'.join(sorted(CLASSES)) + r')\b', n)
    cls = m.group(1) if m else sub_cls
    races = {r for key, r in RACE_WORDS if key in low}
    return cls, sub, races


membership = collections.defaultdict(lambda: {'class': set(), 'sub': set(), 'race': set()})
unmapped_lists = collections.Counter()
list_hits = collections.Counter()
for path, _src in LIST_FILES:
    txt = open(path, encoding='utf-8', errors='replace').read()
    for body in LIST_NODE.findall(txt):
        n, s = NAME_RE.search(body), SPELLS_RE.search(body)
        if not (n and s):
            continue
        cls, sub, races = map_list(n.group(1))
        if cls is None and sub is None and not races:
            unmapped_lists[n.group(1)] += 1
            continue
        for sp in filter(None, s.group(1).split(';')):
            if cls: membership[sp]['class'].add(cls)
            if sub: membership[sp]['sub'].add(sub)
            membership[sp]['race'] |= races
            list_hits[sp] += 1

# coverage: list-referenced IDs with no definition in any loaded source
missing_from_pools = sorted(i for i in list_hits if i not in defs)
print('list-referenced ids:', len(list_hits), 'missing from all loaded stat pools:', len(missing_from_pools))
print('missing sample:', missing_from_pools[:40])

# ---- scope filters ----
excl = collections.Counter()
excl_ids = collections.defaultdict(list)
kept = {}
VARIANT = re.compile(r'_(?:\d|L\d+|Ritual|Upcast|Default|SneakAttack|Interrupt)$')
for eid, (code, data) in winners.items():
    listed = bool(membership[eid]['class'] or membership[eid]['sub'] or membership[eid]['race'])
    has_effect = any(data.get(k) for k in ('SpellProperties', 'SpellSuccess', 'TooltipDamageList', 'Boosts'))
    flags = data.get('SpellFlags', '')
    if 'Legendary' in eid or 'IsLegendary' in flags:
        excl['legendary'] += 1
        excl_ids['legendary'].append(eid)
        continue
    if 'UNUSED' in flags:
        excl['unused_flag'] += 1
        excl_ids['unused'].append(eid)
        continue
    if not has_effect and not listed:
        excl['visual_fx_or_no_effect_unlisted'] += 1
        excl_ids['visual_fx'].append(eid)
        continue
    if not listed and code in ('BASE', '5ESP', 'MYST', 'DTHM', 'RAN', 'U5E'):
        excl['not_on_any_class_list_monster_specific'] += 1
        excl_ids['monster'].append(eid)
        continue
    kept[eid] = (code, data)

# Collapse upcast / ritual / interrupt / default variants into their base
collapsed = []
final = {}
for eid, (code, data) in kept.items():
    base = VARIANT.sub('', eid)
    if base != eid and base in kept:
        collapsed.append(eid)
        membership[base]['class'] |= membership[eid]['class']
        membership[base]['sub'] |= membership[eid]['sub']
        membership[base]['race'] |= membership[eid]['race']
        continue
    final[eid] = (code, data)
excl['upcast_or_variant_collapsed'] = len(collapsed)

# ---- classification ----
DTYPES = ['Acid', 'Bludgeoning', 'Cold', 'Fire', 'Force', 'Lightning', 'Necrotic', 'Piercing', 'Poison',
          'Psychic', 'Radiant', 'Slashing', 'Thunder']
SCHOOLS = ['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy',
           'Transmutation', 'Chronurgy', 'Graviturgy']
DEALT = re.compile(r'DealDamage\(([^;]*)')
STATUS_CALL = re.compile(r'ApplyStatus\(([^)]*)\)')
CONTROL = re.compile(r'STUN|KNOCK|FEAR|CHARM|FROZ|INCAPAC|ENTANGL|RESTRAIN|PARALY|SLEEP|BLIND|HOLD|PRONE|'
                     r'POLYMORPH|GRAPPL|DOMINAT|PETRIF|UNCONSC|SILENC|CONFUS|BANISH|HELD|DOWN|FALL')
DEF_HP = re.compile(r'TEMP_?HP|HITPOINT|VITALITY')
DEF_AC = re.compile(r'ARMOR|_AC\b|^AC_')
DEF_RES = re.compile(r'RESIST')
DEF_IMM = re.compile(r'IMMUN')
DEF_ST = re.compile(r'SAVING_?THROW|SAVE_(?:BONUS|ADV|DC)|ADVANTAGE_ON_SAVE')
DEF_SPECIAL = re.compile(r'SHIELD|BARRIER|MIRROR|PROTECT|WARD|GLOBE|BLUR|STONESKIN|ABSORB|SANCT')
SUMMON_KW = {'beast': 'Beast', 'fey': 'Fey', 'elemental': 'Elemental', 'construct': 'Construct',
             'aberration': 'Aberration', 'beholder': 'Aberration', 'celestial': 'Celestial', 'fiend': 'Fiend',
             'infernal': 'Fiend', 'undead': 'Undead', 'skeleton': 'Undead', 'zombie': 'Undead',
             'dragon': 'Dragon', 'draconic': 'Dragon', 'giant': 'Giant', 'ooze': 'Ooze', 'plant': 'Plant',
             'monstrosity': 'Monstrosity', 'humanoid': 'Humanoid', 'shadowspawn': 'Undead'}
RACE_KW = {'halfling', 'gnome', 'dwarf', 'elf', 'dragonborn', 'tiefling', 'orc', 'goblin', 'drow', 'aasimar'}

buckets = {
    'DamageTypes': {t: set() for t in DTYPES},
    'SpellSchools': {s: set() for s in SCHOOLS},
    'Class': {c: set() for c in ['Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
                                 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']},
    'EnemyType': {e: set() for e in ['Aberration', 'Beast', 'Celestial', 'Construct', 'Dragon', 'Elemental', 'Fey',
                                     'Fiend', 'Giant', 'Humanoid', 'Monstrosity', 'Plant', 'Ooze', 'Undead']},
    'Type': {t: set() for t in ['SpellDamage_Single', 'SpellDamage_AOE_Small', 'SpellDamage_AOE_Large',
                                'Control_Single', 'Control_AOE_Small', 'Control_AOE_Large',
                                'Defense_HitPoints', 'Defense_ArmorClass', 'Defense_SavingThrows',
                                'Defense_DamageResistance', 'Defense_ConditionImmunity', 'Defense_Special',
                                'Healing_Single', 'Healing_AOE', 'Buff_Single', 'Buff_Multiple',
                                'Debuff_Single', 'Debuff_Multiple', 'Teleportation']},
    'Subclass': {s: set() for s in ['Paladin', 'Oathbreaker', 'Eldritch Knight', 'Arcane Trickster',
                                    'Arcane Archer', 'Archfey', 'Fiend', 'Great Old One', 'Hexblade',
                                    'Death Domain', 'Knowledge Domain', 'Life Domain', 'Light Domain',
                                    'Nature Domain', 'Tempest Domain', 'Trickery Domain', 'War Domain',
                                    'Swarmkeeper', 'Bladesinger', 'Swashbuckler', 'Glamour Bard',
                                    'Drunken Master', 'Shadow Sorcerer', 'Circle of Stars']},
    'Races': {r: set() for r in ['Halfling', 'Gnome', 'Dwarf', 'Elf', 'Dragonborn', 'Tiefling', 'Orc',
                                 'Goblin', 'Drow', 'Aasimar', 'Githyanki']},
    'MagicItemType': {m: set() for m in ['Headwear', 'Cloak', 'Armor/Clothing', 'Gloves', 'Boots', 'Necklace',
                                         'Ring', 'Martial Weapon', 'Ranged Weapon', 'Shield']},
}


def entry_label(eid, code):
    return f'{eid} [{CODES[code]}]'


def categorize(eid, code, data):
    out = collections.defaultdict(set)
    mem = membership.get(eid, {'class': set(), 'sub': set()})
    for c in mem['class']:
        out[('Class', c)].add(1)
    for s in mem['sub']:
        out[('Subclass', s)].add(1)
    for r in mem['race']:
        out[('Races', r)].add(1)

    txt_dmg = ' '.join(data.get(k, '') for k in ('SpellSuccess', 'SpellProperties', 'TooltipDamageList', 'SpellFail'))
    dmg_types = set()
    segs = DEALT.findall(txt_dmg)
    for seg in segs:
        for t in DTYPES:
            if re.search(r'(?<![A-Za-z])' + t + r'(?![A-Za-z])', seg):
                dmg_types.add(t)
    # Inherited DamageType only counts when the spell actually deals damage
    has_damage = bool(segs)
    if has_damage and data.get('DamageType') in DTYPES:
        dmg_types.add(data['DamageType'])
    for t in dmg_types:
        out[('DamageTypes', t)].add(1)

    if data.get('SpellSchool') in SCHOOLS:
        out[('SpellSchools', data['SpellSchool'])].add(1)

    radius = 0.0
    try:
        radius = float(data.get('AreaRadius', '0') or 0)
    except ValueError:
        pass
    stype = data.get('SpellType', '')
    aoe = radius > 0 or stype in ('Zone', 'Shout', 'Wall', 'Cone', 'Tornado')
    size = 'Large' if radius > 6 else 'Small'

    # SpellFail carries save-marker statuses (SAVED_AGAINST_*), so status detection skips it
    status_txt = ' '.join(data.get(k, '') for k in ('SpellSuccess', 'SpellProperties'))
    statuses = set()
    for args in STATUS_CALL.findall(status_txt):
        for tok in args.split(','):
            tok = tok.strip()
            if re.match(r'^[A-Z][A-Z0-9_]+$', tok) and tok not in ('SELF', 'TARGET', 'GROUND', 'ALL') \
                    and not tok.startswith('SAVED_'):
                statuses.add(tok)
    flags = data.get('SpellFlags', '')
    hostile = has_damage or 'IsHarmful' in flags or 'IsEnemySpell' in flags
    control = [s for s in statuses if CONTROL.search(s)]
    other = [s for s in statuses if s not in control]
    heal = bool(re.search(r'\bHeal\(|RegainHitPoints', txt_dmg + data.get('SpellProperties', '')))
    if stype == 'Teleportation' or 'Teleport' in data.get('SpellProperties', ''):
        out[('Type', 'Teleportation')].add(1)

    if has_damage:
        out[('Type', 'SpellDamage_AOE_' + size if aoe else 'SpellDamage_Single')].add(1)
    if control:
        out[('Type', 'Control_AOE_' + size if aoe else 'Control_Single')].add(1)
    if heal:
        out[('Type', 'Healing_AOE' if aoe else 'Healing_Single')].add(1)
    if other and not has_damage:
        if hostile:
            out[('Type', 'Debuff_Multiple' if aoe else 'Debuff_Single')].add(1)
        else:
            out[('Type', 'Buff_Multiple' if aoe else 'Buff_Single')].add(1)
    boosts = data.get('Boosts', '') + ' ' + ' '.join(statuses)
    if 'AC(' in data.get('Boosts', '') or any(DEF_AC.search(s) for s in statuses):
        out[('Type', 'Defense_ArmorClass')].add(1)
    if DEF_HP.search(boosts) or 'GainTemporaryHitPoints' in txt_dmg:
        out[('Type', 'Defense_HitPoints')].add(1)
    if DEF_ST.search(boosts) or 'SavingThrow' in data.get('Boosts', ''):
        out[('Type', 'Defense_SavingThrows')].add(1)
    if DEF_RES.search(boosts) or 'Resistance(' in data.get('Boosts', ''):
        out[('Type', 'Defense_DamageResistance')].add(1)
    if DEF_IMM.search(boosts) or 'Immune' in data.get('Boosts', ''):
        out[('Type', 'Defense_ConditionImmunity')].add(1)
    if any(DEF_SPECIAL.search(s) for s in statuses):
        out[('Type', 'Defense_Special')].add(1)

    low_id = eid.lower()
    if 'summon' in low_id or 'Summon(' in data.get('SpellProperties', ''):
        for kw, et in SUMMON_KW.items():
            if kw in low_id:
                out[('EnemyType', et)].add(1)

    tokens = {t.lower() for t in re.split(r'[_\s]+', eid)}
    for r in RACE_KW & tokens:
        out[('Races', r.capitalize() if r != 'dwarf' else 'Dwarf')].add(1)
    return out


def norm_race(v):
    return {'Elf': 'Elf', 'Drow': 'Drow'}.get(v, v)


assign = collections.defaultdict(dict)  # (group, key) -> {eid: code}
for eid, (code, data) in final.items():
    cat = categorize(eid, code, data)
    for (group, key) in cat:
        if group in buckets and key in buckets[group]:
            buckets[group][key].add(entry_label(eid, code))
        elif group in buckets:
            buckets[group].setdefault(key, set()).add(entry_label(eid, code))

# ---- output ----
os.makedirs(OUT, exist_ok=True)
ORDER_KEYS = ['DamageTypes', 'SpellSchools', 'Class', 'EnemyType', 'Type', 'Subclass', 'Races', 'MagicItemType']
result = {}
for g in ORDER_KEYS:
    result[g] = {k: sorted(v) for k, v in buckets[g].items()}
with open(f'{OUT}/keyword_to_spells.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)
    f.write('\n')

# ---- diagnostics for log ----
src_counts = collections.Counter(code for (code, _) in final.values())
diag = {
    'source_counts_final': dict(src_counts),
    'raw_spell_defs_per_src': {c: len(spell_ids_by_src[c]) for c in LO},
    'stats': dict(stats),
    'excl': dict(excl),
    'unmapped_lists': dict(unmapped_lists),
    'final_total': len(final),
    'collapsed_examples': collapsed[:20],
    'excl_examples': {k: v[:15] for k, v in excl_ids.items()},
    'bucket_counts': {g: {k: len(v) for k, v in buckets[g].items()} for g in ORDER_KEYS},
}
with open(os.path.join(os.environ.get('SCR', '.'), 'diag.json'), 'w', encoding='utf-8') as f:
    json.dump(diag, f, indent=1)
print(json.dumps({k: diag[k] for k in ('source_counts_final', 'raw_spell_defs_per_src', 'stats', 'excl', 'final_total')}, indent=1))
for g in ORDER_KEYS:
    print(g, {k: len(v) for k, v in buckets[g].items() if v})
