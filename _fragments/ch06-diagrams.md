---
### DIAGRAM 1 — Data pipeline as a stock-flow system (Figure 6.1)
---

```{mermaid}
flowchart LR
    DS(["Data Sources"])
    CD(["Consumed Data"])

    RDB[["Raw Data\nBacklog"]]
    PDS[["Processed\nData Stock"]]
    DQS[["Data Quality\nScore"]]

    DS  -->|"ingest rate\n(continuous)"| RDB
    RDB -->|"processing rate\n(capacity-limited)"| PDS
    PDS -->|"consumption"| CD
    RDB -->|"data issues"| DQS
    PDS -->|"monitoring +\nvalidation"| DQS

    style RDB fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style PDS fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style DQS fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style DS  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style CD  fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 6.1. Data pipeline as a stock-flow system. The raw data backlog accumulates when ingest rate exceeds processing capacity — the same asymmetric inflow/outflow structure as urban housing shortage. Data quality is a separate stock maintained by the balancing feedback of monitoring and validation; without active monitoring, quality decays through schema drift and sensor calibration errors. The three stocks have different response timescales: backlog responds to throughput changes in hours; processed data stock responds in days; data quality degradation may be invisible for months.

---
### DIAGRAM 2 — ML retraining balancing loop (Figure 6.2)
---

```{mermaid}
graph LR
    MA["Model\nAccuracy"]
    PE["Prediction\nError"]
    RS["Retraining\nSignal"]
    LL["Labelling\nLatency"]
    TR["Training\nRun"]
    MW["Model\nWeights"]
    CD["Concept\nDrift"]

    MA -->|"−"| PE
    PE -->|"+"| RS
    RS -->|"+"| LL
    LL -->|"+"| TR
    TR -->|"+"| MW
    MW -->|"+ [B]"| MA
    CD -->|"−"| MA

    style MA fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style PE fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style RS fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style LL fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style TR fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style MW fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style CD fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 6.2. ML retraining as a balancing feedback loop. Prediction error drives a retraining signal, which (after labelling latency and training cost delays) updates model weights and reduces error. Concept drift is the external stress that continuously pushes accuracy downward, competing against the corrective retraining flow. The loop's ability to maintain accuracy depends on whether the retraining rate exceeds the drift rate — a direct application of the disturbance-vs-correction rate comparison from Chapter 2.

---
### DIAGRAM 3 — Concept drift reinforcing degradation loop (Figure 6.3)
---

```{mermaid}
graph LR
    MA["Model\nAccuracy"]
    UT["User\nTrust"]
    UFV["User\nFeedback\nVolume"]
    TDQ["Training\nData\nQuality"]
    RE["Retraining\nEffectiveness"]
    CD["Concept\nDrift"]

    MA  -->|"+"| UT
    UT  -->|"+"| UFV
    UFV -->|"+"| TDQ
    TDQ -->|"+"| RE
    RE  -->|"+ [R]"| MA
    CD  -->|"−"| MA

    style MA  fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style UT  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style UFV fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style TDQ fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style RE  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style CD  fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 6.3. Concept drift reinforcing degradation loop. When accuracy falls, users trust the model less and provide less feedback. Less feedback degrades training data quality. Poorer training data reduces the effectiveness of each retraining cycle. Lower retraining effectiveness allows accuracy to fall further. Zero − signs in the main loop → reinforcing (R). This is the Detroit inversion from Chapter 5 applied to ML systems: the same mechanism that makes a platform valuable when accuracy is high makes it collapse rapidly when accuracy falls past a threshold.

---
### DIAGRAM 4 — Filter bubble reinforcing loop (Figure 6.4)
---

```{mermaid}
graph LR
    RN["Recommendation\nNarrowness"]
    UE["User Engagement\nWith Narrow\nContent"]
    TSN["Training Signal\nNarrowness"]
    MCB["Model\nContent Bias"]
    UPD["User Preference\nDiversity"]

    RN  -->|"+"| UE
    UE  -->|"+"| TSN
    TSN -->|"+"| MCB
    MCB -->|"+ [R]"| RN
    UPD -->|"−"| RN

    style RN  fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style UE  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style TSN fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style MCB fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style UPD fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 6.4. Filter bubble reinforcing loop. Recommendations narrow user engagement, which narrows training signals, which increases model content bias, which narrows recommendations further. Zero − signs in the main loop → reinforcing (R). The critical structural flaw: user preference diversity (what users would prefer if shown a wider selection) is not in the feedback loop — it is measured only indirectly through engagement with what was already recommended. The loop amplifies its own training signal rather than learning from the full preference distribution.
