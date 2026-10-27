"""Session 09 - Example 4: ask a vision-language model about an image.

Many chat models accept an image together with a text question.
We send the image as base64 text inside the message.
Run: python vision_llm_prompt.py [path/to/image.jpg]
  - with OPENAI_API_KEY and an image path: real answer
  - otherwise: a mock answer so the code still runs
"""
import base64
import sys
from llm_client import is_live, MODEL

# PLACEHOLDER: never write your real key in code. Set it in the terminal instead:
#   Windows:  set OPENAI_API_KEY=sk-...      macOS/Linux:  export OPENAI_API_KEY=sk-...

question = "Describe this image in one sentence, then list any text you can read in it."
image_path = sys.argv[1] if len(sys.argv) > 1 else None

def image_to_data_url(path):
    """Read an image file and turn it into a data URL the API understands."""
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    image_type = "png" if path.lower().endswith(".png") else "jpeg"
    return f"data:image/{image_type};base64,{encoded}"

# Step 1: fall back to a mock answer when we cannot make a real call
if not (is_live() and image_path):
    print("(mock) A student is writing Python code on a laptop. Text: 'print(\"Hello\")'")
    print("Tip: set OPENAI_API_KEY and run:  python vision_llm_prompt.py photo.jpg")
    raise SystemExit

# Step 2: build one user message that contains BOTH text and an image
from openai import OpenAI
client = OpenAI()
messages = [{
    "role": "user",
    "content": [
        {"type": "text", "text": question},
        {"type": "image_url", "image_url": {"url": image_to_data_url(image_path)}},
    ],
}]

# Step 3: send it to a vision-capable model and print the reply
response = client.chat.completions.create(model=MODEL, messages=messages)
print(response.choices[0].message.content)
