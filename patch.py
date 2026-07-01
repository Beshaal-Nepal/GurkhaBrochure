from pathlib import Path
import re
path = Path(r'c:\Users\bishn\Downloads\Gurkha\newGurkhaindex.html')
text = path.read_text(encoding='utf-8')
old = '''        /* Individual Page Colors */
        .page-2-bg { background-color: #f7f9f6; } /* Very light sage */
        .page-3-bg { background-color: #fdfbf7; } /* Warm ivory */
        .page-4-bg { background-color: #f4f6f8; } /* Pale slate blue */
        .page-5-bg { background-color: #fcf9f2; } /* Cream */
        .page-6-bg { background-color: #f8f6f5; } /* Misty rose tint */
        .page-7-bg { background-color: #f5f7fa; } /* Soft ice blue */
        .page-8-bg { background-color: #f9f8f4; } /* Light parchment */
        .page-9-bg { background-color: #f5f8f5; } /* Mint hint */
        .page-10-bg { background-color: #fbf7f5; } /* Blush sand */
        .page-11-bg { background-color: #f6f5f8; } /* Lavender whisper */
        .page-12-bg { background-color: #f8f9f6; } /* Light moss */
        .page-13-bg { background-color: #fdfaf6; } /* Alabaster */
        .page-14-bg { background-color: #f5f6f7; } /* Platinum */
        .page-15-bg { background-color: #faf8f5; } /* Linen */

        /* Seamless Sunglass Background on Text Pages */
        .watermark-bg {
            position: absolute;
            inset: 0;
            z-index: 0;
            background-size: cover;
            background-position: center;
            opacity: 0.12; /* Professional low-opacity for readability */
            mix-blend-mode: multiply;
            filter: grayscale(100%) contrast(120%);
            pointer-events: none;
        }
        .page-2-bg .watermark-bg,
        .page-3-bg .watermark-bg {
            opacity: 0.16;
            mix-blend-mode: normal;
            filter: grayscale(100%) contrast(85%) brightness(1.2);
            background-size: 120% auto;
            background-position: center 35%;
            background-repeat: no-repeat;
            transform: rotate(-8deg) scale(1.03);
            transform-origin: center center;
        }
'''
new = '''        /* Individual Page Colors */
        .page-2-bg { background-color: #edf4ee; } /* Sage silk */
        .page-3-bg { background-color: #fbf4e9; } /* Warm parchment */
        .page-4-bg { background-color: #eef2f6; } /* Mist blue */
        .page-5-bg { background-color: #f7f3ef; } /* Soft sand */
        .page-6-bg { background-color: #eef2ef; } /* Crisp moss */
        .page-7-bg { background-color: #f3f6f8; } /* Quiet sky */
        .page-8-bg { background-color: #faf6ee; } /* Golden ivory */
        .page-9-bg { background-color: #eef5f1; } /* Fog white */
        .page-10-bg { background-color: #fbf1e8; } /* Antique cream */
        .page-11-bg { background-color: #eef1f4; } /* Silver mist */
        .page-12-bg { background-color: #f4f3f8; } /* Lavender haze */
        .page-13-bg { background-color: #f1f4ef; } /* Cloud stone */
        .page-14-bg { background-color: #f7f7f7; } /* Soft pearl */
        .page-15-bg { background-color: #fcf7ee; } /* Cashmere */

        /* Seamless Sunglass Background on Text Pages */
        .watermark-bg {
            position: absolute;
            inset: 0;
            z-index: 0;
            background-size: cover;
            background-position: center;
            opacity: 0.12; /* Professional low-opacity for readability */
            mix-blend-mode: multiply;
            filter: grayscale(100%) contrast(120%);
            pointer-events: none;
        }
        .page-2-bg .watermark-bg,
        .page-3-bg .watermark-bg {
            opacity: 0.16;
            mix-blend-mode: normal;
            filter: grayscale(100%) contrast(85%) brightness(1.2);
            background-size: 120% auto;
            background-position: center 35%;
            background-repeat: no-repeat;
            transform: rotate(-8deg) scale(1.03);
            transform-origin: center center;
        }
        .text-field-img {
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
if old not in text:
    raise SystemError('Old CSS block not found')
text = text.replace(old, new)
pattern = re.compile(r'(<div class="watermark-bg"[^>]*><\/div>\s*\n)')
images = [
    'Glass images/Glass1.jpg',
    'Glass images/Glass2.jpg',
    'Glass images/Glass3.jpg',
    'Glass images/Glass4.jpg',
    'Glass images/Glass5.jpg',
    'Glass images/Glass6.jpg',
    'Glass images/Glass7.jpg',
    'Glass images/Glass8.jpg',
    'Glass images/Glass9.jpg',
    'Glass images/Glass10.jpg',
    'Glass images/Glass11.png',
    'Glass images/col1.jpeg',
    'Glass images/col2.jpeg',
    'Glass images/col3.jpeg',
]
count = {'v':0}
def repl(m):
    if count['v'] < len(images):
        out = m.group(1) + "                        <img src='" + images[count['v']] + "' class='text-field-img' alt='Glasses overlay'>\n"
        count['v'] += 1
        return out
    return m.group(1)
text, n = pattern.subn(repl, text)
path.write_text(text, encoding='utf-8')
print('updated', n, 'markers, inserted', count['v'], 'images')
