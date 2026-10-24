"""Session 02 - The same digits task with PyTorch (optional, CPU is fine).

Install: pip install torch --index-url https://download.pytorch.org/whl/cpu
Shows the four steps every deep learning training loop has:
forward pass -> loss -> backward pass -> optimizer step.
"""
import torch
from torch import nn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

torch.manual_seed(0)
X, y = load_digits(return_X_y=True)
X = X / 16.0                                     # scale pixels to 0..1
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)
X_tr, X_te = torch.tensor(X_tr, dtype=torch.float32), torch.tensor(X_te, dtype=torch.float32)
y_tr, y_te = torch.tensor(y_tr), torch.tensor(y_te)

model = nn.Sequential(
    nn.Linear(64, 128), nn.ReLU(),
    nn.Linear(128, 64), nn.ReLU(),
    nn.Linear(64, 10),                           # 10 output classes (digits 0-9)
)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(1, 201):
    model.train()
    logits = model(X_tr)                         # 1. forward
    loss = loss_fn(logits, y_tr)                 # 2. loss
    optimizer.zero_grad()
    loss.backward()                              # 3. backward (autograd)
    optimizer.step()                             # 4. update weights
    if epoch % 50 == 0:
        model.eval()
        with torch.no_grad():
            acc = (model(X_te).argmax(dim=1) == y_te).float().mean().item()
        print(f"epoch {epoch:2d}  loss={loss.item():.3f}  test_acc={acc:.2%}")
