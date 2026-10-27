"""Session 09 - Example 1: to a computer, an image is just a grid of numbers.

We build tiny images with NumPy so no image file is needed.
Run: python image_as_numbers.py
"""
import numpy as np

# Step 1: a 5x5 grayscale image. 0 = black, 255 = white. This draws a plus sign.
gray = np.zeros((5, 5), dtype=np.uint8)
gray[2, :] = 255          # middle row white
gray[:, 2] = 255          # middle column white
print("Grayscale image (5 x 5):")
print(gray)

# Step 2: show it with characters so we can "see" it
for row in gray:
    print("".join("##" if pixel > 127 else ". " for pixel in row))

# Step 3: a colour image has 3 numbers per pixel: Red, Green, Blue
color = np.zeros((2, 2, 3), dtype=np.uint8)
color[0, 0] = [255, 0, 0]       # red pixel
color[0, 1] = [0, 255, 0]       # green pixel
color[1, 0] = [0, 0, 255]       # blue pixel
color[1, 1] = [255, 255, 0]     # yellow = red + green
print("\nColour image shape (height, width, channels):", color.shape)

# Step 4: models usually want numbers between 0 and 1 ("normalization")
normalized = color / 255.0
print("Top-left pixel normalized:", normalized[0, 0])

# Step 5: a phone photo is much bigger
height, width = 3000, 4000
print(f"\nA 12-megapixel photo holds {height * width * 3:,} numbers")
