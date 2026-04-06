<!-- ch02-prose.md — production fragments for Chapter 02: Feedback Structures -->
<!-- Three deliverables: Delay Section, Pipeline Reconnect insert, Cross-link Callouts -->

---

### DELAY SECTION — insert between "System archetypes" and the simulation section

---

## Delays in feedback loops

A delay is not simply a lag in the colloquial sense. In a stock-flow system, a delay is a stock — an intermediate accumulation that sits between a sensing point and a control point. Information or material must fill that stock before the signal reaches the regulator. Three kinds appear in practice.

A *material delay* is physical: hydrocarbon in transit between an injection point and a terminal cannot arrive instantaneously, regardless of how urgent the need. The pipeline itself is a delay stock. A *information delay* is the gap between a change in the real world and the point at which a decision-maker sees it: apportionment notices on a pipeline system propagate on monthly nomination cycles; a price signal must be observed, aggregated, and transmitted before it reaches a producer. A *perception and response delay* is the lag between receiving information and acting on it: a drilling programme takes eighteen to thirty-six months from investment decision to first barrel. Any realistic feedback loop contains at least one of these, and most contain all three in series.

The counterintuitive behaviour follows directly from the mechanism. In a balancing loop without delay, the corrective flow is proportional to the current gap between the stock and its goal. As the gap closes, the correction weakens. The system approaches the goal smoothly.

With a delay, the corrective flow is proportional to the gap *as it was D time units ago* — not as it is now. By the time the correction takes effect, the gap has already changed. Often it has reversed sign: the stock has already crossed the goal. The correction that was calibrated to the old gap is now excessive. It drives the stock past the goal in the other direction. A new corrective signal is generated, but it too arrives late. The result is oscillation around the goal, not convergence to it.

This is not a pathology of poorly designed systems. It is the mathematical consequence of inserting a stock between a sensing point and a control point. The longer the delay relative to the speed of correction, the wider the oscillation. If the delay is long enough, the oscillation does not dampen — the system becomes unstable.

The oil pipeline system from Chapter 1 runs two delays in series. Apportionment notices — the mechanism that communicates excess inventory to upstream nominators — propagate on monthly cycles. The drilling and completion programme that would increase supply operates on a horizon of one to three years: wells must be permitted, drilled, completed, and connected before a barrel moves. The balancing loop that connects a widening wellhead-to-export price spread to increased production volume exists, but its total delay is measured in years. During that interval, the reinforcing loops of investor expectation and speculative positioning can amplify the original imbalance rather than dampen it.

The data monitoring case is structurally identical. A deployed model's performance begins to degrade — concept drift, distributional shift, upstream data quality changes. The time between when degradation begins and when a monitoring system detects it is an information delay embedded in the feedback loop between model performance (the stock state) and the retraining decision (the corrective flow). A pipeline that batches evaluation metrics weekly and triggers retraining only after three consecutive failing evaluation windows may carry a total detection-to-response delay of several weeks. During that interval, the balancing loop that should correct the drift is not operating. The model continues to serve degraded predictions. The longer the monitoring lag, the wider the performance oscillation between retraining cycles.

The prescription that follows from recognising a delay is not to act faster — a faster correction through a delayed loop produces worse oscillation, not better. The prescription is either to shorten the delay or to reduce the aggressiveness of the correction.

::: {.callout-note}
## The mathematics of delayed feedback

The behaviour described in this section — oscillation, damping, instability as a function of delay — has a formal mathematical treatment in control theory. Eigenvalues of the closed-loop system determine whether oscillations dampen or grow. Transfer functions in the Laplace domain make the delay explicit as a phase shift.

[WH Maths Vol 8, Ch 1: Control, Feedback, and Stability](https://wayward.house/learn/maths/advanced/) develops this machinery in full, starting from the same thermostat example. If you want to know precisely *why* a gain of k and a delay of D produce instability when k × D exceeds a threshold, that is the place to go.
:::

---

### PIPELINE RECONNECT — 4-sentence insert into "Supply and demand as balancing loops"

---

**Insertion point:** after "the balancing loop operates slowly. During the delay..."

> The oil pipeline system from Chapter 1 runs both delays in series. Apportionment notices — the mechanism that communicates excess inventory to upstream nominators — propagate on monthly cycles. The drilling and completion programme that would increase supply operates on a horizon of one to three years. The balancing loop connecting wellhead price to production volume exists, but its total delay is measured in years, not weeks.

---

### CROSS-LINK CALLOUTS — 3 callouts with insertion positions

---

**Callout 1 — WH Maths Vol 8**
Insertion point: end of `## Delays in feedback loops` section, as the final element before the next section header.
(Also rendered inline in the Delay Section above — reproduced here for clarity.)

::: {.callout-note}
## The mathematics of delayed feedback

The behaviour described in this section — oscillation, damping, instability as a function of delay — has a formal mathematical treatment in control theory. Eigenvalues of the closed-loop system determine whether oscillations dampen or grow. Transfer functions in the Laplace domain make the delay explicit as a phase shift.

[WH Maths Vol 8, Ch 1: Control, Feedback, and Stability](https://wayward.house/learn/maths/advanced/) develops this machinery in full, starting from the same thermostat example. If you want to know precisely *why* a gain of k and a delay of D produce instability when k × D exceeds a threshold, that is the place to go.
:::

---

**Callout 2 — Data Engineering Ch 7–8**
Insertion point: end of `### Regularisation in machine learning (Data systems)` subsection — after the prose, before the next subsection header (`## System archetypes`).

::: {.callout-note}
## When the balancing loop breaks

Regularisation is a balancing loop *designed into* the training process. But the feedback loop between a deployed model's performance and the decision to retrain it is a different structure — one that operates in production, not in training, and one that can be severed entirely by monitoring gaps, organisational boundaries, or budget constraints.

[WH Data Engineering Ch 7–8](https://wayward.house/learn/data-engineering/) treats this as a production engineering problem: what processes maintain the feedback loop between model performance and model update? The systems thinking diagnosis is that concept drift is feedback starvation — the balancing loop exists in principle but is not operating in practice.
:::

---

**Callout 3 — Comp Geo Part 5**
Insertion point: end of `### Agglomeration in cities (Human systems)` subsection — after the prose, before the next subsection header.

::: {.callout-note}
## Agglomeration in spatial models

The reinforcing loop described above is the conceptual skeleton of economic geography. In spatial models, agglomeration feedback appears as a spatial autocorrelation structure: firms and workers cluster because of proximity benefits, and the cluster reinforces itself.

[WH Computational Geography Part 5 (Economic Systems)](https://wayward.house/learn/computational-geography/economic-systems/) models this structure explicitly — the same feedback loop, expressed as a spatial weight matrix and a regression on labour market density. The systems thinking lens here is the mechanism; the spatial model is its measurable expression.
:::
