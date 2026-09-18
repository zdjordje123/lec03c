import csv

import numpy as np

CSV_PATH = "temperature_data.csv"

celsius, fahrenheit_randomized = [], []
with open(CSV_PATH, newline="") as f:
    for row in csv.DictReader(f):
        celsius.append(float(row["temperature_celsius"]))
        fahrenheit_randomized.append(float(row["temperature_fahrenheit_randomized"]))

X_train = np.array(celsius)
y_train = np.array(fahrenheit_randomized)

if __name__ == "__main__":
    print("X_train:", X_train)
    print("y_train:", y_train)
