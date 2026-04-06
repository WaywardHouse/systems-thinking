---
### DIAGRAM 1 — City as a stock-flow system (Figure 5.1)
---

```{mermaid}
flowchart LR
    MP(["Migration Pool"])
    CI(["Construction Industry"])
    INV(["Investment"])
    DC(["Destination Cities"])
    RS(["Removed Stock"])
    DC2(["Depreciated Capital"])

    CP[["City Population"]]
    HS[["Housing Stock"]]
    EO[["Economic Output"]]

    MP  -->|"in-migration"| CP
    CP  -->|"out-migration"| DC
    CI  -->|"new construction"| HS
    HS  -->|"demolition +\ndepreciation"| RS
    INV -->|"capital inflow"| EO
    EO  -->|"depreciation"| DC2
    CP  -->|"labour supply"| EO
    EO  -->|"wages +\namenities"| CP
    HS  -->|"housing cost"| CP

    style CP  fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style HS  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style EO  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style MP  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style CI  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style INV fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style DC  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style RS  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style DC2 fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 5.1. City as a coupled stock-flow system. Three primary stocks — population, housing, and economic output — are connected by flows with different response timescales. Population responds to wage and cost signals on years timescales; housing responds to population pressure with a 2–5 year construction delay; economic output responds to labour supply and investment. The delays between stocks produce the boom-bust cycles characteristic of urban housing markets.

---
### DIAGRAM 2 — Agglomeration reinforcing loop (Figure 5.2)
---

```{mermaid}
graph LR
    CS["City Size"]
    LMT["Labour Market\nThickness"]
    WFM["Worker-Firm\nMatch Quality"]
    PR["Productivity"]
    WG["Wages"]
    IM["In-Migration"]

    CS  -->|"+"| LMT
    LMT -->|"+"| WFM
    WFM -->|"+"| PR
    PR  -->|"+"| WG
    WG  -->|"+"| IM
    IM  -->|"+ [R]"| CS

    style CS  fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style LMT fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style WFM fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style PR  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style WG  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style IM  fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 5.2. Agglomeration reinforcing loop. A larger city supports a thicker labour market, improving worker-firm matching, raising productivity and wages, attracting further in-migration. Zero − signs → reinforcing (R). The loop has no internal correction. It is limited only by the congestion balancing feedback (Figure 5.3).

---
### DIAGRAM 3 — Congestion balancing loop (Figure 5.3)
---

```{mermaid}
graph LR
    CS["City Size"]
    HC["Housing\nCosts"]
    CL["Cost of\nLiving"]
    NA["Net\nAttractiveness"]
    IM["In-Migration"]

    CS -->|"+"| HC
    HC -->|"+"| CL
    CL -->|"−"| NA
    NA -->|"− [B]"| IM
    IM -->|"+"| CS

    style CS fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style HC fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style CL fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style NA fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style IM fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 5.3. Congestion balancing loop. City growth raises housing costs and cost of living, reducing net attractiveness for marginal residents and firms, slowing in-migration. Two − signs → balancing (B). This loop sets an upper limit on city growth, producing an equilibrium size where agglomeration benefits exactly offset congestion costs for the marginal resident.

---
### DIAGRAM 4 — Dutch Disease and oil sector lock-in (Figure 5.4)
---

```{mermaid}
graph LR
    OSS["Oil Sector\nScale"]
    PSC["Provincial\nSkills +\nSupply Chain"]
    OSP["Oil Sector\nProductivity"]
    OSW["Oil Sector\nWages"]
    LFO["Labour Flow\nto Oil Sector"]
    OER["Oil Export\nRevenue"]
    ER["Exchange\nRate"]
    MC["Manufacturing\nCompetitiveness"]
    ME["Manufacturing\nEmployment"]

    OSS -->|"+"| PSC
    PSC -->|"+"| OSP
    OSP -->|"+"| OSW
    OSW -->|"+"| LFO
    LFO -->|"+ [R]"| OSS

    OSS -->|"+"| OER
    OER -->|"+"| ER
    ER  -->|"−"| MC
    MC  -->|"−"| ME

    style OSS fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style PSC fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style OSP fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style OSW fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style LFO fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style OER fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style ER  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style MC  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style ME  fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 5.4. Oil sector lock-in and Dutch Disease. The oil sector maintains a self-reinforcing agglomeration loop (R): sector scale builds skills and supply chain depth, raising productivity and wages, drawing further labour into the sector. The Dutch Disease mechanism operates in parallel: oil export revenues raise the exchange rate, reducing manufacturing competitiveness and employment. Both mechanisms concentrate economic activity in the resource sector — the first through positive feedback, the second through competitive displacement.
