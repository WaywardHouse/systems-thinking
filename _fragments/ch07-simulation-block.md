## The predator-prey model

The Lotka-Volterra equations are the canonical demonstration of coupled oscillating stocks. Two interacting populations — prey and predator — produce sustained periodic oscillations purely through the interaction of a reinforcing feedback (prey reproducing) and two balancing feedbacks (predation removing prey; predator starvation when prey are scarce). No external forcing is needed. The oscillation is structural: it is encoded in the equations themselves. The time series makes the rhythm visible, but it is the phase portrait — prey on the x-axis, predator on the y-axis — that reveals the cyclic attractor. Each scenario traces a closed orbit around the same equilibrium point. The orbit does not spiral in or out; it simply circles. That is what sustained oscillation looks like in state space.

```{python}
#| label: fig-predator-prey
#| fig-cap: "Figure 7.5. Lotka-Volterra predator-prey model across three scenarios (Euler integration, dt=0.05 yr, t=80 yr). Left: time series of prey (solid) and predator (dashed) populations. All three scenarios share the same initial conditions (prey=40, predator=9) but differ in predation rate and prey birth rate, producing orbits of different amplitude and period. Right: phase portrait (prey vs. predator). Each trajectory traces a closed orbit around the analytical equilibrium at (d/b, r/a) — marked with a cross for Scenario 1. Directional arrows show the sense of rotation. The phase portrait makes the cyclic attractor visible in a way the time series cannot: identical structure, different orbit size."
#| fig-width: 12
#| fig-height: 5
"""Lotka-Volterra predator-prey model — Chapter 7.
Euler integration of two coupled stocks: prey and predator populations.
Three scenarios isolate the effect of predation pressure and prey birth rate.

NOTE on time step: dt=0.05 is required for numerical stability in this
oscillatory system. With dt=1.0 the Euler method accumulates error each
step in a way that amplifies the orbit outward — the trajectory spirals
away from the true closed orbit rather than closing on it. This is a
property of Euler integration applied to oscillatory ODEs, not a property
of the underlying model. A demonstration: set DT=1.0 for Scenario 1 and
observe the slow outward spiral over 80 years."""

import numpy as np
import matplotlib.pyplot as plt

# -- Named constants -----------------------------------------------------------
DT     = 0.05    # Euler time-step (years) — small dt required for stability
T_END  = 80.0    # simulation horizon (years)

# Scenario parameters: (r, a, b, d, prey0, predator0, color, ls, lw, label)
# r = prey birth rate (yr⁻¹)
# a = predation rate (encounters per unit time)
# b = predator growth efficiency (prey consumed → predator born)
# d = predator mortality rate (yr⁻¹)
SCENARIOS = [
    dict(r=0.4,  a=0.02,  b=0.01, d=0.3,
         prey0=40, pred0=9,
         color="#888888", ls="--", lw=1.2,
         label="Baseline"),
    dict(r=0.4,  a=0.04,  b=0.01, d=0.3,
         prey0=40, pred0=9,
         color="#d52a2a", ls="-",  lw=1.8,
         label="High predation"),
    dict(r=0.3,  a=0.015, b=0.01, d=0.3,
         prey0=40, pred0=9,
         color="#111111", ls="-",  lw=1.8,
         label="Prey refuge"),
]

# Equilibrium for Scenario 1: prey* = d/b, predator* = r/a
EQ_PREY = SCENARIOS[0]["d"] / SCENARIOS[0]["b"]   # = 30
EQ_PRED = SCENARIOS[0]["r"] / SCENARIOS[0]["a"]   # = 20


# -- Euler integration ---------------------------------------------------------
def run_lotka_volterra(r, a, b, d, prey0, pred0):
    """
    Integrate the Lotka-Volterra system using the Euler method.

    d(prey)/dt   = r * prey  - a * prey * predator
    d(predator)/dt = b * prey * predator - d * predator

    Returns: (t, prey, predator) as 1-D numpy arrays.
    """
    steps    = int(T_END / DT) + 1
    t        = np.linspace(0.0, T_END, steps)
    prey     = np.empty(steps)
    predator = np.empty(steps)

    prey[0]     = prey0
    predator[0] = pred0

    for i in range(1, steps):
        x = prey[i - 1]
        y = predator[i - 1]

        # Rates of change at the current state
        dx = r * x - a * x * y          # prey: births minus predation losses
        dy = b * x * y - d * y          # predator: prey-driven growth minus mortality

        # Euler step — advance both stocks simultaneously
        prey[i]     = x + dx * DT
        predator[i] = y + dy * DT

        # Clamp to zero: populations cannot go negative under Euler discretisation
        if prey[i]     < 0: prey[i]     = 0.0
        if predator[i] < 0: predator[i] = 0.0

    return t, prey, predator


# -- Run all scenarios ---------------------------------------------------------
results = []
for sc in SCENARIOS:
    t, prey, predator = run_lotka_volterra(
        sc["r"], sc["a"], sc["b"], sc["d"], sc["prey0"], sc["pred0"]
    )
    results.append((t, prey, predator))


# -- Figure: 2-panel layout ----------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), dpi=150)


# -- Panel 1: Time series -------------------------------------------------------
for sc, (t, prey, predator) in zip(SCENARIOS, results):
    # Prey: solid line within scenario color
    ax1.plot(t, prey,     color=sc["color"], linestyle="-",  linewidth=sc["lw"])
    # Predator: dotted line within same scenario color
    ax1.plot(t, predator, color=sc["color"], linestyle=":",  linewidth=sc["lw"])

# Annotate "Prey" and "Predator" labels with arrows, pointing to Scenario 1 lines
# Pick a point in the upper portion of the plot where both curves are visible
t_ann  = 15.0                              # annotation target year (≈ first prey peak)
idx_ann = int(t_ann / DT)
prey_ann = results[0][1][idx_ann]
pred_ann = results[0][2][idx_ann]

ax1.annotate("Prey",
             xy=(t_ann, prey_ann),
             xytext=(t_ann + 6, prey_ann + 10),
             fontsize=8.5, color="#888888",
             arrowprops=dict(arrowstyle="-", color="#888888", lw=0.8),
             va="center")

ax1.annotate("Predator",
             xy=(t_ann, pred_ann),
             xytext=(t_ann + 6, pred_ann - 8),
             fontsize=8.5, color="#888888",
             arrowprops=dict(arrowstyle="-", color="#888888", lw=0.8),
             va="center")

# Annotate scenario labels at right edge of each prey line
label_offsets = {"Baseline": 4, "High predation": -6, "Prey refuge": 10}
for sc, (t, prey, predator) in zip(SCENARIOS, results):
    yoff = label_offsets[sc["label"]]
    ax1.annotate(sc["label"],
                 xy=(t[-1], prey[-1]),
                 xytext=(t[-1] - 1.5, prey[-1] + yoff),
                 fontsize=8, color=sc["color"],
                 ha="right", va="center")

ax1.set_xlabel("Year")
ax1.set_ylabel("Population")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.grid(False)


# -- Panel 2: Phase portrait ----------------------------------------------------
for sc, (t, prey, predator) in zip(SCENARIOS, results):
    # Full orbit
    ax2.plot(prey, predator, color=sc["color"], linestyle=sc["ls"],
             linewidth=sc["lw"])

    # Mark initial condition with a filled dot
    ax2.plot([sc["prey0"]], [sc["pred0"]], "o",
             color=sc["color"], markersize=4)

    # Directional arrow at roughly the midpoint of the trajectory
    mid = len(t) // 2
    ax2.annotate("",
                 xy=(prey[mid + 1], predator[mid + 1]),
                 xytext=(prey[mid],  predator[mid]),
                 arrowprops=dict(arrowstyle="-|>", color=sc["color"],
                                 lw=sc["lw"], mutation_scale=10))

# Mark the analytical equilibrium for Scenario 1 with a cross
ax2.plot([EQ_PREY], [EQ_PRED], "x",
         color="#888888", markersize=8, markeredgewidth=1.5)
ax2.annotate("Equilibrium\n(30, 20)",
             xy=(EQ_PREY, EQ_PRED),
             xytext=(EQ_PREY + 4, EQ_PRED + 5),
             fontsize=8, color="#888888", va="bottom")

# Annotate scenario labels near each orbit
# Position labels near the upper-right portion of each orbit
phase_label_xy = {
    "Baseline":      (65, 26),
    "High predation":(68, 36),
    "Prey refuge":   (54, 22),
}
phase_label_off = {
    "Baseline":      ( 4,  4),
    "High predation":( 4, -8),
    "Prey refuge":   (-4,  6),
}
for sc in SCENARIOS:
    xy  = phase_label_xy[sc["label"]]
    off = phase_label_off[sc["label"]]
    ax2.annotate(sc["label"],
                 xy=xy,
                 xytext=(xy[0] + off[0], xy[1] + off[1]),
                 fontsize=8, color=sc["color"], ha="left", va="center")

ax2.set_xlabel("Prey population")
ax2.set_ylabel("Predator population")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.grid(False)

plt.tight_layout(pad=1.5)
plt.savefig("_assets/ch07-predator-prey.png", dpi=150, bbox_inches="tight")
plt.show()
```

