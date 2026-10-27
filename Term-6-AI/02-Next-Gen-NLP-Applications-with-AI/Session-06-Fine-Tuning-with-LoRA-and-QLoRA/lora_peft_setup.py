"""Session 06 - Example 4 (optional, needs downloads): add LoRA to a real model with PEFT.

This only PREPARES the model and prints how many parameters are trainable.
Training itself is best done on Google Colab with a GPU.
Install: pip install torch transformers peft
Run:     python lora_peft_setup.py
"""
try:
    from transformers import AutoModelForCausalLM
    from peft import LoraConfig, get_peft_model
except ImportError:
    print("Please install first:  pip install torch transformers peft")
    raise SystemExit

# Step 1: load a small pre-trained model (about 330 MB, downloaded once)
model_name = "distilgpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)

# Step 2: describe the LoRA adapters we want
config = LoraConfig(
    r=8,                          # rank of A and B
    lora_alpha=16,                # scaling: the update is multiplied by alpha / r
    lora_dropout=0.05,            # a little dropout to reduce overfitting
    target_modules=["c_attn"],    # the attention projection layer in GPT-2 models
    task_type="CAUSAL_LM",        # we are adapting a text-generation model
)

# Step 3: wrap the model - the original weights are frozen automatically
model = get_peft_model(model, config)

# Step 4: see how few parameters will be trained
model.print_trainable_parameters()

# Step 5 (on Colab): train with transformers.Trainer, then save only the adapter:
# model.save_pretrained("my-lora-adapter")    # a few MB instead of the full model
