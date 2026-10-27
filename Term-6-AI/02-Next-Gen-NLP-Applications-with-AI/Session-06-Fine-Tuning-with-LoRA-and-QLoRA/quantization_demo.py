"""Session 06 - Example 3: what "4-bit quantization" in QLoRA means.

QLoRA stores the frozen base model with only 4 bits per number (16 levels)
instead of 16 bits. We squeeze some weights into 16 levels and measure
the memory saved and the small error we pay for it.
Run: python quantization_demo.py
"""
import numpy as np

np.random.seed(1)

# Step 1: some "weights" (real layers hold millions of these)
weights = np.random.randn(10).astype(np.float32)

# Step 2: 4 bits can store 2**4 = 16 different levels (0..15)
levels = 2 ** 4
w_min, w_max = weights.min(), weights.max()
step = (w_max - w_min) / (levels - 1)          # distance between two levels

# Step 3: QUANTIZE - turn each weight into a small whole number 0..15
codes = np.round((weights - w_min) / step).astype(np.uint8)

# Step 4: DEQUANTIZE - turn the codes back into approximate weights
restored = codes * step + w_min

# Step 5: compare
for original, code, back in zip(weights, codes, restored):
    print(f"original {original:+.4f} -> code {code:2d} -> restored {back:+.4f}")

error = np.abs(weights - restored).mean()
print(f"\nAverage error: {error:.4f}")

# Step 6: memory for a 7B model at different precisions
params = 7_000_000_000
for name, bits in [("32-bit float", 32), ("16-bit float", 16), ("8-bit", 8), ("4-bit (QLoRA)", 4)]:
    gigabytes = params * bits / 8 / 1_000_000_000
    print(f"{name:<14}: {gigabytes:5.1f} GB")
