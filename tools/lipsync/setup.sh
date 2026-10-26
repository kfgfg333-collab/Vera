#!/usr/bin/env bash
# Установка Wav2Lip для липсинка Веры (CPU). Запуск: bash tools/lipsync/setup.sh <рабочая_папка>
# Ставит всё ВНЕ репозитория (в рабочую папку): код Wav2Lip, venv, веса моделей.
set -euo pipefail
W="${1:?укажите рабочую папку, например scratchpad/lipsync}"
mkdir -p "$W"; cd "$W"
[ -d w2l ] || git clone -q --depth 1 https://github.com/Rudrabha/Wav2Lip.git w2l
# совместимость с новым librosa
sed -i 's/librosa.filters.mel(hp.sample_rate, hp.n_fft, n_mels=/librosa.filters.mel(sr=hp.sample_rate, n_fft=hp.n_fft, n_mels=/' w2l/audio.py
[ -d venv ] || python3 -m venv venv
./venv/bin/pip -q install --index-url https://download.pytorch.org/whl/cpu torch
./venv/bin/pip -q install numpy opencv-python-headless librosa scipy tqdm
HF=https://huggingface.co/camenduru/Wav2Lip/resolve/main
[ -s w2l/checkpoints/wav2lip_gan.pth ] || curl -sSL -o w2l/checkpoints/wav2lip_gan.pth $HF/checkpoints/wav2lip_gan.pth
[ -s w2l/face_detection/detection/sfd/s3fd.pth ] || curl -sSL -o w2l/face_detection/detection/sfd/s3fd.pth $HF/face_detection/detection/sfd/s3fd.pth
echo "готово: $W"
