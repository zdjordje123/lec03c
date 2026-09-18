import torch
import torch.nn as nn


class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.w = nn.Parameter(torch.randn(1))
        self.b = nn.Parameter(torch.randn(1))

    def forward(self, x):
        return self.w * x + self.b


model = LinearRegressionModel()

if __name__ == "__main__":
    print(model)
    print("w:", model.w.item(), "b:", model.b.item())
