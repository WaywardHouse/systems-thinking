# CHAPTER-03-PLAN.md — Chapter 3 Production Plan: "Complexity and Emergence"

**Status at plan date:** 2026-04-05
**For agents:** Writer, Simulation Engineer, Diagram Specifier
**What exists:** Full prose skeleton — puzzle, nonlinearity, tipping points (3 domain examples), emergence, resilience/resistance/brittleness, exercises. Voice is correct. Math register (no calculus) is correct.
**What is missing:** No simulation code block. No Mermaid causal loop diagrams. No cross-link callouts. No emergence vs. complexity conceptual bridge. No data/AI example in the resilience section. No simulation-introduction bridge paragraph. No visual for tipping point structure.

---

## 1. Gap Analysis

| Element | Present in Ch 1/2 | Present in Ch 3 seed | Disposition |
|---|---|---|---|
| Simulation code block (`{python}`, Euler or equivalent) | Ch 1 (glacier), Ch 2 (thermostat) | Absent | ADD — Schelling segregation model |
| "What to try" callout (`.callout-tip`) after simulation | Ch 1, Ch 2 | Absent | ADD — with simulation |
| Simulation introduction paragraph | Ch 1, Ch 2 | Absent | ADD — bridge before code block |
| Mermaid causal loop diagrams | Ch 2 (five diagrams) | Absent | ADD — three diagrams |
| Figure captions in `> Figure N.M.` format | Ch 1, Ch 2 | Absent | ADD — one per diagram + simulation figure |
| Cross-link callouts (`.callout-note`) | Ch 1 (2), Ch 2 (3) | Absent | ADD — exactly three |
| Bridge prose before every figure | Ch 1, Ch 2 | Absent | ADD — see §2.4 |
| `{python}` block label and `fig-cap` options | Ch 2 | Absent | ADD — on simulation block |
| Data/AI example in resilience section | Ch 2 (all 3 domains per section) | Missing | ADD — see §2.2 |
| Emergence vs. complexity distinction | Internal gap | Absent | ADD — see §2.1 |
| Figure numbering continuity | Ch 1 (1.1–1.4), Ch 2 (2.1–2.7) | Absent | Figures 3.1–3.4 |
| Status line updated | Both chapters updated | Still "seed" | UPDATE after assembly |

---

## 2. Writer Assignments

### 2.1 Emergence vs. complexity distinction

**Problem:** The emergence section lists conditions and examples but does not distinguish emergence from complexity, or complexity from "complicated."

**Content to convey:**
- Complicated (a jet engine): many components in precisely designed relationships, behaviour predictable from design
- Complex: many components with nonlinear, adaptive, history-dependent interactions; behaviour not predictable from components alone
- Emergence is what complex systems *produce* — system-level properties not present in components. Emergence is the phenomenon; complexity is the structural condition
- Engineering implication: optimising components does not prevent emergent failures. Complex system failures are typically interaction structure failures, not component failures

**Target:** 80–100 words. No subsection header. Active voice, mechanism-first.
**Insertion point:** Immediately before the `---` separator closing `## Emergence`, after the sentence ending "...it is an emergent property of optimisation in a high-dimensional space with insufficient data."

### 2.2 Data/AI example for resilience section

**Content to convey:**
- A deployed ML system can appear resistant (stable accuracy on fixed test set) while resilience erodes
- Resilience = capacity of monitoring + retraining loop to restore performance after perturbation
- High resilience: operational retraining loop, fresh data pipelines, comprehensive monitoring
- Low resilience: monitoring reduced, retraining cadence stretched, feedback loop severed by data governance gaps — system appears stable until threshold crossed, then error rate spikes without warning
- Connect forward to Exercise 3.4

**Target:** 80–100 words. No subsection header. Match register of coral reef paragraph — declarative, mechanism-first.
**Insertion point:** After "...not just to optimise for expected conditions." and before `## Exercises`.

