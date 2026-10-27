"""Session 10 - Example 4: text-to-speech (TTS) with an offline engine or an API.

Option A: pyttsx3 uses the voices already on your computer (offline, free).
          pip install pyttsx3
Option B: the OpenAI speech API (needs OPENAI_API_KEY), natural voices.
If neither is available, the script explains what would happen.
Run: python text_to_speech.py
"""
import os

text = "Welcome to Aptech. Your class starts at five pm today."

def speak_offline(message):
    """Option A: save speech to a WAV file with the computer's own voice."""
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)                 # words per minute
    engine.save_to_file(message, "speech_offline.wav")
    engine.runAndWait()
    return "speech_offline.wav"

def speak_api(message):
    """Option B: ask the OpenAI API for an MP3 file."""
    from openai import OpenAI
    client = OpenAI()
    response = client.audio.speech.create(model="tts-1", voice="alloy", input=message)
    with open("speech_api.mp3", "wb") as f:
        f.write(response.content)
    return "speech_api.mp3"

# Step 1: try the offline engine first
try:
    print("Saved:", speak_offline(text))
except Exception:                                   # missing package or no voice engine
    # Step 2: then the API, if a key is set
    if os.getenv("OPENAI_API_KEY"):
        print("Saved:", speak_api(text))
    else:
        # Step 3: fallback so the lesson continues
        print("(mock) Would turn this text into speech:", text)
        print("(mock) Install pyttsx3 or set OPENAI_API_KEY to create an audio file.")
