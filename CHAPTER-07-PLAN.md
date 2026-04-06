# CHAPTER-07-PLAN.md — Chapter 7 Production Plan: "Modelling and Simulation"

**Status at plan date:** 2026-04-05
**For agents:** Writer, Simulation Engineer, Diagram Specifier
**What exists:** Stub (`07-modelling-and-simulation.qmd`, 3 lines) — full design required.
**What this plan specifies:** Complete chapter architecture — YAML front matter, section structure,
prose assignments, simulation specification, diagram specifications, cross-link callouts, and assembly instructions.

---

## 1. Chapter-Level Design

### YAML Front Matter

```yaml
---
title: "Modelling and Simulation"
subtitle: "From verbal description to running code — the craft of building stock-flow models"
status: seed → draft
axiom: "A model is always wrong. The question is whether it is wrong in ways that matter for the decision you are trying to make."
rewrite: "Structural accuracy matters more than parameter precision. A model with the right feedback loops and approximate numbers tells you more about a system than one with precise data and no feedback structure."
opens_to:
  - chapter: 08-systems-intervention
    relationship: enables
  - course: ESDE 401
    relationship: anchors
destinations:
  - field: earth
    hook: "The 2014–2016 collapse of western Antarctic glaciers was predicted by ice sheet models a decade before it was observed. The models had large uncertainties in their parameters. They got the qualitative result right because the feedback structure — marine ice sheet instability, the geometry of the bedrock, the ocean heat flux — was captured correctly. No amount of better parameters would have mattered if the loop structure had been wrong."
  - field: human
    hook: "In 1958, Jay Forrester at MIT showed that a simple three-node supply chain — retailer, distributor, factory — oscillates violently in response to a small, steady increase in consumer demand. No individual node is making an irrational decision. The oscillation is a property of the feedback structure: the combination of inventory correction ordering and shipment delays. He called this the 'bullwhip effect'. It was not discovered by studying supply chains more carefully. It was discovered by building a model."
  - field: data
    hook: "A production ML pipeline with three monitoring loops — feature distribution checking, model accuracy checking, and data freshness checking — can fail silently if all three loops have different detection delays. A model of the pipeline with approximate parameters will tell you this before you experience it in production. The question is not whether to model it. The question is whether to model it explicitly or to let the system model itself through repeated incidents."
---
```

### Opening Puzzle

**The "oh" moment:** The Limits to Growth (World3 model, 1972).

In 1972, a team of MIT researchers published projections for global industrial civilisation to 2100 using a system dynamics model called World3. The model had approximately 200 variables and 12 state variables. It was built with Jay Forrester's methodology on a CDC mainframe.

The "business as usual" scenario projected that industrial output per capita would peak around 2020 and then collapse, driven by resource depletion and increasing pollution. Contemporary critics were dismissive. Yale economist Henry Wallich called it "nonsense." Robert Solow, Nobel laureate, called it "bad science." William Nordhaus published a detailed critique of its economic mechanisms.

In 2021, Gaya Herrington (KPMG) published a comparison of World3's projections against 50 years of actual data across ten variables: population, industrial output, food production, services, pollution, non-renewable resources, and related indices. The "business as usual" scenario tracked actual data within a few percent on most variables. The critics were right that the parameter choices were rough and the economic mechanisms were simplified. They were wrong about the conclusion that followed from this.

The puzzle: how did a 1972 model with limited historical data and deliberately simplified economics correctly characterise the trajectory of global industrial civilisation for 50 years — when detailed quantitative forecasting did not?

**The answer is structural.** World3 did not need to model every mechanism correctly. It needed to capture the right feedback loops: the balancing loop between population and food supply; the delays between resource extraction and depletion; the reinforcing loop between industrial capital and output; the second-order effects of pollution on food supply. Parameters drift and get revised with better data. Feedback structures are harder to change, because they are properties of the real system, not assumptions about it.

This puzzle earns the chapter's claim: what makes a model useful is structural accuracy. The craft of modelling is identifying which stocks, which flows, and which feedback connections are load-bearing for the question you are trying to answer — and building those, and nothing more, with sufficient precision to trust the output.

---

## 2. Section Structure

