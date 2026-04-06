"""Delayed thermostat — Chapter 2. Euler method with collections.deque delay buffer."""
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# Parameters
T_goal, T0, k, loss = 20.0, 15.0, 0.5, 0.05  # goal °C, start °C, gain, heat-loss rate
dt, t_end = 1.0, 240                           # Euler step (min), duration (min)
steps = int(t_end / dt) + 1
time  = np.arange(steps) * dt

# Three scenarios: (delay_minutes, colour, label)
scenarios = [
    ( 5, "#888888", "5-min delay"),
    (15, "#d52a2a", "15-min delay"),
    (45, "#111111", "45-min delay"),
]

fig, ax = plt.subplots(figsize=(8, 4), dpi=150)

for delay_min, color, label in scenarios:
    D_steps = int(delay_min / dt)                   # buffer length in time steps
    buf = deque([0.0] * D_steps, maxlen=D_steps)    # pre-fill with zeros (heater off)

    T = np.empty(steps); T[0] = T0
    for i in range(steps - 1):
        gap       = T_goal - T[i]           # current sensing gap
        buf.append(k * gap)                 # store current control signal in buffer
        heating   = buf[0]                  # oldest (delayed) signal drives heater
        T[i + 1]  = T[i] + (heating - loss * T[i]) * dt

    ax.plot(time, T, color=color, linewidth=1.5, label=label)
    ax.annotate(label, xy=(240, T[-1]), fontsize=9, color=color, ha="right", va="center")

# Goal reference line
ax.axhline(y=T_goal, color="#888888", linestyle="--", linewidth=0.8)
ax.annotate("Goal (20°C)", xy=(5, T_goal), fontsize=8, color="#888888", va="bottom")

ax.set_xlim(0, 240)
ax.set_xlabel("Time (minutes)")
ax.set_ylabel("Room temperature (°C)")
ax.set_title("Thermostat with delay: three scenarios")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(False)

plt.tight_layout()
plt.savefig("_assets/ch02-thermostat-simulation.png", dpi=150, bbox_inches="tight")
plt.show()
