## Simulating two-city agglomeration: path dependence and lock-in

The model below places two cities in direct competition for a fixed national population. Because agglomeration and congestion feedbacks both scale with city size, small random differences in starting conditions compound into large, irreversible outcomes — the same structural parameters produce opposite winners depending only on which city began with a fractional head start.

```{python}
#| label: fig-city-growth
#| fig-cap: "Figure 5.5. Two-city agglomeration model across three parameter scenarios, each run eight times with random initial conditions (ε ~ Uniform(−0.05, 0.05)). Red traces: City A ends dominant (share > 0.55). Black traces: City B ends dominant (share < 0.45). Grey traces: intermediate outcomes. The dashed reference line marks equal population split (0.5). Identical structural parameters produce opposite winners — the final state is path-dependent, not structurally determined."
#| fig-width: 10
#| fig-height: 9
"""Two-city agglomeration model — Chapter 5.
Euler integration of population share dynamics under simultaneous
reinforcing (agglomeration) and balancing (congestion) feedbacks.
Three parameter scenarios × 8 random seeds = 24 trajectories."""
import numpy as np
import matplotlib.pyplot as plt

# -- Named constants -----------------------------------------------------------
P_TOTAL  = 2_000_000        # total conserved national population
P_REF    = 1_000_000        # reference population for elasticity scaling
W0       = 60_000.0         # baseline wage (CAD/yr)
C0       = 50_000.0         # baseline cost of living (CAD/yr equivalent)
MU       = 0.15             # migration responsiveness (yr⁻¹)
DT       = 1.0              # Euler time-step (years)
T_START  = 0
T_END    = 200
N_SEEDS  = 8                # ensemble size per scenario
EPS_MAG  = 0.05             # maximum initial perturbation magnitude

# WH palette
COL_A_DOM  = "#d52a2a"      # City A dominant at t=200
COL_B_DOM  = "#111111"      # City B dominant at t=200
COL_MID    = "#888888"      # intermediate / near-equal

# Outcome classification thresholds
THRESH_HI  = 0.55           # City A dominant if final share > this
THRESH_LO  = 0.45           # City B dominant if final share < this


# -- Wage and cost functions ---------------------------------------------------
def wage(pop, alpha):
    """Agglomeration premium: wage rises as city size grows (power law)."""
    return W0 * (pop / P_REF) ** alpha


def cost(pop, gamma):
    """Congestion penalty: cost of living rises as city size grows."""
    return C0 * (pop / P_REF) ** gamma


# -- Single Euler run ----------------------------------------------------------
def run_simulation(alpha, gamma, seed):
    """Run one 200-year trajectory. Returns array of City A population share."""
    np.random.seed(seed)
    epsilon = np.random.uniform(-EPS_MAG, EPS_MAG)
    # Initial conditions: near-equal split with small random asymmetry
    pa = P_TOTAL / 2.0 * (1.0 + epsilon)
    pb = P_TOTAL - pa

    years   = np.arange(T_START, T_END + 1, DT)
    share_a = np.empty(len(years))
    share_a[0] = pa / P_TOTAL

    for i in range(1, len(years)):
        # Net attractiveness of each city (wage minus cost of living)
        a_a = wage(pa, alpha) - cost(pa, gamma)
        a_b = wage(pb, alpha) - cost(pb, gamma)
        # Migration: proportional to sizes of both donor pools × attractiveness gap
        flow = MU * (pa * pb / P_TOTAL) * (a_a - a_b)
        pa = max(1.0, min(P_TOTAL - 1.0, pa + flow * DT))
        pb = P_TOTAL - pa          # conservation enforced exactly
        share_a[i] = pa / P_TOTAL

    return years, share_a


# -- Three scenario definitions ------------------------------------------------
scenarios = [
    {"alpha": 0.12, "gamma": 0.08, "label": "Agglomeration α=0.12, Congestion γ=0.08"},
    {"alpha": 0.15, "gamma": 0.08, "label": "Strong agglomeration α=0.15"},
    {"alpha": 0.10, "gamma": 0.09, "label": "Balanced α=0.10, γ=0.09"},
]


# -- Run all scenarios ---------------------------------------------------------
all_results = []
for sc in scenarios:
    runs = []
    for seed in range(N_SEEDS):
        years, share_a = run_simulation(sc["alpha"], sc["gamma"], seed)
        runs.append((years, share_a))
    all_results.append(runs)


# -- Figure: 3 panels (one per scenario) --------------------------------------
fig, axes = plt.subplots(3, 1, figsize=(10, 9), dpi=150)

for panel_idx, (ax, sc, runs) in enumerate(zip(axes, scenarios, all_results)):
    # Draw each run, coloured by final outcome
    for years, share_a in runs:
        final = share_a[-1]
        if final > THRESH_HI:
            color, lw, zorder = COL_A_DOM, 1.6, 3
        elif final < THRESH_LO:
            color, lw, zorder = COL_B_DOM, 1.6, 2
        else:
            color, lw, zorder = COL_MID,   1.2, 1
        ax.plot(years, share_a, color=color, linewidth=lw,
                alpha=0.85, zorder=zorder)

    # Reference line: equal population split
    ax.axhline(0.5, color="#aaaaaa", linestyle="--", linewidth=0.8, zorder=0)
    ax.annotate("Equal split", xy=(2, 0.50),
                fontsize=8, color="#aaaaaa", va="bottom")

    # Scenario label — upper right
    ax.annotate(sc["label"],
                xy=(0.98, 0.93), xycoords="axes fraction",
                fontsize=9, color="#333333", ha="right", va="top")

    # Colour key — inline text, no legend box
    ax.annotate("City A dominant", xy=(0.98, 0.83), xycoords="axes fraction",
                fontsize=8, color=COL_A_DOM, ha="right", va="top")
    ax.annotate("City B dominant", xy=(0.98, 0.75), xycoords="axes fraction",
                fontsize=8, color=COL_B_DOM, ha="right", va="top")

    # Axes labels and limits
    ax.set_xlim(T_START, T_END)
    ax.set_ylim(0.0, 1.0)
    ax.set_ylabel("City A population share")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(False)

# x-axis label only on bottom panel
axes[-1].set_xlabel("Year")

plt.tight_layout(pad=1.5)
plt.savefig("_assets/ch05-city-growth.png", dpi=150, bbox_inches="tight")
plt.show()
```

