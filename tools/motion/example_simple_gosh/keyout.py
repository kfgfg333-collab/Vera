import sys,glob,os,numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
D=sys.argv[1]; os.makedirs(f"{D}/cut",exist_ok=True)
def key(path,out,tol=26):
    im=np.array(Image.open(path).convert("RGB")).astype(int)
    h,w,_=im.shape
    border=np.concatenate([im[0],im[-1],im[:,0],im[:,-1]])
    bg=np.median(border,axis=0)
    dist=np.sqrt(((im-bg)**2).sum(-1))
    m=dist<tol
    lab,n=ndimage.label(m)
    edge=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
    bgmask=np.isin(lab,list(edge))
    alpha=np.where(bgmask,0,255).astype(np.uint8)
    a=Image.fromarray(alpha).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
    rgba=Image.fromarray(im.astype(np.uint8)).convert("RGBA"); rgba.putalpha(a)
    bb=a.getbbox(); rgba=rgba.crop(bb) if bb else rgba
    rgba.save(out)
for p in glob.glob(f"{D}/*.png"):
    n=os.path.basename(p)[:-4]
    if n in ("sheet","crops_preview"): continue
    key(p,f"{D}/cut/{n}.png")
print("ok")