### Section overview

| # | Section title | Domain examples | Diagram? | Cross-link callout? |
|---|---|---|---|---|
| 0 | The puzzle (Limits to Growth) | Human only (World3) | None | No |
| 1 | The modelling cycle | Earth: glacier; Human: supply chain; Data: ML pipeline | Mermaid 7.1 (6-stage cycle) | No |
| 2 | From verbal description to equations | Earth: glacier equations; Human: inventory equations; Data: backlog equations | Mermaid 7.2 (glacier CLD + SFD) | No |
| 3 | Implementing in Python | Earth: glacier code + Fig 7.3; Human: code preview | Python glacier simulation | WH Data Engineering |
| 4 | Validation and sensitivity | Earth: glacier parameter sweep; Human: delay sensitivity | None (prose examples) | WH Maths Vol 8 |
| 5 | Model failure modes | All three domains | Mermaid 7.4 (wrong boundary example) | No |
| 6 | Simulation: supply chain dynamics | Human + cross-domain | Python supply chain + Fig 7.5 | WH Comp Geo |
| 7 | Exercises | — | — | — |

---

### Section 0: The puzzle

**Purpose:** Generate the question the chapter answers. Arrive at "structural accuracy > parameter precision" without stating it until the end.

**Content:**
- Open with Limits to Growth publication (1972) and the dismissal by mainstream economics
- Describe World3 model briefly: 200 variables, 12 stocks, system dynamics methodology
- Describe Herrington (2021) comparison: 50 years of actual data tracked the projection
- State the puzzle explicitly: the critics were right on the details. How was the model right on the trajectory?
- Resolve: structural accuracy. The feedback loops were right even when the parameters were rough.
- Close with the chapter's framing: modelling is the craft of identifying the load-bearing loops. This chapter is about that craft.

**Target:** 450–500 words. No subsection headers. Voice: state the observation, let the contrast between prediction and dismissal do the work. No enthusiasm.

**Separator:** `---`

---

### Section 1: The modelling cycle

**Header:** `## The modelling cycle`

**Purpose:** Give the reader a procedural map of model-building before diving into any step. The six stages should feel like a familiar engineering design cycle — not a new methodology but a systematised version of what careful engineers already do.

**The six stages:**

1. **Observation** — identify the behaviour of concern. What oscillates, grows, collapses, or fails to reach its goal? What data exists?
2. **Conceptual model** — verbal description of the stocks, flows, and feedback connections that seem responsible. Draw the boundary.
3. **Causal loop diagram** — map the feedback loops. Identify which are reinforcing, which are balancing, where the delays are.
4. **Stock-flow diagram** — translate the causal loops into stocks and flows with explicit mathematical relationships. No equations yet.
5. **Equations and code** — write the differential equations implied by the stock-flow diagram. Implement in code. Run.
6. **Validation** — test structural consistency, behavioral validity, sensitivity. Iterate.

**Key pedagogical points:**
- The cycle is iterative, not linear. Stage 6 regularly sends you back to Stage 2.
- The single most common error is trying to go directly from observation to equations (Stage 1 → Stage 5), skipping the structural thinking. This produces models that are mathematically precise and structurally wrong.
- Model boundary decisions happen at Stage 2. The boundary determines what variables are endogenous (explained by the model) and exogenous (treated as given). A boundary that is too narrow misses the dominant feedback. A boundary that is too wide includes irrelevant complexity that obscures the structure.

**Three-domain examples:**

*Earth:* A glacier mass balance model. The behaviour of concern: Athabasca Glacier (Canadian Rockies) has lost 60% of its volume since 1900. The boundary decision: what do we include? Accumulation (snowfall in winter), ablation (melt in summer), albedo feedback (less ice → lower albedo → more solar absorption → more melt). This is the minimum boundary that captures the dominant dynamics. Upstream precipitation patterns and global temperature are treated as exogenous forcing.

*Human:* A supply chain model. The behaviour of concern: beer game experiments (Sterman, MIT Sloan, 1989) show that participants managing a three-node supply chain consistently produce wild inventory oscillations in response to a small, constant increase in consumer demand — even when all actors are fully rational and have complete information. The boundary: three inventory stocks, shipping delays, order-up-to replenishment policy.

