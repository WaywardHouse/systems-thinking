---
### DIAGRAM 1 — Ice-albedo reinforcing loop (replaces text arrow chain in "The ice-albedo feedback")
---

```{mermaid}
graph LR
    IM["Ice Mass"]       -->|"+"| SA["Surface Albedo"]
    SA                   -->|"−"| SR["Solar Absorption"]
    SR                   -->|"+"| ST["Surface Temperature"]
    ST                   -->|"+"| MR["Ice Melt Rate"]
    MR                   -->|"− [R]"| IM

    style IM fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style SA fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style SR fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style ST fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style MR fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
```

> **Caption** Figure 2.1. Ice-albedo reinforcing loop. Two negative causal links and three positive links produce a reinforcing (R) loop: any reduction in ice mass ultimately produces further reduction.
>
> *Notation: a **+** label means cause and effect move in the same direction (both up or both down). A **−** label means they move in opposite directions. A loop is reinforcing (R) when it contains an even number of − signs; balancing (B) when it contains an odd number.*

---
### DIAGRAM 2 — Agglomeration loop (replaces text arrow chain in "Agglomeration in cities")
---

```{mermaid}
graph LR
    SW["Skilled Workers"]    -->|"+"| FC["Firm Concentration"]
    FC                       -->|"+"| JA["Job Availability"]
    JA                       -->|"+ [R]"| SW

    style SW fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style FC fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style JA fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
```

> **Caption** Figure 2.2. Agglomeration reinforcing loop. All three causal links are positive: more workers attract more firms, which create more jobs, which attract more workers. The loop is self-sustaining once initiated.
>
> *Notation: **+** = cause and effect move in the same direction; **−** = opposite directions. Zero − signs in this loop → reinforcing (R).*

---
### DIAGRAM 3 — Recommender amplification loop (replaces text arrow chain)
---

```{mermaid}
graph LR
    EN["Engagement"]         -->|"+"| RP["Recommendation\nProbability"]
    RP                       -->|"+"| EX["Exposure"]
    EX                       -->|"+ [R]"| EN

    style EN fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style RP fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style EX fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
```

> **Caption** Figure 2.3. Recommender reinforcing loop. Content that receives engagement is recommended more, increasing exposure, which increases engagement. The loop amplifies whatever signal is already present in the engagement data.
>
> *Notation: **+** = cause and effect move in the same direction; **−** = opposite directions. Zero − signs → reinforcing (R).*

---
### DIAGRAM 4 — Supply-demand balancing loop (replaces text arrow chain)
---

```{mermaid}
graph LR
    PR["Price"]              -->|"−"| QD["Quantity\nDemanded"]
    PR                       -->|"+"| QS["Quantity\nSupplied"]
    QD                       -->|"+"| GAP["Supply-Demand\nGap"]
    QS                       -->|"−"| GAP
    GAP                      -->|"+"| DLY(["Delay"])
    DLY                      -->|"+ [B]"| PR

    style PR  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style QD  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style QS  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style GAP fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style DLY fill:#fff3f3,stroke:#d52a2a,stroke-width:2px,stroke-dasharray:4 3
```

> **Caption** Figure 2.4. Supply-demand balancing loop. Price sends opposing signals to demand (reducing it) and supply (raising it). Both effects narrow the supply-demand gap, reducing upward pressure on price. The loop seeks equilibrium — but only as fast as supply can respond. The dashed **Delay** node marks the lag between the gap widening and supply adjusting.
>
> *Notation: **+** = cause and effect move in the same direction; **−** = opposite directions. The path through Quantity Supplied carries one − sign (net odd) → balancing (B).*

---
### DIAGRAM 5 — Regularisation balancing loop (replaces text arrow chain)
---

```{mermaid}
graph LR
    MC["Model Complexity"]   -->|"+"| RP["Regularisation\nPenalty"]
    RP                       -->|"+"| PG["Penalty Gradient"]
    PG                       -->|"− [B]"| MC

    style MC fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style RP fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style PG fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
```

> **Caption** Figure 2.5. Regularisation as a designed balancing loop. As model complexity increases, the regularisation penalty increases, increasing the gradient signal that pushes complexity back down. The goal is an implicit complexity target set by the regularisation coefficient λ.
>
> *Notation: **+** = cause and effect move in the same direction; **−** = opposite directions. One − sign on the closing edge → odd → balancing (B).*

---
### DIAGRAM 6 — Archetype overview (matplotlib, 5 subplots)
---

```{python}
#| label: fig-archetypes
#| fig-cap: "Figure 2.6. Signature behaviour of the five system archetypes. Each pattern is generated by a specific feedback structure: (1) a single unconstrained reinforcing loop; (2) a balancing loop with no delay; (3) a balancing loop with significant delay; (4) a reinforcing loop eventually opposed by a balancing loop; (5) the same structure as (4) but with the constraining loop delayed until after overshoot."
#| fig-width: 12
#| fig-height: 3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

t = np.linspace(0, 120, 500)

# Curves — analytically generated, no simulation
curves = [
    ("Exponential growth",      np.exp(0.04 * t),                                              "#d52a2a", None),
    ("Goal seeking",            20 - 5 * np.exp(-0.05 * t),                                    "#111111", 20),
    ("Oscillation",             20 + 4 * np.cos(0.15 * t) * np.exp(-0.01 * t),                "#d52a2a", 20),
    ("Limits to growth",        20 / (1 + np.exp(-0.08 * (t - 60))),                           "#111111", 20),
    ("Overshoot & collapse",    np.where(t < 80, 0.12 * t, 0.12 * 80 * np.exp(-0.06*(t-80))),"#888888", 0.12 * 80),
]

fig, axes = plt.subplots(1, 5, figsize=(12, 3), dpi=150)

for ax, (title, y, color, ref) in zip(axes, curves):
    ax.plot(t, y, color=color, linewidth=1.8)

    if ref is not None:
        ax.axhline(ref, color="#888888", linewidth=0.9, linestyle="--")

    ax.set_title(title, fontsize=8, pad=6)

    # Minimal spines — left and bottom only
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # No tick labels, no gridlines
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=0)
    ax.grid(False)

    # Tight y-margins
    y_range = y.max() - y.min()
    pad = y_range * 0.12 if y_range > 0 else 1
    ax.set_ylim(y.min() - pad, y.max() + pad)

fig.tight_layout(pad=1.2)
plt.savefig("_assets/ch02-archetype-sketches.png", dpi=150, bbox_inches="tight")
plt.show()
```
