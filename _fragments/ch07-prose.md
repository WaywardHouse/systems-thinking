---
title: "Modelling and Simulation"
subtitle: "From causal diagrams to running models — and what validation actually means"
status: seed
axiom: "A model that includes everything is just the system. The simplification is not a weakness. It is the point. Every modelling decision is a hypothesis about which parts of the system matter for the question you are trying to answer."
rewrite: "Model validation is not about whether the model is correct. No model is correct. It is about whether the model is useful — whether it generates insights that hold up when tested against data and behaviour the model was not built to reproduce."
opens_to:
  - chapter: 08-systems-intervention
    relationship: enables
  - course: ESDE 307
    relationship: anchors
destinations:
  - field: earth
    hook: "The Limits to Growth model, built in 1972 on a mainframe with twelve differential equations, produced population and resource trajectories that have tracked historical data for fifty years. Not because the model was detailed. Because it captured the right feedback structures."
  - field: human
    hook: "The boom-bust cycle in oil and gas investment follows the same equations as predator-prey dynamics. Capital chases resource rent. High investment depletes the resource base. Depleted rents reduce investment. Reduced investment allows the resource base to recover. The equations are the same. The timescales differ."
  - field: data
    hook: "Overfitting is predator-prey dynamics in loss space. Model complexity is the predator. Training data signal is the prey. When the predator grows too fast — when complexity consumes all available signal — the prey collapses and the model generalises to nothing."
---

## The puzzle

The puzzle is the Limits to Growth model. In 1972, a team at MIT — Donella Meadows, Dennis Meadows, Jørgen Randers, and William Behrens — published a systems dynamics model of global civilisation. Twelve differential equations. Five major stocks: world population, food production, industrial output, non-renewable resources, and pollution. The model was built on a computer the size of a room. The computations took hours. The results were stark: on a business-as-usual trajectory, industrial output per capita would peak around 2015 and collapse by mid-century, driven by resource depletion and pollution feedback.

The model was widely criticised. Too simple. Too pessimistic. Wrong about specific quantities. The criticism was partly correct — the model was simple, and specific predictions were imprecise. But subsequent researchers who overlaid actual historical data on the Limits to Growth trajectories found a result that surprised many critics: the system-level behaviour of the BAU scenario tracked observed historical data on population growth, food production, industrial output, resource use, and pollution with reasonable fidelity for five decades. Not because the model was detailed. Because it captured the right feedback structures. The specific numbers were wrong in many cases. The dynamic behaviour — the pattern of growth, overshoot, and approaching collapse — was approximately right.

This is what models are for. Not to be correct. To be useful. A model is correct when every parameter is precisely known, every relationship is accurately specified, every boundary condition is properly set. No model of a complex system is correct in this sense. A model is useful when it generates insights about dynamic behaviour that survive contact with data — when the patterns the model produces are recognisable in the patterns the system produces. The Limits to Growth model was useful. It remains useful. Its simplicity was a feature, not a flaw.

---

## What models are and are not

A model is a deliberately simplified representation of a system, built to answer a specific question. The simplification is the point. A model that represents everything is the system itself — it predicts the future no better than the future predicts itself, and it tells you nothing about which parts of the system are responsible for which behaviours.

Every model embeds assumptions. The assumptions determine which variables are included and which are left out, which relationships are linear and which are nonlinear, which timescales are resolved and which are aggregated. These are not secondary engineering choices. They are the core intellectual commitments of the model. Two models of the same system can produce qualitatively different behaviours depending on which feedbacks are included — not because one is right and one is wrong, but because they are answering different questions.

The relevant question to ask of any model is not "is it correct?" It is: "what question was it built to answer, and does it answer that question usefully?" The Limits to Growth model was not built to predict precisely when food production would peak. It was built to ask whether exponential growth in a finite system produces overshoot and collapse — and if so, under what conditions interventions could alter the trajectory. It answered those questions usefully.

Three categories of model failure are worth naming explicitly. The first is structural failure: the model omits a feedback loop that is dominant in the actual system. The behaviour the model generates is wrong in kind, not just in degree — because the loop that is missing is the loop that determines qualitative behaviour. The second is parameter failure: the model structure is correct but the parameters are wrong. This produces quantitatively incorrect predictions that may still get the qualitative behaviour right. The third is boundary failure: the model's boundary is drawn in the wrong place. A consequence of interest lies outside the model, or a cause of important behaviour is external to the model by assumption. The model cannot produce the observed behaviour because the relevant mechanism is not inside the boundary.

