import sys, numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
D = sys.argv[1]
sh = Image.open(f"{D}/sheet2.png").convert("RGB")
B = {"p_calm":(0,0,212,302),"p_conf":(203,0,401,302),"p_puzzled":(395,0,630,302),"p_angry":(615,0,880,302),
     "p_smirk":(870,0,1075,302),"p_shock":(1066,0,1310,302),"p_point":(1300,0,1536,302),
     "k_bc":(15,370,215,935),"k_gosh":(215,370,415,935),"k_liquid":(415,370,610,935),
     "i_knight":(660,375,865,565),"i_score":(865,395,1160,540),"i_crypto":(1165,380,1495,555),
     "i_ban":(640,560,945,695),"i_yes":(965,570,1250,690),"i_q":(1270,565,1505,700),
     "i_au":(620,700,795,808),"i_mn":(815,700,990,815),"b_white":(1005,700,1185,800),"b_yel":(1175,700,1355,800),"b_red":(1335,700,1530,810),
     "i_avatar":(655,812,875,1015),"i_sub":(915,850,1410,1005)}
BORDER={'k_bc','i_yes'}
import os; os.makedirs(f"{D}/cut", exist_ok=True)
for n,b in B.items():
    im = np.array(sh.crop(b)).astype(int)
    r,g,bl = im[...,0],im[...,1],im[...,2]
    green = (g > 170) & (g - r > 90) & (g - bl > 90)
    fg = ~green
    if n in BORDER:
        lb, _ = ndimage.label(green); e = set(np.unique(np.concatenate([lb[0],lb[-1],lb[:,0],lb[:,-1]]))) - {0}
        fg = ~np.isin(lb, list(e))
        szs = ndimage.sum(green, lb, range(1, lb.max()+1))
        fg &= ~np.isin(lb, [i+1 for i,z in enumerate(szs) if z > 1500])
    lab, k = ndimage.label(fg)
    if k:
        sizes = ndimage.sum(fg, lab, range(1, k+1)); big = sizes.max()
        H_, W_ = fg.shape
        ok = []
        for i, sl in enumerate(ndimage.find_objects(lab)):
            sz = sizes[i]
            edge = sl[1].start == 0 or sl[1].stop == W_ or sl[0].start == 0
            if sz == big or (sz > big * 0.04 and not (edge and sz < big * 0.3)): ok.append(i + 1)
        keep = np.isin(lab, ok)
    else: keep = fg
    a = Image.fromarray((keep*255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    # despill
    im2 = im.copy(); gl = np.minimum(im2[...,1], np.maximum(im2[...,0], im2[...,2]) + 30); edge = np.array(a) < 250
    im2[...,1] = np.where(edge, gl, im2[...,1])
    out = Image.fromarray(im2.astype(np.uint8)).convert("RGBA"); out.putalpha(a)
    out = out.crop(out.getbbox()); out.save(f"{D}/cut/{n}.png")
print("ok")
# trim separated slivers: keep the widest run of non-empty columns/rows
def run(v):
    best=(0,0); s=None
    for i,x in enumerate(list(v)+[0]):
        if x>0 and s is None: s=i
        if x==0 and s is not None:
            if i-s>best[1]-best[0]: best=(s,i)
            s=None
    return best
for n in B:
    im=Image.open(f"{D}/cut/{n}.png"); a=np.array(im.getchannel("A"))>40
    if n.startswith("b_"): continue
    c0,c1=run(a.sum(0)); r0,r1=run(a[:,c0:c1].sum(1))
    if n=="p_puzzled": r0,r1=0,a.shape[0]
    im=im.crop((c0,r0,c1,r1))
    al=np.array(im.getchannel("A")); m=np.zeros_like(al); m[:]=al
    im.save(f"{D}/cut/{n}.png")
print("trim ok")
