# Kinyarwanda_Voice_AI 🇷🇼
Kinyarwanda Voice Assistant - A locally-run AI assistant that understands and speaks Kinyarwanda. Features speech recognition (STT), natural language processing, and text-to-speech (TTS) with Gradio web interface. Ideal for Rwandan developers, researchers, and language preservation efforts.

Demo Screenshot 
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/f99c74f7-1673-49fb-8fbc-85526c824cd8" />


## Features ✨

- 🎙️ Speech-to-text for Kinyarwanda using NeMo Conformer model
- 🔊 Text-to-speech with custom KinyaTTS VITS2 model
- 💬 Natural language processing for question answering
- 🖥️ Gradio web interface with:
  - Microphone recording
  - Audio file upload
  - Automatic response playback
- 🌐 Ready for deployment

  ## Installation 🛠️

### Prerequisites
- Python 3.8 or higher
- pip package manager
- (Optional) NVIDIA GPU for faster inference

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Chloe-sys/kinyarwanda_Voice_AI.git
cd kinyarwanda_Voice_AI
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download models (automatic on first run):

```bash
ASR: mbazaNLP/Kinyarwanda_nemo_stt_conformer_model
TTS: Pre-trained KinyaTTS model
```
### Usage 🚀

Running the Web Interface

```bash
python interface.py
```
The interface will launch at:

```bash
http://localhost:7860
```

Using the Assistant

Speak or upload audio in Kinyarwanda
The assistant will:
- Transcribe your speech
- Generate an appropriate response
- Speak back the response

### Project Structure 📂
```bash
.
├── interface.py               # Gradio interface
├── assistant.py         # Main assistant pipeline
├── stt_module.py        # Speech-to-text processing
├── tts_module.py        # Text-to-speech synthesis
├── nlp_module.py        # Natural language processing
├── audio_samples/       # Example audio files
├── outputs/             # Generated response audio
└── requirements.txt     # Dependencies
```

### Requirements
```bash
gradio>=3.0
torch>=1.10
torchaudio>=0.10
nemo_toolkit[asr]>=1.7
soundfile>=0.10
huggingface_hub>=0.10
numpy>=1.21
matplotlib>=3.5  # Required by some NeMo components
```
### Contributing 🤝
Contributions are welcome! Please open an issue or pull request for:
- Bug fixes
- New features
- Improved documentation

### ⚠️ Limitations
- Accuracy depends on audio quality (quiet environments work best)
- Fixed number of patterns/intents (can be extended easily)
- Requires specific model paths and initialization before TTS

### 📚 Resources and Credits
- STT Model: https://huggingface.co/mbazaNLP/Kinyarwanda_nemo_stt_conformer_model
- TTS Engine: https://github.com/anzeyimana/KinyaTTS
- Gradio Interface: https://gradio.app/
- NVIDIA NeMo: https://github.com/NVIDIA/NeMo
- Audio Processing: https://github.com/jiaaro/pydub, https://pytorch.org/audio/stable/index.html
- STT model: https://github.com/agent87/RW-DEEPSPEECH-API

### 🙏 Acknowledgements
- Rwanda MIT Research Team – for open-sourcing KinyaTTS
- Hugging Face – for hosting and distributing models
- NVIDIA – for the NeMo framework