**Human domain: The oil price cycle as a model validation case**

The commodity price cycle — the multi-year boom-bust pattern in oil, copper, and other commodities — is a test case for structural modelling. A model that treats commodity prices as random fluctuations will not produce the characteristic 5–10 year oscillation observed in historical data. A model that includes the investment-capacity-production feedback structure — capital chases high prices, investment builds capacity with a multi-year delay, capacity depresses prices, low prices reduce investment, depleted capacity eventually raises prices again — will produce the oscillation structurally. The oscillation is not noise. It is the signature of a balancing feedback loop with a long delay. A model that produces this oscillation has captured the right structure, even if the specific period of the cycle is parameterised imprecisely.

**Data domain: What overfitting is, structurally**

An overfit model has the wrong boundary. The boundary is drawn too wide — it includes noise in the training data as signal, fitting the idiosyncratic features of the training set rather than the generalisable relationship between inputs and outputs. Structural modelling and ML generalisation failure are the same problem from two angles: both involve a model that has learned from a specific dataset and must perform on a different one. The question "will this model generalise?" is the question "is the structure I have identified in this data the structure of the underlying system, or the structure of this particular sample?"

---

## From verbal model to causal loop diagram

Every model begins as a verbal model. Someone describes a system in natural language: prices rise, investment increases, supply expands, prices fall, investment contracts. The verbal model is already a model. It contains implicit assumptions about causality, timescale, and which variables matter. The causal loop diagram makes those assumptions explicit, visible, and testable.

The translation from verbal to diagram follows four steps.

**Step 1: Identify the variables.** List every noun in the verbal model that changes over time. Not every noun — only those that vary. Population changes. Land area (mostly) does not. Wages change. The Celsius scale does not.

**Step 2: Identify causal links.** For each pair of variables, ask: if the first increases, does the second increase or decrease, all else equal? Write a + if the same direction, a − if the opposite direction. Be specific about the direction and mechanism. "Investment increases capacity" is a link. "Investment affects capacity" is not — it does not commit to a direction.

**Step 3: Identify loops.** Trace paths through the diagram that return to their starting variable. Count the − signs. Even: reinforcing. Odd: balancing. Label each loop.

**Step 4: Identify delays.** For each link, ask: how long does it take for a change in the cause to produce a change in the effect? Links with delays of months or years change the qualitative behaviour of the loop — they are what produces oscillation in balancing loops and overshoot in reinforcing ones.

The causal loop diagram is not the model. It is the model's skeleton — the qualitative structure that a quantitative model must be consistent with. A quantitative model that violates the causal loop diagram is structurally wrong, regardless of how well it fits historical data.

**Earth domain: Phytoplankton-zooplankton as a worked CLD**

The open ocean surface layer is dominated by two interacting populations: phytoplankton (microscopic photosynthesising organisms) and zooplankton (microscopic grazers). Phytoplankton grow through photosynthesis, limited by light and nutrient availability. Zooplankton graze on phytoplankton. Their growth rate is proportional to phytoplankton availability. Zooplankton mortality returns nutrients to the water column.

The causal loop structure: phytoplankton increase → zooplankton have more food → zooplankton increase. Zooplankton increase → phytoplankton consumed faster → phytoplankton decrease. Phytoplankton decrease → zooplankton have less food → zooplankton decrease. Zooplankton decrease → phytoplankton consumed more slowly → phytoplankton increase. The loop is balancing — it produces oscillation. The spring bloom and subsequent crash in Northern Hemisphere coastal waters is the observational signature of this loop in real ocean data.

The diagram below traces the full modelling workflow from verbal description through causal loop diagram, stock-flow model, simulation, and validation — showing where each step adds precision and where each step introduces commitments that must be tested.

[DIAGRAM 7.1 GOES HERE]

The phytoplankton-zooplankton causal loop diagram isolates the two coupled balancing loops — the self-limiting growth loop within the phytoplankton population and the predator-prey loop between populations — and marks the delays that determine the period of oscillation.

[DIAGRAM 7.2 GOES HERE]

---

## From causal loop diagram to stock-flow model

A causal loop diagram specifies which variables influence which other variables and in what direction. It does not specify how variables accumulate over time. That requires distinguishing stocks from flows — the same distinction from Chapter 1.

The translation from CLD to stock-flow model has three steps.

