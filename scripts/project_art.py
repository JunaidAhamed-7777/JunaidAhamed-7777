"""Original, self-contained technical poster illustrations for the README.

The four cards are diagrams, not screenshots or live application telemetry.
`build_project_art(vars(build_assets))` shares the profile's type and SVG helpers.
"""

def build_project_art(api):
    get = api.get if isinstance(api, dict) else lambda name: getattr(api, name)
    text, display, rect, path, circle, save = (
        get(name) for name in ("text", "display", "rect", "path", "circle", "save")
    )
    ink, paper, sage = "#171b18", "#e9e7df", "#b9c9a0"
    warm = "#d49b7d"

    def polygon(points, fill, stroke="none", sw=1):
        return f'<polygon points="{points}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'

    def group(body, transform="", extra=""):
        return f'<g transform="{transform}" {extra}>{body}</g>'

    def frame(index, label, dark=True):
        fg, rule = ("#a6afa0", "#394037") if dark else ("#616957", "#c1c3b5")
        body = path("M30 44V30H44M676 30H690V44M30 376V390H44M676 390H690V376", rule, 1)
        body += text(label, 48, 45, 11, fg, 1.6)
        body += text(index, 648, 45, 11, fg, 1.4)
        return body

    def foot(left, right, dark=True):
        fg, rule = ("#8d9987", "#394037") if dark else ("#69715e", "#c1c3b5")
        return path("M48 372H672", rule, 1) + text(left, 48, 393, 10, fg, 1.6) + text(right, 539, 393, 10, fg, 1.2)

    # DrainTracer: memory is a physical, layered object; a single trace leaves
    # the stack, making the relationship legible even at a small card size.
    body = '<style>@keyframes follow-trace{to{stroke-dashoffset:-72}}.trace-flow{animation:follow-trace 3.6s linear infinite}@media(prefers-reduced-motion:reduce){.trace-flow{animation:none}}</style>'
    body += frame("01", "PROCESS / MEMORY")
    # Quiet construction grid and a narrow guide coordinate line.
    for x in range(84, 684, 36):
        for y in range(84, 354, 36):
            body += circle(x, y, .8, "#3b4338")
    body += path("M86 94V318", "#697760", 1.5)
    for y in (104, 172, 240, 308):
        body += path(f"M86 {y}H157", "#697760", 1.5)
        body += rect(76, y-10, 20, 20, ink, "#92a282", 1, 1.5)
        body += rect(82, y-4, 8, 8, sage)
    body += text("PID", 49, 81, 10, "#8d9987", 1)
    # Render from the lowest plate upward. Broad, carefully colored surfaces
    # retain the dimensional silhouette when the image is reduced on mobile.
    slabs = [(235, "#394738", "#242e25", "#2c382b"),
             (180, "#53644b", "#32422e", "#405039"),
             (125, sage, "#6c7f56", "#8b9e72"),
             (70, "#d9dfcc", "#879879", "#a4b28f")]
    for y, top, left, right in slabs:
        body += polygon(f"196,{y+22} 407,{y-24} 605,{y+75} 394,{y+121}", "#0b0f0c")
        body += polygon(f"196,{y} 394,{y+99} 394,{y+121} 196,{y+22}", left, "#11170f", 1)
        body += polygon(f"394,{y+99} 605,{y+53} 605,{y+75} 394,{y+121}", right, "#11170f", 1)
        body += polygon(f"196,{y} 407,{y-46} 605,{y+53} 394,{y+99}", top, "#11170f", 1.5)
        body += path(f"M215 {y+1} 396 {y+91} 589 {y+49}", "#eff1df" if y == 70 else "#81916f", 1)
        # Slot marks on the right-hand face.
        for x in range(438, 580, 18):
            yy = y+99-(x-394)*46/211
            body += path(f"M{x} {yy+6}v7", "#25341f" if y < 180 else "#1b241b", 2)
    # A custom top-surface register: the affine transform follows the plate.
    top_art = rect(0, 0, 185, 85, "none", "#7c8b6a", 1, 1.4)
    top_art += rect(7, 7, 171, 71, "#c7d1b6", "#a0ad8a", 1, 1)
    top_art += display("PY", 22, 63, 66, ink, width=66)
    for y in (22, 36, 50, 64):
        top_art += rect(108, y, 49 if y != 50 else 31, 4, "#788b62")
    body += group(top_art, "matrix(.98 .49 -1.07 .233 346 50)")
    # Trace exits a single plate. An animated dash follows the path rather
    # than suggesting that these decorative marks are real resource data.
    trace_d = "M574 181 637 167V292H590"
    body += path(trace_d, "#614f41", 2)
    body += path(trace_d, warm, 3, extra='class="trace-flow" stroke-dasharray="16 20"')
    body += circle(574, 181, 6, warm)
    body += circle(590, 292, 6, ink, warm, 2)
    body += text("TRACE", 586, 328, 11, warm, 2)
    body += foot("PROCESS TREE", "LEAK TRACING")
    save("project-draintracer", 720, 420, "DrainTracer — process trees and leak tracing", body, ink,
         "An illustrative stack of process memory plates, connected to a process tree. A warm dashed trace moves from one layer to a marked endpoint. This is artwork, not live telemetry.")

    # Emotion Detector: a face constructed as a cut-paper sculpture. The
    # facial landmarks become a score line and enter a record's grooves.
    body = '<defs><clipPath id="face-clip"><path d="M152 102Q176 62 222 66Q284 65 309 118L319 205Q315 263 282 299L239 330Q211 339 184 315L150 273Q132 241 133 188Z"/></clipPath></defs>'
    body += frame("02", "EXPRESSION / SOUND", False)
    # Offset circular geometry is the music surface; a wide paper cut keeps
    # the two subjects separate while the continuous guide joins them.
    body += circle(537, 211, 139, ink)
    for r in (128, 123, 117, 111, 104, 98, 90, 84, 78):
        body += circle(537, 211, r, "none", "#3a4337", 1)
    body += circle(537, 211, 62, sage)
    body += circle(537, 211, 16, paper)
    body += circle(537, 211, 5, ink)
    # Record sleeve details, avoiding playback or live-status UI.
    body += path("M478 201H514M560 220h35", "#61724e", 1)
    body += text("SIDE A", 515, 180, 8, "#526044", 1.2)
    body += text("MUSIC", 520, 246, 8, "#526044", 1)
    # The head's flat facets: intentional asymmetry gives this a human,
    # editorial illustration character rather than a symmetric wireframe.
    body += path("M152 102Q176 62 222 66Q284 65 309 118L319 205Q315 263 282 299L239 330Q211 339 184 315L150 273Q132 241 133 188Z", ink, 0, ink)
    facets = polygon("222,61 320,100 321,218 245,187 204,152", "#829774")
    facets += polygon("245,187 321,218 283,301 230,331 225,249", sage)
    facets += polygon("135,187 204,152 191,244 152,275", "#303b2e")
    facets += polygon("191,244 225,249 230,331 174,308", "#56674b")
    facets += path("M223 119 245 187 227 221 249 229", "#e0e5d4", 2)
    facets += path("M164 166q23-15 44-2M258 160q23-11 39 3", "#e0e5d4", 3)
    facets += path("M197 272q29 17 64-4", "#d1dabc", 3)
    body += group(facets, extra='clip-path="url(#face-clip)"')
    # The landmark network stays focused on the face, with open circles and
    # small crosshairs borrowed from photographic registration marks.
    body += path("M154 132 188 162 226 145 276 159 306 129M188 162 201 224 227 232 259 221 276 159M160 270 201 257 258 258 291 272M201 257 229 285 258 258M226 145 227 232", "#b7c3a6", 1.2)
    for x, y in ((154,132),(188,162),(226,145),(276,159),(306,129),(201,224),(227,232),(259,221),(160,270),(201,257),(258,258),(291,272),(229,285)):
        body += circle(x, y, 4, paper, ink, 1.2)
    body += path("M119 106V82h24M295 82h24v24M119 294v24h24M295 318h24v-24", "#939e87", 1.5)
    # Sound transduction appears as a broad, measured bridge, with a few
    # crisp bars that remain visible at the smallest two-column layout.
    body += path("M306 211H471", "#9ca68f", 1)
    for x, height in [(341,24),(352,44),(363,65),(374,87),(385,67),(396,43),(407,26),(418,53),(429,73),(440,46),(451,25)]:
        body += rect(x, 211-height/2, 5, height, "#798b65", radius=2)
    body += foot("FACIAL LANDMARKS", "MUSIC MATCH", False)
    save("project-emotion-detector", 720, 420, "Emotion Detector — expression to music", body, paper,
         "A sculptural face with facial landmarks is connected by a sound waveform to the grooves of a record. An illustration of webcam emotion detection and music recommendations.")

    # Heimdall: a workspace arranged as a compact piece of architecture.
    # The calendar is the main plane; tasks and habits are tactile overlays.
    body = frame("03", "TASKS / HABITS / TIME")
    # Wide shadow forms and offset paper sheets establish depth without
    # glows, gradients, or generic application-window chrome.
    body += polygon("103,123 504,77 617,316 218,355", "#080c09")
    body += group(rect(0, 0, 405, 254, "#4e5e45", "#65745b", 2, 1), "translate(110 104) rotate(-6)")
    body += group(rect(0, 0, 405, 254, "#87997a", "#adbca1", 2, 1), "translate(132 89) rotate(-2)")
    sheet = rect(0, 0, 405, 254, paper, "#e0e4d5", 2, 1)
    sheet += rect(0, 0, 405, 45, "#c5ceb8", radius=2)
    sheet += display("WEEK", 21, 34, 33, ink, width=79)
    sheet += text("M   T   W   T   F", 189, 29, 11, "#4e6044", 1)
    # Calendar as broad modular blocks; no pretend date or activity counts.
    for x in (20, 93, 166, 239, 312, 385):
        sheet += path(f"M{x} 59V235", "#b5bdab", 1)
    for y in (59, 103, 147, 191, 235):
        sheet += path(f"M20 {y}H385", "#b5bdab", 1)
    sheet += rect(25, 65, 136, 32, "#7f936e", radius=2)
    sheet += rect(171, 109, 62, 75, "#afbd9c", radius=2)
    sheet += rect(244, 153, 136, 32, "#506743", radius=2)
    sheet += rect(98, 197, 136, 32, "#b7c2a6", radius=2)
    sheet += path("M37 80H84M256 168h73", "#d9e1cc", 2)
    body += group(sheet, "translate(153 73) rotate(4)")
    # Two binding loops make the central object an unmistakable planner.
    body += path("M281 73v24q0 9 8 9t8-9V74M474 87v24q0 9 8 9t8-9V88", "#1a2418", 6)
    body += path("M279 70v24q0 9 8 9t8-9V71M472 84v24q0 9 8 9t8-9V85", "#acba9e", 3)
    # A dark, oversized task tile overlays the corner. The check is a
    # graphic symbol, not an assertion about a user's task completion.
    tile = rect(0, 0, 154, 145, "#090e0a", "#7b8c6c", 3, 1.5)
    tile += rect(14, 14, 126, 117, "#202d1e", "#455b3c", 2, 1)
    tile += path("M37 73 65 97 116 43", sage, 13)
    tile += path("M20 123h32", "#586f4b", 2)
    body += group(tile, "translate(483 195) rotate(9)")
    # Repetition strip is the habit motif, laid over the calendar's left.
    habits = rect(0, 0, 57, 169, "#cfdbbd", "#1b2517", 1, 1)
    for i in range(5):
        habits += circle(28.5, 24+i*30, 7, "#3a4d30" if i < 3 else "none", "#5d734e", 1.5)
    body += group(habits, "translate(78 170) rotate(-9)")
    body += foot("TASKS / HABITS", "SCHEDULING")
    save("project-heimdall", 720, 420, "Heimdall — a workspace for tasks, habits, and scheduling", body, ink,
         "An architectural stack of planner pages, with a weekly grid, a repeating habit strip, and an oversized checkmark tile. Decorative artwork for a Google Workspace productivity companion.")

    # TypeShift: large dimensional keycaps set against a timing scale. WPM
    # is a unit label, deliberately shown without an invented score.
    body = '<style>@keyframes keypress{0%,30%,55%,100%{transform:translateY(0)}38%,47%{transform:translateY(7px)}}.key-cap{animation:keypress 4.8s ease-in-out infinite}@media(prefers-reduced-motion:reduce){.key-cap{animation:none}}</style>'
    body += frame("04", "KEYSTROKES / SPEED", False)
    body += display("WPM", 43, 214, 183, "#b8bdae", width=321)
    body += text("WORDS PER MINUTE", 49, 243, 11, "#737e65", 2)
    # Instrument-style ticks show the act of measurement without fabricating
    # a metric. One extended mark anchors the horizontal baseline.
    body += path("M49 299H330", "#9eaa90", 1.3)
    for i, x in enumerate(range(49, 331, 14)):
        body += path(f"M{x} 299v{-22 if i%5==0 else -9}", "#829173", 1)
    body += path("M259 274v48", ink, 3)
    body += polygon("253,270 265,270 259,278", ink)

    def key(x, y, width, height, label=None, active=False, return_key=False):
        # Complete shell remains static; the inset cap is the moving part.
        shadow = rect(5, 10, width, height, "#b3b9a7", radius=16)
        shell = rect(0, 0, width, height, "#182019", "#0c110d", 16, 1.5)
        shell += path(f"M12 {height-17}H{width-12}", "#43553b", 2)
        shell += path(f"M{width-10} 24V{height-21}", "#55664b", 2)
        cap = rect(9, 8, width-18, height-27, sage if active else "#2c3929", "#e0e6d4" if active else "#5f7155", 11, 1)
        cap += path(f"M20 17H{width-22}", "#d6dfc9" if active else "#7d8c72", 1)
        if label:
            cap += display(label, 26, height-45, 79 if len(label)==1 else 39, ink if active else paper, width=54 if len(label)==1 else width-52)
        if return_key:
            cap += path(f"M{width-36} 36v38H31m17-17L31 74l17 17", paper, 6)
        return group(shadow+shell+group(cap, extra='class="key-cap"' if active else ""), f"translate({x} {y})")

    # The whole keyboard fragment is angled as one object; key faces remain
    # parallel and the depression stays local to the highlighted cap.
    keys = key(0, 0, 126, 137, "A", active=True)
    keys += key(137, 0, 126, 137, "S")
    keys += key(38, 148, 225, 120, return_key=True)
    body += group(keys, "translate(378 54) rotate(10)")
    # A clean return route under the keys gives the composition a deliberate
    # directional ending, rather than another floating decorative icon.
    body += path("M352 335H466", "#879879", 1.2)
    body += circle(345, 335, 3, "#647b55")
    body += foot("TYPING SPEED CHECKER", "KEY BY KEY", False)
    save("project-typeshift", 720, 420, "TypeShift — typing speed checker", body, paper,
         "Oversized A, S, and return keycaps sit beside a words-per-minute unit label and an unnumbered measurement scale. The A key gently depresses. This is illustrative artwork, not a reported typing score.")