### 2.3 Simulation introduction paragraph

**Section header (fixed):** `## Simulating segregation: from mild preferences to macro-level patterns`

**Content:** Exercise 3.2 asks you to implement the Schelling model. The code below is one version. Run it before reading the interpretation. The macro-level outcome (near-total segregation from mild preferences) is genuinely surprising — the reader should feel the surprise before the explanation.

**Target:** 2–3 sentences, ~50–70 words. Match Ch 2 register exactly: "Exercise 2.3 asks you to trace the thermostat's behaviour by hand under different delay assumptions; the code below runs those same assumptions across 240 minutes so the trajectories are visible at once."
**Insertion point:** As opening prose of `## Simulating segregation` section, before the `{python}` block.

### 2.4 Bridge sentences before Mermaid diagrams

Three single sentences (15–25 words each), to be placed immediately before each Mermaid block:

**Before Diagram 3.1 (generic tipping point) in `## Tipping points` opening:**
Name what the diagram shows: the generic two-loop structure — balancing feedback and reinforcing feedback sharing a stock, with external stress controlling which dominates.

**Before Diagram 3.2 (coral reef) in `### Coral reef regime shift`:**
Name what the diagram shows: both the balancing loop that maintains the healthy reef and the reinforcing loop that takes over after bleaching, both operating on the same Coral Cover stock.

**Before Diagram 3.3 (Schelling) in `### Neighbourhood segregation`:**
Name what the diagram shows: the feedback between individual satisfaction and neighbourhood composition that connects local preferences to the macro-level outcome.

---

## 3. Simulation Engineer Assignment

### Model specification: Schelling segregation

**Grid:** 40 × 40. Populate: ~45% Type A, ~45% Type B, ~10% empty. `numpy.random.seed(42)`.

**Satisfaction threshold:** Base run T = 0.33 (matches puzzle section). Additional runs T = 0.20 and T = 0.50 for time series comparison.

**Neighbourhood:** Moore neighbourhood (8 cells). Denominator = occupied cells only (ignore empty).

**Step:** Each step: identify all unsatisfied agents; move each to a randomly chosen empty cell; update grid.

**What the simulation demonstrates:**
1. At T = 0.33, near-total macro-level segregation emerges within 30–50 steps from a randomly mixed start
2. Segregation index (average fraction same-type occupied neighbours) plotted as time series — rises from ~0.50 to >0.80
3. Side-by-side: initial random grid, final grid after 50 steps

**Figure layout:** 3 panels, `figsize=(12, 4)`, `dpi=150`
- Panel 1: Initial grid (imshow, no tick labels, title "Initial state")
- Panel 2: Final grid after 50 steps, T = 0.33 (title "After 50 steps, T = 0.33")
- Panel 3: Time series of segregation index for T = 0.20, 0.33, 0.50, three lines in `#888888`, `#d52a2a`, `#111111`; x-axis "Step"; y-axis "Segregation index"; y-range 0.4–1.0; annotated with `ax.annotate` (no legend)

**Colours:** Type A `#d52a2a`, Type B `#111111`, empty `#f5f5f5` (construct custom ListedColormap from these three).

**Code style:**
- numpy + matplotlib only. No ABM library.
- 50–70 lines with comments on every logical block
- Named constants at top: `GRID_SIZE`, `DENSITY_A`, `DENSITY_B`, `THRESHOLD`, `N_STEPS`, `SEED`
- Docstring: `"""Schelling segregation — Chapter 3. Grid: GRID_SIZE × GRID_SIZE. Two agent types. Agents move if fraction same-type neighbours < THRESHOLD."""`
- `plt.tight_layout()` before save
- Save: `plt.savefig("_assets/ch03-schelling-simulation.png", dpi=150, bbox_inches="tight")`

