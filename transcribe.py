import speech_recognition as sr
import sys
from pathlib import Path

r = sr.Recognizer()

for wav_path in sorted(Path(r'./').glob('chunk-*.wav'), key=lambda path: float(path.stem.rsplit("-", 1)[1])):
    audio_filename = str(wav_path)

    with sr.AudioFile(audio_filename) as source:
        audio = r.record(source)

    result = None
    try:
        result = r.recognize_google(audio, language='yue-Hant-HK')
    except:
        pass

    if result is not None:
        print(result)