*Data:* A production ML pipeline. The behaviour of concern: model accuracy degrades, data freshness is maintained, but alerting latency means teams discover failures weeks after they occur. The boundary: three monitoring loops (feature drift, accuracy drift, data freshness) with different detection and response delays.

**Diagram:** Mermaid 7.1 — a circular flowchart showing the six stages of the modelling cycle as a loop, with "iterate" feedback from Stage 6 back to Stage 2. Clean and minimal.

**Target:** 600–700 words. Voice: procedural precision. Name the stages clearly. The reader should feel they have a checklist, not a philosophy.

**Separator:** `---`

---

### Section 2: From verbal description to differential equations

**Header:** `## From verbal description to equations`

**Purpose:** Teach the mechanical translation from stock-flow diagram to differential equations. This is the step most students find non-obvious.

**Translation rules (the core of this section):**
- Every stock → one state variable (its current level)
- Every inflow → a positive term in the stock's rate equation (dS/dt = +inflow)
- Every outflow → a negative term (dS/dt = ... -outflow)
- Flows that depend on stock levels → functional relationships (e.g., outflow = k * S, or outflow = S/τ)
- Feedback enters through these functional relationships

**Worked example: glacier mass balance**

Verbal description:
- Ice mass M (the stock) accumulates through net snowfall accumulation (inflow A, treated as approximately constant seasonally)
- Ice mass melts through ablation (outflow L), which depends on temperature and ice surface area
- Key feedback: as ice retreats, surface albedo decreases (ice reflects ~80% of solar radiation; exposed rock and water reflect ~15%). Lower albedo means more solar energy absorbed, which increases ablation. Less ice → lower albedo → more ablation → less ice. This is a reinforcing loop.

Causal loop notation:
- M → (+) surface area → (-) albedo → (-) absorbed radiation → ... → wait
- Actually: M ↓ → albedo ↓ → solar absorption ↑ → ablation ↑ → M ↓ (reinforcing, sign product: negative × negative × positive = negative of change = amplifying collapse)

Stock-flow diagram → equations:
```
dM/dt = A - L(M)
```
where:
```
L(M) = L₀ + α·(M₀ - M)
```
- L₀ = baseline ablation at reference ice mass M₀ (units: Gt/yr)
- α = albedo feedback coefficient (stronger α → faster runaway)
- When M < M₀: albedo is lower than reference, so ablation is higher than L₀ (reinforcing loss)
- When M > M₀: albedo is higher, ablation is lower (stabilising in the other direction)

This gives:
```
dM/dt = A - L₀ - α·(M₀ - M) = (A - L₀) + α·M - α·M₀
```
Which is a linear ODE with a single equilibrium at M* = M₀ - (A - L₀)/α.
- If A > L₀: equilibrium exists above zero. Glacier reaches steady state.
- If A < L₀ and feedback is strong: equilibrium below zero — glacier melts away.

**Supply chain inventory equations (briefer):**
```
dI/dt = receipt_rate - shipment_rate
```
where:
- receipt_rate = P/τ (pipeline stock draining at rate 1/τ)
- shipment_rate = min(I, demand) (bounded by inventory)
- dP/dt = order_rate - P/τ (pipeline accumulates ordered goods, drains as they arrive)

**Incident backlog equations:**
```
dB/dt = incident_rate - resolution_rate(B)
```
where resolution_rate decreases when B is large (alert fatigue — balancing loop that weakens under load). This is the reason incident management systems degrade under high load.

**Target:** 750–850 words. Voice: precise and instructional. Show the algebra. The reader should be able to replicate the translation independently after this section.

**Diagrams:** Mermaid 7.2 — glacier CLD (reinforcing ablation loop) and stock-flow diagram side by side (or as two sequential diagrams).

**Separator:** `---`

---

### Section 3: Implementing in Python

**Header:** `## Implementing in Python`

**Purpose:** Demonstrate the Euler method as the direct computational realisation of the differential equation. Show the glacier model implemented in full. Make the connection between the equation and the code explicit and one-to-one.

