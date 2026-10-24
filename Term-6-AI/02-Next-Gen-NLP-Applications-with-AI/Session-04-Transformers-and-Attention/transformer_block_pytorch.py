"""Session 04 - A complete transformer encoder block in PyTorch.

Components: token embedding + sinusoidal positional encoding,
multi-head self-attention, residual connections, layer normalization,
position-wise feed-forward network.
"""
import math
import torch
from torch import nn

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=512):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        pos = torch.arange(max_len).unsqueeze(1)
        div = torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(pos * div)      # even dimensions
        pe[:, 1::2] = torch.cos(pos * div)      # odd dimensions
        self.register_buffer("pe", pe)

    def forward(self, x):                       # x: (batch, seq, d_model)
        return x + self.pe[: x.size(1)]

class EncoderBlock(nn.Module):
    def __init__(self, d_model=64, n_heads=4, d_ff=256, dropout=0.1):
        super().__init__()
        self.attn = nn.MultiheadAttention(d_model, n_heads, dropout=dropout, batch_first=True)
        self.norm1, self.norm2 = nn.LayerNorm(d_model), nn.LayerNorm(d_model)
        self.ff = nn.Sequential(nn.Linear(d_model, d_ff), nn.GELU(), nn.Linear(d_ff, d_model))
        self.drop = nn.Dropout(dropout)

    def forward(self, x):
        attn_out, weights = self.attn(x, x, x)            # self-attention: Q = K = V = x
        x = self.norm1(x + self.drop(attn_out))           # residual + layer norm
        x = self.norm2(x + self.drop(self.ff(x)))         # feed-forward + residual + norm
        return x, weights

torch.manual_seed(0)
vocab_size, d_model = 1000, 64
embed = nn.Embedding(vocab_size, d_model)
posenc = PositionalEncoding(d_model)
block = EncoderBlock(d_model)

token_ids = torch.tensor([[12, 45, 7, 300, 2, 99]])       # one sentence of 6 token ids
x = posenc(embed(token_ids))
out, attn = block(x)
print("token ids     :", token_ids.shape)
print("after embed+PE:", x.shape)
print("block output  :", out.shape, "(same shape, richer context)")
print("attention map :", attn.shape, "(averaged over heads)")
print("parameters in one block:", sum(p.numel() for p in block.parameters()))
