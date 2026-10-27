"""Session 09 - Example 2: how a Vision Transformer (ViT) "reads" an image.

A ViT cuts the image into small square PATCHES, flattens each patch into
a vector and treats the patches like words (tokens) in a sentence.
Run: python vit_patches.py
"""
import numpy as np

np.random.seed(0)

# Step 1: a fake 8x8 grayscale image with random pixel values
image = np.random.randint(0, 256, size=(8, 8))
patch_size = 4                                   # 4x4 patches -> 2 x 2 = 4 patches

# Step 2: cut the image into patches, row by row
patches = []
for top in range(0, image.shape[0], patch_size):
    for left in range(0, image.shape[1], patch_size):
        patch = image[top:top + patch_size, left:left + patch_size]
        patches.append(patch.flatten())          # 4x4 grid -> 16 numbers

patches = np.array(patches)
print("Number of patches (image tokens):", len(patches))
print("Numbers per patch:", patches.shape[1])

# Step 3: a learned "projection" turns each patch into an embedding (here size 6)
embedding_size = 6
projection = np.random.randn(patches.shape[1], embedding_size) * 0.01
patch_embeddings = (patches / 255.0) @ projection

# Step 4: add position information so the model knows where each patch was
positions = np.arange(len(patches)).reshape(-1, 1) * 0.1
tokens = patch_embeddings + positions

print("Token matrix shape:", tokens.shape, "-> ready for transformer layers (Session 04)")
print("A 224x224 image with 16x16 patches gives", (224 // 16) ** 2, "tokens")
