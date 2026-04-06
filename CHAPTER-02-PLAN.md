# Chapter 02 Production Plan — Feedback Structures

Status of existing prose: strong. Opening puzzle, two-types section, reinforcing loops (3 domain examples), balancing loops (3 domain examples), system archetypes (5), exercises — all present and at production quality. Three items require production work before the chapter reaches draft status.

---

## 1. Delay Section Spec

### Placement

Insert immediately after `## System archetypes` and before `## Exercises`. The archetypes section introduces oscillation and overshoot-and-collapse with the phrase "The delay is key" — the delay section cashes that claim. The simulation section (see §2 below) follows immediately after the delay section, before Exercises.

The chapter flow becomes:

```
## Two types of feedback
## Reinforcing loops
## Balancing loops
## System archetypes
## Delays in feedback loops       ← NEW
## Simulating the thermostat...   ← NEW (see §2)
## Exercises
```

### Target length

300–400 words. No subsections. Match the chapter's register: declarative, precise, no preamble.

### Content specification

The section must cover four things in order:

**1. What a delay is in a stock-flow system (roughly 60–80 words)**

Delays are not vague "lags" — they are stocks in their own right. When information about a stock's state must travel through an intermediate accumulation before it reaches the flow regulator, the signal is delayed. Three kinds are worth naming:

- *Material delay*: physical throughput through a pipe, queue, or production process (e.g., hydrocarbon in transit between injection point and terminal — it cannot arrive instantaneously no matter how urgent the need)
- *Information delay*: the time between a change in the real world and the point at which a decision-maker sees it (e.g., apportionment notices on a pipeline system propagate on a monthly nomination cycle; a price signal must be observed, aggregated, and transmitted before it reaches a producer)
- *Perception/response delay*: the lag between receiving information and acting on it (e.g., a drilling programme takes 18–36 months from decision to first barrel)

Do not define these as taxonomy — weave them into a brief explanation of mechanism. The point is that any realistic feedback loop contains at least one of these.

**2. Why delays cause counterintuitive behaviour (roughly 100–120 words)**

The mechanism is specific. In a balancing loop without delay: the corrective flow is proportional to the current gap. As the gap closes, the correction weakens. The system homes in on the goal smoothly.

With a delay: the corrective flow is proportional to the gap *as it was D time units ago*, not as it is now. By the time the correction takes effect, the gap has already changed — often it has reversed sign (the system has already crossed the goal). The correction that was appropriate when initiated is now excessive. It drives the stock past the goal in the other direction. A new corrective signal is generated, but it too arrives late. The result is oscillation around the goal.

This is not a pathology of poorly designed systems. It is the mathematical consequence of inserting a stock between a sensing point and a control point. The longer the delay, the wider the oscillation. If the delay is long relative to the correction speed, the oscillation can grow rather than dampen — the system becomes unstable.

**3. Domain examples: pipeline and data systems (roughly 80–100 words)**

*Pipeline thread (continue from Ch 1):* In Chapter 1, the midstream pipeline was a stock-flow system with inventory as the buffer. The same system contains at least two feedback delays. Apportionment notices — the mechanism that caps inflow — operate on monthly nomination cycles. The production response to a widened wellhead-to-export price spread (which signals under-supply) lags by months to years: drilling programmes take time to initiate, wells take time to complete, and new pipeline capacity takes years to permit and construct. The balancing loop that should correct a supply shortage is operating with a delay of one to three years. During that interval, the price signal is doing the corrective work — and the reinforcing loops of investor expectation and speculative production can amplify rather than dampen the imbalance.

*Data systems example:* A machine learning model is deployed. Its performance begins to degrade — concept drift, distributional shift, upstream data quality changes. The time between when degradation begins and when a monitoring system detects it is the monitoring lag. This is an information delay embedded in the feedback loop between model performance (the stock state) and the retraining decision (the corrective flow). A monitoring pipeline that batches evaluation metrics weekly and triggers retraining only after three consecutive failing windows may have a total detection-to-response delay of several weeks. During this interval, the balancing loop that should correct model drift is not operating. The model continues to serve degraded predictions. The longer the monitoring lag, the wider the performance oscillation between retraining cycles.

**4. Closing observation (roughly 40–50 words)**

