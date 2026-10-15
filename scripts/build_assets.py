"""Build the profile artwork: python scripts/build_assets.py.

Requires fonttools. Display type uses the bundled OFL-licensed Barlow Condensed.
The masthead incorporates the original frame_0119.png without modifying it.
All exported SVGs are self-contained and work as GitHub README images.
"""

from base64 import b64encode
from html import escape
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
FONT = TTFont(Path(__file__).parent / "fonts" / "BarlowCondensed-Bold.ttf")
GLYPHS = FONT.getGlyphSet()
CMAP = FONT.getBestCmap()
UPM = FONT["head"].unitsPerEm
INK = "#eeede7"
MUTED = "#a4a7a0"
GREEN = "#b8d888"
DARK = "#101210"
PAPER = "#e9e7df"


def text(value, x, y, size=18, fill=MUTED, spacing=0, family="mono"):
    font = "Consolas,'Liberation Mono',monospace" if family == "mono" else "Arial,Helvetica,sans-serif"
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-family="{font}" letter-spacing="{spacing}">{escape(value)}</text>'


def display(value, x, y, size, fill=INK, width=None):
    pen = SVGPathPen(GLYPHS, ntos=lambda n: f"{n:.1f}".rstrip("0").rstrip("."))
    cursor = 0
    for char in value:
        glyph = GLYPHS[CMAP[ord(char)]]
        glyph.draw(TransformPen(pen, (1, 0, 0, 1, cursor, 0)))
        cursor += glyph.width
    sy = size / UPM
    sx = width / cursor if width else sy
    return f'<g aria-label="{escape(value)}" transform="translate({x} {y}) scale({sx:.6f} {-sy:.6f})"><path fill="{fill}" d="{pen.getCommands()}"/></g>'


def rect(x, y, width, height, fill="none", stroke="none", radius=0, sw=1):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def path(d, stroke=GREEN, sw=2, fill="none", extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


def circle(x, y, radius, fill=GREEN, stroke="none", sw=1):
    return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def save(name, width, height, title, body, background=DARK, description=None):
    value = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">\n'
        f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description or title)}</desc>\n'
        + rect(0, 0, width, height, background) + body + '\n</svg>\n'
    )
    OUT.mkdir(exist_ok=True)
    (OUT / f"{name}.svg").write_text(value, encoding="utf-8")


def hero(mobile=False):
    width, height = (640, 478) if mobile else (1200, 440)
    image = b64encode((ROOT / "frame_0119.png").read_bytes()).decode()
    body = text("JunaidAhamed-7777", 34 if mobile else 44, 42, 17, MUTED)
    body += text("India", width-92, 42, 17, MUTED)
    body += path(f"M{34 if mobile else 44} 62H{width-34 if mobile else width-44}", "#30332d", 1)
    if mobile:
        body += f'<image href="data:image/png;base64,{image}" x="270" y="269" width="370" height="208"/>'
        body += display("JUNAID", 29, 242, 220, width=484)
        body += display("AHAMED", 29, 402, 220, width=484)
    else:
        body += f'<image href="data:image/png;base64,{image}" x="596" y="90" width="604" height="340"/>'
        body += display("JUNAID", 38, 234, 215, width=514)
        body += display("AHAMED", 38, 393, 215, width=514)
    save("hero-mobile" if mobile else "hero", width, height, "Junaid Ahamed", body, "#000000",
         "Junaid Ahamed, India. Original green ASCII artwork of two reaching hands.")


def spotify():
    body = '<style>.external{stroke:#576050}@media(prefers-color-scheme:dark){.external{stroke:#a4a7a0}}</style>'
    body += circle(20, 22, 14, "#1db954")
    body += path("M11 18q9-5 19 1M12 23q8-4 16 1M14 28q6-3 12 0", DARK, 2)
    body += path("M50 27 60 17M50 17h10v10", MUTED, 1.5, extra='class="external"')
    save("spotify", 72, 44, "My Spotify playlist", body, "none")


def portfolio(mobile=False):
    width, height = (640, 154) if mobile else (1200, 106)
    body = '<style>.portfolio-arrow{animation:invite 5s ease-in-out infinite}@keyframes invite{0%,66%,100%{transform:translate(0,0)}80%{transform:translate(6px,-6px)}}@media(prefers-reduced-motion:reduce){.portfolio-arrow{animation:none}}</style>'
    body += display("VISIT MY PORTFOLIO", 32 if mobile else 40, 64 if mobile else 71,
                    56 if mobile else 60, DARK, width=458 if mobile else 480)
    body += text("junaidahamed.runs-on.dev", 34 if mobile else 670, 119 if mobile else 61,
                 23 if mobile else 20, DARK)
    x, y = (550, 46) if mobile else (1110, 34)
    body += '<g class="portfolio-arrow">' + path(f'M{x} {y+34}l34-34m-34 0h34v34', DARK, 3) + '</g>'
    save("portfolio-mobile" if mobile else "portfolio", width, height,
         "Visit my portfolio — junaidahamed.runs-on.dev", body, GREEN)


def gmail():
    body = '<style>.external{stroke:#576050}@media(prefers-color-scheme:dark){.external{stroke:#a4a7a0}}</style>'
    body += path('M6 31V13', "#4285f4", 4)
    body += path('M34 13V31', "#34a853", 4)
    body += path('M6 13 20 24 34 13', "#ea4335", 4)
    body += path('M50 27 60 17M50 17h10v10', MUTED, 1.5, extra='class="external"')
    save("gmail", 72, 44, "Email junuhammad2@gmail.com", body, "none",
         "Gmail contact button. Opens a new email addressed to junuhammad2@gmail.com.")


def static_variants():
    # Let the README's <picture> choose an explicitly static file. This also
    # covers browsers that don't propagate reduced-motion into SVG images.
    for name in ("portfolio", "portfolio-mobile", "project-draintracer", "project-typeshift"):
        source = (OUT / f"{name}.svg").read_text(encoding="utf-8")
        source = source.replace('</svg>', '<style>*{animation:none!important;transition:none!important}</style></svg>')
        (OUT / f"{name}-static.svg").write_text(source, encoding="utf-8")


if __name__ == "__main__":
    from project_art import build_project_art

    hero()
    hero(mobile=True)
    build_project_art(globals())
    spotify()
    portfolio()
    portfolio(mobile=True)
    gmail()
    static_variants()
    print("Built 14 profile assets, including static motion fallbacks.")
