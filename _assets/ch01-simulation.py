"""Glacier ice mass — Chapter 1. Euler method: S[i+1] = S[i] + (acc - abl) * dt"""
import numpy as np
import matplotlib.pyplot as plt

# Parameters — change these to explore
S0, dt, T = 50.0, 1.0, 120   # initial stock (km³), time step (yr), duration (yr)
steps = int(T / dt) + 1
time  = np.arange(steps) * dt

def euler(acc, abl):
    """Integrate stock over T years given constant inflow acc and outflow abl."""
    S = np.empty(steps); S[0] = S0
    for i in range(steps - 1):
        S[i+1] = S[i] + (acc - abl) * dt   # stock = integral of net flow
    return S

# Three scenarios: (accumulation, ablation) in km³/yr
S_balanced   = euler(acc=1.2, abl=1.20)   # net flow = 0
S_advancing  = euler(acc=1.5, abl=1.20)   # net flow = +0.3
S_retreating = euler(acc=1.2, abl=1.45)   # net flow = −0.25

# Plot
fig, ax = plt.subplots(figsize=(8, 4), dpi=150)
ax.plot(time, S_balanced,   color="#888888", linewidth=1.5, label="Balanced (acc = abl = 1.2 km³/yr)")
ax.plot(time, S_advancing,  color="#d52a2a", linewidth=1.5, label="Advancing (acc = 1.5 km³/yr)")
ax.plot(time, S_retreating, color="#111111", linewidth=1.5, label="Retreating (abl = 1.45 km³/yr)")
ax.axhline(y=0, color="#888888", linestyle="--", linewidth=0.8, label="Glacier disappears")

# Annotations at year 120
ax.annotate("Glacier advances", xy=(120, S_advancing[-1]),  fontsize=9, color="#d52a2a", ha="right")
ax.annotate("Glacier retreats", xy=(120, S_retreating[-1]), fontsize=9, color="#111111", ha="right")
ax.annotate("Balanced",         xy=(120, 50),               fontsize=9, color="#888888", ha="right")

ax.set_xlim(0, 120);  ax.set_ylim(0, 75)
ax.set_xticks(range(0, 121, 20));  ax.set_yticks(range(0, 76, 15))
ax.set_xlabel("Time (years)");     ax.set_ylabel("Ice mass (km³)")
ax.set_title("Glacier ice mass under three flow scenarios")
ax.legend(loc="upper left", fontsize=8)
ax.spines["top"].set_visible(False);  ax.spines["right"].set_visible(False)
ax.grid(False)

plt.tight_layout()
plt.savefig("_assets/ch01-glacier-simulation.png", dpi=150, bbox_inches="tight")
plt.show()
