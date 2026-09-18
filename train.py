import torch
import torch.nn as nn

from model import model
from train_data import train_dl

LEARNING_RATE = 0.01
EPOCHS = 100

loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)

for epoch in range(EPOCHS):
    epoch_loss = 0.0
    for batch_X, batch_y in train_dl:
        optimizer.zero_grad()
        z = model(batch_X)
        loss = loss_fn(z, batch_y)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()

    if epoch % 10 == 0 or epoch == EPOCHS - 1:
        print(f"epoch {epoch:3d}  loss {epoch_loss / len(train_dl):.4f}")

print("w:", model.w.item(), "b:", model.b.item())
