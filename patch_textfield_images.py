from pathlib import Path
import re
path = Path(r'c:\Users\bishn\Downloads\Gurkha\newGurkhaindex.html')
text = path.read_text(encoding='utf-8')
old_css = '''        .text-field-img {
            position: absolute;
            bottom: 1.5rem;
            right: 1.5rem;
            width: clamp(110px, 20%, 165px);
            opacity: 0.18;
            filter: saturate(0.05) brightness(1.08);
            object-fit: contain;
            pointer-events: none;
            z-index: 0;
        }
'''
new_css = '''        .text-field-img-wrapper {
            position: absolute;
            inset: 0;
            z-index: 0;
            overflow: hidden;
            pointer-events: none;
        }
        .text-field-img-wrapper img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.16;
            filter: saturate(0.06) brightness(1.05);
            display: block;
        }
'''
if old_css not in text:
    raise SystemError('Expected text-field-img CSS block not found')
text = text.replace(old_css, new_css)
pattern = re.compile(r'<img\s+src="(Glass images/[^"]+)"\s+class="text-field-img"\s+alt="([^"]+)">')
text, count = pattern.subn(r'<div class="text-field-img-wrapper"><img src="\1" alt="\2"></div>', text)
if count == 0:
    raise SystemError('No text-field-img markup replacements were made')
path.write_text(text, encoding='utf-8')
print(f'Updated CSS and replaced {count} text-field-img markup occurrences')
