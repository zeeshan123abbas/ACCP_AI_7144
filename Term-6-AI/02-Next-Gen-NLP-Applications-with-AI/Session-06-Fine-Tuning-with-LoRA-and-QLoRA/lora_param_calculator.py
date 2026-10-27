"""Session 06 - Example 2: how many parameters does LoRA really train?

We count trainable numbers for a transformer where LoRA is added to the
query (q) and value (v) projection of every layer - a very common setup.
Run: python lora_param_calculator.py
"""

def lora_params_per_matrix(d_in, d_out, rank):
    """A is rank x d_in and B is d_out x rank."""
    return rank * d_in + d_out * rank


# Step 1: describe a model similar to a 7-billion-parameter LLM
total_model_params = 7_000_000_000
hidden_size = 4096        # width of each layer
num_layers = 32           # number of transformer blocks
matrices_per_layer = 2    # we adapt q_proj and v_proj only

# Step 2: try several ranks and print a small table
print(f"{'rank':>5} | {'trainable params':>17} | {'% of model':>10}")
print("-" * 40)
for rank in [4, 8, 16, 64]:
    one_matrix = lora_params_per_matrix(hidden_size, hidden_size, rank)
    trainable = one_matrix * matrices_per_layer * num_layers
    percent = trainable / total_model_params * 100
    print(f"{rank:>5} | {trainable:>17,} | {percent:>9.3f}%")

# Step 3: the size of the saved adapter file (16-bit numbers = 2 bytes each)
rank = 8
adapter_params = lora_params_per_matrix(hidden_size, hidden_size, rank) * matrices_per_layer * num_layers
print(f"\nAdapter file at rank {rank}: about {adapter_params * 2 / 1_000_000:.1f} MB")
print(f"Full model copy in 16-bit : about {total_model_params * 2 / 1_000_000_000:.0f} GB")