One sentence to close. Tone: Meadows-precise, not consolatory. Something in the register of: *The prescription that follows from recognising a delay is not to act faster — a faster correction through a delayed loop produces worse oscillation. The prescription is either to shorten the delay or to reduce the aggressiveness of the correction.*

### Exact section header

```markdown
## Delays in feedback loops
```

No subsection headers. Inline prose throughout.

---

## 2. Simulation Spec

### Placement

New section titled `## Simulating the thermostat: delay and oscillation`. Inserted immediately after `## Delays in feedback loops` and before `## Exercises`. It is introduced by a one-sentence bridge from the delay section: something in the form "The behaviour described above is easier to see than to describe — the following code makes the oscillation visible."

### What the simulation models

Stock: room temperature (°C). Goal: 20°C. Heater activates when temperature is below goal; the control signal (heating rate proportional to gap) is stored in a deque and applied after a fixed delay D. The simulation runs for 240 minutes (matching the exercise spec).

### Method

Euler integration, time step dt = 1 minute. Consistent with Ch 1. No scipy, no pysd. numpy + matplotlib + collections.deque only.

### Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `T_goal` | 20.0 °C | Target temperature |
| `T0` | 15.0 °C | Initial temperature |
| `k` | 0.3 | Feedback strength (°C/min per °C gap) |
| `loss` | 0.05 | Passive heat loss rate (°C/min) — a small constant outflow |
| `dt` | 1 min | Euler step |
| `t_end` | 240 min | Simulation duration |

Three runs differ only in delay:

| Scenario | Delay D | Colour |
|----------|---------|--------|
| Short delay | 5 min | `#888888` |
| Specified delay | 15 min | `#d52a2a` |
| Long delay | 45 min | `#111111` |

### Delay implementation

Use `collections.deque(maxlen=D_steps)` where `D_steps = int(D / dt)`. At each step, append the current control signal to the deque. The *applied* heating rate is `deque[0]` (the oldest value still in the buffer). For the first D steps, before the deque is full, the applied rate is zero (the heater signal has not yet propagated).

This is a minimal, transparent implementation of a pipeline delay. No scipy signal processing. The deque is the stock that creates the delay.

### What the plot must show

Single figure, three overlaid time-series on one axes panel. X-axis: time in minutes (0–240). Y-axis: room temperature in °C. A dashed horizontal line at T_goal = 20°C labelled "Goal (20°C)". Three lines in the colours above, labelled by delay duration. Legend inside the figure.

Behaviour that must be visible:
- Short delay (5 min): smooth approach to goal with slight initial undershoot. Temperature settles near 20°C before t = 100 min.
- Specified delay (15 min): clear oscillation, two to three full cycles, amplitude decreasing. Does not fully settle within 240 min.
- Long delay (45 min): sustained or growing oscillation. Repeated overshoot and undershoot, amplitude not visibly damping within the simulation window.

If the parameters above do not produce visibly distinct behaviours, adjust `k` upward (try 0.5) or increase the long delay to 60 min. The plot is only correct if the three regimes are visually unambiguous.

### Line count target

40–55 lines including comments. No helper functions beyond the Euler loop itself. Use a `for delay_min, color, label in scenarios` loop to avoid repetition.

### Figure caption

> Figure 2.X. Room temperature over 240 minutes under three delay scenarios. With a short delay the balancing loop corrects smoothly. As delay increases, the loop overshoots its goal, generating oscillation. The 45-minute delay produces sustained cycling — the correction that was appropriate when initiated arrives after the system has already reversed direction.

### "What to try" callouts

Three prompts in a `.callout-tip` block, consistent with Ch 1 style:

1. **Increase the feedback strength** (`k = 0.8`) while keeping the 15-minute delay. What happens to the oscillation amplitude and frequency? Does stronger correction help or hurt?
2. **Set loss = 0** (a perfectly insulated room). How does this change the behaviour of the short-delay scenario? What does this tell you about the role of passive damping?
3. **Match this to the pipeline system from Chapter 1.** In that system, what plays the role of T_goal, T0, k, and D? Write down the analogy explicitly before reading on.

### Save path

```python
plt.savefig("_assets/ch02-thermostat-simulation.png", dpi=150, bbox_inches="tight")
```

---

## 3. Diagram Specs

