"""Session 09 - Example 3: CLIP-style matching of images and text.

CLIP-like models put images and sentences into the SAME vector space.
A matching image and caption get vectors pointing in a similar direction.
Here we use small hand-made vectors to show the maths of zero-shot labelling.
Run: python clip_style_matching.py
"""
import numpy as np

def normalize(vector):
    return vector / np.linalg.norm(vector)

# Step 1: pretend an image encoder produced this vector for a photo.
# The 4 dimensions loosely mean: [animal, vehicle, food, outdoor]
image_vector = normalize(np.array([0.9, 0.0, 0.1, 0.6]))   # looks like an animal outdoors

# Step 2: pretend a text encoder produced vectors for candidate captions
captions = {
    "a photo of a cat in a garden": np.array([0.8, 0.0, 0.0, 0.7]),
    "a photo of a car on a road":   np.array([0.0, 0.9, 0.0, 0.5]),
    "a photo of a plate of biryani": np.array([0.0, 0.0, 1.0, 0.1]),
}

# Step 3: cosine similarity between the image and each caption
scores = {}
for caption, vector in captions.items():
    scores[caption] = float(image_vector @ normalize(vector))

# Step 4: softmax turns scores into probabilities (CLIP multiplies by a "temperature" first)
logits = np.array(list(scores.values())) * 10
probabilities = np.exp(logits) / np.exp(logits).sum()

for (caption, score), prob in zip(scores.items(), probabilities):
    print(f"{prob:6.1%}  (similarity {score:.2f})  {caption}")
print("\nPredicted label:", max(scores, key=scores.get))
