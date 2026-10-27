"""Session 10 - Example 3: speech-to-text with Whisper (two options + fallback).

Option A: the open-source Whisper model on your own computer (free).
          pip install openai-whisper   (also needs ffmpeg installed)
Option B: the OpenAI transcription API (needs OPENAI_API_KEY).
          pip install openai
If neither is available, a mock transcript is printed.
Run: python transcribe_whisper.py my_voice.mp3
"""
import os
import sys

audio_file = sys.argv[1] if len(sys.argv) > 1 else "my_voice.mp3"

def transcribe_local(path):
    """Option A: run the small Whisper model locally."""
    import whisper                                  # the openai-whisper package
    model = whisper.load_model("base")              # tiny, base, small, medium, large
    result = model.transcribe(path)                 # language is detected automatically
    return result["text"]

def transcribe_api(path):
    """Option B: send the file to the OpenAI API."""
    from openai import OpenAI
    client = OpenAI()                               # reads OPENAI_API_KEY from the environment
    with open(path, "rb") as f:
        result = client.audio.transcriptions.create(model="whisper-1", file=f)
    return result.text

# Step 1: check the file exists
if not os.path.exists(audio_file):
    print(f"(mock) File '{audio_file}' not found. Sample transcript:")
    print("(mock) Assalam o alaikum, I want to know the fee for the AI course.")
    raise SystemExit

# Step 2: try local Whisper, then the API, then give up politely
try:
    print("Local Whisper:", transcribe_local(audio_file))
except ImportError:
    if os.getenv("OPENAI_API_KEY"):
        print("OpenAI API:", transcribe_api(audio_file))
    else:
        print("(mock) Install openai-whisper or set OPENAI_API_KEY to get a real transcript.")
