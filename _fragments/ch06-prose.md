---
title: "Data as a System"
subtitle: "Pipelines, feedback loops in machine learning, and the dynamics of concept drift"
status: seed
axiom: "A deployed model changes the world it observes. The world it observes is the world it was trained on. When those two worlds diverge, the model fails — not because of a bug, but because feedback starvation is structural."
rewrite: "Concept drift is not a data quality problem. It is a feedback loop problem: the balancing loop that should keep the model current has been severed, starved, or delayed past its useful timescale."
opens_to:
  - chapter: 07-modelling-and-simulation
    relationship: enables
  - course: ESDE 302
    relationship: anchors
destinations:
  - field: earth
    hook: "A land cover classifier trained on Landsat data from 2010 will misclassify shrub expansion into tundra as it accelerates after 2020. The model hasn't changed. The Arctic has. The classifier's training distribution no longer matches the world it's classifying."
  - field: human
    hook: "Credit scoring models trained on pre-2020 economic behaviour failed during COVID-19 not because the models were wrong about the pre-2020 world, but because the pre-2020 world no longer existed. Every model embeds assumptions about the stability of the system it was trained on."
  - field: data
    hook: "A recommendation system that trains on its own outputs is not learning from the world. It is learning from itself. The feedback loop between recommendation and engagement produces a self-referential system whose long-run behaviour is determined by its own loop structure, not by the preferences of its users."
---

---
### FRAGMENT 1 — The puzzle
---

## The puzzle

The spam filter trained on two years of labelled email data achieves 98% accuracy. Six months later, accuracy has fallen to 91%. No one changed the filter. No code was modified. No rules were altered. Email traffic is higher than ever. The filter is being tested on more data than it was trained on. It is failing on cases that look, to a human reviewer, like obvious spam.

The explanation is not a software bug. The spammers changed their vocabulary. The phrases that characterised spam in the training data — specific product names, phrasing patterns, URL formats — are no longer the phrases that characterise spam in the current data. The world drifted. The model stayed still.

This is concept drift: the phenomenon where the statistical relationship between inputs and outputs that a model learned from historical data no longer holds in the present. It is not a pathological edge case. It is the default condition for any model deployed into a world that continues to change after the training snapshot was taken.

The puzzle extends in both directions. Concept drift is the version where the world changes and the model doesn't. But models also change the world they observe — through their own outputs. A recommendation model changes what users see. What users see changes what they click. What they click changes the training data for the next model iteration. A credit scoring model changes who gets loans. Who gets loans changes the loan repayment data that the next model is trained on. These feedback loops between model output and training data are not anomalies. They are structural features of any system where the model acts in the world it predicts.

This chapter applies the feedback structures from Chapters 1–5 to data systems directly. Data pipelines are stock-flow systems. Machine learning models sit inside feedback loops. Concept drift is what happens when a balancing loop is severed. Data quality is a stock that deteriorates without active maintenance. The mechanisms are the same. Only the material changes.

---
### FRAGMENT 2 — Data pipelines as stock-flow systems
---

## Data pipelines as stock-flow systems

Raw data is a stock. It accumulates through ingestion — sensor telemetry, user events, transactional records — and drains through processing. The ingest rate is typically continuous and externally driven: it depends on what is happening in the world, not on the processing system's state. A sensor array generates readings at its sampling frequency regardless of whether the downstream pipeline is keeping pace. A web platform accumulates user events regardless of whether the ETL job has cleared yesterday's batch. The processing rate is capacity-constrained. It cannot exceed what the infrastructure can handle. This asymmetry is the fundamental data engineering problem: ingest can always outpace throughput. When it does, the backlog accumulates.

An unprocessed data backlog is a stock in its own right. It accumulates when ingest exceeds processing capacity and drains when processing clears ahead. A growing backlog is not only a latency problem — it is a diagnostic signal that the inflow-outflow balance has been disrupted. Clearing a backlog requires running processing above its normal rate, which typically requires capacity investment: more compute, more parallel workers, more pipeline stages. The delay between the backlog accumulating and the capacity investment becoming operational is the same construction lag that appears in Chapter 5. Housing supply cannot expand instantly. Processing capacity cannot expand instantly. The backlog persists during the delay. The longer the delay, the larger the backlog grows before the corrective capacity comes online.

