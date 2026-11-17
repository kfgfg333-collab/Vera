import json, math, random, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, zlib

D = sys.argv[1]
W, H, FPS = 720, 1280, 60
TL = json.load(open(f"{D}/timeline.json"))
S = TL["sent"]; TOTAL = TL["total"]
FONT = f"{D}/fonts/M.ttf"
_fc = {}
def F(size, weight="ExtraBold"):
    k = (size, weight)
    if k not in _fc:
        f = ImageFont.truetype(FONT, size)
        try: f.set_variation_by_name(weight)
        except Exception: pass
        _fc[k] = f
    return _fc[k]
SYM = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 170)

YEL = (255, 210, 30); RED = (226, 44, 52); GRN = (60, 205, 110); WHITE = (245, 245, 245)
NAVY = (14, 22, 44); PANEL = (20, 30, 60); BORDER = (70, 100, 170)

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease_out(x): x = clamp(x); return 1 - (1 - x) ** 3
def back(x):
    x = clamp(x); c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2
def lerp(a, b, t): return a + (b - a) * t

# ---------- static background ----------
def make_bg(tint):
    bg = Image.new("RGB", (W, H), (5, 7, 14))
    d = ImageDraw.Draw(bg)
    for i in range(60):
        r = int(900 - i * 14)
        c = tuple(int(lerp(v * 0.25, v, i / 60)) for v in tint)
        d.ellipse([W // 2 - r, 420 - r, W // 2 + r, 420 + r], fill=c)
    bg = bg.filter(ImageFilter.GaussianBlur(40))
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); o = ImageDraw.Draw(ov)
    o.polygon([(W // 2 - 70, -10), (W // 2 + 70, -10), (W // 2 + 260, 1010), (W // 2 - 260, 1010)], fill=(255, 255, 255, 26))
    ov = ov.filter(ImageFilter.GaussianBlur(28))
    bg = Image.alpha_composite(bg.convert("RGBA"), ov)
    fl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); f = ImageDraw.Draw(fl)
    for i in range(260):
        f.line([(0, 1000 + i), (W, 1000 + i)], fill=(0, 0, 0, min(255, int(i * 1.2))))
    f.rectangle([0, 1260, W, H], fill=(0, 0, 0, 255))
    return Image.alpha_composite(bg, fl)
BGS = {k: make_bg(v) for k, v in {"blue": (30, 55, 120), "red": (120, 25, 35), "green": (25, 95, 60), "gold": (120, 90, 25), "sepia": (110, 80, 45)}.items()}
random.seed(3)
DUST = [(random.uniform(0, W), random.uniform(0, 1100), random.uniform(0.5, 2.2), random.uniform(0, 6.28)) for _ in range(90)]

# ---------- drawing helpers ----------
def text_c(d, xy, s, size, fill=WHITE, weight="ExtraBold", stroke=0, sfill=(0, 0, 0), anchor="mm"):
    d.text(xy, s, font=F(size, weight), fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=sfill)

def panel(img, box, alpha=255, border=BORDER, fill=PANEL, r=18, glow=True):
    x0, y0, x1, y1 = box
    if glow:
        g = Image.new("RGBA", img.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
        gd.rounded_rectangle([x0 - 6, y0 - 6, x1 + 6, y1 + 6], r + 6, fill=border + (int(70 * alpha / 255),))
        img.alpha_composite(g.filter(ImageFilter.GaussianBlur(10)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle(box, r, fill=fill + (alpha,), outline=border + (alpha,), width=3)

def tag(img, cx, cy, s, col=RED, size=34, p=1.0):
    if p <= 0: return
    f = F(size, "Black"); tw = f.getbbox(s)[2] + 44; th = size + 24
    sc = back(p); w, h = tw * sc, th * sc
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], 10, fill=col + (255,))
    if sc > 0.6: d.text((cx, cy), s, font=F(max(8, int(size * sc)), "Black"), fill=WHITE, anchor="mm")

def stamp(img, cx, cy, s, col=RED, size=70, p=1.0, ang=-12):
    if p <= 0: return
    f = F(size, "Black"); tw = f.getbbox(s)[2] + 60; th = size + 40
    lay = Image.new("RGBA", (tw + 20, th + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([10, 10, 10 + tw, 10 + th], 14, outline=col + (255,), width=8)
    d.text((10 + tw / 2, 10 + th / 2), s, font=f, fill=col + (255,), anchor="mm")
    sc = lerp(2.2, 1.0, ease_out(p * 1.6)); a = clamp(p * 3)
    lay = lay.resize((int(lay.width * sc), int(lay.height * sc)), Image.BICUBIC).rotate(ang, expand=True, resample=Image.BICUBIC)
    if a < 1:
        al = lay.getchannel("A").point(lambda v: int(v * a)); lay.putalpha(al)
    img.alpha_composite(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)))

def silhouette(d, cx, cy, s=1.0, col=(40, 48, 70), outline=None):
    d.ellipse([cx - 34 * s, cy - 110 * s, cx + 34 * s, cy - 42 * s], fill=col, outline=outline, width=3 if outline else 0)
    d.rounded_rectangle([cx - 62 * s, cy - 40 * s, cx + 62 * s, cy + 70 * s], int(40 * s), fill=col, outline=outline, width=3 if outline else 0)

def flag(d, x, y, kind, w=60, h=40):
    if kind == "dk":
        d.rectangle([x, y, x + w, y + h], fill=(198, 12, 48)); d.rectangle([x + w * 0.28, y, x + w * 0.4, y + h], fill=WHITE); d.rectangle([x, y + h * 0.42, x + w, y + h * 0.58], fill=WHITE)
    elif kind == "mn":
        d.rectangle([x, y, x + w, y + h], fill=(196, 39, 47)); d.rectangle([x + w / 3, y, x + 2 * w / 3, y + h], fill=(1, 87, 155)); d.rectangle([x + w * 0.12, y + h * 0.3, x + w * 0.22, y + h * 0.75], fill=(249, 207, 2))
    elif kind == "au":
        d.rectangle([x, y, x + w, y + h], fill=(0, 33, 125))
        for (a, b) in [(0.7, 0.3), (0.82, 0.55), (0.62, 0.7), (0.3, 0.75)]:
            d.ellipse([x + w * a - 3, y + h * b - 3, x + w * a + 3, y + h * b + 3], fill=WHITE)
        d.rectangle([x, y, x + w * 0.45, y + h * 0.5], fill=(10, 50, 150)); d.line([x, y, x + w * 0.45, y + h * 0.5], fill=WHITE, width=3); d.line([x, y + h * 0.5, x + w * 0.45, y], fill=WHITE, width=3)
    elif kind == "ua":
        d.rectangle([x, y, x + w, y + h / 2], fill=(0, 87, 183)); d.rectangle([x, y + h / 2, x + w, y + h], fill=(255, 215, 0))
    d.rectangle([x, y, x + w, y + h], outline=(0, 0, 0), width=2)

def meter(img, cy, val, col, label):
    panel(img, (90, cy - 120, 630, cy + 120))
    d = ImageDraw.Draw(img)
    text_c(d, (360, cy - 75), label, 30, (200, 210, 235))
    text_c(d, (360, cy - 10), f"{int(round(val))}%", 92, col, "Black", 4)
    d.rounded_rectangle([130, cy + 55, 590, cy + 85], 14, fill=(40, 48, 75))
    d.rounded_rectangle([130, cy + 55, 130 + max(28, 460 * val / 100), cy + 85], 14, fill=col)

def scoreboard(img, cy, left, right, mid="VS", lcol=(255, 160, 30), rcol=(90, 170, 255), p=1.0, top=None):
    sc = back(p)
    if sc <= 0.05: return
    w = 560 * sc; h = 170 * sc
    panel(img, (360 - w / 2, cy - h / 2, 360 + w / 2, cy + h / 2))
    if sc < 0.7: return
    d = ImageDraw.Draw(img)
    if top: text_c(d, (360, cy - 58), top, 22, (170, 185, 220), "Bold")
    text_c(d, (205, cy + 10), left, 44, lcol, "Black"); text_c(d, (515, cy + 10), right, 44, rcol, "Black")
    text_c(d, (360, cy + 10), mid, 40, WHITE, "Black")

def red_x(d, cx, cy, r, p):
    if p <= 0: return
    q = ease_out(p)
    d.line([cx - r, cy - r, cx - r + 2 * r * q, cy - r + 2 * r * q], fill=RED, width=12)
    if p > 0.5:
        q2 = ease_out((p - 0.5) * 2); d.line([cx + r, cy - r, cx + r - 2 * r * q2, cy - r + 2 * r * q2], fill=RED, width=12)

def wtime(si, k):
    """absolute start time of k-th word of sentence si"""
    w = S[si]["abs"]; return w[min(k, len(w) - 1)][0]

# ---------- reference art ----------
REF = f"{D}/refs/cut"
_IC = {}
def _load(name):
    if name not in _IC: _IC[name] = Image.open(f"{REF}/{name}.png").convert("RGBA")
    return _IC[name]
_ICS = {}
CUR = {"t": 0.0, "si": 0, "lt": 0.0, "cam": (0.0, 0.0)}
def ease_io(x): x = clamp(x); return x * x * (3 - 2 * x)
def _icon_img(name, hh, gray):
    key = (name, hh, gray)
    if key not in _ICS:
        src = _load(name); w = max(4, int(src.width * hh / src.height))
        im = src.resize((w, hh), Image.LANCZOS)
        if gray:
            a = im.getchannel("A"); im = im.convert("L").convert("RGBA"); im = Image.blend(im, Image.new("RGBA", im.size, (40, 40, 50, 255)), 0.35); im.putalpha(a)
        if len(_ICS) > 600: _ICS.clear()
        _ICS[key] = im
    return _ICS[key]
def _put(img, im, cx, cy, ang, a, glow):
    if ang: im = im.rotate(ang, expand=True, resample=Image.BICUBIC)
    if a < 1:
        im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
    x, y = int(cx - im.width / 2), int(cy - im.height / 2)
    if glow:
        g = Image.new("RGBA", (im.width + 60, im.height + 60), (0, 0, 0, 0))
        sh = Image.new("RGBA", im.size, (0, 0, 0, 255)); sh.putalpha(im.getchannel("A").point(lambda v: int(v * 0.55)))
        g.alpha_composite(sh, (30, 38)); img.alpha_composite(g.filter(ImageFilter.GaussianBlur(12)), (x - 30, y - 30))
    img.alpha_composite(im, (x, y))
def icon(img, name, cx, cy, h, p=1.0, ang=0, glow=True, alpha=1.0, gray=False):
    if p <= 0: return
    t = CUR["t"]; cam = CUR["cam"]; seed = zlib.crc32(name.encode()) % 97
    side = -1 if seed % 2 else 1
    def pose(pp):
        e = ease_out(pp)
        x = cx + cam[0] * 0.6 + math.sin(t * 0.9 + seed) * 1.5 + side * (1 - e) * 60
        y = cy + cam[1] * 0.6 + math.sin(t * 1.1 + seed) * 2 + (1 - e) * 100 - math.sin(e * math.pi) * 25
        r = ang + math.sin(t * 0.8 + seed) * 0.6 + side * (1 - e) * 12
        return x, y, r
    if p < 1:  # motion trail
        for k, ga in ((0.16, 0.18), (0.08, 0.32)):
            pp = p - k
            if pp > 0:
                x, y, r = pose(pp); hh = max(4, int(h * back(pp)) // 2 * 2)
                _put(img, _icon_img(name, hh, gray), x, y, r, ga * alpha * clamp(pp * 3), False)
    x, y, r = pose(p); hh = max(4, int(h * back(p)) // 2 * 2) if p < 1 else int(h)
    _put(img, _icon_img(name, hh, gray), x, y, r, clamp(p * 3) * alpha, glow)

# character: pose busts (refs2) with team patch swap, or full-body kits
POSE = {"calm": "p_calm", "worried": "p_puzzled", "angry": "p_angry", "smirk": "p_smirk", "conf": "p_conf", "shock": "p_shock", "point": "p_point"}
POSE_PATCH = {"p_calm": (78, 190, 148, 253), "p_conf": (75, 184, 138, 209), "p_puzzled": (94, 196, 162, 256), "p_angry": (93, 192, 172, 263),
              "p_smirk": (75, 185, 155, 240), "p_shock": (95, 185, 170, 240), "p_point": (110, 195, 180, 256)}
KIT = {"BC.GAME": "k_bc", "GOSH": "k_gosh", "LIQUID": "k_liquid"}
TEAM_ICON = {"BC.GAME": "bcgame", "GOSH": "gosh", "LIQUID": "liquid", "NAVI": None, "???": "?"}
_CH = {}
def _fade(src, frac):
    a = np.array(src.getchannel("A")).astype(np.float32); H = a.shape[0]
    f = np.clip((H - np.arange(H)) / (H * frac), 0, 1)[:, None]; src.putalpha(Image.fromarray((a * f).astype(np.uint8))); return src
def _sprite(badge, mood):
    key = (badge, mood)
    if key in _CH: return _CH[key]
    if mood == "full":
        src = _load(KIT.get(badge, "k_bc")).copy(); src = src.crop((0, 0, src.width, int(src.height * 0.6))); src = _fade(src, 0.22)
    else:
        name = POSE[mood]; src = _load(name).copy()
        kind = TEAM_ICON.get(badge)
        if kind is not None:
            x0, y0, x1, y1 = POSE_PATCH[name]; d = ImageDraw.Draw(src); jc = (25, 26, 35, 255)
            d.rounded_rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2], 4, fill=jc)
            if kind == "?":
                d.text(((x0 + x1) / 2, (y0 + y1) / 2), "?", font=F(int((y1 - y0) * 0.9), "Black"), fill=(210, 210, 210), anchor="mm")
            else:
                lg = _load(kind); bw, bh = x1 - x0, y1 - y0
                r = min(bw / lg.width, bh / lg.height); lg = lg.resize((max(1, int(lg.width * r)), max(1, int(lg.height * r))), Image.LANCZOS)
                src.alpha_composite(lg, (int((x0 + x1) / 2 - lg.width / 2), int((y0 + y1) / 2 - lg.height / 2)))
        src = _fade(src, 0.16)
    _CH[key] = src; return src
_CHS = {}
def character(img, cx, cy, s=1.0, badge="BC.GAME", t=0.0, mood="calm", bcol=None):
    t = CUR["t"]; lt = CUR["lt"]; cam = CUR["cam"]
    base = 560 if mood == "full" else 470
    hh = int(base * s); key = (badge, mood, hh)
    if key not in _CHS:
        sp = _sprite(badge, mood); w = int(sp.width * hh / sp.height)
        if len(_CHS) > 300: _CHS.clear()
        _CHS[key] = sp.resize((w, hh), Image.LANCZOS)
    sp = _CHS[key]
    beat = 0.0
    for a_, b_, w_ in S[CUR["si"]]["abs"]:
        if a_ <= t: beat = math.exp(-(t - a_) * 9)
    spring = math.exp(-lt * 4) * math.cos(lt * 10)
    breath = math.sin(t * 2.2)
    sy = 1 + 0.03 * spring + 0.006 * beat + 0.006 * breath
    sx = 1 - 0.022 * spring - 0.004 * beat
    lean = math.sin(t * 0.6) * 1.0 + (math.sin(t * 9) * 0.5 if mood == "angry" else 0)
    w2, h2 = max(4, int(sp.width * sx)), max(4, int(sp.height * sy))
    im = sp.resize((w2, h2), Image.BILINEAR)
    pad = Image.new("RGBA", (w2 + 80, h2 + 40), (0, 0, 0, 0)); pad.alpha_composite(im, (40, 40))
    im = pad.rotate(lean, center=(pad.width / 2, pad.height), resample=Image.BICUBIC)
    bottom = cy - 215 * s + base * s + cam[1] + math.sin(t * 1.6) * 1.5
    x = int(cx - im.width / 2 + cam[0] + math.sin(t * 0.6) * 2); y = int(bottom - im.height)
    g = Image.new("RGBA", (im.width + 80, im.height + 80), (0, 0, 0, 0))
    rim = Image.new("RGBA", im.size, (255, 220, 120, 255)); rim.putalpha(im.getchannel("A").point(lambda v: int(v * 0.35)))
    g.alpha_composite(rim, (40, 40)); img.alpha_composite(g.filter(ImageFilter.GaussianBlur(16)), (x - 40, y - 40))
    img.alpha_composite(im, (x, y))

BRUSH = {YEL: "b_yel", RED: "b_red", WHITE: "b_white"}
def tape(img, cx, cy, s, ang=-6, col=YEL, tcol=(15, 15, 15), size=40, p=1.0):
    """brush-stroke label from the reference brushes"""
    if p <= 0: return
    f = F(size, "Black"); tw = int(f.getbbox(s)[2] * 1.3) + 110; th = int(size * 2.3)
    br = _load(BRUSH.get(col, "b_yel")).resize((tw, th), Image.LANCZOS)
    lay = Image.new("RGBA", (tw + 20, th + 20), (0, 0, 0, 0))
    sh = Image.new("RGBA", br.size, (0, 0, 0, 255)); sh.putalpha(br.getchannel("A").point(lambda v: int(v * 0.5)))
    lay.alpha_composite(sh, (14, 16)); lay = lay.filter(ImageFilter.GaussianBlur(5)); lay.alpha_composite(br, (6, 6))
    ImageDraw.Draw(lay).text((6 + tw / 2, 6 + th / 2), s, font=f, fill=tcol, anchor="mm", stroke_width=3, stroke_fill=col)
    sc = back(p); t = CUR["t"]; cam = CUR["cam"]
    ang = ang + (1 - ease_out(p)) * 8 + math.sin(t * 1.0 + len(s)) * 0.5
    cx += cam[0] * 0.7 + (1 - ease_out(p)) * -80; cy += cam[1] * 0.7
    lay = lay.resize((max(1, int(lay.width * sc)), max(1, int(lay.height * sc))), Image.BICUBIC).rotate(ang, expand=True, resample=Image.BICUBIC)
    img.alpha_composite(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)))

# ---------- scenes ----------
def scene(img, si, t, lt, dur):
    d = ImageDraw.Draw(img)
    pin = lambda delay=0.0, length=0.35: clamp((lt - delay) / length)
    wt = lambda k: wtime(si, k) - S[si]["start"]
    fl = math.sin(t * 1.2) * 3
    if si == 0:
        icon(img, "region", 360, 300 + fl, 190, pin(0.05))
        tag(img, 360, 450, "РЕГИОН СМЕНЁН", RED, 34, pin(wt(3)))
        character(img, 360, 780, 1.0, "BC.GAME", t, "calm")
    elif si == 1:
        icon(img, "bcgame", 360, 300 + fl, 210, pin(0.05))
        p = pin(wt(3), 0.3)
        if p > 0: d = ImageDraw.Draw(img); d.line([150, 300, 150 + 420 * ease_out(p), 300 - 40 * ease_out(p)], fill=RED, width=16)
        tape(img, 360, 460, "НОВОЕ НАЗВАНИЕ?", -5, YEL, size=36, p=pin(wt(3) + 0.2))
        character(img, 360, 790, 0.95, "BC.GAME", t, "worried")
    elif si == 2:
        icon(img, "cal2026", 360, 320 + fl, 280, pin(0.05), ang=-4)
        character(img, 360, 800, 0.9, "BC.GAME", t, "full")
    elif si == 3:
        icon(img, "bcgame", 180, 250, 130, pin(0.05), ang=6)
        pts = [(270 + i * 50, 200 + (i % 2) * 30 + i * 30) for i in range(8)]
        n = int(len(pts) * clamp(lt / max(0.5, dur - 0.6))) + 1
        d = ImageDraw.Draw(img); d.line(pts[:max(2, n)], fill=RED, width=12, joint="curve")
        if n >= 2:
            x, y = pts[min(n, len(pts)) - 1]; d.polygon([(x - 22, y - 6), (x + 20, y - 6), (x, y + 28)], fill=RED)
        tag(img, 360, 520, "ВСЁ КАТИТСЯ ВНИЗ", RED, 32, pin(wt(6)))
        character(img, 360, 820, 0.9, "BC.GAME", t, "shock")
    elif si == 4:
        text_c(d, (360, 190), "ОТКРЫТЫЕ КВАЛИФИКАЦИИ", 32, (220, 225, 240), "Black", 3)
        icon(img, "quals6", 360, 420 + fl, 340, pin(0.05), ang=-3)
        d = ImageDraw.Draw(img)
        for i in range(6):
            x = 135 + i * 90
            red_x(d, x, 680, 26, clamp((lt - 0.4 - i * (dur - 1.4) / 6) / 0.3))
        tape(img, 360, 820, "6 ВЫЛЕТОВ ПОДРЯД", -4, RED, WHITE, 40, pin(dur - 1.0))
    elif si == 5:
        text_c(d, (360, 180), "ПОСЛЕДНЯЯ КВАЛИФИКАЦИЯ", 30, (225, 230, 245), "Black", 3)
        icon(img, "i_score", 360, 275, 110, pin(0.05), ang=-3)
        icon(img, "dk83", 360, 440 + fl, 150, pin(0.35), ang=-5)
        tag(img, 360, 560, "ВЫЛЕТ", RED, 40, pin(wt(4)))
        character(img, 360, 850, 0.8, "BC.GAME", t, "angry")
    elif si == 6:
        text_c(d, (360, 190), "ШАНС НА МЕЙДЖОР", 40, WHITE, "Black", 4)
        icon(img, "pct9", 360, 360 + fl, 270, pin(0.25))
        character(img, 360, 820, 0.85, "BC.GAME", t, "worried")
    elif si == 7:
        for r in range(4):
            for c in range(6):
                col = (60, 70, 100) if (r + c) % 2 else (30, 36, 58)
                d.rectangle([90 + c * 90, 180 + r * 90, 180 + c * 90, 270 + r * 90], fill=col)
        p = ease_out(pin(0.2, max(0.4, dur - 0.6)))
        path = [(135, 495), (135, 315), (315, 315)]
        if p < 0.6: x, y = lerp(path[0][0], path[1][0], p / 0.6), lerp(path[0][1], path[1][1], p / 0.6)
        else: q = (p - 0.6) / 0.4; x, y = lerp(path[1][0], path[2][0], q), path[1][1]
        icon(img, "i_knight", x, y, 120, 1.0, glow=False)
        tape(img, 360, 650, "ХОД КОНЁМ", -5, YEL, size=46, p=pin(0.5))
        character(img, 360, 920, 0.65, "BC.GAME", t, "smirk")
    elif si == 8:
        tag(img, 360, 180, "22 СЕНТЯБРЯ", RED, 34, pin(0))
        icon(img, "navi", 360, 290, 100, pin(0.1), glow=False)
        icon(img, "portrait", 200, 500 + fl, 210, pin(0.2), ang=-3)
        drop = ease_out(clamp((t - wtime(8, 4)) / 0.6))
        icon(img, "electronic", 520, lerp(500, 720, drop), 210, pin(0.35), ang=lerp(3, 10, drop), gray=drop > 0.5)
        if drop > 0.5: tag(img, 520, 860, "ЗАПАС", (70, 70, 80), 30, clamp((drop - 0.5) * 3))
        if t > wtime(8, 7): tape(img, 300, 960, "НАПАРНИК ЕЩЁ ПО NAVI", -3, YEL, size=32, p=clamp((t - wtime(8, 7)) / 0.35))
    elif si in (9, 10):
        icon(img, "portrait", 200, 400 + fl, 200, 1.0 if si == 10 else pin(0.0), ang=-3)
        slide = ease_out(pin(0.2, 0.6)) if si == 9 else 1
        icon(img, "aceap", lerp(860, 520, slide), 400 - fl, 200, 1.0, ang=3)
        icon(img, "i_au", lerp(860, 520, slide) + 70, 280 - fl, 55, 1.0, ang=6)
        if si == 10:
            sc = 1 + 0.04 * math.sin(lt * 4)
            icon(img, "i_q", 360, 700, int(190 * sc), 1.0)
            character(img, 360, 1000, 0.55, "BC.GAME", t, "worried")
        else:
            character(img, 360, 830, 0.8, "BC.GAME", t, "calm")
    elif si == 11:
        icon(img, "asia3", 360, 330 + fl, 220, pin(0.1))
        icon(img, "i_mn", 590, 210, 60, pin(0.5), ang=8)
        tape(img, 360, 560, "3 ИЗ 5 — АЗИЯ", -4, YEL, size=46, p=pin(dur - 1.6))
        character(img, 360, 900, 0.7, "BC.GAME", t, "smirk")
    elif si == 12:
        icon(img, "region", 360, 300 + fl, 170, pin(0.05))
        icon(img, "bcgame", lerp(150, 560, ease_out(pin(0.4, 1.2))), 430, 80, pin(0.3), glow=False)
        tag(img, 360, 530, "СОПЕРНИКИ СЛАБЕЕ", GRN, 32, pin(wt(5)))
        character(img, 360, 850, 0.8, "BC.GAME", t, "smirk")
    elif si == 13:
        text_c(d, (360, 190), "ШАНС НА МЕЙДЖОР", 40, WHITE, "Black", 4)
        sw = pin(max(0.4, dur * 0.4), 0.4)
        if sw < 1: icon(img, "pct9", 360, 360, 250, 1.0, alpha=1 - sw)
        icon(img, "pct85", 360, 360 + fl, 260, sw)
        character(img, 360, 820, 0.85, "BC.GAME", t, "conf")
    elif si == 14:
        icon(img, "major", 360, 330 + fl, 230, pin(0.1), ang=-4)
        icon(img, "i_yes", 500, 480, 90, pin(wt(1), 0.4), ang=-8)
        character(img, 360, 810, 0.85, "BC.GAME", t, "smirk")
    elif si == 15:
        icon(img, "singapore", 330, 320 + fl, 260, pin(0.05))
        icon(img, "nogamble", 540, 470, 170, pin(wt(7), 0.4), ang=8)
        tag(img, 360, 610, "ЗАКОН ОБ АЗАРТНЫХ ИГРАХ", RED, 28, pin(wt(9)))
        character(img, 360, 910, 0.7, "BC.GAME", t, "shock")
    elif si in (16, 17):
        icon(img, "bcgame", 360, 290 + fl, 210, pin(0.0) if si == 16 else 1.0)
        if si == 16: tape(img, 360, 490, "КРИПТОКАЗИНО", -5, YEL, size=50, p=pin(wt(4)))
        else: icon(img, "i_ban", 360, 300, 120, pin(0.1, 0.35), ang=-10)
        if si == 16: icon(img, "i_crypto", 560, 420, 130, pin(0.4), ang=6)
        character(img, 360, 830, 0.82, "BC.GAME", t, "smirk" if si == 16 else "shock")
    elif si == 18:
        remain = max(0, 24 * 3600 - (lt / max(1, dur)) * 24 * 3600)
        hh, mm, ss = int(remain // 3600), int(remain % 3600 // 60), int(remain % 60)
        icon(img, "h24", 190, 320, 220, pin(0.05), ang=math.sin(t * 3) * 1.5)
        text_c(d, (480, 290), "НА НОВОЕ", 28, (230, 215, 215), "Black", 3); text_c(d, (480, 325), "НАЗВАНИЕ", 28, (230, 215, 215), "Black", 3)
        text_c(d, (480, 385), f"{hh:02d}:{mm:02d}:{ss:02d}", 50, RED, "Black", 4)
        tape(img, 360, 510, "СУТКИ", -4, YEL, size=46, p=pin(wt(4)))
        character(img, 360, 850, 0.8, "???", t, "worried")
    elif si == 19:
        p = pin(wt(3), 0.45)
        if p > 0:
            g = Image.new("RGBA", img.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
            gd.ellipse([120, 180, 600, 460], fill=YEL + (int(110 * p),))
            img.alpha_composite(g.filter(ImageFilter.GaussianBlur(50)))
        icon(img, "gosh", 360, 320 + fl, 230, p)
        tag(img, 360, 500, "НОВАЯ КОМАНДА", GRN, 32, p)
        character(img, 360, 840, 0.82, "GOSH" if p > 0.5 else "BC.GAME", t, "full")
    elif si == 20:
        text_c(d, (360, 180), "МЕЙДЖОР · СИНГАПУР · 1 МАТЧ", 26, (220, 225, 240), "Black", 3)
        icon(img, "gosh", lerp(-150, 185, ease_out(pin(0.0, 0.5))), 330 + fl, 150, 1.0)
        icon(img, "liquid", lerp(870, 540, ease_out(pin(0.15, 0.5))), 330 - fl, 190, 1.0)
        text_c(ImageDraw.Draw(img), (365, 335), "VS", int(lerp(10, 70, back(pin(0.5, 0.3)))) if lt > 0.5 else 10, YEL, "Black", 5)
        character(img, 360, 820, 0.85, "GOSH", t, "angry")
    elif si == 21:
        sep = Image.new("RGBA", img.size, (90, 60, 30, 90)); img.alpha_composite(sep)
        icon(img, "liquid", 360, 280 + fl, 170, pin(0.05), gray=False)
        d = ImageDraw.Draw(img)
        text_c(d, (360, 420), "10 ЛЕТ НАЗАД", 30, (240, 220, 180), "Black", 3)
        tape(img, 360, 490, "ФИНАЛ МЕЙДЖОРА", -3, YEL, size=40, p=pin(0.4))
        character(img, 360, 850, 0.8, "LIQUID", t, "full")
        for _ in range(250):
            x, y = random.randint(0, W - 1), random.randint(0, 1100); d.point((x, y), fill=(255, 230, 190))
    elif si == 22:
        icon(img, "scales", 360, 340, 300, pin(0.05), ang=math.sin(t * 1.5) * 2)
        character(img, 360, 860, 0.8, "GOSH", t, "point")
        if t > S[22]["end"] + 0.3:
            tape(img, 360, 600, "А ВЫ КАК ДУМАЕТЕ?", -3, YEL, size=40, p=clamp((t - S[22]["end"] - 0.3) / 0.35))
        if t > S[22]["end"] + 0.9:
            q = clamp((t - S[22]["end"] - 0.9) / 0.35)
            icon(img, "i_avatar", 150, 1110, 130, q)
            icon(img, "i_sub", 430, 1110, 95, clamp(q * 1.2 - 0.1), ang=math.sin(t * 3) * 0.8)

BGMAP = {0: "blue", 1: "red", 2: "blue", 3: "red", 4: "red", 5: "red", 6: "red", 7: "gold", 8: "blue", 9: "blue", 10: "blue", 11: "gold", 12: "blue", 13: "green", 14: "green", 15: "red", 16: "gold", 17: "red", 18: "red", 19: "gold", 20: "blue", 21: "sepia", 22: "blue"}

# ---------- captions ----------
CH = []
for si, s in enumerate(S):
    cur = []
    for (a, b, w) in s["abs"]:
        cur.append((a, b, w))
        txt = " ".join(x[2] for x in cur)
        if len(cur) >= 3 or len(txt) > 15 or w[-1] in ".,?!—…" or w.endswith("..."):
            CH.append(cur); cur = []
    if cur: CH.append(cur)
def chunk_at(t):
    for i, c in enumerate(CH):
        end = CH[i + 1][0][0] if i + 1 < len(CH) else c[-1][1] + 0.5
        end = min(end, c[-1][1] + 0.6)
        if c[0][0] - 0.03 <= t < end: return c, t - c[0][0]
    return None, 0
def draw_caption(img, t):
    c, lt = chunk_at(t)
    if not c: return
    words = [w[2].upper().strip("—") for w in c]
    words = [w for w in words if w]
    if not words: return
    key = max(range(len(words)), key=lambda i: len(words[i].strip(".,?!…")))
    sc = 0.85 + 0.15 * ease_out(lt / 0.12)
    f = F(int(54 * sc), "Black")
    lines = [" ".join(words)]
    if f.getbbox(lines[0])[2] > 640 and len(words) > 1:
        lines = [" ".join(words[:2]), " ".join(words[2:])] if len(words) > 2 else [words[0], words[1]]
    d = ImageDraw.Draw(img); y0 = 1120 - (len(lines) - 1) * 34
    wi = 0
    for li, line in enumerate(lines):
        ws = line.split(" "); tw = sum(f.getbbox(w)[2] for w in ws) + 16 * (len(ws) - 1)
        x = 360 - tw / 2; y = y0 + li * 68
        for w in ws:
            col = YEL if wi == key else WHITE
            st = c[min(wi, len(c) - 1)][0]; pw = 1 + 0.07 * math.exp(-max(0, t - st) * 11) if t >= st else 1
            ww = f.getbbox(w)[2]
            fw = F(int(54 * sc * pw), "Black") if pw > 1.01 else f
            d.text((x + ww / 2, y - (pw - 1) * 20), w, font=fw, fill=col, anchor="mm", stroke_width=5, stroke_fill=(0, 0, 0)); x += ww + 16; wi += 1

def sentence_at(t):
    for i, s in enumerate(S):
        nxt = S[i + 1]["start"] if i + 1 < len(S) else TOTAL + 1
        if t < nxt: return i, max(0.0, t - s["start"]), nxt - s["start"]
    return len(S) - 1, 0, 1


# ---------- painted backgrounds (refs2) ----------
SCENE_BG = {0: "arena", 1: "arena", 2: "arena", 3: "arena", 4: "room", 5: "room", 6: "room", 7: "arena", 8: "arena", 9: "arena", 10: "arena",
            11: "arena", 12: "arena", 13: "arena", 14: "singapore", 15: "singapore", 16: "arena", 17: "arena", 18: "room", 19: "singapore", 20: "singapore", 21: "sepia", 22: "arena"}
TINT = {"blue": None, "red": (150, 20, 30, 70), "green": (20, 120, 60, 60), "gold": (150, 110, 20, 55), "sepia": None}
_PB = {}
def painted_bg(name, tint):
    key = (name, tint)
    if key not in _PB:
        im = Image.open(f"{D}/refs2/bg_{name}.png").convert("RGB").resize((int(W * 1.08), int(H * 1.08)), Image.LANCZOS).convert("RGBA")
        im = Image.blend(im, Image.new("RGBA", im.size, (0, 0, 0, 255)), 0.28)
        tc = TINT.get(tint)
        if tc and name != "sepia": im.alpha_composite(Image.new("RGBA", im.size, tc))
        fl = Image.new("RGBA", im.size, (0, 0, 0, 0)); f = ImageDraw.Draw(fl)
        y0 = int(1000 * 1.08)
        for i in range(im.height - y0): f.line([(0, y0 + i), (im.width, y0 + i)], fill=(0, 0, 0, min(235, int(i * 1.3))))
        im.alpha_composite(fl); _PB[key] = im
    return _PB[key]
def bg_frame(si, t, lt, dur):
    im = painted_bg(SCENE_BG[si], BGMAP[si])
    mx, my = im.width - W, im.height - H
    q = clamp(lt / max(1.0, dur)); dirx = 1 if si % 2 else -1
    x = int(mx / 2 + dirx * (q - 0.5) * mx * 0.9); y = int(my * (0.8 - 0.6 * q))
    return im.crop((x, y, x + W, y + H))

def _zoom(im, z, blur=0):
    if abs(z - 1) > 0.002:
        w, h = int(W / z), int(H / z); x, y = (W - w) // 2, int((H - h) * 0.4)
        im = im.crop((x, y, x + w, y + h)).resize((W, H), Image.BILINEAR)
    if blur > 0.4: im = im.filter(ImageFilter.GaussianBlur(blur))
    return im
def layer(si, t):
    st = S[si]["start"]; nxt = S[si + 1]["start"] if si + 1 < len(S) else TOTAL + 1
    lt = max(0.0, t - st); dur = nxt - st
    CUR.update(t=t, si=si, lt=lt)
    img = bg_frame(si, t, lt, dur)
    d = ImageDraw.Draw(img)
    for (x, y, r, ph) in DUST:
        yy = (y - t * 12 * r) % 1100; a = int(60 + 60 * math.sin(t * 1.5 + ph))
        d.ellipse([x - r + CUR["cam"][0] * 0.3, yy - r, x + r + CUR["cam"][0] * 0.3, yy + r], fill=(255, 255, 255, a))
    scene(img, si, t, lt, dur)
    return _zoom(img, 1 + 0.035 * ease_io(lt / max(1.0, dur)))
TR = 0.35
def frame(t):
    si, lt, dur = sentence_at(t)
    CUR["cam"] = (math.sin(t * 0.3) * 6, math.cos(t * 0.25) * 4)
    img = layer(si, t)
    if si > 0 and lt < TR:
        q = ease_io(lt / TR); sp = math.sin(q * math.pi)
        prev = _zoom(layer(si - 1, t), 1 + 0.10 * q, 2 * sp)
        new = _zoom(img, 1.08 - 0.08 * q, 2 * sp)
        img = Image.blend(prev, new, q)
        CUR.update(si=si, lt=lt)
    draw_caption(img, t)
    return img.convert("RGB")
def _fb(i): return frame(i / FPS).tobytes()

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "preview":
        ts = [float(x) for x in sys.argv[3].split(",")]
        ims = [frame(t).resize((240, 427)) for t in ts]
        sheet = Image.new("RGB", (240 * len(ims), 427)); [sheet.paste(im, (i * 240, 0)) for i, im in enumerate(ims)]
        sheet.save(f"{D}/preview.jpg"); sys.exit()
    n = int(TOTAL * FPS)
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-vf", "scale=1080:1920:flags=lanczos", "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", f"{D}/video_noaudio.mp4"], stdin=subprocess.PIPE)
    import multiprocessing as mp
    with mp.get_context("fork").Pool(4) as pool:
        for buf in pool.imap(_fb, range(n), chunksize=24): p.stdin.write(buf)
    p.stdin.close(); p.wait(); print("frames", n)
