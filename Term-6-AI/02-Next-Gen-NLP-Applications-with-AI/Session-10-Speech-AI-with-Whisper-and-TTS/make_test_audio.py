"""Session 10 - Example 1: create a WAV audio file with plain Python.

Sound is a wave. A computer stores it as many small numbers (samples)
per second. We generate: 1 s tone, 0.5 s silence, 1 s higher tone.
Run: python make_test_audio.py   -> creates test_audio.wav
"""
import math
import struct
import wave

SAMPLE_RATE = 16000          # 16,000 samples per second (what Whisper uses)

def tone(frequency, seconds, volume=0.5):
    """Return a list of samples for a sine-wave tone."""
    samples = []
    for i in range(int(SAMPLE_RATE * seconds)):
        value = volume * math.sin(2 * math.pi * frequency * i / SAMPLE_RATE)
        samples.append(int(value * 32767))          # scale to 16-bit whole numbers
    return samples

def silence(seconds):
    return [0] * int(SAMPLE_RATE * seconds)

# Step 1: build the sound: tone, pause, higher tone
samples = tone(440, 1.0) + silence(0.5) + tone(880, 1.0)

# Step 2: save as a mono, 16-bit WAV file
with wave.open("test_audio.wav", "wb") as wav:
    wav.setnchannels(1)              # mono
    wav.setsampwidth(2)              # 2 bytes = 16 bits per sample
    wav.setframerate(SAMPLE_RATE)
    wav.writeframes(struct.pack(f"<{len(samples)}h", *samples))

print(f"Saved test_audio.wav: {len(samples):,} samples = {len(samples) / SAMPLE_RATE} seconds")