**Why Euler method?**
- Not because it is the most accurate numerical integrator (it is not)
- Because the update rule is a direct transcription of the differential equation: `x(t + dt) = x(t) + f(x, t) * dt`
- The reader can see every mechanism in the code
- For the feedback structures in this book — smooth flows, no stiffness — Euler with a small enough dt is adequate
- When Euler is not adequate: stiff systems (fast and slow timescales in the same model), precise quantitative work. scipy.integrate.solve_ivp is the production alternative for those cases — brief mention only.

**Choice of dt:**
- Rule of thumb: dt should be no more than 1/4 of the fastest time constant in the model
- If the fastest feedback loop operates on a 1-year timescale, dt = 0.1 yr is safe
- Test by halving dt: if the result changes significantly, dt was too large

**Three-domain connection:**
- Earth: glacier model implemented in full (main Python block)
- Human: supply chain (preview — full implementation in Section 6 simulation)
- Data: the retraining loop from Chapter 6 was already an Euler implementation — this section retroactively names the method that was used there

**Glacier simulation (Fig 7.3):**
Three scenarios:
1. A > L₀ (accumulation dominates): glacier grows to equilibrium
2. A < L₀, weak feedback (α small): glacier retreats slowly to lower equilibrium
3. A < L₀, strong feedback (α large): runaway retreat, glacier collapses to zero

Two panels:
- Left: ice mass M(t) over 200 years, three scenarios
- Right: phase portrait dM/dt vs M, showing equilibrium point and instability

The phase portrait connects back to Chapter 2 (feedback archetypes) and forwards to WH Maths Vol 8 (stability analysis).

**Cross-link callout:** Data Engineering Ch 7–8. The Euler implementation of an ML pipeline model (feature drift, model accuracy, monitoring response) is the blueprint for data engineering teams who want to reason about monitoring system design before building it.

**Target:** 700–800 words. Voice: instructional. Show code, explain each decision, connect each line back to the equation.

**Separator:** `---`

---

### Section 4: Validation and sensitivity

**Header:** `## Validation and sensitivity`

**Purpose:** Teach what "testing a model" means for system dynamics — which is different from testing software or statistical models.

**Three types of validation:**

1. **Structural validation** — does the model have the right feedback loops? Test by inspection and by asking whether removing any element breaks the qualitative behaviour. If removing a loop has no effect, the loop may be unnecessary.

2. **Behavioural validation** — does the model reproduce the reference mode? Not precise quantitative fit — but does it produce the same qualitative pattern (growth, oscillation, overshoot, collapse)?
   - Reference mode: the historical or observed time pattern you are trying to explain
   - The model should produce this pattern from plausible parameter values, not just one carefully chosen set
   
3. **Sensitivity analysis** — vary parameters systematically. Which parameters, when varied substantially, change the qualitative conclusion? Those parameters need careful empirical grounding. Parameters that don't change the qualitative conclusion matter less.

**Glacier sensitivity example:**
- Vary accumulation rate A: model remains structurally valid across a range
- Vary feedback coefficient α: qualitative transition from stable retreat to runaway at a threshold value
- The threshold is the interesting finding — not the precise number, but the fact that a threshold exists

**Supply chain sensitivity example:**
- Vary delay τ: longer delays → larger oscillation amplitude
- The relationship between delay length and oscillation amplitude is superlinear (small increase in delay → large increase in swing)
- This is the actionable insight: reducing supply chain delays reduces inventory volatility faster than reducing delays proportionally

**What validation is not:**
- It is not calibration (fitting parameters to historical data)
- It is not prediction of a specific future state
- A calibrated model that fails structural validation is less trustworthy than an uncalibrated model that passes it
- The purpose of calibration is to narrow the range of plausible scenarios — not to determine which scenario is "correct"

**Cross-link callout:** WH Maths Vol 8 (Ch 1: Control, Feedback, Stability). Eigenvalue analysis of the linearised system provides a formal basis for the sensitivity analysis described here. The glacier model's Jacobian ∂f/∂M = α has eigenvalue α — positive when α > 0 (reinforcing loop) and the size of α determines the growth rate. The stability threshold discussed informally here is the zero-crossing of this eigenvalue.

