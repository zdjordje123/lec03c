import csv

import numpy as np
import torch
from torch.utils.data import DataLoader, TensorDataset

CSV_PATH = "temperature_data.csv"

celsius, fahrenheit_randomized = [], []
with open(CSV_PATH, newline="") as f:
    for row in csv.DictReader(f):
        celsius.append(float(row["temperature_celsius"]))
        fahrenheit_randomized.append(float(row["temperature_fahrenheit_randomized"]))

X_train = np.array(celsius)
y_train = np.array(fahrenheit_randomized)

X_train_norm = torch.tensor(
    (X_train - X_train.mean()) / X_train.std(), dtype=torch.float32
)
y_train = torch.tensor(y_train, dtype=torch.float32)

train_ds = TensorDataset(X_train_norm, y_train)
train_dl = DataLoader(train_ds, batch_size=1)

if __name__ == "__main__":
    print("X_train:", X_train)
    print("X_train_norm:", X_train_norm)
    print("y_train:", y_train)
    print("train_ds length:", len(train_ds))
    for batch_X, batch_y in train_dl:
        print("batch:", batch_X, batch_y)
