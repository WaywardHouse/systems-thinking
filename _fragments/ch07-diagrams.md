---
### DIAGRAM 1 — The modelling workflow (Figure 7.1)
---

```{mermaid}
flowchart LR
    VM["Verbal\nModel"]
    CLD["Causal Loop\nDiagram"]
    SFE["Stock-Flow\nEquations"]
    SIM["Simulation"]
    MO["Model\nOutput"]
    VT["Validation\n& Testing"]
    RWD["Real World\nData"]

    VM  --> CLD
    CLD --> SFE
    SFE --> SIM
    SIM --> MO
    MO  --> VT
    VT  -->|"revise\nstructure"| CLD
    VT  -->|"revise\nparameters"| SFE
    RWD -->|"compare"| VT

    style VT  fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style VM  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style CLD fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style SFE fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style SIM fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style MO  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style RWD fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 7.1. The modelling workflow as a feedback process. Building a model is not a linear sequence ending at simulation output — it is a balancing loop where validation drives revision of model structure and parameters. Structural revision (changing which variables and loops are included) is higher-leverage than parameter revision (changing numerical values within a fixed structure). Real-world data enters only at the validation step; the model structure is derived from mechanistic knowledge, not from fitting the data.

---
### DIAGRAM 2 — Predator-prey causal loop diagram (Figure 7.2)
---

```{mermaid}
graph LR
    PP["Prey\nPopulation"]
    PBR["Prey\nBirth Rate"]
    PR["Predation\nRate"]
    PDR["Predator\nPopulation"]
    PM["Predator\nMortality"]

    PP  -->|"+"| PBR
    PBR -->|"+ [R]"| PP
    PP  -->|"+"| PR
    PR  -->|"+"| PDR
    PDR -->|"− [B]"| PP
    PDR -->|"+"| PM
    PM  -->|"−"| PDR

    style PP  fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style PBR fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style PR  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style PDR fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style PM  fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 7.2. Predator-prey causal loop diagram. The prey population drives a self-reinforcing growth loop (R): more prey → higher birth rate → more prey. Predation creates a balancing loop (B): more prey → higher predation → more predators → fewer prey. The two loops operating simultaneously produce oscillation — the reinforcing loop drives prey up, the balancing loop follows with a lag, drives prey down, the reinforcing loop rebuilds. The period of oscillation is determined by the parameter values; the oscillatory behaviour is determined by the loop structure.

---
### DIAGRAM 3 — Model validation as a balancing feedback loop (Figure 7.3)
---

```{mermaid}
graph LR
    MS["Model\nStructure"]
    MO["Model\nOutput"]
    OB["Observed\nBehaviour"]
    SG["Structural\nGap"]
    MR["Model\nRevision"]
    ND["New\nData"]

    MS  -->|"+"| MO
    MO  -->|"+"| SG
    OB  -->|"−"| SG
    SG  -->|"+"| MR
    MR  -->|"− [B]"| MS
    ND  -->|"updates"| OB

    style SG  fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style MS  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style MO  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style OB  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style MR  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style ND  fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 7.3. Model validation as a balancing feedback loop. The gap between model output and observed behaviour drives model revision, which changes model structure, which closes the gap. This is the same goal-seeking structure as any balancing loop: the goal is zero structural gap (perfect fit), the corrective action is revision, and the delay is the time required to understand the source of discrepancy and implement a structural change. Note that parameter calibration and structural revision are different interventions: parameter calibration can reduce quantitative gap without changing qualitative behaviour; structural revision changes which behaviours are possible.

---
### DIAGRAM 4 — Stock-flow structure of the predator-prey model (Figure 7.4)
---

```{mermaid}
flowchart LR
    B(["Births"])
    PD(["Prey\nDeaths"])
    PDeath(["Predator\nDeaths"])

    PP[["Prey\nPopulation"]]
    PDR[["Predator\nPopulation"]]

    B    -->|"r × prey"| PP
    PP   -->|"a × prey × predator\n(predation)"| PD
    PP   -->|"b × prey × predator\n(conversion)"| PDR
    PDR  -->|"d × predator\n(mortality)"| PDeath
    PDR  -.->|"sets predation rate"| PP

    style PP     fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style PDR    fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style B      fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style PD     fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style PDeath fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 7.4. Predator-prey stock-flow diagram. Two coupled stocks — prey and predator populations — connected by flows that are functions of both stocks simultaneously. The predation term (a × prey × predator) is a bilinear coupling: it appears in both the prey outflow and the predator inflow. This coupling is what makes the Lotka-Volterra system nonlinear and produces the cyclic behaviour. A model with only linear flows (growth proportional to the single stock only) could not produce sustained oscillation.