All inline text-arrow chains use ↑↓ notation and are not Mermaid diagrams. Replace each with a `graph LR` Mermaid block using standard causal loop notation: `+` and `−` edge labels, loop label `[R]` or `[B]` on the closing edge.

Node names must be short noun phrases (not full sentences). Use `:::wh-red` class or inline `style` declarations for the WH palette. All diagrams use `graph LR`.

WH palette for Mermaid: node fill `#f5f5f5`, stroke `#111111`; accent/loop-label nodes fill `#fff3f3`, stroke `#d52a2a`.

### Diagram 1 — Ice-albedo reinforcing loop

**Location:** Replace the text chain `Ice mass ↓ → Surface albedo ↓ → Solar absorption ↑ → Surface temperature ↑ → Ice melt ↑ → Ice mass ↓ ...` in the `### The ice-albedo feedback (Earth systems)` subsection. Place the diagram block immediately before or after the paragraph beginning "This is a reinforcing loop."

**Nodes and edges:**

```
Ice Mass -->|"−"| Surface Albedo
Surface Albedo -->|"+"| Solar Absorption
Solar Absorption -->|"+"| Surface Temperature
Surface Temperature -->|"+"| Ice Melt Rate
Ice Melt Rate -->|"−  [R]"| Ice Mass
```

Reading: Ice Mass decreases → Surface Albedo decreases (negative causal link: they move in the same direction, but the edge label is − because albedo falls as mass falls — this is the convention where − means "the effect moves opposite to the cause"). 

**Notation note for the production agent:** Standard CLD convention uses + when cause and effect move in the same direction, − when they move in opposite directions. In this loop: Ice Mass ↑ → Albedo ↑ (+), Albedo ↑ → Solar Absorption ↓ (−), Solar Absorption ↑ → Temperature ↑ (+), Temperature ↑ → Ice Melt ↑ (+), Ice Melt ↑ → Ice Mass ↓ (−). The loop has two − signs → even number → reinforcing (R). Loop label on the closing edge: `[R]`.

**Figure caption:** Figure 2.1. Ice-albedo reinforcing loop. Two negative causal links and three positive links produce a reinforcing (R) loop: any reduction in ice mass ultimately produces further reduction.

### Diagram 2 — Agglomeration in cities

**Location:** Replace `Workers ↑ → Firms ↑ → Jobs ↑ → Workers ↑ ...` in `### Agglomeration in cities (Human systems)`.

**Nodes and edges:**

```
Skilled Workers -->|"+"| Firm Concentration
Firm Concentration -->|"+"| Job Availability
Job Availability -->|"+"| Skilled Workers
```

Closing edge: `Job Availability -->|"+ [R]"| Skilled Workers`

All links positive → odd number of negatives = zero → reinforcing. Loop label `[R]`.

**Figure caption:** Figure 2.2. Agglomeration reinforcing loop. All three causal links are positive: more workers attract more firms, which create more jobs, which attract more workers. The loop is self-sustaining once initiated.

### Diagram 3 — Recommender amplification loop

**Location:** Replace `Engagement ↑ → Recommendation probability ↑ → Exposure ↑ → Engagement ↑ ...` in `### Recommender system amplification (Data systems)`.

**Nodes and edges:**

```
Engagement -->|"+"| Recommendation Probability
Recommendation Probability -->|"+"| Exposure
Exposure -->|"+ [R]"| Engagement
```

All links positive → reinforcing. Loop label `[R]`.

**Figure caption:** Figure 2.3. Recommender reinforcing loop. Content that receives engagement is recommended more, increasing exposure, which increases engagement. The loop amplifies whatever signal is already present in the engagement data.

### Diagram 4 — Supply-demand balancing loop

**Location:** Replace `Price ↑ → Demand ↓, Supply ↑ → Price ↓ ...` in `### Supply and demand as balancing loops (Human systems)`. The text-arrow chain is in the paragraph beginning "When demand for a commodity exceeds supply."

Note: the inline chain tries to show two simultaneous effects of price (demand down, supply up). The Mermaid diagram should show both paths explicitly. Use a split: Price → Demand (−) and Price → Supply (+), both paths leading back to Price.

**Nodes and edges:**