**Target:** 600–700 words. Voice: methodological precision. The reader should understand that building a model is not the same as trusting it.

**Separator:** `---`

---

### Section 5: Model failure modes

**Header:** `## Model failure modes`

**Purpose:** Teach the standard ways models go wrong — not as cautionary tales, but as a practical checklist for the model-builder.

**Five failure modes:**

1. **Wrong boundary** — the dominant feedback loop is outside the boundary. The model produces a result that looks reasonable at first but cannot reproduce extreme behaviours because the mechanism that drives extremes is excluded. Example: a model of housing prices that excludes developer response to price signals will not produce the supply adjustment that moderates price bubbles (Ch 5 connection). Example: a model of an ML pipeline that excludes the labelling lag will miss the most important delay.

2. **Missing delays** — the model connects stocks with instantaneous flows where reality has a significant delay. Instantaneous connections suppress oscillation. The supply chain model without shipping delay does not produce the bullwhip effect — the delay is the cause of the oscillation, not a refinement.

3. **Linear approximation of nonlinear feedback** — replacing a nonlinear feedback relationship with a linear one may produce correct behaviour near the operating point but wrong behaviour under stress. The glacier albedo feedback is genuinely nonlinear (albedo depends on ice fraction, which approaches limits at 0 and 1). Linearising it is adequate for small perturbations from the reference state; it fails under the large perturbations that are most interesting.

4. **Over-specification** — adding detail that does not affect the behaviour of concern. A model of supply chain oscillation does not need detailed product demand forecasting. A model of glacier retreat does not need ice crystal rheology. Over-specified models are harder to validate, harder to interpret, and no more accurate on the question they were built to answer. Meadows called this "complexity that obscures rather than illuminates."

5. **Parameter fetishism** — treating a structurally wrong model as valid because it is precisely calibrated. A model with the wrong feedback loops produces the wrong qualitative behaviour regardless of how accurately its parameters are estimated. The correct response to poor behavioural validation is not better data — it is a revised feedback structure.

**Earth domain example:** A permafrost carbon feedback model that excludes the active layer thaw depth feedback — the reinforcing loop where warming → deeper active layer → more organic matter available for decomposition → more CO₂/CH₄ release → warming — will underestimate warming even with perfect parameter estimates for everything it includes.

**Data domain example:** An incident management model that models resolution rate as constant (ignoring alert fatigue) will produce optimistic estimates of mean time to resolution under high-load conditions — exactly when accurate estimates matter most.

**Diagram:** Mermaid 7.4 — a wrong-boundary example: the housing supply model from Ch 5 with developer response excluded, shown as a boundary line cutting through the feedback loop. Caption explains what the excluded loop does.

**Target:** 650–750 words. Voice: precise and slightly forensic. These are real failure modes that produce real errors; treat them as such.

**Separator:** `---`

---

### Section 6: Simulation — supply chain dynamics

**Header:** `## Simulating the bullwhip effect`

**Purpose:** Demonstrate the full model-building methodology on a canonical example. The supply chain is historically significant (Forrester 1958), pedagogically clean, and directly applicable across domains.

**Framing prose (before code):**
- Beer game origin: Forrester 1958 MIT; Sterman 1989 popularised the experiment
- Three-node chain: retailer, distributor, producer
- Consumer demand step: +20% at week 8 (from 10 to 12 units/week)
- Each node uses order-up-to policy with correction term
- Key variables: inventory at each node (Stocks), pipeline orders in transit (delay stocks), order rates

**Three scenarios:**
1. τ = 1 week: minimal delay, small oscillation, demand signal transmits cleanly
2. τ = 3 weeks: standard delay, bullwhip emerges — producer inventory swings ±40% from a 20% demand change
3. τ = 3 weeks, amplify = 2.0: panic ordering, severe oscillation, periodic stockouts

**Figure 7.5:** Two panels
- Panel 1: Inventory at retailer, distributor, producer over 60 weeks (Scenario 2)
  - Shows amplification: retailer swings less than distributor, distributor less than producer
  - Vertical line at week 8 marks the demand step
- Panel 2: Order rates at each node for all three scenarios on one plot
  - Shows panic ordering amplification vs. standard delay vs. minimal delay

