# test_run.py

import os
from assistant import run_assistant
from tts_module import setup_kinya_tts

# Initialize TTS
setup_kinya_tts()

# Folder path
audio_folder = os.path.join(os.path.dirname(__file__), "audio_samples")

# Run assistant on all audio in the folder
results = run_assistant(audio_folder)

for idx, (transcription, response_wav) in enumerate(results):
    print(f"\n🎧 Audio #{idx + 1}")
    print("🗣️ Transcription:", transcription)
    print("🔊 Response saved at:", response_wav)

print("\n✅ All audio files processed!")
