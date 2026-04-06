---
### DIAGRAM 1 — Generic tipping point structure (Figure 3.1)
---

```{mermaid}
graph LR
    SS["System State"]  -->|"+"| BF["Balancing\nFeedback\nStrength"]
    BF                  -->|"− [B]"| SS
    EX["External\nStress"] -->|"−"| BF
    EX                  -->|"+"| RF["Reinforcing\nFeedback\nStrength"]
    RF                  -->|"+ [R]"| SS

    style SS fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style BF fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style RF fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style EX fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
```

> Figure 3.1. Generic tipping point structure. Two feedback loops operate on the same stock (System State): a balancing loop (B) that stabilises the current state, and a reinforcing loop (R) that amplifies departures from it. External stress weakens the balancing feedback and strengthens the reinforcing one. Before the threshold, B dominates; past it, R dominates. The transition is a switch in which loop governs behaviour, not a gradual change.

---
### DIAGRAM 2 — Coral reef regime shift (Figure 3.2)
---

```{mermaid}
graph LR
    CC["Coral Cover"]   -->|"+"| GR["Grazing Rate"]
    GR                  -->|"−"| AC["Algae Cover"]
    AC                  -->|"− [R1]"| CC
    AC                  -->|"+"| BS["Bleaching /\nSmothering"]
    BS                  -->|"− [R2]"| CC
    WS["Warming /\nNutrient Stress"] -->|"+"| BS

    style CC fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style GR fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style AC fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style BS fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style WS fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 3.2. Coral reef regime shift: two competing reinforcing loops sharing the Coral Cover stock. Loop R1 (upper path): high coral cover supports grazing that suppresses algae, protecting coral — a self-sustaining healthy state. Loop R2 (lower path): algae proliferation causes bleaching and smothering that reduces coral cover, which reduces competition against algae — a self-sustaining degraded state. Warming and nutrient stress (left) tips the system from R1 dominance into R2 dominance. The reef does not oscillate between these states — it shifts.

---
### DIAGRAM 3 — Schelling move-decision loop (Figure 3.3)
---

```{mermaid}
graph LR
    SEG["Segregation\n(Fraction\nSame-Type)"] -->|"+"| SAT["Individual\nSatisfaction"]
    SAT                                        -->|"−"| MV["Move Rate"]
    MV                                         -->|"+ [B]"| SEG

    style SEG fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style SAT fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style MV  fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 3.3. Schelling move-decision feedback loop. High local segregation raises individual satisfaction (+), which reduces the rate of moves away from the neighbourhood (−), which maintains or increases local same-type fractions (+). The loop is balancing — it drives the system toward a stable equilibrium. That equilibrium is near-total segregation: not because anyone chose it, but because mild individual preferences are sufficient to tip the system to the segregated stable state.