**What to try callout:**
1. Add a fourth node (second distributor). How does the bullwhip amplitude change?
2. Change the ordering policy: instead of correcting over one delay period, smooth the correction over three. What happens to oscillation amplitude?
3. Reduce the demand step to 5% (from 10 to 10.5 units/wk). Is the bullwhip amplitude roughly proportional to the step size?

**Cross-link callout:** Computational Geography Parts 4 and 5 (Hazards, Economic Systems). The supply chain model here is the feedback-dynamics precursor to the economic disruption models in Comp Geo Part 5. The same delay-amplification structure appears in electrical grid frequency dynamics (a fast version of the same problem) and in wildfire resource allocation chains (a slow version). The model here captures the mechanism; the domain-specific chapters apply it with realistic parameters.

**Target prose:** 300–400 words (framing + what-to-try). Python code does the rest.

**Separator:** `---`

---

### Section 7: Exercises

**Six exercises following the standard four types:**

1. **System identification:** A city's emergency medical services faces the following: call volume increases during heat waves (more cardiac events), which depletes available ambulance units, which increases response times, which increases the severity of cases requiring treatment, which prolongs time at hospital, which further depletes available units. Draw the causal loop diagram. Identify all feedback loops. Are they reinforcing or balancing? Where are the delays?

2. **Archetype recognition (with modelling extension):** The Sahel region experienced a long-term desertification cycle in the 20th century. Reduced rainfall → reduced vegetation cover → reduced evapotranspiration → reduced local rainfall (vegetation-precipitation feedback, well-established). Sketch the stock-flow diagram. Write the differential equations. What conditions are necessary for the system to have a stable vegetated equilibrium? What conditions produce a desert trap?

3. **Simulation build:** Using the glacier model from Section 3, add a second feedback: warming temperature increases ablation directly (temperature-driven melt, separate from the albedo feedback). Add a temperature stock T(t) that rises slowly due to greenhouse forcing (a linear drift: dT/dt = forcing_rate). How does this change the threshold between stable retreat and runaway? What is the effect of different values of forcing_rate?

4. **Validation exercise:** The carbon cycle simulation from Chapter 4 was implemented with three stocks and approximate flow values. (a) Describe a structural validation test for that model. What feedback loops should it reproduce? (b) Describe a behavioral validation test. What reference mode should it match? (c) Which parameters, if varied, would change the qualitative conclusion about long-run atmospheric CO₂ accumulation?

5. **Leverage point identification:** The supply chain model from Section 6. Using Meadows' leverage point hierarchy from Chapter 8 (preview): (a) At what leverage point does reducing the shipping delay τ operate? (b) At what leverage point does changing the ordering policy from aggressive correction to smooth correction operate? (c) Which intervention would be more effective at eliminating the bullwhip? Justify your answer in terms of the model structure.

6. **Model design:** You are building a model of urban heat island dynamics. The behaviour of concern: urban core temperature has been rising relative to surrounding rural areas at approximately 0.03°C/year over the past 40 years. Sketch the causal structure: what stocks and flows are involved? What are the dominant feedback loops? Draw a boundary that is wide enough to capture the dominant dynamics but no wider. List one variable you would explicitly exclude and justify the exclusion.

---

## 3. Diagram Specifications

### Diagram 7.1 — The modelling cycle

**Type:** Mermaid flowchart (LR or TD)
**Content:** Six stages as nodes in a loop:
- Observation → Conceptual model → Causal loop diagram → Stock-flow diagram → Equations and code → Validation → (back to) Conceptual model
- The return arrow from Validation to Conceptual model labelled "iterate"
- Style: rectangular nodes, clean left-to-right flow

### Diagram 7.2 — Glacier mass balance (CLD + SFD)

**Type:** Two Mermaid diagrams, sequential
**Diagram 7.2a:** Causal loop diagram
- Nodes: ice mass, surface albedo, solar absorption, ablation
- Loop: ice mass ↓ → albedo ↓ → solar absorption ↑ → ablation ↑ → ice mass ↓
- Mark as reinforcing (R) with sign arrows (+/-)
**Diagram 7.2b:** Stock-flow diagram
- Stock box: Ice mass M
- Inflow arrow: Accumulation A (exogenous — constant from left)
- Outflow arrow: Ablation L(M) (function of M — include expression)
- Feedback shown as curved arrow from M back to L(M)

