"""Session 06 - Example 1: the LoRA idea with small NumPy matrices.

Full fine-tuning changes every number in a big weight matrix W.
LoRA keeps W frozen and learns two thin matrices A and B instead.
The update is  delta_W = B @ A  and the new weight is  W + delta_W.
Run: python lora_idea_numpy.py
"""
import numpy as np

np.random.seed(0)                      # same random numbers every run

d = 8          # size of the layer (real models use 768, 4096, ...)
r = 2          # LoRA rank: how "thin" A and B are

# Step 1: the pre-trained weight matrix - FROZEN, we never change it
W = np.random.randn(d, d)

# Step 2: the two small LoRA matrices - these are the only trainable parts
A = np.random.randn(r, d) * 0.01       # r x d, small random start
B = np.zeros((d, r))                   # d x r, starts at zero, so delta_W starts at zero

# Step 3: pretend training has changed B a little (random small values here)
B = np.random.randn(d, r) * 0.1

# Step 4: build the low-rank update and the adapted weight
delta_W = B @ A                        # (d x r) @ (r x d) = d x d
W_adapted = W + delta_W

# Step 5: compare how many numbers each approach must train
full_params = W.size                   # every number in W
lora_params = A.size + B.size          # only A and B
print("Shape of W       :", W.shape)
print("Shape of A and B :", A.shape, B.shape)
print("Shape of delta_W :", delta_W.shape)
print("Full fine-tuning trains", full_params, "numbers")
print("LoRA trains       ", lora_params, "numbers")
print("Rank of delta_W  :", np.linalg.matrix_rank(delta_W), "(never more than r)")

# Step 6: a forward pass works exactly like before, just with W_adapted
x = np.random.randn(d)                 # one input vector
print("Output changed by:", np.round(W_adapted @ x - W @ x, 3))