Data quality does not remain constant over time. It deteriorates. Schema evolution in upstream systems introduces fields that parsers do not handle. Source systems change their encoding conventions without notifying downstream consumers. Sensor calibration coefficients drift as instruments age. Labels applied by human annotators two years ago no longer reflect current category definitions. Each of these is a flow draining the data quality stock. The balancing feedback that maintains quality is monitoring: automated checks detect quality failures, which trigger remediation, which restores quality. If monitoring is insufficient — too infrequent, too narrow in scope, too slow to produce an alert — the balancing loop is starved. Quality declines. The decline may be invisible for months because the degradation is gradual and no single failure is large enough to trigger an alert. By the time quality has fallen enough to be visible in downstream outputs, it has been deteriorating for an extended period.

The response timescale of a data quality issue depends on which stock is affected and how the failure mode propagates. A schema change that breaks a downstream parser fails immediately and visibly — the pipeline errors, the monitoring fires, the on-call engineer is paged within minutes. A gradual shift in a sensor's calibration coefficient may not be detectable from any single record. It only appears as a statistical shift across thousands of records compared against an external reference. The same mismatch between fast inflows and slow detection that produces urban housing cycles produces data quality debt: by the time the problem is large enough to detect, it has been accumulating for months. The remediation cost at that point is larger than it would have been with earlier detection — exactly the committed damage structure from Chapter 4.

**Earth domain: The GRACE data gap as feedback starvation**

The GRACE satellite measured terrestrial water storage and ice mass through gravity anomalies. It was decommissioned in October 2017. Its replacement, GRACE-FO, launched in May 2018. The 11-month gap between them severed the feedback loop between observed ice mass change and Earth system models that used GRACE data as a forcing or validation input. Models continued running during the gap. Their outputs drifted from the true system state at a rate proportional to the unobserved change in Greenland and Antarctic mass balance. The gap is the data engineering version of committed warming from Chapter 4: future model error was locked in during the period when the feedback loop was severed, regardless of what happened after GRACE-FO data became available. The backlog of unobserved Earth system state cannot be recovered retrospectively. The stock evolved; the observation did not.

**Data domain: A production ML pipeline as a multi-stock system**

A production ML pipeline contains three primary stocks: raw features (upstream data, continuously generated), trained model weights (updated on a schedule), and model performance metrics (measured continuously against held-out data or live outcomes). Three flows connect them: feature ingestion fills the raw features stock, training runs consume raw features and update model weights, and performance evaluation measures the gap between model state and current world state. The delays between these flows determine the system's response time to concept drift. A model retrained monthly will lag a world that changes weekly by a gap that grows throughout each retraining interval. The delay structure of the pipeline determines the worst-case accuracy degradation that can accumulate before the next corrective action.

The stock-flow structure here is diagnostic. When model accuracy falls, the question is not "what is wrong with the model?" The question is: "which stock has deteriorated, which flow is insufficient, and what delay is preventing the corrective loop from operating at the required frequency?"

The following diagram shows the stock-flow structure of a production data pipeline: the raw data stock, the processing capacity stock, the backlog stock, and the data quality stock, with all inflows, outflows, and the monitoring balancing loop.

[DIAGRAM 6.1 GOES HERE]

::: {.callout-note}
## Pipeline architecture and data quality monitoring

The stock-flow structure described here — raw data, processing capacity, backlog, data quality — has a direct engineering counterpart in production data systems. Schema validation, data lineage tracking, anomaly detection on feature distributions, and SLA monitoring are the engineering instruments that keep the balancing loops operational.