### Diagram 7.3 — Supply chain stock-flow (used in Section 6)

**Type:** Mermaid flowchart
**Content:** Three inventory stocks (Retailer, Distributor, Producer) with pipeline delay stocks between them
- Show: Customer demand → Retailer → [pipeline P_r] → Distributor → [pipeline P_d] → Producer
- Order flows going upstream (dashed or different colour)
- Label: "delay τ" on each pipeline

### Diagram 7.4 — Wrong boundary example (Section 5)

**Type:** Mermaid diagram
**Content:** Housing price model with developer response feedback loop
- Inside boundary: house prices, demand, mortgage rates
- Outside boundary (greyed out or dashed): developer response, new construction, housing supply
- The broken loop shown explicitly — the model inside the boundary cannot produce the supply adjustment that moderates price bubbles
- Caption explains what happens when you exclude the developer response loop

---

## 4. Simulation Specification

### Simulation 1 (Section 3): Glacier mass balance

**File:** `_assets/ch07-glacier-simulation.png`
**Implementation:** Euler integration, dt = 0.1 yr, T = 200 yr
**Stocks:** Ice mass M (Gt)
**Equations:**
```
L(M) = L₀ + α*(M₀ - M)
dM/dt = A - L(M)
```
**Three scenarios:**
1. A = 52, L₀ = 45, α = 0.05 (accumulation > ablation at M₀, weak feedback: stable growth to higher equilibrium)
2. A = 45, L₀ = 50, α = 0.03 (ablation > accumulation, weak feedback: slow retreat to lower equilibrium)
3. A = 45, L₀ = 50, α = 0.10 (ablation > accumulation, strong feedback: runaway — glacier collapses)

**Parameters:**
- M₀ = 1000 Gt (reference ice mass)
- M_init = 1000 Gt (starting at reference)

**Figure:** 2 panels
- Panel 1: M(t) over 200 years, three scenarios with distinct line styles
- Panel 2: Phase portrait — dM/dt vs M — for each scenario, showing equilibrium (dM/dt = 0) intersection and stability

**WH palette:**
- Scenario 1 (growth): `#111111` solid
- Scenario 2 (slow retreat): `#888888` dashed
- Scenario 3 (runaway): `#d52a2a` solid

---

### Simulation 2 (Section 6): Supply chain dynamics

**File:** `_assets/ch07-supply-chain.png`
**Implementation:** Euler integration, dt = 0.1 week, T = 60 weeks
**Stocks:** I_r (retailer inventory), I_d (distributor inventory), I_p (producer inventory), P_r (retailer pipeline), P_d (distributor pipeline)

**Equations:**
```
# Pipeline dynamics (first-order material delay)
dP_r/dt = OR_r - P_r/τ
dP_d/dt = OR_d - P_d/τ

# Inventory dynamics
dI_r/dt = (P_r/τ) - min(I_r, demand)
dI_d/dt = (P_d/τ) - min(I_d, OR_r)
dI_p/dt = production_rate - min(I_p, OR_d)

# Order-up-to policy
OR_r = max(0, demand + amplify * (I_TARGET - I_r) / max(τ, 1))
OR_d = max(0, OR_r   + amplify * (I_TARGET - I_d) / max(τ, 1))
production_rate = max(0, OR_d + amplify * (I_TARGET - I_p) / max(τ, 1))
```

**Three scenarios:**
1. τ = 1.0 week, amplify = 1.0 (minimal delay)
2. τ = 3.0 weeks, amplify = 1.0 (standard — main result)
3. τ = 3.0 weeks, amplify = 2.0 (panic ordering)

**Initial conditions:** I_r = I_d = I_p = 20 units; P_r = P_d = demand * τ (equilibrium pipeline)

**Demand:** step from 10 to 12 units/wk at t = 8 weeks

