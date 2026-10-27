"""Session 10 - Example 2: read a WAV file and find where the sound is.

Speech systems first check the audio: duration, sample rate, and which
parts are silence. Finding speech vs silence is called Voice Activity
Detection (VAD). Run make_test_audio.py first.
Run: python audio_basics.py [file.wav]
"""
import struct
import sys
import wave

filename = sys.argv[1] if len(sys.argv) > 1 else "test_audio.wav"

# Step 1: open the file and read its properties
with wave.open(filename, "rb") as wav:
    sample_rate = wav.getframerate()
    channels = wav.getnchannels()
    frame_count = wav.getnframes()
    raw = wav.readframes(frame_count)

print("Sample rate:", sample_rate, "Hz | channels:", channels)
print("Duration   :", round(frame_count / sample_rate, 2), "seconds")

# Step 2: turn the bytes into numbers (16-bit mono assumed)
samples = struct.unpack(f"<{frame_count * channels}h", raw)

# Step 3: cut into 250 ms windows and measure loudness (average absolute value)
window = sample_rate // 4                       # 250 ms of samples
print("\nTime   Loudness  Sound?")
for start in range(0, len(samples), window):
    chunk = samples[start:start + window]
    loudness = sum(abs(s) for s in chunk) / len(chunk)
    is_sound = loudness > 500                    # simple threshold
    seconds = start / sample_rate
    bar = "#" * int(loudness / 1000)
    print(f"{seconds:5.2f}s  {loudness:8.0f}  {'yes' if is_sound else 'no '}  {bar}")
