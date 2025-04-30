# stt_module.py

import os
import nemo.collections.asr as nemo_asr
from huggingface_hub import login 
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACE_TOKEN = os.getenv("HF_TOKEN")

login(token=HUGGINGFACE_TOKEN, add_to_git_credential=True)

# Load STT model
model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained(
    model_name="mbazaNLP/Kinyarwanda_nemo_stt_conformer_model"
)

def transcribe_audio(audio_input):
    """Handle both folder paths and direct file lists"""
    supported_ext = ('.wav', '.mp3')
    
    if isinstance(audio_input, str):
        # Input is a folder path
        if not os.path.isdir(audio_input):
            raise ValueError(f"Path {audio_input} is not a valid directory")
            
        audio_files = [
            os.path.join(audio_input, f)
            for f in sorted(os.listdir(audio_input))
            if f.lower().endswith(supported_ext)
        ]
    elif isinstance(audio_input, list):
        # Input is already a list of files
        audio_files = [
            f for f in audio_input 
            if isinstance(f, str) and f.lower().endswith(supported_ext)
        ]
    else:
        raise ValueError("Input must be either a folder path or list of audio files")

    if not audio_files:
        raise FileNotFoundError("No supported audio files found")

    return model.transcribe(audio_files)