**Block header:**
```
#| label: fig-schelling
#| fig-cap: "Figure 3.4. Schelling segregation model. Left: initial random placement of Type A (red), Type B (black), and empty (grey) cells. Centre: state after 50 steps with T = 0.33 — near-complete segregation has emerged. Right: segregation index over time for three thresholds. Even at T = 0.20 macro-level segregation emerges within 30 steps. The tipping point is in the interaction structure, not in the individual preferences."
#| fig-width: 12
#| fig-height: 4
```

**"What to try" callout:**

```markdown
::: {.callout-tip}
## What to try

1. **Lower the threshold to T = 0.10** (agents satisfied as long as even one neighbour shares their type). Does segregation still emerge? What does this tell you about the minimum preference that produces macro-level separation?

2. **Increase the grid to 60 × 60 and run for 100 steps.** Does the final segregation index change? What does this tell you about scale?

3. **Set DENSITY_A = 0.30 and DENSITY_B = 0.60** (asymmetric populations). What happens to the spatial structure of the final state? Is the minority group more or less segregated than in the symmetric case?
:::
```

**Figure caption:**
> Figure 3.4. Schelling segregation model. Left: initial random placement. Centre: state after 50 steps with satisfaction threshold T = 0.33 — near-complete segregation has emerged from a randomly mixed start. Right: segregation index over time for three threshold values. At T = 0.20 segregation still emerges; at T = 0.50 it is faster and more complete. The macro-level outcome is not a reflection of the individual preference — it is a product of the feedback between individual decisions and neighbourhood composition.

---

## 4. Diagram Specifier Assignment

All diagrams: `graph LR`. All node styles inline. WH palette: standard nodes `fill:#f5f5f5,stroke:#111111,stroke-width:2px`; accent nodes `fill:#fff3f3,stroke:#d52a2a,stroke-width:2px`. Accent = the node carrying `[R]`, `[B]`, or the key shared stock. Match Ch 2 style exactly.

### Diagram 3.1 — Generic tipping point structure (Figure 3.1)

**Location:** `## Tipping points` section, after Writer bridge sentence, before `### Coral reef regime shift`

**Nodes and edges:**
```
SS["System State"] -->|"+"| BF["Balancing\nFeedback\nStrength"]
BF -->|"− [B]"| SS
EX["External\nStress"] -->|"−"| BF
EX -->|"+"| RF["Reinforcing\nFeedback\nStrength"]
RF -->|"+ [R]"| SS
```

**Accent (highlight) node:** `EX["External\nStress"]` — `fill:#fff3f3,stroke:#d52a2a,stroke-width:2px`

**Caption:**
> Figure 3.1. Generic tipping point structure. Two feedback loops operate on the same stock (System State): a balancing loop (B, left) that stabilises the current state, and a reinforcing loop (R, right) that amplifies departures from it. External stress weakens the balancing feedback and strengthens the reinforcing one. Before the threshold, B dominates; past it, R dominates. The transition is not gradual — it is a switch in which loop governs behaviour.

### Diagram 3.2 — Coral reef regime shift (Figure 3.2)

**Location:** `### Coral reef regime shift`, after Writer bridge sentence, before "Warming and nutrient loading..."

**Two competing reinforcing loops sharing Coral Cover:**
```
CC["Coral Cover"] -->|"+"| GR["Grazing Rate"]
GR -->|"−"| AC["Algae Cover"]
AC -->|"− [R1]"| CC

AC -->|"+"| BS["Bleaching /\nSmothering"]
BS -->|"− [R2]"| CC
WS["Warming /\nNutrient Stress"] -->|"+"| BS
```

**Accent node:** `CC["Coral Cover"]` — the shared stock between both loops. `fill:#fff3f3,stroke:#d52a2a,stroke-width:2px`

**Caption:**
> Figure 3.2. Coral reef regime shift: two competing reinforcing loops sharing the Coral Cover stock. Loop R1: high coral cover supports grazing that suppresses algae, which protects coral — a self-sustaining healthy state. Loop R2: algae proliferation causes bleaching and smothering that reduces coral cover, which reduces competition against algae — a self-sustaining degraded state. Warming and nutrient stress (left) is the external pressure that weakens R1 and tips the system into R2. The reef does not oscillate between states — it shifts.

