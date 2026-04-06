# Chapter 01 — Prose Additions

Produced by: Writer agent  
Date: 2026-04-05  
Status: ready for assembly

All additions are insertions only. No existing prose has been altered.

---

### ADDITION 1 — Response time display equation (insert in "What a stock-flow analysis tells you" section)

**Position:** After the numbered list that ends with item 5 ("What is outside the boundary you drew?"), immediately before the paragraph that begins "The response time is particularly important."

**Replace:** Nothing — this is a pure insertion between the numbered list and that paragraph.

**Insert the following block:**

---

$$\tau = \frac{S}{|F_{\text{net}}|}$$

where $\tau$ is the response time, $S$ is the stock, and $F_{\text{net}}$ is the net flow (inflow minus outflow). When the net flow is negative — outflows exceed inflows — $\tau$ tells you how long the stock can persist before it reaches zero at the current rate of loss.

---

### ADDITION 2 — Three cross-link callouts (insert at positions specified in plan)

---

**CALLOUT 1 — position: after "Stocks and flows" section (after the existing calculus note callout), before the horizontal rule that opens "Drawing the system"**

```markdown
::: {.callout-note}
## The mathematics in depth

The equation $dS/dt = \text{inflow} - \text{outflow}$ is the entry point to a large body of mathematics. If you want to understand equilibria, stability, and what happens when flows are not constant, [WH Maths Vol 5](https://wayward.house/learn/maths/core/) covers differential calculus from first principles, and Vol 8 covers the stability analysis of feedback systems in full.
:::
```

---

**CALLOUT 2 — position: after "Three examples" section (after the data pipeline subsection), before the horizontal rule that opens "Simulating the glacier"**

```markdown
::: {.callout-note}
## Concept drift as a stock-flow problem

The training dataset example above is not just an analogy. In [WH Data Engineering Ch 7–8](https://wayward.house/learn/data-engineering/), the same structure appears as a production engineering problem: what governance processes keep the inflow of fresh, relevant data above the deprecation rate? The systems thinking framework here is the diagnosis; Data Engineering Ch 7–8 is the engineering response.
:::
```

---

**CALLOUT 3 — position: after "Boundaries" section, before the horizontal rule that opens "Purpose"**

```markdown
::: {.callout-note}
## Boundaries and downstream systems

Widening the glacier boundary to include downstream water users is not a theoretical exercise — it is the central problem of hazard modelling. [WH Computational Geography Part 4 (Hazards)](https://wayward.house/learn/computational-geography/hazards/) works through exactly this coupling: how glacier retreat, wildfire, and flood systems interact with the human systems that depend on them.
:::
```
