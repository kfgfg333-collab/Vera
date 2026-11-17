"""Липсинк Веры: перерисовывает рот в клипе Flow под русскую озвучку ElevenLabs (Wav2Lip, CPU).

Запуск (venv из setup.sh):
  <W>/venv/bin/python -I tools/lipsync/lipsync.py <W>/w2l clip.mp4 voice16k.wav out_noaudio.mp4 [--keep 63-93,120-130]
--keep — диапазоны кадров, где лицо НЕ видно (Вера отвернулась): там остаётся оригинал,
иначе детектор принимает затылок за лицо и смазывает волосы. Кадры подбирать по раскадровке.
Звук в выходном файле не пишется — его подмешивает ffmpeg (см. README.md).
"""
import sys, os, argparse, numpy as np, cv2, torch

ap = argparse.ArgumentParser()
ap.add_argument("w2l"); ap.add_argument("video"); ap.add_argument("wav"); ap.add_argument("out")
ap.add_argument("--keep", default="")
a = ap.parse_args()
sys.path.insert(0, a.w2l)
import audio, face_detection
from models import Wav2Lip

keep = set()
for part in filter(None, a.keep.split(",")):
    lo, hi = map(int, part.split("-")); keep.update(range(lo, hi + 1))

cap = cv2.VideoCapture(a.video); fps = cap.get(cv2.CAP_PROP_FPS)
frames = []
while True:
    ok, f = cap.read()
    if not ok: break
    frames.append(f)
wav = audio.load_wav(a.wav, 16000); mel = audio.melspectrogram(wav)
frames = frames[:int(len(wav) / 16000 * fps) + 1]

det = face_detection.FaceAlignment(face_detection.LandmarksType._2D, flip_input=False, device="cpu")
preds = []
for i in range(0, len(frames), 4):
    preds.extend(det.get_detections_for_batch(np.array(frames[i:i + 4])))
boxes = []
for r, img in zip(preds, frames):
    if r is None: boxes.append(None); continue
    h, w = img.shape[:2]
    boxes.append([max(0, r[0]), max(0, r[1]), min(w, r[2]), min(h, r[3] + 10)])
smooth = boxes[:]
for i, b in enumerate(boxes):
    if b is None: continue
    win = [boxes[j] for j in range(max(0, i - 2), min(len(boxes), i + 3)) if boxes[j] is not None]
    smooth[i] = [int(np.mean([x[k] for x in win])) for k in range(4)]
print("кадров", len(frames), "fps", fps, "без лица", [i for i, b in enumerate(smooth) if b is None])

model = Wav2Lip()
ck = torch.load(os.path.join(a.w2l, "checkpoints/wav2lip_gan.pth"), map_location="cpu", weights_only=True)
model.load_state_dict({k.replace("module.", ""): v for k, v in ck["state_dict"].items()}); model.eval()

h, w = frames[0].shape[:2]
vw = cv2.VideoWriter(a.out, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
for i, f in enumerate(frames):
    b = smooth[i]
    if b is None or i in keep:
        vw.write(f); continue
    s = int(i * 80.0 / fps)
    m = mel[:, s:s + 16] if s + 16 <= mel.shape[1] else mel[:, -16:]
    x1, y1, x2, y2 = b
    face = cv2.resize(f[y1:y2, x1:x2], (96, 96))
    masked = face.copy(); masked[48:] = 0
    img = torch.FloatTensor(np.transpose(np.concatenate([masked, face], axis=2)[None] / 255., (0, 3, 1, 2)))
    with torch.no_grad():
        p = model(torch.FloatTensor(m[None, None]), img)
    p = cv2.resize((p.numpy().transpose(0, 2, 3, 1)[0] * 255).astype(np.uint8), (x2 - x1, y2 - y1))
    # мягкая вклейка только нижней части лица
    hh, ww = p.shape[:2]; mask = np.zeros((hh, ww), np.float32)
    mask[int(hh * .52):int(hh * .97), int(ww * .12):int(ww * .88)] = 1
    mask = cv2.GaussianBlur(mask, (0, 0), max(2, ww * .05))[..., None]
    g = f.copy(); reg = g[y1:y2, x1:x2].astype(np.float32)
    g[y1:y2, x1:x2] = (reg * (1 - mask) + p.astype(np.float32) * mask).astype(np.uint8)
    vw.write(g)
vw.release(); print("ok")