**Step 1: Classify variables as stocks or flows.** A stock accumulates. It has memory — its current value depends on its history. A flow changes a stock. Stocks are measured at a point in time. Flows are measured over a period. Population is a stock. Birth rate is a flow. Carbon in the atmosphere is a stock. CO₂ emissions are a flow. Model implementation error is almost always an error of misclassification at this step — treating a flow as a stock or vice versa.

**Step 2: Write the differential equations.** Each stock has a differential equation of the form dS/dt = (sum of inflows) − (sum of outflows). Each inflow and outflow is either a constant, a function of the current stock levels, or a function of other auxiliary variables. In the predator-prey system: d(prey)/dt = r_prey × prey − a × prey × predator. d(predator)/dt = b × prey × predator − d × predator. Every term has a clear physical interpretation.

**Step 3: Specify initial conditions and parameters.** The model is not specified until every initial stock level and every parameter is given a value. The initial conditions determine where in the state space the model starts. The parameters determine the shape of the trajectories from that starting point. Sensitivity analysis asks which parameters most strongly influence the model's outputs — those are the parameters whose uncertainty most needs to be reduced before the model is used to inform decisions.

::: {.callout-note}
## Differential equations and linear stability

The stock-flow equations derived here are ordinary differential equations (ODEs). Their equilibria — the points where all flows balance and all stocks stop changing — can be found by setting the right-hand side to zero. Whether those equilibria are stable depends on the eigenvalues of the Jacobian matrix at the equilibrium point: negative real parts → stable (balancing); positive real parts → unstable (reinforcing); purely imaginary → oscillatory.