::: {.callout-tip}
## What to try

1. **Set alpha = gamma (equal agglomeration and congestion elasticities).** What happens to the time series? Does a dominant city still emerge? What determines the final equilibrium now? Try alpha = gamma = 0.10 and alpha = gamma = 0.15 — does the magnitude matter when the two elasticities are identical?

2. **Add a third city** by modifying `P_TOTAL` and introducing `P_C`. Start all three cities at equal size (plus small random perturbations). What fraction of runs across 50 seeds produce a single dominant city vs. two co-dominant cities vs. approximate three-way equality? Does the answer change as you increase `alpha` relative to `gamma`?

3. **Map this to a data engineering context.** Two cloud providers compete for enterprise customers. What plays the role of agglomeration (`alpha`) — the network effect that makes a larger platform more valuable to each new customer? What plays the role of congestion (`gamma`) — the factor that makes a dominant platform less attractive as it grows? What would a migration rate (`mu`) look like for cloud switching — and why is it typically an order of magnitude lower than for human migration? What does that imply for lock-in timescales?
:::

> Figure 5.5. Two-city agglomeration model across three parameter scenarios (Scenario 1: α=0.12, γ=0.08; Scenario 2: α=0.15, γ=0.08; Scenario 3: α=0.10, γ=0.09), each run eight times from randomly perturbed equal initial conditions. Red traces: City A ends dominant (share > 0.55). Black traces: City B ends dominant (share < 0.45). Grey traces: near-equal outcomes. The reinforcing agglomeration loop amplifies tiny early advantages into near-complete dominance; the balancing congestion loop determines the speed and ceiling of that dominance. Path dependence is visible in every panel: structural parameters determine the shape of the outcome distribution, not which city wins.
