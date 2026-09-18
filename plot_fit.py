import matplotlib.pyplot as plt
import torch

import train  # noqa: F401  (runs the training loop)
from model import model
from train_data import X_train, X_train_norm, y_train

COLOR_FIT = "#2a78d6"
COLOR_EXPERIMENTAL = "#eb6834"

with torch.no_grad():
    z = model(X_train_norm).numpy()

order = sorted(range(len(X_train)), key=lambda i: X_train[i])
celsius_sorted = X_train[order]
z_sorted = z[order]

fig, ax = plt.subplots(figsize=(7, 5), dpi=150)

ax.plot(
    celsius_sorted,
    z_sorted,
    color=COLOR_FIT,
    linewidth=2,
    zorder=2,
    label="Fitted model",
)
ax.scatter(
    X_train,
    y_train.numpy(),
    color=COLOR_EXPERIMENTAL,
    s=36,
    zorder=3,
    edgecolors="white",
    linewidths=0.5,
    label="Experimental data",
)

ax.set_title("Fitted Model vs. Experimental Data", fontsize=13, color="#0b0b0b", pad=12)
ax.set_xlabel("Temperature (°C)", fontsize=11, color="#52514e")
ax.set_ylabel("Temperature (°F)", fontsize=11, color="#52514e")

ax.grid(True, color="#e5e4de", linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
for spine in ("left", "bottom"):
    ax.spines[spine].set_color("#c3c2b7")

ax.tick_params(colors="#52514e", labelsize=9)
ax.legend(frameon=False, fontsize=9, labelcolor="#52514e", loc="upper left")

fig.tight_layout()
fig.savefig("fitted_model_vs_experimental.png")
print("Saved fitted_model_vs_experimental.png")
