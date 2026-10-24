"""Session 04 - Example 4: one transformer encoder block in PyTorch.

Block = multi-head self-attention -> add & layer norm -> feed-forward -> add & layer norm
Setup: pip install torch
Run:   python transformer_block_pytorch.py
"""
import torch
from torch import nn

torch.manual_seed(0)
d_model = 16        # size of each token vector
num_heads = 4       # attention heads working in parallel


class EncoderBlock(nn.Module):
    def __init__(self):
        super().__init__()
        # multi-head self-attention layer
        self.attention = nn.MultiheadAttention(d_model, num_heads, batch_first=True)
        # layer normalization keeps the numbers in a stable range
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        # feed-forward network: applied to each token separately
        self.feed_forward = nn.Sequential(
            nn.Linear(d_model, 64),
            nn.ReLU(),
            nn.Linear(64, d_model),
        )

    def forward(self, x):
        # 1) self-attention: every token looks at every other token (Q = K = V = x)
        attn_output, attn_weights = self.attention(x, x, x)
        # 2) residual connection (add the input back) + layer norm
        x = self.norm1(x + attn_output)
        # 3) feed-forward + residual + layer norm
        x = self.norm2(x + self.feed_forward(x))
        return x, attn_weights


# Step 1: a fake batch with 1 sentence of 5 tokens, each a 16-number vector
tokens = torch.randn(1, 5, d_model)

# Step 2: pass it through the block
block = EncoderBlock()
output, weights = block(tokens)

print("Input shape  :", tuple(tokens.shape))
print("Output shape :", tuple(output.shape), "-> same shape, but now each token knows its context")
print("Attention map:", tuple(weights.shape), "-> 5 x 5 weights (averaged over heads)")
print("Trainable parameters:", sum(p.numel() for p in block.parameters()))
