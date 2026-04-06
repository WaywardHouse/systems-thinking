---
### DIAGRAM 1 — replaces ASCII placeholder in "Drawing the system" section
---

```{mermaid}
flowchart LR
    P([Precipitation\ninflow]) -->|accumulation\nkm³/yr| V1{Accumulation\nvalve}
    V1 --> S[[Ice Mass\nkm³]]
    S --> V2{Ablation\nvalve}
    V2 -->|melt + calving\nkm³/yr| A([Ablation\noutflow])
    T(Temperature) -.->|raises rate| V2
    ELA(ELA elevation) -.->|lowers rate| V1

    style S fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style V1 fill:#ffffff,stroke:#888888
    style V2 fill:#ffffff,stroke:#888888
    style T fill:#fff3f3,stroke:#d52a2a
    style ELA fill:#fff3f3,stroke:#d52a2a
```

> Figure 1.1. Glacier ice mass as a stock-flow system. Rectangles are stocks (accumulations). Diamonds are valves (flow regulators). Rounded rectangles are auxiliaries (variables that control flow rates). Dashed arrows carry information; solid arrows carry material flows. Temperature acts only through information — it does not flow into the glacier; it changes the rate at which ice leaves it.

---
### DIAGRAM 2 — insert after Exercise 1.3 text
---

::: {layout-ncol=2}

```{mermaid}
flowchart LR
    C([Construction\ncompletions]) --> V1{Build\nvalve}
    V1 --> S[[Dwelling\nUnits]]
    S --> V2{Loss\nvalve}
    V2 --> D([Demolitions +\nconversions])
    P(Permits\nissued) -.-> V1

    style S fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style V1 fill:#ffffff,stroke:#888888
    style V2 fill:#ffffff,stroke:#888888
    style P fill:#fff3f3,stroke:#d52a2a
```

Narrow boundary: supply side only.

```{mermaid}
flowchart LR
    C([Construction\ncompletions]) --> V1{Build\nvalve}
    V1 --> S[[Dwelling\nUnits]]
    S --> V2{Loss\nvalve}
    V2 --> D([Demolitions +\nconversions])
    P(Permits\nissued) -.-> V1
    POP(Population\npressure) -.->|raises demand| V1
    PR(Rental\nprice) -.->|signals shortage| V1
    S -.->|vacancy rate\nreduces pressure| POP

    style S fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style V1 fill:#ffffff,stroke:#888888
    style V2 fill:#ffffff,stroke:#888888
    style P fill:#fff3f3,stroke:#d52a2a
    style POP fill:#fff3f3,stroke:#d52a2a
    style PR fill:#fff3f3,stroke:#d52a2a
```

Wide boundary: demand-side flows and feedback included. The arrow from dwelling units back to population pressure is a balancing feedback loop — a structure we will examine formally in Chapter 2.

:::

> Figure 1.2. The same housing stock drawn with two different boundaries. The narrow model (left) shows only supply-side flows. The wide model (right) adds demand pressure and price signalling. The loop from stock back to population pressure — absent in the narrow model — is what drives the overshoot-and-collapse behaviour described in section 3.2.

---
### DIAGRAM 3 — Figure 1.3 caption block (the figure itself is produced by simulation code)
---

> Figure 1.3. Ice mass over 120 years under three constant-flow scenarios. In all three cases the stock changes at a constant rate — the curve is a straight line. The behaviour diverges completely depending on whether inflow exceeds, equals, or falls short of outflow. This is the simplest demonstration of what a stock does: it accumulates the difference between flows, and its trajectory is determined entirely by that difference over time.
