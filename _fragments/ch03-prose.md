---
### FRAGMENT 1 — Emergence vs. complexity (insert at end of ## Emergence)
---

A jumbo jet is complicated. It has hundreds of thousands of components in precisely engineered relationships. Its behaviour is derivable from its design. A city, an ecosystem, a training pipeline is complex: components interact adaptively, system state is history-dependent, and behaviour cannot be derived by inspecting any component in isolation. Complicated systems can be understood by decomposition. Complex systems cannot.

Emergence is what complex systems produce: system-level properties absent from any component. Emergence is the phenomenon; complexity is the structural condition that generates it.

The engineering implication is direct. Optimising components does not prevent emergent failures. Failures in complex systems are typically failures of the interaction structure — the feedback loops, delays, and adaptive responses between components — not failures of the components themselves.

---
### FRAGMENT 2 — Data/AI resilience (insert at end of ## Resilience...)
---

A deployed ML system can appear resistant while its resilience erodes. Accuracy on a fixed test set stays flat — the system looks stable. But resilience here means the capacity of the monitoring-and-retraining feedback loop to restore performance after a perturbation: a distribution shift, an upstream schema change, a data quality degradation. A system with an active retraining cadence, fresh data pipelines, and broad monitoring coverage has high resilience. A system whose monitoring scope has been cut, whose retraining schedule has stretched, or whose feedback loop has been severed by a data governance boundary appears stable until a threshold is crossed — then error rate spikes without warning. The external stability masked internal fragility: the corrective loop was present in principle but not operating in practice. Exercise 3.4 asks you to map this structure as a causal loop diagram and identify where the feedback starvation occurs.

---
### FRAGMENT 3 — Simulation bridge (insert as opening of ## Simulating segregation)
---

Exercise 3.2 asks you to implement the Schelling model; the code below is one version. Run it before reading the interpretation. The three threshold scenarios use the same grid size and differ only in T — and that difference is enough to produce macro-level outcomes that prose describing them does not adequately convey.

---
### FRAGMENT 4 — Bridge sentences for Mermaid diagrams
---

**Bridge A (before Diagram 3.1 — generic tipping point):**
Two feedback loops share a stock — one balancing, one reinforcing — and external stress determines which loop dominates, producing two stable regimes separated by an unstable threshold.

**Bridge B (before Diagram 3.2 — coral reef):**
Two competing reinforcing loops operate on the Coral Cover stock: one sustains the healthy high-coral state, the other sustains the degraded algae-dominated state, and which loop runs depends on which side of the threshold the system sits.

**Bridge C (before Diagram 3.3 — Schelling loop):**
A reinforcing loop connects individual satisfaction to neighbourhood composition: as composition shifts, the fraction of satisfied residents changes, which drives further departure or arrival, which shifts composition further.
