## Simulating the carbon cycle: three stocks, one perturbation

WRITER BRIDGE PARAGRAPH GOES HERE

```{python}
#| label: fig-carbon-cycle
#| fig-cap: "Figure 4.5. 3-box carbon cycle model: atmosphere, ocean, and land biosphere under three emission scenarios, 1750–2150. Top: atmospheric CO₂ continues rising in all non-zero-emission scenarios. The reduced-emission scenario slows accumulation but does not return CO₂ to pre-industrial levels — the atmospheric stock accumulates more slowly, not in reverse. Centre: ocean carbon stock grows in all scenarios, reflecting ongoing ocean acidification risk. Bottom: land biosphere carbon with land sink uncertainty (dashed) from 2050. The key result: atmospheric overshoot reflects cumulative stock change, not just current emission rate."
#| fig-width: 10
#| fig-height: 9
"""3-box carbon cycle — Chapter 4. Euler method: atmosphere (A), ocean (O), land biosphere (L) stocks. Anthropogenic CO₂ emission added to atmosphere from 1750 onward. Three scenarios: equilibrium, BAU, reduced."""
import numpy as np
import matplotlib.pyplot as plt

# Named constants — pre-industrial initial stocks (GtC)
A0         = 590.0          # atmosphere
O0         = 38000.0        # ocean
L0         = 2150.0         # land biosphere
# Pre-industrial equilibrium flows (GtC/yr)
F_OA       = 90.0           # ocean → atmosphere outgassing (constant)
F_LA       = 120.0          # land → atmosphere respiration (constant)
F_W        = 0.2            # weathering + volcanism into atmosphere (constant)
k_AO       = F_OA / A0     # atmosphere → ocean uptake rate constant
k_AL       = F_LA / A0     # atmosphere → land photosynthesis rate constant
# Integration parameters
dt         = 1.0            # years
YEAR_START = 1750
YEAR_END   = 2150
PPM_CONV   = 2.13           # 1 ppm = 2.13 GtC

# -- Emission trajectory -------------------------------------------------------
def emissions(year, scenario):
    """Return anthropogenic CO₂ emission (GtC/yr) for a given year and scenario.
    Scenario 0: equilibrium (zero emissions throughout).
    Scenario 1: business-as-usual (BAU).
    Scenario 2: aggressive emissions reduction.
    Scenario 2b: same as 2, with land sink saturation from 2050.
    """
    if scenario == 0:
        return 0.0
    # Historical period shared by all non-zero scenarios
    if year < 1850:
        return 0.5
    if year < 1950:
        return 0.5 + (year - 1850) / 100.0 * (6.0 - 0.5)
    if year < 2023:
        return 6.0 + (year - 1950) / 73.0 * (11.0 - 6.0)
    # Scenario branches from 2023 onward
    if scenario == 1:                                  # BAU
        if year <= 2100:
            return 11.0 + (year - 2023) / 77.0 * (14.0 - 11.0)
        return 14.0
    if scenario in (2, "2b"):                          # reduced emissions
        if year <= 2075:
            return 11.0 + (year - 2023) / 52.0 * (2.0 - 11.0)
        return 2.0
    return 0.0

# -- Run simulation for each scenario -----------------------------------------
scenarios = {
    "eq":  {"id": 0,    "color": "#888888", "ls": "--", "lw": 1.0},
    "bau": {"id": 1,    "color": "#d52a2a", "ls": "-",  "lw": 1.8},
    "red": {"id": 2,    "color": "#111111", "ls": "-",  "lw": 1.8},
    "2b":  {"id": "2b", "color": "#111111", "ls": "--", "lw": 1.2},
}

years = np.arange(YEAR_START, YEAR_END + 1, dt)
results = {}

for name, cfg in scenarios.items():
    A, O, L = A0, O0, L0
    A_arr, O_arr, L_arr = [A], [O], [L]
    for year in years[:-1]:
        # Land sink rate constant — reduced by 20 % from 2050 in scenario 2b
        k_al = k_AL * (0.80 if (name == "2b" and year >= 2050) else 1.0)
        E = emissions(year, cfg["id"])
        dA = F_OA - k_AO * A + F_LA - k_al * A + F_W + E
        dO = k_AO * A - F_OA
        dL = k_al * A - F_LA
        A += dA * dt
        O += dO * dt
        L += dL * dt
        A_arr.append(A)
        O_arr.append(O)
        L_arr.append(L)
    results[name] = {
        "A": np.array(A_arr),
        "O": np.array(O_arr),
        "L": np.array(L_arr),
    }

# -- Figure: 3 panels (rows) --------------------------------------------------
fig, axes = plt.subplots(3, 1, figsize=(10, 9), dpi=150)

# Annotation config: label, panel assignment, position offset
anno = {
    "eq":  "Pre-industrial equilibrium",
    "bau": "Business-as-usual",
    "red": "Reduced emissions",
    "2b":  "Reduced (low land sink)",
}

# Panel 1 (top): atmospheric CO₂ in ppm
ax = axes[0]
for name, cfg in scenarios.items():
    ppm = results[name]["A"] / PPM_CONV
    ax.plot(years, ppm, color=cfg["color"], linestyle=cfg["ls"], linewidth=cfg["lw"])
    # Right-edge annotation for all lines; equilibrium label only in Panel 1
    if name in ("eq", "bau", "red", "2b"):
        ax.annotate(
            anno[name], xy=(YEAR_END, ppm[-1]),
            fontsize=8, color=cfg["color"], ha="right", va="center",
        )
# Pre-industrial reference line
ax.axhline(280, color="#888888", linestyle="--", linewidth=0.7)
ax.annotate("Pre-industrial (280 ppm)", xy=(1755, 280),
            fontsize=8, color="#888888", va="bottom")
# Present-day marker
ax.axvline(2023, color="#888888", linestyle="--", linewidth=0.7)
ax.annotate("2023", xy=(2023, ax.get_ylim()[1]), fontsize=8,
            color="#888888", ha="left", va="top")
ax.set_xlim(YEAR_START, YEAR_END)
ax.set_ylim(250, 650)
ax.set_ylabel("Atmospheric CO\u2082 (ppm)")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(False)

# Panel 2 (middle): ocean carbon stock (GtC)
ax = axes[1]
for name, cfg in scenarios.items():
    ax.plot(years, results[name]["O"],
            color=cfg["color"], linestyle=cfg["ls"], linewidth=cfg["lw"])
# Acidification annotation arrow
ax.annotate(
    "Rising ocean carbon \u2192 ocean acidification",
    xy=(2080, results["bau"]["O"][years == 2080][0]),
    xytext=(2040, 38150),
    fontsize=8, color="#444444",
    arrowprops=dict(arrowstyle="->", color="#444444", lw=0.8),
    ha="left",
)
ax.axvline(2023, color="#888888", linestyle="--", linewidth=0.7)
ax.annotate("2023", xy=(2023, 38400), fontsize=8,
            color="#888888", ha="left", va="top")
ax.set_xlim(YEAR_START, YEAR_END)
ax.set_ylim(37800, 38400)
ax.set_ylabel("Ocean carbon stock (GtC)")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(False)

# Panel 3 (bottom): land biosphere carbon stock (GtC)
ax = axes[2]
for name, cfg in scenarios.items():
    ax.plot(years, results[name]["L"],
            color=cfg["color"], linestyle=cfg["ls"], linewidth=cfg["lw"])
    # Annotate diverging lines in Panel 3
    if name in ("red", "2b"):
        ax.annotate(
            anno[name], xy=(YEAR_END, results[name]["L"][-1]),
            fontsize=8, color=cfg["color"], ha="right", va="center",
        )
ax.axvline(2023, color="#888888", linestyle="--", linewidth=0.7)
ax.annotate("2023", xy=(2023, 2390), fontsize=8,
            color="#888888", ha="left", va="top")
ax.set_xlim(YEAR_START, YEAR_END)
ax.set_ylim(2050, 2400)
ax.set_ylabel("Land biosphere carbon (GtC)")
ax.set_xlabel("Year")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(False)

plt.tight_layout(pad=1.5)
plt.savefig("_assets/ch04-carbon-cycle.png", dpi=150, bbox_inches="tight")
plt.show()
```