**Figure:** 2 panels
- Panel 1: Inventory at retailer, distributor, producer over 60 weeks (Scenario 2 only — most readable)
  - Three lines: retailer (thin black), distributor (medium grey), producer (thick red)
  - Vertical dashed line at t = 8 (demand step)
  - Horizontal reference line at I_TARGET = 20
- Panel 2: Order rates at all three nodes for Scenarios 2 and 3 (two line styles per node)
  - Shows panic ordering amplification
  - Label curves at right edge

---

## 5. Cross-Link Callout Specifications

### Callout 1 (Section 3) — Data Engineering

**Location:** After the Python implementation discussion
**Header:** `## Model implementation and ML pipeline design`
**Content:** The Euler implementation of a system dynamics model is structurally identical to the simulation used in Chapter 6 for the ML retraining loop. Both are explicit state-machine implementations: stock values are updated at each step by applying flow equations. Data engineering teams who model their pipelines formally — writing out the stocks (data backlog, model weights, accuracy score), the flows (ingest rate, training rate, evaluation rate), and the feedback connections — before building the pipeline will design better monitoring systems. The model reveals which delays are load-bearing and which metrics need the shortest detection latency.

### Callout 2 (Section 4) — WH Maths Vol 8

**Location:** After the sensitivity analysis discussion
**Header:** `## Stability analysis and the mathematics of feedback`
**Content:** The sensitivity analysis described in this section has a precise mathematical formulation in WH Maths Vol 8, Ch 1 (Control, Feedback, Stability). The eigenvalue of the Jacobian matrix at a fixed point determines the stability type: negative eigenvalues (stable equilibrium), positive eigenvalues (unstable — reinforcing loop dominates), imaginary component (oscillation). The glacier model's linearised Jacobian ∂f/∂M = α has eigenvalue α — when α > 0 (reinforcing feedback), the equilibrium is unstable and small perturbations grow. This is the formal version of the sensitivity threshold identified in this section.

### Callout 3 (Section 6) — Computational Geography

**Location:** After the supply chain simulation
**Header:** `## Supply chain dynamics in physical and economic systems`
**Content:** The delay-amplification structure in the supply chain model appears across domains in WH Computational Geography. In Part 4 (Hazards), fire suppression resource deployment follows the same pattern: demand for resources at the fire front propagates through a procurement and logistics chain with delays, generating oscillations between resource shortage and surplus. In Part 5 (Economic Systems), the bullwhip effect in commodity supply chains — oil, grain, metals — produces the commodity price cycles that are a recurring feature of resource economies. The model here captures the mechanism. The Computational Geography chapters apply it with domain-specific calibration.

---

## 6. Assembly Instructions

### Writing order

1. Write Section 0 (puzzle) first — sets the chapter's intellectual stakes
2. Write Section 1 (modelling cycle) + Diagram 7.1
3. Write Section 2 (equations) + Diagrams 7.2a and 7.2b
4. Write Section 3 (Python) — include working glacier simulation code and Fig 7.3
5. Write Sections 4 and 5 (validation and failure modes) + Diagram 7.4
6. Write Section 6 (simulation) — include working supply chain code and Fig 7.5
7. Write exercises
8. Insert cross-link callouts at specified locations

### Validation before finalising

Run all Python code cells. Confirm:
- Glacier simulation: three distinct trajectories, correct qualitative behaviour (growth/retreat/runaway)
- Phase portrait: equilibrium at correct M* for each scenario, stable/unstable correctly shown
- Supply chain: bullwhip amplitude scales with delay; panic ordering scenario shows stockouts (inventory reaching zero)
- All figures saved to `_assets/ch07-*.png` with dpi=150

### Checklist before handoff

- [ ] YAML front matter complete with all required fields
- [ ] All six sections present
- [ ] Three Mermaid diagrams render (flowchart, CLD+SFD, wrong boundary)
- [ ] Glacier simulation: three scenarios, 2-panel figure, callout-tip with three "What to try" items
- [ ] Supply chain simulation: three scenarios, 2-panel figure, callout-tip with three items
- [ ] Three cross-link callouts at correct locations
- [ ] Six exercises covering all four exercise types
- [ ] No sections end on a summary — last sentence of each section sets up the next
- [ ] Dollar signs not relevant in this chapter (no monetary values)