::: {.callout-tip}
## What to try

1. **Set `DT = 1.0`** (change the Euler step size from 0.05 to 1.0) for Scenario 1. What happens to the trajectory? Does it converge to a cycle, spiral inward, or spiral outward? What does this tell you about the relationship between time step size and numerical stability in oscillatory systems?

2. **Find the equilibrium analytically.** For the Lotka-Volterra equations, the non-trivial equilibrium is at `prey* = d/b` and `predator* = r/a`. Verify this for Scenario 1 (the answer is prey\*=30, predator\*=20). Now start the simulation at exactly `(prey0=30, pred0=20)` — does the model stay there? What does this tell you about numerical stability of the equilibrium versus analytical stability?

3. **Add a carrying capacity for the prey.** Modify the prey equation to `dx = r * x * (1 - x / K) - a * x * y`, where `K = 200` is the carrying capacity. How does this change the phase portrait? Does the system still produce sustained oscillations, or does it spiral into the equilibrium? What structural change to the feedback loops did adding `K` introduce?
:::

> Figure 7.5. Lotka-Volterra predator-prey model across three scenarios (Euler integration, dt=0.05 yr, t=80 yr). Left: time series of prey (solid lines) and predator (dotted lines) populations. All three scenarios share the same initial conditions (prey=40, predator=9) and predator parameters (b=0.01, d=0.3), but differ in predation rate and prey birth rate: Baseline (r=0.4, a=0.02, grey dashed), High predation (r=0.4, a=0.04, red), and Prey refuge (r=0.3, a=0.015, black). Right: phase portrait (prey on x-axis, predator on y-axis). Each scenario traces a closed orbit around the analytical equilibrium at (d/b, r/a) — marked with a cross at (30, 20) for the Baseline scenario. Filled dots mark the shared initial condition. Directional arrows show the counter-clockwise sense of rotation. The phase portrait makes the cyclic attractor explicit: prey rises first (reinforcing loop), which drives predator growth (balancing loop on prey), which depletes prey, which starves predators, which allows prey to recover — and the cycle repeats. The High predation scenario produces a larger-amplitude orbit; the Prey refuge scenario produces a tighter one, reflecting slower dynamics on both stocks.
