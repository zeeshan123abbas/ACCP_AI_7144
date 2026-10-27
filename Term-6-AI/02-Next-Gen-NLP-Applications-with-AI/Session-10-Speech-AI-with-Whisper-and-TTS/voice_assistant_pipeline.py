"""Session 10 - Example 5: the voice assistant pipeline, step by step.

Speech -> text (ASR) -> understand and answer (NLP/LLM) -> speech (TTS).
Each stage is a small function; here they are simple stand-ins so the
flow runs offline. Swap in Examples 3 and 4 for real audio.
Run: python voice_assistant_pipeline.py
"""

def speech_to_text(audio_name):
    """Stage 1 (ASR). Stand-in: pretend we transcribed the audio file."""
    fake_transcripts = {
        "q1.wav": "what time does the centre open",
        "q2.wav": "how much is the monthly fee",
    }
    return fake_transcripts.get(audio_name, "")

def understand_and_answer(text):
    """Stage 2 (NLU + answer). A tiny keyword brain; an LLM or RAG could go here."""
    if "time" in text or "open" in text:
        return "The centre opens at 9 am, Monday to Saturday."
    if "fee" in text:
        return "The monthly fee is 25,000 rupees."
    return "Sorry, could you repeat that?"

def text_to_speech(text):
    """Stage 3 (TTS). Stand-in: show what would be spoken."""
    return f"[speaking] {text}"

# Run the full pipeline for two recorded questions
for audio in ["q1.wav", "q2.wav", "q3.wav"]:
    heard = speech_to_text(audio)
    answer = understand_and_answer(heard)
    print(f"{audio}: heard='{heard}'")
    print("        ", text_to_speech(answer))