::: {.callout-tip}
## What to try

1. **Set emissions to zero in 2050 in Scenario 2.** Does atmospheric CO₂ immediately start falling? Why or why not? How many years does it take for the atmospheric stock to begin declining? What controls that timescale?

2. **Change `k_AO` to 0.80 × its baseline value from 2050 onward** — simulating ocean sink saturation as the ocean surface acidifies. What happens to the atmospheric stock trajectory? How does this compare to the land sink saturation uncertainty in Panel 3?

3. **Map this model to a data pipeline system.** In a large satellite Earth observation processing pipeline: what plays the role of the atmosphere stock? The ocean stock? The anthropogenic emission flow? What would "ocean acidification" look like in a data pipeline context — a stock accumulating something that degrades future processing capacity? Write down the analogy explicitly before continuing.
:::

> Figure 4.5. 3-box carbon cycle model under three emission scenarios, 1750–2150. Top: atmospheric CO₂ (ppm) — even aggressive emissions reduction slows accumulation rather than reversing it on this timescale, because the stock integrates all past emissions. Centre: ocean carbon stock (GtC) — continues growing in all scenarios, corresponding to ongoing acidification. Bottom: land biosphere carbon with land sink uncertainty (dashed) from 2050 onward. The model demonstrates why "net-zero emissions" stabilises the atmospheric stock — it does not reduce it.
