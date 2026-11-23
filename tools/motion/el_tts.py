"""ElevenLabs TTS with timestamps -> out.mp3 + words.json [[start,end,word],...]
usage: python el_tts.py VOICE_ID MODEL SPEED text.txt OUTPREFIX"""
import sys, json, base64, urllib.request
vid, model, speed, tf, out = sys.argv[1:6]
text = open(tf, encoding="utf-8").read().strip()
body = {"text": text, "model_id": model, "language_code": "ru",
        "voice_settings": {"stability": 0.45, "similarity_boost": 0.8, "style": 0.3, "speed": float(speed)}}
req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{vid}/with-timestamps?output_format=mp3_44100_128",
    data=json.dumps(body).encode(), headers={"xi-api-key": "proxy-injected", "Content-Type": "application/json"})
try: r = json.load(urllib.request.urlopen(req, timeout=300))
except urllib.error.HTTPError as e: print(e.code, e.read()[:500].decode(errors="replace")); sys.exit(1)
open(out + ".mp3", "wb").write(base64.b64decode(r["audio_base64"]))
al = r.get("alignment") or r.get("normalized_alignment")
ch, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
words, cur, s0 = [], "", None
for c, a, b in zip(ch, st, en):
    if c.isspace():
        if cur: words.append([s0, pe, cur]); cur = ""
        continue
    if not cur: s0 = a
    cur += c; pe = b
if cur: words.append([s0, pe, cur])
json.dump(words, open(out + "_words.json", "w"), ensure_ascii=False)
print("words", len(words), "dur", round(words[-1][1], 2))