[WH Data Engineering Ch 3 (Pipelines and ETL) and Ch 7 (Governance)](https://wayward.house/learn/data-engineering/) covers the specific tools and architectural patterns — dbt, Great Expectations, Apache Airflow — that implement these monitoring loops. This chapter provides the systems thinking framework; Data Engineering provides the implementation.
:::

---
### FRAGMENT 3 — Feedback loops in machine learning
---

## Feedback loops in machine learning

A deployed model is not an isolated system. It acts in the world. Its actions change the world. The changed world generates new data. The new data becomes the training signal for the next model iteration. This chain is a feedback loop, and its properties — reinforcing or balancing, fast or slow, stable or oscillating — determine the long-run behaviour of the model as much as its architecture or training procedure.

Three loop types appear consistently in production ML systems.

**Loop 1: The retraining balancing loop (the intended design).** The intended architecture of a production ML system is a balancing loop. The model makes predictions. Some fraction of those predictions can be verified against observed outcomes. The gap between predicted and observed — the error — drives retraining. Retraining reduces error. A smaller error generates less retraining signal. The loop seeks a goal state: minimum prediction error on the current data distribution.

This is a goal-seeking feedback structure — identical to the thermostat from Chapter 2. The goal is zero prediction error on the current distribution. The corrective action is retraining. The delays are labelling latency (how long before outcomes can be observed and labelled), retraining cost (compute and time required to retrain), and deployment cycle (time between a retrained model being ready and its deployment in production). Long delays in this loop produce the same oscillation and lag that delays produce in any balancing system. The model that was optimal at training time arrives in production weeks or months later into a world that has continued to change during the delay.

**Loop 2: Reinforcing degradation through distribution shift.** When the retraining balancing loop is too slow — when concept drift accumulates faster than retraining clears it — a secondary reinforcing loop can activate. Model accuracy falls. Users begin to distrust or ignore model outputs. Feedback from users (clicks, corrections, explicit labels) declines in volume or quality. The training signal weakens. Less retraining signal means less effective retraining. Less effective retraining means accuracy continues to fall. The loop is reinforcing in the downward direction: accuracy decline → weaker feedback → less retraining → further accuracy decline.

This is the Detroit inversion from Chapter 5 applied to ML systems. The same mechanism that produces urban disinvestment cascades produces model degradation cascades. The feedback starvation that allows this loop to activate is structural: if the monitoring and retraining infrastructure is not built, the balancing loop does not exist, and the reinforcing loop operates unchecked.

**Loop 3: The filter bubble — reinforcing constriction.** In recommendation systems, the deployed model produces training data for its own successor. The model recommends content. Users engage with the recommended content. The engagement record becomes training data labelled as "relevant." The next model iteration learns that what was recommended was relevant — because relevance was measured by engagement with recommendations, not by independent assessment of the content space. The loop: model recommends narrowly → users engage with narrow content → narrow engagement record → next model trained to recommend narrowly. The distribution of recommended content constricts over time, not because users prefer narrower content, but because the feedback loop measures engagement with what was shown, not preferences across what was not shown.

**Human domain: Credit scoring during COVID-19**

Credit scoring models trained on pre-2020 repayment behaviour were built on the assumption that the economic conditions generating repayment signals would remain approximately stable. COVID-19 violated that assumption instantaneously. Unemployment rates spiked. Government transfer payments replaced earned income. Loan forbearance programmes suspended normal repayment signals. The features that predicted default in the training data — missed payments, income instability — were being triggered by a government policy response rather than by creditworthiness in the traditional sense. Banks that continued using pre-pandemic models for credit decisions were running the spam filter scenario at enormous scale: the world had changed, the models had not, and the gap between the two was growing.

**Earth domain: Land cover classifier drift**

A Landsat-based land cover classifier trained on data from 2000–2010 will misclassify shrub expansion into tundra as warming drives it northward in the 2020s. The spectral signatures of shrub-covered tundra and grass-covered tundra were distinguishable in the training period. The proportions of those classes at high latitudes were approximately stable. By 2025, the Arctic is measurably different from what the model was trained on. The classifier's confusion matrix for Arctic pixels has drifted. The model is not wrong about the 2000–2010 Arctic. It is wrong about the 2025 Arctic, and the drift is accelerating.

The following diagram shows the retraining balancing loop: model weights, prediction error, labelling flow, and the delays that determine loop response time.

[DIAGRAM 6.2 GOES HERE]

The following diagram shows the reinforcing degradation loop: how accuracy decline starves feedback and amplifies further decline.

[DIAGRAM 6.3 GOES HERE]

The following diagram shows the filter bubble loop: how recommendation outputs become training inputs, producing progressive content concentration.

[DIAGRAM 6.4 GOES HERE]

---
### FRAGMENT 4 — Loss landscapes as energy landscapes
---

## Loss landscapes as energy landscapes

Gradient descent is a feedback loop. The model makes predictions. The predictions are compared to labels. The discrepancy is the loss. The gradient of the loss with respect to the model parameters points in the direction of increasing loss. The update rule moves the parameters in the opposite direction. The loop: high loss → gradient signal → parameter update → reduced loss. This is a balancing loop: the loss is the discrepancy from the goal state of zero error, and the gradient is the corrective action.

The loss landscape is the energy landscape of this feedback system. A convex loss landscape has a single basin — one attractor. The balancing loop reliably converges to the global minimum regardless of starting point. A non-convex loss landscape has multiple basins — multiple local minima. The balancing loop converges to whichever minimum is nearest to the starting point. The model that gradient descent finds is determined not only by the data but by the initialisation and the path taken through parameter space. This is path dependence in loss space: the same mechanism that determines which city wins in the two-city simulation from Chapter 5. The attractor the system reaches depends on where it started, not just on the shape of the landscape.

The learning rate is the parameter that controls the strength of the corrective action. Too low: convergence is slow, and the model may stop improving before reaching the minimum, stalling in a flat region. Too high: the update overshoots the minimum, and the model oscillates or diverges. This is the same delay-and-gain trade-off that governs any balancing feedback system. The right learning rate is the one that produces goal-seeking convergence without overshoot — the same design criterion as a well-tuned thermostat or a well-calibrated policy response in any stock-flow system. The analogy is exact: gain too high in a balancing loop produces oscillation; gain too low produces sluggish under-response. Learning rate is the gain of the gradient descent feedback loop.

::: {.callout-note}
## Gradient descent as a dynamical system

The connection between gradient descent and dynamical systems is exact, not metaphorical. Gradient flow — the continuous-time limit of gradient descent — is a differential equation of the form dx/dt = −∇L(x), where L is the loss function. The fixed points of this equation are the critical points of the loss: minima, maxima, and saddle points. Stability of a critical point is determined by the eigenvalues of the Hessian at that point — exactly the linear stability analysis from the climate sensitivity section of Chapter 4.

[WH Maths Vol 8, Ch 1 (Control, Feedback, Stability)](https://wayward.house/learn/maths/advanced/) develops the connection between gradient flow and control theory: the loss landscape is the Lyapunov function, and convergence is guaranteed when the loss is strongly convex. Non-convex landscapes — the norm in deep learning — are where the analogy with tipping points from Chapter 3 becomes relevant.
:::

---
### FRAGMENT 5 — Concept drift — the balancing loop severed
---

## Concept drift — the balancing loop severed

Concept drift is the structural condition where the statistical distribution the model was trained on diverges from the distribution on which it is being evaluated. Three mechanisms produce it.

**Data drift** — the input distribution changes. The kinds of inputs arriving at the model change in frequency or character: different spam vocabulary, different user demographics, different sensor reading ranges as climate changes. The model has not changed. The world feeding it has.

**Label drift** — the mapping from inputs to outputs changes. The same input now corresponds to a different correct label: a phrase that was not spam in 2022 is spam in 2024 because its use has been adopted by spammers. The feature space is the same. The target function has moved.

**Prior drift** — the base rate of the target variable changes. Fraud was 0.1% of transactions in 2019; it was 0.4% of transactions in 2021 because the COVID-19 period enabled new fraud vectors. A model calibrated to a 0.1% prior is miscalibrated. Its decision threshold, set to be optimal at the training-time prior, generates too many false negatives at the current prior.

All three produce the same system-level symptom: the balancing retraining loop, which should keep model accuracy near its goal state, is operating against a shifting target. If the target moves faster than the loop can follow, accuracy degrades continuously. The severity depends on the ratio of drift rate to retraining frequency — the same ratio of disturbance rate to corrective response rate that determines whether any balancing loop stays near its goal.

The detection problem is as important as the correction problem. Concept drift is often invisible until it has accumulated to a detectable threshold — by which point, the model has been wrong at scale for an extended period. Early detection requires monitoring the input distribution, not only model performance. Tracking feature statistics over time and comparing current data distributions to training distributions places the monitoring upstream of the accuracy degradation in the causal chain. A monitoring system that only measures model accuracy will detect drift late, after the accuracy has already fallen. A monitoring system that measures input distributions will detect drift early — distribution shift precedes accuracy degradation causally, because the distribution must shift before the predictions degrade. The detection delay that separates early from late monitoring is a delay in the balancing loop: shorter delay, faster correction, smaller total accuracy loss.

**Data domain: EO classifier retraining in a changing Arctic**

A cryosphere classification model monitoring permafrost extent from Sentinel-1 SAR data faces accelerating concept drift. The permafrost extent it was trained to classify is shrinking. New terrain types are appearing — thermokarst lakes, subsided tundra, drainage channels — that were rare or absent in the training data. Retraining requires new field validation data from these novel terrain types, which requires field campaigns in remote Arctic locations. The retraining loop is slow: field campaign planning, data collection, model retraining, validation, and deployment takes 18–24 months. The drift rate may be faster. This is a case where the balancing loop — retraining — cannot keep pace with the disturbance rate, and the model's concept of "permafrost" diverges from the current Arctic faster than it can be corrected.

::: {.callout-note}
## Concept drift in Earth observation classifiers

The phenomena described here — Arctic land cover change, permafrost thaw, vegetation encroachment — appear in [WH Computational Geography Parts 2 and 4 (Earth Observation and Hazards)](https://wayward.house/learn/computational-geography/) as classification and change detection problems. The computational geography treatment covers the specific remote sensing techniques for detecting these changes. This chapter explains why classifiers trained on historical data fail to detect them: the training distribution and the current distribution have diverged, and the retraining loop cannot keep pace with the rate of change.
:::

---
### FRAGMENT 6 — Simulation
---

## Simulation: the retraining balancing loop under concept drift

The model below simulates the retraining balancing loop under concept drift. Model accuracy is a stock that drifts downward as the world changes. Retraining raises it — but with a delay, and only to the extent that fresh training data is available. Three scenarios run in parallel: no retraining (accuracy drifts to floor), periodic retraining (accuracy oscillates around a degraded mean), and adaptive retraining triggered by a threshold (accuracy stabilises near the goal). The key result: the adaptive loop outperforms periodic retraining not because it retrains more often on average, but because it retrains at the right time — when the accuracy gap is largest. Periodic retraining that fires on a schedule may retrain when drift is minimal and miss the window when drift is accelerating. Threshold-triggered retraining acts proportionally to the discrepancy, which is the design of any well-functioning balancing feedback loop.

[SIMULATION BLOCK GOES HERE]

---
### FRAGMENT 7 — Exercises
---

## Exercises

**6.1 — Data pipeline stock-flow**

A production data pipeline ingests sensor data at 10,000 records/hour. The processing system has a validated throughput capacity of 8,000 records/hour. Processing takes the raw records through three stages: validation, enrichment, and aggregation.

a. Draw the stock-flow diagram for this pipeline. Identify the backlog stock and all relevant flows. What is the net accumulation rate of the backlog under current conditions?
b. The processing capacity can be doubled by adding parallel processing workers, but requires 6 weeks of infrastructure work to deploy. Sketch the time series of backlog size over the next 6 months under the assumption that the expansion proceeds. What archetype from Chapter 2 describes this trajectory?
c. A naive solution is to lower validation strictness to increase throughput. Which flow does this intervention affect, and what stock does it deteriorate? Why might this intervention make the long-run problem worse even though it solves the short-run backlog?

**6.2 — ML retraining loop**

A fraud detection model is deployed in a payments system. The model produces scores for each transaction. Transactions flagged as high-risk are reviewed by human analysts, who confirm or correct the model's label. Confirmed fraud cases and corrected non-fraud cases become training data for the next model version. The model is retrained every 90 days.

a. Draw the full causal loop diagram for this system. Identify the retraining balancing loop and all delays within it.
b. Fraud tactics evolve on a roughly 30-day cycle: after a new attack pattern is flagged and blocked, fraudsters adapt. What does this imply about the 90-day retraining frequency relative to the drift rate? Describe the expected accuracy trajectory over a 12-month period under current conditions.
c. The fraud operations team proposes reducing the retraining cycle to 30 days. What new risks does this introduce? Identify the specific feedback loops and stocks affected by higher retraining frequency.

**6.3 — Filter bubble loop analysis**

A video recommendation platform trains its model on user engagement data. A user who watches one political commentary video is subsequently shown more videos with similar content. The user's watch history becomes progressively more concentrated in that content category over 6 months.

a. Draw the full causal loop diagram showing how the recommendation loop produces content concentration. Label every link and every loop as R or B.
b. The platform introduces a "diversity injection" mechanism: 10% of recommendations are randomly selected from outside the user's current content cluster. Which link in your diagram does this intervention modify? Is the loop structure R or B after the intervention?
c. Propose a metric that would allow the platform to detect filter bubble formation before users notice it. Describe: (i) what it measures, (ii) how it would change over time in the presence and absence of a filter bubble, and (iii) what threshold would trigger an intervention.

**6.4 — Concept drift detection**

A sentiment analysis model is trained on product reviews from 2019–2021. It is deployed to monitor brand sentiment in 2023.

a. List three specific mechanisms by which concept drift could affect this model between 2021 and 2023. For each, identify whether it is data drift, label drift, or prior drift.
b. The monitoring team measures model accuracy weekly using a sample of human-labelled reviews. Accuracy appears stable for 8 months, then drops 12% in 6 weeks. Propose a causal explanation for this sudden drop that is consistent with gradual concept drift accumulating over 8 months before becoming visible in accuracy metrics.
c. Redesign the monitoring system to detect drift earlier. What additional metrics, beyond model accuracy, would you track? How does each metric connect to the causal chain between world change and model failure?

**6.5 — Loss landscape and learning rate**

A neural network is being trained on a classification task. The loss landscape in the neighbourhood of the current parameters has the following properties: convex in one direction (corresponding to the primary feature) and nearly flat in another direction (corresponding to a feature with low predictive value).

a. Sketch the expected trajectory of gradient descent in this landscape for (i) a learning rate that is too high, (ii) a learning rate that is too low, and (iii) an approximately optimal learning rate. For each, describe the corresponding behaviour of the loss over training iterations.
b. The flat direction of the landscape corresponds to a feature that has low predictive value in the training data but high predictive value for the actual deployment task (a domain shift). How does the gradient descent update rule handle this — and what does this imply about the model's ability to perform well on the deployment task?
c. Connect this scenario to the concept drift framework. The flat landscape direction corresponds to a feature the model has not learned. When the deployment distribution shifts to make that feature important, what happens to the accuracy trajectory? What would retraining on the new distribution require?

**6.6 — System design for resilience**

You are designing the monitoring and retraining infrastructure for a land cover classification model deployed in a wildfire risk assessment system in western Canada. The model classifies vegetation type from Sentinel-2 imagery. Wildfire risk scores for specific locations are downstream outputs.

a. Identify three feedback loops that this system depends on to remain accurate over time. For each loop, identify: the stock being maintained, the corrective flow, and the delay.
b. Identify the most critical single point of feedback starvation in this system — the severing of which loop would most rapidly degrade the risk assessment outputs. Justify your choice.
c. Design a monitoring protocol that would detect feedback starvation in your identified critical loop before it causes visible accuracy degradation. Specify: monitoring frequency, the specific distribution or metric being tracked, the threshold for escalation, and the escalation action.
d. In 2024, the Canadian Forest Service substantially changes its vegetation classification schema to include additional shrub subcategories. Identify which type of concept drift this represents and describe the expected impact on the wildfire risk model's outputs if no retraining occurs within 12 months.
