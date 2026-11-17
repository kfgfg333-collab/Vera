"""Timeline from a ready voice file (ElevenLabs): whisper word timestamps -> sentences of script.txt.
usage: python -I align.py voice.mp3 script.txt OUTDIR  -> OUTDIR/voice.wav, OUTDIR/timeline.json"""
import sys, re, json, subprocess, numpy as np
from faster_whisper import WhisperModel
src, script, out = sys.argv[1:4]
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-ar", "48000", "-ac", "2", "-af", "loudnorm=I=-15:TP=-1.5", f"{out}/voice.wav"], check=True)
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-f", "f32le", "-ac", "1", "-ar", "16000", "-"], capture_output=True, check=True).stdout
dur = len(pcm) / 4 / 16000
m = WhisperModel("medium", device="cpu", compute_type="int8")
segs, _ = m.transcribe(np.frombuffer(pcm, dtype=np.float32), language="ru", word_timestamps=True)
words = [(w.start, w.end, w.word.strip()) for s in segs for w in s.words]
text = open(script, encoding="utf-8").read().strip()
sents = [s.strip() for s in re.split(r"(?<=[.!?…])\s+", text) if s.strip()]
norm = lambda x: re.sub(r"[^\wё]", "", x.lower())
# align script words to recognised words (difflib), interpolate the rest
import difflib
sw = [(k, w) for k, s_ in enumerate(sents) for w in s_.split()]
A = [norm(w) for _, w in sw]; Bw = [norm(w[2]) for w in words]
tm = [None] * len(sw)
for blk in difflib.SequenceMatcher(None, A, Bw, autojunk=False).get_matching_blocks():
    for q in range(blk.size): tm[blk.a + q] = (words[blk.b + q][0], words[blk.b + q][1])
known = [i for i, x in enumerate(tm) if x]
for i in range(len(tm)):
    if tm[i]: continue
    p = max([k for k in known if k < i], default=None); nx = min([k for k in known if k > i], default=None)
    t0 = tm[p][1] if p is not None else 0.0; t1 = tm[nx][0] if nx is not None else dur
    gp = [k for k in range(p + 1 if p is not None else 0, nx if nx is not None else len(tm))]
    j = gp.index(i); step = (t1 - t0) / len(gp); tm[i] = (t0 + j * step, t0 + (j + 1) * step)
res = []
for k, s_ in enumerate(sents):
    ab = [[tm[i][0], tm[i][1], w] for i, (kk, w) in enumerate(sw) if kk == k]
    res.append(dict(text=s_, start=ab[0][0], end=ab[-1][1], abs=ab))
n = len(words)
json.dump(dict(total=dur + 1.5, sent=res), open(f"{out}/timeline.json", "w"), ensure_ascii=False)
print("sentences", len(res), "words", n, "dur", round(dur, 2))
