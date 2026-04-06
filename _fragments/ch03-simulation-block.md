## Simulating segregation: from mild preferences to macro-level patterns

WRITER BRIDGE PARAGRAPH GOES HERE

```{python}
#| label: fig-schelling
#| fig-cap: "Figure 3.4. Schelling segregation model. Left: initial random placement of Type A (red), Type B (black), and empty (grey) cells. Centre: state after 50 steps with satisfaction threshold T = 0.33 — near-complete segregation has emerged. Right: segregation index over time for three thresholds. Even at T = 0.20 macro-level segregation emerges within 30 steps. The tipping point is in the interaction structure, not in the individual preferences."
#| fig-width: 12
#| fig-height: 4
"""Schelling segregation — Chapter 3. Grid: GRID_SIZE × GRID_SIZE. Two agent types. Agents move if fraction same-type neighbours < THRESHOLD."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Named constants
GRID_SIZE = 40
DENSITY_A = 0.45
DENSITY_B = 0.45
N_STEPS   = 50
SEED      = 42

# Threshold values to compare; T=0.33 is used for the spatial panels
THRESHOLDS = [0.20, 0.33, 0.50]
T_SPATIAL  = 0.33

# -- Initialise grid ----------------------------------------------------------
np.random.seed(SEED)
n_cells  = GRID_SIZE * GRID_SIZE
n_a      = int(n_cells * DENSITY_A)
n_b      = int(n_cells * DENSITY_B)
flat     = np.zeros(n_cells, dtype=np.int8)
flat[:n_a]      = 1                          # Type A
flat[n_a:n_a + n_b] = 2                      # Type B
np.random.shuffle(flat)
base_grid = flat.reshape(GRID_SIZE, GRID_SIZE)

# -- Moore neighbourhood helpers ----------------------------------------------
def neighbour_counts(grid):
    """Return (same-type count, occupied count) arrays for every cell."""
    from numpy.lib.stride_tricks import sliding_window_view
    padded  = np.pad(grid, 1, mode="wrap")
    windows = sliding_window_view(padded, (3, 3))     # shape (R, C, 3, 3)
    same    = np.zeros_like(grid, dtype=np.int8)
    occ     = np.zeros_like(grid, dtype=np.int8)
    for dr in range(3):
        for dc in range(3):
            if dr == 1 and dc == 1:
                continue                              # skip centre cell
            nb = windows[:, :, dr, dc]
            occ  += (nb > 0).astype(np.int8)
            same += (nb == grid).astype(np.int8) * (grid > 0).astype(np.int8)
    return same, occ

# -- Segregation index --------------------------------------------------------
def segregation_index(grid):
    """Average fraction of same-type occupied neighbours across all agents."""
    same, occ = neighbour_counts(grid)
    occupied  = grid > 0
    fracs     = np.where((occupied) & (occ > 0), same / occ, np.nan)
    return float(np.nanmean(fracs))

# -- Single step: move unsatisfied agents to random empty cells ---------------
def step(grid, threshold):
    same, occ  = neighbour_counts(grid)
    occupied   = grid > 0
    satisfied  = np.where(occupied & (occ > 0), same / occ >= threshold, True)
    unsatisfied_idx = list(zip(*np.where(~satisfied & occupied)))
    empty_idx       = list(zip(*np.where(grid == 0)))
    np.random.shuffle(unsatisfied_idx)
    for pos in unsatisfied_idx:
        if not empty_idx:
            break
        dest = empty_idx.pop(np.random.randint(len(empty_idx)))
        grid[dest], grid[pos] = grid[pos], 0
        empty_idx.append(pos)
    return grid

# -- Run simulation for each threshold ----------------------------------------
series    = {}
grid_init = None
grid_final = None

for T in THRESHOLDS:
    g = base_grid.copy()
    s = [segregation_index(g)]           # record initial state
    if T == T_SPATIAL:
        grid_init = g.copy()             # save initial grid for panel 1
    for _ in range(N_STEPS):
        g = step(g, T)
        s.append(segregation_index(g))
    series[T] = s
    if T == T_SPATIAL:
        grid_final = g.copy()            # save final grid for panel 2

# -- Figure: 3 panels ---------------------------------------------------------
cmap = ListedColormap(["#f5f5f5", "#d52a2a", "#111111"])

fig, axes = plt.subplots(1, 3, figsize=(12, 4), dpi=150)

# Panel 1: initial grid
axes[0].imshow(grid_init, cmap=cmap, vmin=0, vmax=2, interpolation="nearest")
axes[0].set_title("Initial state")
axes[0].set_xticks([])
axes[0].set_yticks([])

# Panel 2: final grid after T=0.33
axes[1].imshow(grid_final, cmap=cmap, vmin=0, vmax=2, interpolation="nearest")
axes[1].set_title("After 50 steps  (T = 0.33)")
axes[1].set_xticks([])
axes[1].set_yticks([])

# Panel 3: segregation index time series
ax = axes[2]
palette = {0.20: "#888888", 0.33: "#d52a2a", 0.50: "#111111"}
labels  = {0.20: "T = 0.20", 0.33: "T = 0.33", 0.50: "T = 0.50"}
steps_x = list(range(N_STEPS + 1))

for T in THRESHOLDS:
    ax.plot(steps_x, series[T], color=palette[T], linewidth=1.5)
    ax.annotate(
        labels[T],
        xy=(N_STEPS, series[T][-1]),
        fontsize=9, color=palette[T],
        ha="right", va="center",
    )

ax.set_xlabel("Step")
ax.set_ylabel("Segregation index")
ax.set_ylim(0.4, 1.0)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(False)

plt.tight_layout()
plt.savefig("_assets/ch03-schelling-simulation.png", dpi=150, bbox_inches="tight")
plt.show()
```

::: {.callout-tip}
## What to try

1. **Lower the threshold to T = 0.10** (agents satisfied as long as even one neighbour shares their type). Does segregation still emerge? What does this tell you about the minimum preference that produces macro-level separation?

2. **Increase the grid to 60 × 60 and run for 100 steps.** Does the final segregation index change? What does this tell you about scale?

3. **Set DENSITY_A = 0.30 and DENSITY_B = 0.60** (asymmetric populations). What happens to the spatial structure of the final state? Is the minority group more or less segregated than in the symmetric case?
:::

> Figure 3.4. Schelling segregation model. Left: initial random placement. Centre: state after 50 steps with satisfaction threshold T = 0.33 — near-complete segregation has emerged from a randomly mixed start. Right: segregation index over time for three threshold values. At T = 0.20 segregation still emerges; at T = 0.50 it is faster and more complete. The macro-level outcome is not a reflection of the individual preference — it is a product of the feedback between individual decisions and neighbourhood composition.
