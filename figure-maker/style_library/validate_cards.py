from pathlib import Path
import re

base = Path(r'D:\MCM-ICM_Agent_Skills\figure-maker\style_library')
cards_dir = base / 'cards'

required_scalar = [
    'use_case',
    'layout.aspect',
    'layout.legend',
    'layout.label',
    'style.font',
    'style.linewidth',
    'style.marker',
    'style.grid',
    'color.palette',
    'color.note',
]

hex_re = re.compile(r'#[0-9A-Fa-f]{6}')

errors = []

for card in sorted(cards_dir.glob('*.md')):
    text = card.read_text(encoding='utf-8')
    lines = text.splitlines()
    data = {}

    # simple parser for top-level and nested keys
    current_section = None
    for line in lines:
        if re.match(r'^\w[^:]*:$', line.strip()):
            key = line.strip()[:-1]
            current_section = key
            continue
        m = re.match(r'^(\s*)([A-Za-z_]+):\s*(.*)$', line)
        if m:
            indent, key, val = m.group(1), m.group(2), m.group(3)
            if indent and current_section:
                full_key = f"{current_section}.{key}"
            else:
                full_key = key
            data[full_key] = val

    # required scalars
    for k in required_scalar:
        v = data.get(k, '')
        if v is None or v.strip() == '':
            errors.append(f"{card.name}: {k} is empty")

    # palette must have >=3 hex
    pal = data.get('color.palette', '')
    if len(hex_re.findall(pal)) < 3:
        errors.append(f"{card.name}: color.palette needs >=3 hex colors")

    # density_tricks bullets
    density = [l for l in lines if l.startswith('density_tricks:')]
    if density:
        # count bullets after section until blank or next section
        idx = lines.index('density_tricks:')
        count = 0
        for l in lines[idx+1:]:
            if re.match(r'^\w[^:]*:$', l.strip()):
                break
            if l.strip().startswith('-') or l.startswith('  -'):
                if l.strip() != '-':
                    count += 1
                else:
                    # empty bullet
                    pass
        if count < 2:
            errors.append(f"{card.name}: density_tricks needs >=2 bullets")
    else:
        errors.append(f"{card.name}: density_tricks missing")

    # caption_style bullets
    caption = [l for l in lines if l.startswith('caption_style:')]
    if caption:
        idx = lines.index('caption_style:')
        count = 0
        for l in lines[idx+1:]:
            if re.match(r'^\w[^:]*:$', l.strip()):
                break
            if l.strip().startswith('-') or l.startswith('  -'):
                if l.strip() != '-':
                    count += 1
        if count < 2:
            errors.append(f"{card.name}: caption_style needs >=2 bullets")
    else:
        errors.append(f"{card.name}: caption_style missing")

if errors:
    print('ERRORS:', len(errors))
    for e in errors:
        print('-', e)
    raise SystemExit(1)

print('OK: 0 errors')