```
Price -->|"−"| Quantity Demanded
Price -->|"+"| Quantity Supplied
Quantity Demanded -->|"+"| Supply-Demand Gap
Quantity Supplied -->|"−"| Supply-Demand Gap
Supply-Demand Gap -->|"+ [B]"| Price
```

The loop from Price → Supply-Demand Gap → Price has one − sign (via Quantity Supplied path) → odd → balancing. Loop label `[B]`.

**Figure caption:** Figure 2.4. Supply-demand balancing loop. Price sends opposing signals to demand (reducing it) and supply (raising it). Both effects narrow the supply-demand gap, reducing the upward pressure on price. The loop seeks equilibrium — but only as fast as supply can respond.

### Diagram 5 — Regularisation balancing loop

**Location:** Replace `Model complexity ↑ → Regularisation penalty ↑ → Gradient updates reduce complexity ↑ → Model complexity ↓ ...` in `### Regularisation in machine learning (Data systems)`.

**Nodes and edges:**

```
Model Complexity -->|"+"| Regularisation Penalty
Regularisation Penalty -->|"+"| Penalty Gradient
Penalty Gradient -->|"− [B]"| Model Complexity
```

One − sign on the closing edge → odd → balancing. Loop label `[B]`.

**Figure caption:** Figure 2.5. Regularisation as a designed balancing loop. As model complexity increases, the regularisation penalty increases, increasing the gradient signal that pushes complexity back down. The goal is an implicit complexity target set by the regularisation coefficient λ.

### Diagram 6 — Archetype overview (matplotlib, not Mermaid)

**Location:** New figure at the end of `## System archetypes`, before `## Delays in feedback loops`. Display after the prose description of all five archetypes. Header: no new subsection — use a figure with caption only.

**Specification:** 5-subplot figure (1 row × 5 columns), each subplot a hand-drawn-style time-series sketch showing the signature behaviour of one archetype. Use numpy to generate the curves analytically — do not simulate.

| Subplot | Title | Curve | Colour |
|---------|-------|-------|--------|
| 1 | Exponential growth | `np.exp(0.04 * t)` | `#d52a2a` |
| 2 | Goal seeking | `20 - 5 * np.exp(-0.05 * t)` (approaches 20) | `#111111` |
| 3 | Oscillation | `20 + 4 * np.cos(0.15 * t) * np.exp(-0.01 * t)` | `#d52a2a` |
| 4 | Limits to growth | `20 / (1 + np.exp(-0.08 * (t - 60)))` (sigmoid) | `#111111` |
| 5 | Overshoot & collapse | custom: rise then sharp fall (see below) | `#888888` |

For subplot 5 (overshoot and collapse): `np.where(t < 80, 0.12 * t, 0.12 * 80 * np.exp(-0.06 * (t - 80)))`. This rises linearly then collapses exponentially.

All subplots: hide tick labels, show only the curve and archetype name as title. Dashed horizontal reference line where relevant (goal line for subplots 2 and 3 at y=20; carrying-capacity line for subplots 4 and 5). Spine: left and bottom only. Figure size: 12 × 3 inches at 150 dpi.

**Figure caption:** Figure 2.6. Signature behaviour of the five system archetypes. Each pattern is generated by a specific feedback structure: (1) a single unconstrained reinforcing loop; (2) a balancing loop with no delay; (3) a balancing loop with significant delay; (4) a reinforcing loop eventually opposed by a balancing loop; (5) the same structure as (4) but with the constraining loop delayed until after overshoot.

**Save path:** `_assets/ch02-archetype-sketches.png`

---

## 4. Cross-link Callouts

### Callout A — WH Maths Vol 8

**Type:** `.callout-note`
**Insertion point:** End of `## Delays in feedback loops` section, as the final element before the next section header.

**Exact wording:**

```markdown
::: {.callout-note}
## The mathematics of delayed feedback

The behaviour described in this section — oscillation, damping, instability as a function of delay — has a formal mathematical treatment in control theory. Eigenvalues of the closed-loop system determine whether oscillations dampen or grow. Transfer functions in the Laplace domain make the delay explicit as a phase shift.

[WH Maths Vol 8, Ch 1: Control, Feedback, and Stability](https://wayward.house/learn/maths/advanced/) develops this machinery in full, starting from the same thermostat example. If you want to know precisely *why* a gain of k and a delay of D produce instability when k × D exceeds a threshold, that is the place to go.
:::
```