[WH Maths Vol 8, Ch 2 (Differential Equations)](https://wayward.house/learn/maths/advanced/) covers the Jacobian linearisation approach in detail. Applied to the Lotka-Volterra system, it explains analytically why predator-prey models produce periodic orbits rather than spirals — a structural property of the equations, not an artefact of specific parameter values.
:::

---

## The Euler method — integrating stock-flow models

The differential equations of a stock-flow model cannot always be solved analytically. They are integrated numerically. The Euler method — the integration scheme used throughout this book — updates each stock at each time step by multiplying the current rate of change by the step size:

S(t + dt) = S(t) + (dS/dt) × dt

This is the simplest possible integration scheme. It is also the most transparent: each update corresponds directly to a physical interpretation. The prey population increases by (birth rate − predation rate) × dt. The atmospheric CO₂ stock increases by (emissions − uptake) × dt. Every update is readable.

The Euler method accumulates error. The exact trajectory of a differential equation is a continuous curve. The Euler approximation is a sequence of straight-line steps. Each step introduces an error proportional to dt². Over many steps, the errors accumulate. The total error over a fixed simulation period is proportional to dt — halving the time step halves the total error. For most systems in this book, dt = 1 (year, or the natural unit of the system) is small enough to produce qualitatively correct trajectories. For systems with fast dynamics — populations measured in days, chemical reactions measured in seconds — a smaller dt is required for numerical stability.

Two symptoms of Euler error are worth recognising. The first is numerical instability: the model produces explosive oscillations that grow without bound, even when the underlying system should be stable. This happens when dt is too large relative to the fastest timescale in the system. The rule of thumb: dt should be at most 1/10th of the shortest time constant in the model. The second symptom is slow convergence: the model tracks the correct qualitative behaviour but the specific trajectory is noticeably different from higher-order integration methods. This indicates that dt is too large for quantitative accuracy, even if qualitative behaviour is preserved.

**Human domain: Parameter estimation in the oil investment cycle**

The oil investment cycle model has two key parameters: the investment delay (how long between capital commitment and production capacity coming online — typically 3–7 years for large projects) and the demand elasticity (how sensitive investment is to oil price). Neither is directly measurable. Both are estimated from historical data by finding values that produce model trajectories matching observed cycle periods and amplitudes. This is parameter calibration. It is not the same as validation: a calibrated parameter is one whose value was chosen to fit the data used in calibration. Validation requires checking the calibrated model against data that was not used in calibration — out-of-sample prediction, or a different commodity cycle in a different era.

**Data domain: Numerical stability in ML training**

The Euler method error structure appears directly in neural network training. The gradient descent update is an Euler step: weights(t+1) = weights(t) − learning_rate × gradient. The learning rate is dt. The loss landscape gradient is dS/dt. If the learning rate is too large, the update overshoots the minimum — the Euler step crosses the basin and ends up on the other side, where the gradient points back, causing oscillation. If the learning rate is too small, convergence is slow. The pathologies of Euler integration and the pathologies of gradient descent are the same pathologies. They arise from the same underlying structure.

::: {.callout-note}
## Ecosystem models in environmental assessment

The predator-prey and ocean ecosystem models in this chapter are simplified versions of the coupled biogeochemical models used in environmental impact assessment and fisheries management. [WH Computational Geography Part 1 (Physical Geography) and Part 4 (Hazards)](https://wayward.house/learn/computational-geography/) covers the specific Earth observation data sources — MODIS ocean colour, chlorophyll-a time series, sea surface temperature — used to validate marine ecosystem models and track phytoplankton bloom dynamics. The systems thinking framework explains the loop structures that produce blooms; the computational geography toolkit provides the data needed to parameterise and validate them.
:::

---

## Model validation

Validation is the process of testing whether a model is useful for the question it was built to answer. It is not the process of proving a model is correct. No model of a complex system is correct. Validation has three components.

**Structural validation.** Does the model's causal structure match what is known about the system? Are all dominant feedback loops represented? Are the directions of causality correct? Are the stocks and flows correctly classified? Structural validation can be done before the model produces any output — by checking the causal loop diagram and stock-flow equations against mechanistic knowledge of the system. A model can fit historical data perfectly and still fail structural validation if the fit is produced by the wrong mechanism.

**Behaviour validation.** Does the model reproduce the characteristic dynamic behaviour of the system — its signature patterns over time? Not the specific numerical values, but the qualitative patterns: does it produce the right archetype? A predator-prey model that produces monotonic growth instead of oscillation fails behaviour validation, regardless of how well it fits the initial conditions. A climate model that does not produce the committed warming structure from Chapter 4 fails behaviour validation for long-run temperature response.

**Predictive validation.** Does the model produce useful predictions for data it was not trained on? This requires holding out some historical data during model development, then testing the model against that held-out data. Or testing against future data after the model has been committed. Predictive validation is the hardest test and the most informative. A model that passes predictive validation has demonstrated that it has captured something real about the system's generative process, not merely fitted noise.

The three components of validation are not independent. A model can pass behaviour validation on the training period and fail predictive validation on the test period — the same as overfitting in ML. A model can pass predictive validation numerically while failing structural validation — it gets the right answer for the wrong reason, which means it will fail when conditions change beyond the training range.

**Data domain: Model cards and the validation gap**

The ML community has developed the concept of a model card: a structured documentation of what a model was trained on, what it was validated against, what its known failure modes are, and what conditions it should not be used in. A model card is a partial specification of the model's boundary and validation status. A model deployed without a model card is a model deployed without documentation of which of the three validation types it has passed. Most deployed ML models are in this category. The systems thinking framework makes clear why this matters: a model with an undocumented boundary is a model where the operator does not know which feedback loops are inside and which are outside the boundary of analysis.

Validation is itself a feedback loop: model outputs are compared to observed behaviour, discrepancies are identified, structural and parameter adjustments are made, and the model is re-run. The diagram below shows this structure — and the delays that make the loop slow when ground truth data is scarce or slow to accumulate.

[DIAGRAM 7.3 GOES HERE]

::: {.callout-note}
## Model reproducibility and pipeline validation

Model validation requires that the model be reproducible: given the same data and parameters, the model should produce the same output. This is a data engineering constraint as much as a modelling constraint — it requires version control of training data, code, parameters, and environment.

[WH Data Engineering Ch 3 (Pipelines and ETL) and Ch 8 (ML Platform Architecture)](https://wayward.house/learn/data-engineering/) covers the specific infrastructure — MLflow, DVC, containerisation — that makes model reproducibility operational. A model that cannot be reproduced cannot be validated; a model that cannot be validated should not be deployed for decision support.
:::

---

## Simulation: the Lotka-Volterra model

The Lotka-Volterra predator-prey model is the simplest system that demonstrates all three core elements of systems modelling: two interacting stocks, reinforcing and balancing feedback loops running simultaneously, and oscillatory behaviour that is structurally determined — it arises from the loop structure, not from any specific parameter values. The model below builds it from the differential equations, runs three scenarios varying the predation rate, and plots both the time series and the phase portrait. The phase portrait — prey on the x-axis, predator on the y-axis — reveals the cyclic attractor that is invisible in the time series alone.

[SIMULATION BLOCK GOES HERE]

---

## Exercises

**7.1 — Verbal model to causal loop diagram**

A university's research output is influenced by its reputation, which attracts high-quality graduate students, who conduct research, which improves the university's reputation. The university's research budget funds laboratory infrastructure and salaries; higher research output increases external grant funding; grant funding supplements the research budget. Declining enrolment reduces tuition revenue, which constrains the research budget when grant funding is insufficient.

a. List all variables that change over time in this description.
b. Draw the full causal loop diagram. Label every link as + or −. Identify all complete loops and label each as R or B.
c. The university's research reputation has been declining for 5 years. Using your diagram, trace the reinforcing loop responsible. What intervention at what leverage point would most effectively reverse the decline?

**7.2 — CLD to stock-flow translation**

Consider the following verbal model of a fishery: fish populations grow through reproduction, limited by the carrying capacity of the habitat. Fish are harvested at a rate proportional to both the fish stock and the number of fishing vessels. Fishing revenue depends on the catch and the fish price. High revenue attracts new vessels; low revenue causes vessels to exit. The fish price rises when the catch is low (scarcity) and falls when the catch is high.

a. Identify all stocks in this system. Classify each as a physical stock or an information/economic stock.
b. Write the differential equations for each stock.
c. Draw the full stock-flow diagram. Identify: the self-limiting balancing loop in the fish population, the reinforcing loop in vessel entry, and the balancing loop that connects fish price to harvest pressure.

**7.3 — Euler integration and step size**

A simple predator-prey system is described by the Lotka-Volterra equations with parameters: r_prey = 0.4, a = 0.02, b = 0.01, d = 0.3. Initial conditions: prey = 40, predator = 9.

a. Implement the Euler method with dt = 1.0 to simulate 100 time steps. Plot the time series for both prey and predator populations.
b. Repeat with dt = 0.1 and dt = 0.01. How does the period of oscillation change? At what dt does the trajectory appear to have converged?
c. Identify one condition in which the Euler method with dt = 1.0 would produce a qualitatively incorrect result (not just numerically imprecise). Describe what "qualitatively incorrect" means in terms of the system's attractor.

**7.4 — Model validation**

A systems dynamics model of urban traffic congestion was calibrated on data from 2010–2019 for a mid-sized Canadian city. The model was used to predict the effect of a new ring road on average commute times.

a. Describe how you would assess the structural validity of this model before running any scenarios. What information would you need, and what would a structural failure look like?
b. The model was validated behaviourally against the 2010–2019 historical data and showed good fit. A colleague argues this is sufficient validation for the ring road prediction. What is missing from this validation, and why does it matter for the specific prediction the model is being used for?
c. The ring road was built. Post-construction data shows commute times fell by 8%, but the model had predicted a 22% reduction. Propose three structural reasons — each corresponding to a different modelling failure type — that could explain the gap.

**7.5 — Sensitivity analysis**

The phytoplankton-zooplankton model has four parameters: phytoplankton growth rate (r), grazing rate (a), zooplankton growth efficiency (b), and zooplankton mortality rate (d).

a. Without running the model, predict which parameter has the greatest influence on the amplitude of oscillation. Justify your prediction using the feedback loop structure.
b. Describe a systematic approach to sensitivity analysis for this model. How would you identify which parameters the model's outputs are most sensitive to?
c. You learn that field measurements of the grazing rate (a) carry 40% uncertainty. The phytoplankton growth rate (r) carries 10% uncertainty. If your sensitivity analysis shows that the model is equally sensitive to both parameters, which uncertainty matters more for the quality of model predictions? Why?

**7.6 — Full modelling workflow**

Choose one of the following systems and build a complete stock-flow model:
(a) A glacial mass balance model: a glacier gains mass through snowfall accumulation and loses mass through surface melt and calving. Mean summer temperature drives melt. Mean winter precipitation drives accumulation. Both are exogenously forced.
(b) A startup funding cycle: a startup's cash stock is depleted by operating expenses and filled by revenue and investment. Investor interest depends on growth rate. Growth rate depends on product-market fit (an auxiliary variable). Operating expenses scale with team size. Team size is a stock driven by hiring and attrition.

For your chosen system:
a. Draw the causal loop diagram.
b. Write the differential equations.
c. Identify the initial conditions and parameters you would need to specify, and state what data source you would use to estimate each.
d. Describe one structural validation test and one behaviour validation test you would apply before using the model for decision support.
