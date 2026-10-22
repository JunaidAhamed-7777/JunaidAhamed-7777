"""Official, unmodified bitmap artwork in profile-card SVG wrappers.

Source artwork is vendored in assets/brand; see sources.json for provenance.
Axiom uses actual game footage, encoded separately by build_axiom_gif.py.
"""

from base64 import b64encode
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def data_image(name):
    return "data:image/png;base64," + b64encode((ROOT / "assets" / "brand" / name).read_bytes()).decode("ascii")


def draintracer_card():
    # Original PNG from DrainTracer 73df0be9ad3b2b110fc7cc52f34283d4d77a414c.
    # The 1000px export contains a wide unused ink-colored area to the right.
    # The nested viewport omits only that empty area; all logo artwork and its
    # tagline remain intact, with the original PNG bytes embedded unchanged.
    source = data_image("draintracer-wordmark-dark.png")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="420" viewBox="0 0 720 420" role="img" aria-labelledby="title desc">
<title id="title">DrainTracer</title>
<desc id="desc">Official DrainTracer wordmark: a teal pipe leaks blue liquid into a tracing reticle. See what keeps growing.</desc>
<rect width="720" height="420" fill="#101820"/>
<svg x="48" y="107.6" width="624" height="204.8" viewBox="0 0 780 256" overflow="hidden">
<image width="1000" height="256" href="{source}"/>
</svg>
</svg>
'''


def modif_card():
    source = data_image("modif-logo.png")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="420" viewBox="0 0 720 420" role="img" aria-labelledby="title desc">
<title id="title">Modif.in</title>
<desc id="desc">Official Modif.in logo: a multicolored pixel M on black.</desc>
<rect width="720" height="420" fill="#000000"/>
<image x="210" y="60" width="300" height="300" preserveAspectRatio="xMidYMid meet" href="{source}"/>
</svg>
'''


def typeshift_card():
    # Original PNG from Type.Shift 80679e4a9999477e968bbbcd8ab9909bf0df3bea.
    source = data_image("typeshift-logo.png")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="420" viewBox="0 0 720 420" role="img" aria-labelledby="title desc">
<title id="title">Type.Shift</title>
<desc id="desc">Official Type.Shift logo: green T and dot, red S, and silver brackets on a dark background.</desc>
<rect width="720" height="420" fill="#040404"/>
<image x="163.265217" y="30.6" width="393.469565" height="358.8" preserveAspectRatio="xMidYMid meet" href="{source}"/>
</svg>
'''


def build_project_art():
    (ROOT / "assets" / "project-draintracer.svg").write_text(draintracer_card(), encoding="utf-8")
    (ROOT / "assets" / "project-modif.svg").write_text(modif_card(), encoding="utf-8")
    (ROOT / "assets" / "project-typeshift.svg").write_text(typeshift_card(), encoding="utf-8")


if __name__ == "__main__":
    build_project_art()
