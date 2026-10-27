"""Session 09 - Example 5 (optional, needs downloads): free image captioning offline.

Uses a small open captioning model from Hugging Face. No API key needed,
but the first run downloads about 1 GB.
Install: pip install torch transformers pillow
Run:     python caption_with_transformers.py photo.jpg
"""
import sys

try:
    from transformers import pipeline
except ImportError:
    print("Please install first:  pip install torch transformers pillow")
    raise SystemExit

if len(sys.argv) < 2:
    print("Usage: python caption_with_transformers.py photo.jpg")
    raise SystemExit

# Step 1: create an image-to-text pipeline with a BLIP captioning model
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# Step 2: caption the image given on the command line
result = captioner(sys.argv[1])

# Step 3: print the generated caption
print("Caption:", result[0]["generated_text"])