### Diagram 3.3 — Schelling move-decision loop (Figure 3.3)

**Location:** `### Neighbourhood segregation`, after Writer bridge sentence, before "Schelling's model demonstrates..."

**Nodes and edges:**
```
SEG["Segregation\n(Fraction\nSame-Type)"] -->|"+"| SAT["Individual\nSatisfaction"]
SAT -->|"−"| MV["Move Rate"]
MV -->|"+ [B]"| SEG
```

**Accent node:** `SEG["Segregation\n(Fraction\nSame-Type)"]` — the macro-level emergent stock. `fill:#fff3f3,stroke:#d52a2a,stroke-width:2px`

**Caption:**
> Figure 3.3. Schelling move-decision feedback loop. High local segregation raises individual satisfaction (+), which reduces the rate of moves away from the neighbourhood (−), which maintains or increases local same-type fractions (+). The loop is balancing — it drives the system toward a stable equilibrium. The surprise is which equilibrium: near-total segregation, not because anyone chose it, but because mild individual preferences are sufficient to tip the system to the segregated stable state.

---

## 5. Cross-Link Callouts

### Callout 3.A — WH Maths (phase portraits and bifurcation theory)

**Insertion point:** End of `## Tipping points`, after all three domain subsections, before `---` separator.

```markdown
::: {.callout-note}
## Phase portraits and bifurcation theory

The tipping point structure described above has a precise mathematical representation. When a system's equilibrium structure changes qualitatively as a parameter varies — when a stable equilibrium disappears, or a new one appears — this is called a bifurcation. The coral reef shift is a fold (saddle-node) bifurcation: the healthy-reef equilibrium disappears as thermal stress passes a critical value, and the system falls to the only remaining equilibrium.

Phase portraits — diagrams that show the system's trajectory in state space rather than over time — make the two-equilibrium structure visible directly. [WH Maths Vol 8 (Dynamical Systems and Stability)](https://wayward.house/learn/maths/advanced/) develops phase portraits, fixed points, and bifurcation diagrams from first principles.
:::
```

### Callout 3.B — WH Computational Geography (spatial patterns of segregation)

**Insertion point:** End of `### Neighbourhood segregation (Human systems)`, after "...pushing against a self-reinforcing structure." and before `### Distribution shift in ML`.

```markdown
::: {.callout-note}
## Measuring segregation spatially

The Schelling model produces a spatial pattern — clusters of same-type agents — that can be measured and compared across cities and time. Spatial statistics offers several segregation indices (the dissimilarity index, Moran's I, the exposure index) that quantify different aspects of the pattern the model generates.

[WH Computational Geography Part 5 (Economic Systems)](https://wayward.house/learn/computational-geography/economic-systems/) applies these measures to real urban data. The systems thinking question is *why* the pattern emerges; the spatial statistics question is *how to measure* it. Both are necessary — measurement without mechanism cannot distinguish a segregation pattern that is self-reinforcing from one with an external cause.
:::
```

### Callout 3.C — WH Data Engineering (drift detection)

**Insertion point:** End of `### Distribution shift in ML (Data systems)`, after "The tipping point was invisible until crossed." and before `---` separator.

```markdown
::: {.callout-note}
## Detecting drift before the tipping point

The diagnosis here — that the system was moving toward a threshold that gave no external signal of its proximity — implies a specific engineering requirement: monitor the *distance* to the threshold, not just the current state. For ML systems, this means monitoring the divergence between training and serving distributions (KL divergence, population stability index), not just downstream accuracy.

[WH Data Engineering Ch 7–8](https://wayward.house/learn/data-engineering/) covers drift detection methods, monitoring pipeline design, and the governance structures that keep the retraining feedback loop operational. The systems thinking framework is the diagnosis; Data Engineering Ch 7–8 is the engineering response.
:::
```

