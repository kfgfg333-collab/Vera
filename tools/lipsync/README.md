# Липсинк Веры — запасной инструмент (Режим B)

С 27.10.2026 основной процесс — русская речь прямо во Flow (`CLAUDE.md`). Этот инструмент используется только по просьбе пользователя.

Проверено на EP01, клип 01: CPU, 7 с видео 720×1280 ≈ 8 минут. Результат: рот перерисован под русскую озвучку; область рта немного мягче остального лица.
Правило проекта — `CLAUDE.md` → «Производственный процесс». Запускать только с разрешения пользователя (сторонний код и веса).

## Шаги для Claude Code
1. Пользователь присылает клип Flow (`EP01_Kxx_flow.mp4`) и MP3 ElevenLabs (`EP01_Kxx_voice.mp3`).
2. Установка (один раз за сессию, вне репозитория): `bash tools/lipsync/setup.sh <scratchpad>/lipsync`.
3. Раскадровка клипа (ffmpeg, кадры каждые 0,2 с) → найти: где Вера говорит в камеру, где отворачивается (кадры для `--keep`).
4. Подгонка звука по времени (ffmpeg): фраза должна звучать, пока лицо Веры к камере; если она отворачивается посреди реплики — разрезать MP3 по паузе и сдвинуть вторую часть (`atrim` + `adelay`), без ускорения речи.
   `ffmpeg -i voice.mp3 -filter_complex "[0]atrim=0:1.6,asetpts=PTS-STARTPTS[a];[0]atrim=start=2.0,asetpts=PTS-STARTPTS,adelay=3900|3900[b];[a][b]amix=inputs=2:normalize=0,apad=whole_dur=7.0" voice_timed.wav`
   `ffmpeg -i voice_timed.wav -ac 1 -ar 16000 voice16.wav`
5. `<W>/venv/bin/python -I tools/lipsync/lipsync.py <W>/w2l EP01_Kxx_flow.mp4 voice16.wav lips.mp4 --keep 63-93`
6. Сборка: `ffmpeg -i lips.mp4 -i voice_timed.wav -map 0:v -map 1:a -t <длина> -c:v libx264 -crf 17 -pix_fmt yuv420p -c:a aac -b:a 192k EP01_Kxx_final.mp4`
7. Проверка по кадрам (крупно рот: обычные кадры и кадры поворота) → отправить пользователю `EP01_Kxx_final.mp4`. В CapCut этот файл ставится **со своим звуком** (русский голос уже внутри), отдельный MP3 к нему не добавляется.
