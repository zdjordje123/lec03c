import csv

import matplotlib.pyplot as plt

CSV_PATH = "temperature_data.csv"
COLOR_EXACT = "#2a78d6"
COLOR_RANDOMIZED = "#eb6834"

celsius, fahrenheit, fahrenheit_randomized = [], [], []
with open(CSV_PATH, newline="") as f:
    for row in csv.DictReader(f):
        celsius.append(float(row["temperature_celsius"]))
        fahrenheit.append(float(row["temperature_fahrenheit"]))
        fahrenheit_randomized.append(float(row["temperature_fahrenheit_randomized"]))

order = sorted(range(len(celsius)), key=lambda i: celsius[i])
celsius_sorted = [celsius[i] for i in order]
fahrenheit_sorted = [fahrenheit[i] for i in order]

fig, ax = plt.subplots(figsize=(7, 5), dpi=150)

ax.plot(
    celsius_sorted,
    fahrenheit_sorted,
    color=COLOR_EXACT,
    linewidth=2,
    zorder=2,
    label="Exact conversion",
)
ax.scatter(
    celsius,
    fahrenheit,
    color=COLOR_EXACT,
    s=36,
    zorder=3,
    edgecolors="white",
    linewidths=0.5,
    label="_nolegend_",
)
ax.scatter(
    celsius,
    fahrenheit_randomized,
    color=COLOR_RANDOMIZED,
    s=36,
    zorder=3,
    edgecolors="white",
    linewidths=0.5,
    label="Randomized (±1 std dev)",
)

ax.legend(
    frameon=False,
    fontsize=9,
    labelcolor="#52514e",
    loc="upper left",
)

ax.set_title("Celsius vs. Fahrenheit", fontsize=13, color="#0b0b0b", pad=12)
ax.set_xlabel("Temperature (°C)", fontsize=11, color="#52514e")
ax.set_ylabel("Temperature (°F)", fontsize=11, color="#52514e")

ax.grid(True, color="#e5e4de", linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
for spine in ("left", "bottom"):
    ax.spines[spine].set_color("#c3c2b7")

ax.tick_params(colors="#52514e", labelsize=9)

fig.tight_layout()
fig.savefig("temperature_celsius_vs_fahrenheit.png")
print("Saved temperature_celsius_vs_fahrenheit.png")
