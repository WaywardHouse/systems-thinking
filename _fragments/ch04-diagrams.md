---
### DIAGRAM 1 — Earth system subsystems (Figure 4.1)
---

```{mermaid}
flowchart LR
    ATM[["Atmosphere\n(GHG, heat)"]]
    OCN[["Ocean\n(heat, carbon)"]]
    CRY[["Cryosphere\n(ice, permafrost C)"]]
    BIO[["Biosphere\n(biomass, soil C)"]]
    LIT[["Lithosphere\n(rock C)"]]

    ATM -->|"CO₂ uptake\n~90 GtC/yr"| OCN
    OCN -->|"outgassing\n~90 GtC/yr"| ATM
    ATM -->|"precipitation"| CRY
    CRY -->|"meltwater,\nalbedo change"| ATM
    ATM -->|"photosynthesis\n~120 GtC/yr"| BIO
    BIO -->|"respiration +\ndecomp ~120 GtC/yr"| ATM
    LIT -->|"weathering +\nvolcanism ~0.3 GtC/yr"| ATM

    style ATM fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style OCN fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style CRY fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style BIO fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style LIT fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 4.1. Earth's five major subsystems as interacting stocks. Double-border rectangles represent stocks; arrows represent material or energy flows. The atmosphere is the central coupling medium — most cross-system flows pass through it or are driven by it. Each stock has a characteristic response time: the atmosphere on years to decades; the deep ocean on centuries to millennia; the lithosphere on millions of years. These mismatched timescales produce the long delays that characterise Earth system behaviour.

---
### DIAGRAM 2 — 3-box carbon cycle (Figure 4.2)
---

```{mermaid}
flowchart LR
    EM(["Fossil fuel\nemissions\n~10 GtC/yr"])
    ATM[["Atmosphere\n590 GtC\n(pre-industrial)"]]
    OCN[["Ocean\n38,000 GtC"]]
    LND[["Land Biosphere\n2,150 GtC"]]
    WTH(["Weathering +\nvolcanism\n~0.2 GtC/yr"])

    EM -->|"E(t)"| ATM
    WTH -->|"background"| ATM
    ATM -->|"uptake\n~90 GtC/yr"| OCN
    OCN -->|"outgassing\n~90 GtC/yr"| ATM
    ATM -->|"photosynthesis\n~120 GtC/yr"| LND
    LND -->|"respiration +\ndecomp\n~120 GtC/yr"| ATM

    style EM  fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style ATM fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style OCN fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style LND fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style WTH fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 4.2. The 3-box carbon cycle. Double-border rectangles are stocks; rounded rectangles are external sources. Pre-industrial: gross atmosphere-ocean and atmosphere-land flows are nearly equal, and the atmospheric stock is stable at ~280 ppm. Perturbation: anthropogenic emissions add ~10 GtC/yr to the atmosphere — a new inflow with no natural outflow at that rate. Ocean and land uptake absorb roughly half; the remainder accumulates in the atmosphere. The atmospheric stock has risen from 590 GtC (~280 ppm) to ~870 GtC (~420 ppm) as a result.

---
### DIAGRAM 3 — Water vapour reinforcing loop (Figure 4.3)
---

```{mermaid}
graph LR
    ST["Surface\nTemperature"]          -->|"+"| WV["Atmospheric\nWater Vapour"]
    WV                                  -->|"+"| DLW["Downwelling\nLongwave\nRadiation"]
    DLW                                 -->|"+ [R]"| ST

    style ST  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style WV  fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style DLW fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 4.3. Water vapour reinforcing feedback loop. Warmer surface temperatures increase atmospheric water vapour content (Clausius-Clapeyron: ~7% per 1°C). Water vapour absorbs outgoing longwave radiation and re-radiates it downward, further warming the surface. Zero − signs → reinforcing (R). This feedback roughly doubles the direct warming from CO₂ alone and operates on timescales of days to weeks — far faster than the ice-albedo feedback.

---
### DIAGRAM 4 — Permafrost-methane tipping point (Figure 4.4)
---

```{mermaid}
graph LR
    PF["Permafrost\nCarbon Stock\n(~1,700 GtC)"] -->|"+"| FR["Frozen State\nStability"]
    FR                                             -->|"− [B]"| PF
    AW["Arctic\nWarming"]                          -->|"−"| FR
    AW                                             -->|"+"| TH["Thaw Rate"]
    TH                                             -->|"+"| GR["CH₄ + CO₂\nRelease"]
    GR                                             -->|"+ [R]"| AW

    style PF fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
    style FR fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style AW fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style TH fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style GR fill:#f5f5f5,stroke:#111111,stroke-width:2px
```

> Figure 4.4. Permafrost-methane tipping point structure. The frozen permafrost state is maintained by a balancing feedback (B): cold Arctic temperatures suppress microbial decomposition. Arctic warming weakens this balancing loop and activates a reinforcing loop (R): thaw → CH₄ and CO₂ release → additional greenhouse warming → further thaw. The permafrost carbon stock (~1,700 GtC) is more than double the current atmospheric carbon content. If the reinforcing loop becomes self-sustaining, carbon release continues independently of further human emissions.

---
### DIAGRAM 5 — AMOC loop and freshwater stress (Figure 4.6)
---

```{mermaid}
graph LR
    AMOC["AMOC\nStrength"]      -->|"+"| HT["Northward\nHeat Transport"]
    HT                          -->|"+"| EVAP["North Atlantic\nEvaporation"]
    EVAP                        -->|"+"| SAL["Surface\nSalinity"]
    SAL                         -->|"+ [B]"| AMOC
    FW["Greenland\nMeltwater"]  -->|"−"| SAL

    style AMOC fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style HT   fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style EVAP fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style SAL  fill:#f5f5f5,stroke:#111111,stroke-width:2px
    style FW   fill:#fff3f3,stroke:#d52a2a,stroke-width:2px
```

> Figure 4.6. AMOC self-sustaining balancing loop and freshwater stress. The thermohaline circulation maintains itself through a balancing loop (B): AMOC transports heat northward → increases evaporation → increases surface salinity → maintains the density contrast that drives AMOC. Greenland meltwater dilutes North Atlantic surface salinity, weakening the loop. Past a threshold freshwater forcing, the density contrast drops below the level required to sustain deep water formation, and AMOC tips to a much weaker state.