---

## 6. Assembly Instructions

### 6.1 Final section order

```
[YAML front matter — unchanged]

## The puzzle                                              [existing — unchanged]
---
## Nonlinearity                                            [existing — unchanged]
---
## Tipping points                                          [existing section header]
  [Writer bridge sentence — Diagram 3.1 intro]
  [Diagram 3.1 — generic tipping point structure]
  [> Figure 3.1 caption]

  ### Coral reef regime shift                              [existing subsection]
  [Writer bridge sentence — Diagram 3.2 intro]
  [Diagram 3.2 — coral reef two loops]
  [> Figure 3.2 caption]
  [existing prose — coral reef paragraphs — unchanged]

  ### Neighbourhood segregation                            [existing subsection]
  [Writer bridge sentence — Diagram 3.3 intro]
  [Diagram 3.3 — Schelling move-decision loop]
  [> Figure 3.3 caption]
  [existing prose — Schelling paragraphs — unchanged]
  [Callout 3.B — Computational Geography]

  ### Distribution shift in ML                             [existing subsection]
  [existing prose — ML drift paragraphs — unchanged]
  [Callout 3.C — Data Engineering]

  [Callout 3.A — WH Maths]
---
## Emergence                                               [existing — unchanged]
  [existing prose — unchanged]
  [Writer: emergence vs. complexity paragraph]
---
## Resilience, resistance, and brittleness                 [existing — unchanged]
  [existing prose — unchanged]
  [Writer: data/AI resilience example paragraph]
---
## Simulating segregation: from mild preferences to macro-level patterns   [NEW]
  [Writer: bridge paragraph]
  [{python} Schelling simulation block]
  [What to try callout]
  [> Figure 3.4 caption]
---
## Exercises                                               [existing — unchanged]

---
*Status: draft — ...*                                      [UPDATE at assembly]
```

### 6.2 Existing prose modifications
None. All additions are insertions. Existing prose preserved verbatim.

### 6.3 Figure numbering

| Figure | Content | Section |
|---|---|---|
| 3.1 | Generic tipping point structure (Mermaid) | `## Tipping points` opening |
| 3.2 | Coral reef regime shift (Mermaid) | `### Coral reef regime shift` |
| 3.3 | Schelling move-decision loop (Mermaid) | `### Neighbourhood segregation` |
| 3.4 | Schelling simulation (Python, 3 panels) | `## Simulating segregation` |

### 6.4 Deliverables checklist

**Writer:**
- [ ] Emergence vs. complexity paragraph (~90 words)
- [ ] Data/AI resilience example paragraph (~90 words)
- [ ] Simulation bridge paragraph (~60 words)
- [ ] Three bridge sentences for Mermaid diagrams (~20 words each)

**Simulation Engineer:**
- [ ] `{python}` Schelling simulation block with `#| label:` and `#| fig-cap:`
- [ ] `.callout-tip` "What to try" block
- [ ] `> Figure 3.4` caption
- [ ] `_assets/ch03-schelling-simulation.png` (save path in code)

**Diagram Specifier:**
- [ ] Mermaid block: Diagram 3.1 — generic tipping point
- [ ] Mermaid block: Diagram 3.2 — coral reef
- [ ] Mermaid block: Diagram 3.3 — Schelling loop
- [ ] `> Figure` caption for each

**Assembly + QA:**
- [ ] Three `.callout-note` cross-link callouts inserted at specified points
- [ ] All `> Figure N.M.` captions present
- [ ] Status line updated to `draft`
- [ ] `DESIGN-BRIEF.md` row for `03-complexity-and-emergence` updated

---

*End of plan. Five structural gaps addressed: simulation, diagrams, cross-links, emergence/complexity distinction, data/AI resilience example. Chapter reaches structural parity with Ch 1 and Ch 2 after these deliverables are assembled.*