### Callout B — Data Engineering (concept drift as feedback starvation)

**Type:** `.callout-note`
**Insertion point:** End of `### Regularisation in machine learning (Data systems)` subsection — after the prose, before the next subsection header (`## System archetypes`).

**Exact wording:**

```markdown
::: {.callout-note}
## When the balancing loop breaks

Regularisation is a balancing loop *designed into* the training process. But the feedback loop between a deployed model's performance and the decision to retrain it is a different structure — one that operates in production, not in training, and one that can be severed entirely by monitoring gaps, organisational boundaries, or budget constraints.

[WH Data Engineering Ch 7–8](https://wayward.house/learn/data-engineering/) treats this as a production engineering problem: what processes maintain the feedback loop between model performance and model update? The systems thinking diagnosis is that concept drift is feedback starvation — the balancing loop exists in principle but is not operating in practice.
:::
```

### Callout C — Computational Geography (agglomeration and economic geography)

**Type:** `.callout-note`
**Insertion point:** End of `### Agglomeration in cities (Human systems)` subsection — after the prose, before the next subsection header.

**Exact wording:**

```markdown
::: {.callout-note}
## Agglomeration in spatial models

The reinforcing loop described above is the conceptual skeleton of economic geography. In spatial models, agglomeration feedback appears as a spatial autocorrelation structure: firms and workers cluster because of proximity benefits, and the cluster reinforces itself.

[WH Computational Geography Part 5 (Economic Systems)](https://wayward.house/learn/computational-geography/economic-systems/) models this structure explicitly — the same feedback loop, expressed as a spatial weight matrix and a regression on labour market density. The systems thinking lens here is the mechanism; the spatial model is its measurable expression.
:::
```

---

## 5. Prose Gap Check — Oil Pipeline Thread

### Finding

The supply-and-demand balancing loop section (under `## Balancing loops`) contains this sentence:

> "But: the response time matters. If the supply side has a long lag (housing under construction, oil wells being drilled, graduate students being trained), the balancing loop operates slowly."

The phrase "oil wells being drilled" is the only mention of the oil sector in this chapter. Chapter 1 developed the midstream pipeline system in detail — inventory stocks, apportionment constraints, response time formula (τ = S / |F_net|), the wellhead-to-export price spread. That thread is not picked up here.

### Recommendation: extend, not leave as-is

The oil pipeline thread should be extended in two places:

**Place 1 — Supply-demand section:** After the sentence "oil wells being drilled", add a parenthetical or a short paragraph (2–4 sentences) that explicitly reconnects to Ch 1. Something in the form: "The pipeline system from Chapter 1 sits between these two delays: the apportionment cycle delays the price signal reaching producers, and the drilling-to-completion cycle delays the supply response. The balancing loop that should clear the wellhead discount operates through both delays in series." This does not require new structural content — it applies the Ch 2 framework retroactively to a system the reader already knows.

**Place 2 — Delay section (new section, §1 above):** The delay section spec already includes the pipeline thread as a required example. This is the primary location for making the connection explicit.

**Rationale:** Ch 1 invests substantially in the pipeline example. Readers who carry that example into Ch 2 should see it confirmed and extended, not orphaned. The connection costs roughly 40–60 words in the supply-demand section and is already included (as a requirement) in the new delay section. Both extensions should be made.

**Action for production agent:** In the supply-demand balancing loop section, after the sentence ending "...the balancing loop operates slowly", add the following paragraph:

> The oil pipeline system from Chapter 1 runs both delays in series. Apportionment notices — the mechanism that communicates excess inventory to upstream nominators — propagate on monthly cycles. The drilling and completion programme that would increase supply operates on a horizon of one to three years. The balancing loop connecting wellhead price to production volume exists, but its total delay is measured in years, not weeks.

This is the Ch 1 thread continued. Do not restate what Ch 1 already established — assume the reader has it. The paragraph above is a connection, not a recap.

---

*End of production plan. Three deliverables required before chapter reaches draft status: delay section prose (~350 words), thermostat simulation code (~50 lines), and six diagrams (5 Mermaid + 1 matplotlib). Cross-link callouts and pipeline extension are lower effort but should ship with the same pass.*
