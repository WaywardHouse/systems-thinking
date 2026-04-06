I now have a thorough understanding of the codebase, patterns, and cross-link targets. I have everything needed to produce the complete chapter plan. Note that this is a planning document — I cannot write it to a file (that would be creating a new file). I will deliver the complete plan as my output, which the user can save.

Here is the complete chapter plan:

---

# CHAPTER-04-PLAN.md — Chapter 4 Production Plan: "Earth as a System"

**Status at plan date:** 2026-04-05
**For agents:** Writer, Simulation Engineer, Diagram Specifier
**What exists:** Empty stub (`04-earth-as-a-system.qmd`) — full design required. No prose, no simulation, no diagrams.
**What this plan specifies:** Complete chapter architecture from scratch — YAML front matter, section structure, prose assignments, simulation specification, diagram specifications, cross-link callouts, and assembly instructions.

---

## 1. Chapter-Level Design

### YAML Front Matter

```yaml
---
title: "Earth as a System"
subtitle: "Coupled stocks, biogeochemical cycles, and the feedbacks that run the planet"
status: seed → draft
axiom: "You have feedback loops: reinforcing structures that amplify, balancing structures that resist, tipping points that switch which loop governs behaviour."
rewrite: "The Earth is not a backdrop. It is a coupled system of interacting stocks and flows — with feedbacks, delays, and tipping points that follow precisely the structures already established."
opens_to:
  - chapter: 05-cities-and-economies-as-systems
    relationship: enables
  - course: ESDE 307
    relationship: anchors
destinations:
  - field: earth
    hook: "The atmosphere holds about 870 gigatonnes of carbon. Before industrialisation it held roughly 590. That difference — roughly 280 GtC added in 175 years — is a perturbation to a stock-flow system that had been near equilibrium for millennia. The atmosphere, ocean, and land biosphere all carry carbon. The flows between them are real, measurable, and slow. The perturbation is fast. The system is still catching up."
  - field: human
    hook: "The oil sands of northern Alberta hold an estimated 166 billion barrels of recoverable bitumen — the third-largest proven oil reserve in the world. Extracting and upgrading it requires vast flows of water, energy, and diluent. Understanding this system as a stocks-and-flows problem — with accumulation rates, depletion rates, and tailings pond stocks that cannot drain faster than the water treatment capacity allows — is not an add-on to resource planning. It is the only way to answer the basic question: what happens next?"
  - field: data
    hook: "Earth observation satellites generate roughly 2.5 petabytes of data per day. To extract a global cryosphere monitoring signal from that stream — a time series of glacier mass, sea ice extent, permafrost active-layer depth — requires a data pipeline that is itself a stock-flow system: raw imagery in, processed geophysical products out, with latency, quality filters, and reprocessing flows that determine how quickly a real-world change in the cryosphere appears in a usable dataset."
---
```

### Opening Puzzle

**The "oh" moment:** The Keeling Curve.

In 1958, Charles David Keeling installed a CO₂ analyser at Mauna Loa, Hawaii — chosen for being far from local sources. He measured 316 parts per million. He kept measuring. Forty years later, the curve he produced had become one of the most recognisable data records in science: a sawtoothed wave rising steadily, year after year.

The puzzle is not the rise. The puzzle is the **sawtooth**. Every year, the CO₂ concentration drops by roughly 6–8 ppm between May and October, then rises by 6–8 ppm between October and May. The amplitude of this seasonal oscillation is roughly twice the signal of anthropogenic forcing in any given year.

What is pulling atmospheric CO₂ down every spring? The Northern Hemisphere's land biosphere — trees leafing out, absorbing carbon as they photosynthesise. Every autumn, as leaves fall and decompose, the carbon returns. The entire Northern Hemisphere landmass inhales and exhales, and Keeling's instrument recorded it.

The puzzle lands on the reader like this: the Earth breathes. Not metaphorically. Literally, the stock of atmospheric carbon oscillates at a planetary scale because of a seasonal imbalance between photosynthesis (inflow to the land biosphere stock, outflow from the atmosphere stock) and respiration/decomposition (inflow back to the atmosphere). The reader has just met a stock-flow system they can feel in a data record.

The **"oh" moment** extends: once you see the sawtooth as a stock-flow signal, you cannot unsee it. And you notice that the trough of each successive cycle is slightly higher than the trough of the last. The balancing seasonal flow is still operating. But a second flow — the anthropogenic emission pulse — is adding to the atmosphere faster than the Earth's natural sinks remove it. The stock is rising. The sawtooth does not flatten it.

This puzzle earns the chapter's central claim: the Earth is a stock-flow system in disequilibrium, and understanding its behaviour requires the full vocabulary of stocks, flows, feedbacks, delays, and tipping points.

---

## 2. Section Structure

### Section overview

| # | Section title | Domain examples | Diagram? | Cross-link callout? |
|---|---|---|---|---|
| 0 | The puzzle (Keeling Curve) | Earth only | None | No |
| 1 | Earth as coupled subsystems | Earth: five subsystems; Human: oil sands as a 3-stock subsystem; Data: EO data pipeline | Stock-flow diagram 4.0 (conceptual) | No |
| 2 | Biogeochemical cycles: the carbon cycle | Earth: pre-industrial carbon cycle; Human: industrial metabolism / oil sands carbon budget; Data: carbon flux remote sensing | Mermaid 4.1 (3-box carbon stock-flow) | WH Data Engineering |
| 3 | Climate feedbacks: the full picture | Earth: ice-albedo + water vapour + ocean heat + permafrost methane; Human: oil sands energy intensity as feedback amplifier; Data: feedback parameter estimation from satellite obs | Mermaid 4.2 (water vapour R loop) | WH Maths Vol 8 |
| 4 | Earth system tipping points | Earth: AMOC, West Antarctic Ice Sheet, Amazon; Human: Athabasca watershed tipping point; Data: satellite early warning signals | Mermaid 4.3 (permafrost-methane tipping point); consider 4.4 (AMOC balancing loop collapse) | WH Comp Geo |
| 5 | Simulation: 3-box carbon cycle | Earth: all three scenarios; Human: emission trajectory analogy; Data: EO validation pipeline | Python simulation | No (inline "What to try") |
| 6 | Exercises | — | — | — |

---

### Section 0: The puzzle

**Purpose:** Generate the question that justifies the chapter. Arrive at the chapter's vocabulary without yet using it.

**Content:**
- Open with the Keeling Curve and the sawtooth. Show or describe the data.
- First question: what produces the sawtooth? (Seasonal Northern Hemisphere photosynthesis/respiration cycle — a seasonal balancing in the land biosphere stock.)
- Second observation: the baseline of the sawtooth is rising. The seasonal oscillation does not arrest the long-run trend.
- The puzzle: the Earth is simultaneously exhibiting a self-correcting seasonal cycle (balancing) and a long-run accumulation (a reinforcing-like perturbation with slow sinks). Two dynamics, one record.
- Close the section by naming what is needed: the vocabulary of stocks, flows, feedbacks, and tipping points — already in the reader's possession from Chapters 1–3.

**Target:** 300–400 words. Voice: state the observation, let it sit, then state what is needed. No subsection header under `## The puzzle`. Consistent with Ch 1 and Ch 3 puzzle openings.

**Separator:** `---` after the puzzle.

---

### Section 1: Earth as coupled subsystems

**Header:** `## Earth as coupled subsystems`

**Purpose:** Give the reader a structural map of the Earth system as interacting stocks. Brief — this is scaffolding, not depth. Depth comes in later sections.

**Content to convey:**
- Five subsystems: atmosphere, ocean, cryosphere, biosphere, lithosphere
- Each is a stock (or collection of stocks): atmospheric mass/composition, ocean heat and chemistry, ice volume, biomass and soil carbon, rock-cycle carbon and weathering fluxes
- The connections between them are flows: gas exchange at the ocean surface, evaporation, precipitation, weathering, photosynthesis, respiration, calving
- The Earth system is not just a list of subsystems — it is coupled: changes in one stock alter the flows that change another
- Response times vary enormously: the atmosphere mixes in weeks to months; the deep ocean circulates on millennial timescales; the lithosphere operates on millions of years. These mismatched response times produce delays that are fundamental to Earth system behaviour.
- The "right boundary" point from Ch 1 extended: most policy questions require drawing the boundary wide enough to capture at least the atmosphere-ocean-cryosphere coupling.

**Three-domain examples:**

*Earth:* The five-subsystem structure as stocks. One paragraph each on atmosphere (stocks: GHG concentrations, heat content; key flows: emission, uptake, radiation), ocean (stocks: heat, dissolved carbon, NADW volume; key flows: gas exchange, thermohaline overturning), cryosphere (stocks: ice mass, permafrost carbon; key flows: accumulation, melt, calving, sublimation — the author's domain expertise). Biosphere and lithosphere named but treated as supporting stocks for later sections.

*Human:* The Alberta oil sands as a 3-stock subsystem: bitumen-in-ground (the geological stock), processed bitumen and synthetic crude in pipeline inventory (the infrastructure stock), and tailings pond volume (the waste stock). Flows: extraction rate, upgrading throughput, tailings generation rate, water use rate. The key structural observation: tailings ponds cannot drain faster than the treatment capacity allows — they are a stock with a slow, regulated outflow, and they accumulate. This is a direct analogy to how slow earth system sinks work. The system is extracting from one stock (bitumen) while accumulating in another (tailings) — both change simultaneously.

*Data:* An Earth observation data pipeline as a stock-flow system. Raw satellite imagery is a rapidly filling stock (2.5 PB/day); processed Level-2 and Level-3 geophysical products are a downstream stock that fills more slowly because processing and validation take time; scientific time series (e.g., GRACE mass change, MODIS land cover, Landsat glacier area) are the furthest-downstream stock, produced by multi-year reprocessing efforts. The flows between these stocks have latency — real-world cryosphere changes appear in publishable satellite-derived time series on timescales of months to years. This delay matters for any operational monitoring application.

**Diagram:** A simple conceptual Mermaid stock-flow diagram showing the five subsystems as boxes with labelled flow arrows between them. Not a full causal loop diagram — a structural overview. This can be kept simple and clean. See Diagram 4.0 specification in Section 4.

**Target:** 600–750 words across all three domain examples plus structural prose. Voice: precise, structural, no enthusiasm — state the mechanism.

**Separator:** `---`

---

### Section 2: Biogeochemical cycles — carbon as the primary example

**Header:** `## Biogeochemical cycles`

**Purpose:** Introduce the carbon cycle as a stock-flow system in detail. Demonstrate pre-industrial equilibrium as a balancing structure. Demonstrate the fossil fuel perturbation as a reinforcing amplifier applied to a slow-sinking system. This section carries most of the chapter's new conceptual weight.

**Content to convey:**

*Pre-industrial equilibrium:*
- Three boxes: atmosphere (~590 GtC pre-industrial), ocean (~38,000 GtC total, ~900 GtC surface), land biosphere (~550 GtC living biomass, ~1,600 GtC soil)
- Key flows and approximate magnitudes (all as annual GtC/yr):
  - Atmosphere ↔ Ocean: gross exchange ~90 GtC/yr each way (net ~2 GtC/yr into ocean historically, effectively zero pre-industrial)
  - Atmosphere ↔ Land: gross exchange ~120 GtC/yr each way (photosynthesis in, respiration/decomposition out — near-zero net pre-industrial)
  - Weathering (lithosphere → ocean → atmosphere, very slow, ~0.2 GtC/yr over geological timescales — essentially background)
  - Volcanic outgassing: ~0.1–0.3 GtC/yr
- Pre-industrial: inflows ≈ outflows for each box. Near-equilibrium. The atmosphere is stable at ~280 ppm CO₂.
- Mechanism: this is a balancing structure at the system level — the flows are large but they cancel. Carbon cycles continuously between boxes but does not accumulate in any one. This is the pre-industrial "goal-seeking" behaviour.

*The fossil fuel perturbation:*
- Since ~1750: burning fossil fuels adds ~10 GtC/yr to the atmosphere (current rate; started lower, rising over time). This is a new inflow with no corresponding natural outflow at that rate.
- The ocean and land biosphere uptake some of this: ocean currently absorbs ~3 GtC/yr of the anthropogenic pulse; land biosphere absorbs ~3 GtC/yr. But ~4 GtC/yr remains in the atmosphere.
- The atmospheric stock rises. 590 GtC pre-industrial → ~870 GtC today.
- Why don't the sinks absorb all of it? Two reasons:
  1. Ocean uptake is limited by the rate of gas exchange and deep ocean mixing — a slow outflow valve on the ocean's surface carbon stock
  2. Ocean acidification (as ocean absorbs CO₂, carbonate chemistry shifts, reducing the ocean's capacity to absorb more) — a saturation effect that weakens the ocean sink over time
- This is the central structural lesson: a large stock with a slow outflow (the ocean) can buffer a fast perturbation temporarily but not indefinitely. The buffering is real but finite.

*Connection to Ch 1–2:* Explicitly name the loop structure. Pre-industrial: near-equilibrium balancing structure. Post-industrial perturbation: a new inflow applied to a stock with slow sinks — behaviour resembles "overshoot" archetype from Ch 2 (R loop plus slow B loop). The atmosphere overshoots any natural equilibrium on human timescales because the sinks are too slow to clear the perturbation at the rate it is applied.

**Three-domain examples:**

*Earth:* The full carbon cycle story above, grounded in the Keeling Curve puzzle. The sawtooth is the seasonal biosphere flow. The rising baseline is the net positive stock change.

*Human:* Industrial metabolism as a biogeochemical cycle. An industrial economy processes raw material stocks (ore, fossil carbon, fresh water, soil nutrients) and produces waste stocks (tailings, atmospheric CO₂, treated and untreated effluent, landfill). The Alberta oil sands are a sharply defined case: the energy required to extract and upgrade bitumen (natural gas, electricity) is itself a large carbon flow — upgrading generates ~15–20% more CO₂ per barrel than conventional crude. The tailings ponds contain dissolved naphthenic acids, trace metals, and unrecovered bitumen — a stock that currently exceeds 1.4 trillion litres. The rate at which water can be returned to the Athabasca River system (the outflow from the tailings stock) is constrained by treatment technology and provincial regulation. The stock is still growing. This is the industrial metabolism analogy to the ocean carbon stock: a large accumulation with a slow, regulated outflow.

*Data:* Remote sensing of carbon fluxes. MODIS provides Net Primary Productivity (NPP) estimates globally at 500m, 8-day resolution — a proxy for the land biosphere's photosynthesis inflow to the organic carbon stock. GOSAT and OCO-2 measure column-averaged CO₂ concentration — an integrated signal of the atmospheric carbon stock. GRACE/-FO measures terrestrial water storage and ice mass changes (connected stocks). The data pipeline challenge: each instrument measures a different part of the system at different spatial and temporal resolutions; fusing them into a coherent picture of global carbon fluxes requires matching units, accounting for retrieval uncertainties, and validating against ground-truth flux tower networks. This is the data analogy to the multi-box Earth system model.

**Diagram:** Mermaid 4.1 — the 3-box carbon cycle stock-flow diagram. See Section 4 for full specification.

**Cross-link callout:** WH Data Engineering. Target: Ch 3 (Pipelines and ETL) and Ch 5 (Streaming and Real-time). Earth observation data pipelines for carbon flux monitoring are a high-stakes instance of the ETL architectures covered there — with the added constraint that the data product must preserve physical units and uncertainty estimates through every transformation step. See Section 6 for callout text specification.

**Target:** 750–900 words including all three domain examples. Voice: mechanism-first. Name the stock, name the flows, name the rates. No hedging about whether climate change is real — state the structure and let it carry.

**Separator:** `---`

---

### Section 3: Climate feedbacks — the full picture

**Header:** `## Climate feedbacks`

**Purpose:** Compile all feedbacks introduced across Ch 2 (ice-albedo) into a unified picture of the climate feedback system. Add water vapour, permafrost methane, and ocean heat. Show that the climate system's response to forcing is not the forcing alone — it is the forcing multiplied by a feedback factor.

**Content to convey:**

*Feedback catalogue (four feedbacks to cover):*

1. **Ice-albedo feedback (R)** — already introduced in Ch 2 (Fig 2.1). Revisit briefly, now in the context of the full system. The reader should feel this as a familiar face in a larger picture, not a repeat. Note: this is strongest in the Arctic and on ice sheets. It is a fast feedback on decadal timescales.

2. **Water vapour feedback (R)** — the largest single amplifier in the climate system. Warmer atmosphere holds more water vapour (Clausius-Clapeyron: ~7% more water vapour per 1°C warming). Water vapour is itself a greenhouse gas — it absorbs outgoing longwave radiation and re-radiates it downward. So warming → more water vapour → more greenhouse warming → more warming. The reinforcing loop: surface temperature → atmospheric water vapour → downwelling longwave radiation → surface temperature. This roughly doubles the direct warming from CO₂ alone.

3. **Ocean heat uptake as a balancing loop with delay (B)** — introduced briefly in Ch 2. Revisit and expand. The ocean's enormous heat capacity means it absorbs much of the radiative forcing, moderating atmospheric temperature rise. But this is not free: the heat goes into the ocean, raising sea surface temperatures and ocean interior temperatures, with consequences for thermal expansion (sea level rise) and marine chemistry. The delay built into this balancing loop is measured in centuries for the deep ocean. Committed warming — warming already locked in by current atmospheric CO₂ that has not yet fully expressed because the ocean is still absorbing — is a consequence of this delay structure.

4. **Permafrost-methane feedback (R) and tipping point connection** — permafrost soils store roughly 1,700 GtC — more than double the current atmospheric carbon stock. As permafrost thaws, microbial decomposition accelerates, releasing CO₂ and methane (CH₄, ~80× more potent as a GHG over 20 years than CO₂). More methane → more warming → more permafrost thaw → more methane. This is a reinforcing loop with a tipping point structure: at a threshold warming level, the permafrost-methane feedback could become self-sustaining, releasing carbon regardless of what humans do to emissions. This connects directly to Ch 3's tipping point framework. The author's expertise in cryosphere is the grounding: permafrost active layer, thermokarst formation, and the spatial heterogeneity of permafrost vulnerability are real-world physical mechanisms behind this feedback.

*Feedback factor concept:*
The total climate response to forcing is not the forcing alone — it is the forcing multiplied by a factor that reflects all active feedbacks. The feedback factor concept: if you double CO₂ (a 3.7 W/m² forcing), the direct temperature response is ~1°C. With ice-albedo + water vapour + cloud feedbacks combined, the equilibrium climate sensitivity is estimated at 2.5–4°C per doubling. The difference is the feedback amplification. Connect back to the loop notation from Ch 2: a reinforcing loop amplifies the initial forcing; a balancing loop dampens it. The climate system contains both.

**Three-domain examples:**

*Earth:* All four feedbacks above, with specific attention to which feedbacks operate on which stocks and timescales. Permafrost methane connects to tipping point section.

*Human:* Oil sands development as a feedback amplifier. Expanding bitumen production increases energy demand from natural gas (used for steam-assisted gravity drainage — SAGD — and upgrading), which increases CO₂ emissions from the extraction process itself, which contributes to warming, which increases permafrost thaw in the Athabasca region and reduces the annual precipitation and snowpack that feeds the Athabasca River (source of process water). Reduced river flow → tighter water allocations → higher operational costs → production pressure. The system feeds back on itself through the climate it is helping to perturb. This is not environmentalist framing — it is the loop structure of the system that producers in the region are navigating.

*Data:* Estimating feedback parameters from satellite observations. The ice-albedo feedback parameter (how much additional absorbed solar radiation per square metre per degree of warming due to ice loss) can be estimated from CERES (radiation budget satellite) combined with sea ice extent from AMSR-E/AMSR2. The water vapour feedback parameter is estimated from radiosonde networks, GPS-derived precipitable water, and reanalysis products. The challenge: feedback parameters estimated from observations include the effects of short-term climate variability (ENSO, volcanic eruptions) that need to be disentangled from the long-term response to CO₂ forcing. This is a signal processing and attribution problem in the data pipeline — exactly the kind of problem covered in WH Computational Geography cryosphere and environmental systems modules.

**Diagrams:** Mermaid 4.2 (water vapour reinforcing loop — new feedback not drawn in Ch 2). Mermaid 4.3 (permafrost-methane tipping point — see Section 4). Consider Mermaid 4.4 for AMOC if space permits.

**Cross-link callout:** WH Maths Vol 8, Ch 1 (Control, Feedback, Stability) and Ch 3 (Continuum Transport). Earth system models are systems of coupled differential equations — the feedback parameters discussed here are the eigenvalues of the linearised system. A positive sum of feedback parameters → unstable equilibrium (reinforcing dominant); negative sum → stable (balancing dominant). Vol 8 develops this machinery. See Section 6 for callout text.

**Target:** 800–1000 words. Voice: technical precision. The author knows these feedbacks from quantitative work in glaciology and climate modelling — this section should feel grounded in measurement, not hand-waving.

**Separator:** `---`

---

### Section 4: Earth system tipping points

**Header:** `## Earth system tipping points`

**Purpose:** Apply the Ch 3 tipping point framework to three specific Earth systems with sufficient technical specificity to ground the abstract structure in real geography and physics. This section is where the author's expertise is most directly visible.

**Content to convey:**

Connect to Ch 3: the generic tipping point structure (Figure 3.1) — external stress weakening the balancing feedback and strengthening the reinforcing one. Now apply it three times to real Earth systems. Each subsection should name: the stock, the balancing feedback (current dominant structure), the external stress (warming, deforestation, etc.), the reinforcing feedback that takes over at the threshold, and the likely end state.

*Three tipping elements:*

**1. AMOC (Atlantic Meridional Overturning Circulation)**
- Stock: Deep water formation rate in the North Atlantic (a flow that drives the overturning) — or more intuitively, the strength of the thermohaline circulation
- The balancing structure: salinity-driven density contrast between warm salty subtropical surface water (moving north) and cold fresh deep water (sinking and moving south). This density difference is what drives AMOC. A self-sustaining loop: AMOC transports heat northward → warms North Atlantic → increases evaporation → increases surface salinity → maintains the density contrast that drives AMOC. A self-sustaining balancing loop keeping the circulation in its active state.
- External stress: freshwater input from Greenland Ice Sheet melt. Fresh water is less dense — it dilutes the salinity of the North Atlantic surface, reducing the density contrast, weakening the deep water formation rate.
- Tipping point: if freshwater input exceeds a threshold, the density contrast drops below the level needed to maintain deep water formation. AMOC weakens. A weaker AMOC transports less heat northward, reducing evaporation, further reducing salinity — a reinforcing collapse loop. The AMOC tips to a much weaker state.
- End state: significantly reduced northward heat transport. Western Europe cools by several degrees despite global warming. Atlantic Meridional Overturning in partial or near-collapse state. Recovery timescale: centuries to millennia.
- Current evidence: palaeoclimate records show AMOC has been in a substantially weaker state (during Younger Dryas, ~12,000 years ago). Current AMOC is the weakest in at least 1,000 years based on proxy records. Critical slowing down signatures (reduced recovery rate after perturbation) are detectable in observational records — a warning signal of declining resilience (connect to Ch 3 Exercise 3.3).

**2. West Antarctic Ice Sheet (WAIS)**
- Stock: Ice volume in the marine-based West Antarctic Ice Sheet (~3.3 million km³, equivalent to ~3.3 m global mean sea level)
- The balancing structure: the ice sheet is buttressed by ice shelves — floating tongues of ice that extend from the grounded ice into the ocean, pinning the ice sheet at the grounding line. The balancing loop: ice flows toward the margin → builds up ice shelves → ice shelves provide back-pressure → slows ice flow → limits further advance
- External stress: ocean warming. The Circumpolar Deep Water (CDW), a warm water mass, is intruding beneath the ice shelves (particularly the Thwaites and Pine Island Glacier systems). As ocean water warms, ice shelf basal melt accelerates.
- The tipping mechanism: Marine Ice Sheet Instability (MISI). The WAIS rests on bedrock that deepens inland — the bed slopes backward. If the grounding line retreats into deeper water, the ice sheet becomes unstable: deeper water → taller ice face at the grounding line → faster ice flow → more calving → further grounding line retreat → deeper water → faster flow. A self-reinforcing collapse loop.
- End state: partial or full WAIS collapse. Timescale: centuries to millennia once initiated — but the initiation threshold may already be close or past for Thwaites.
- This is the author's domain — glaciology. The physical mechanism (MISI) is well-understood. The tipping point may already have been passed for parts of Thwaites based on current observations.

**3. Amazon dieback**
- Stock: Biomass carbon in the Amazon rainforest (~150–200 GtC above-ground)
- The balancing structure (self-maintaining healthy state): forest creates its own rainfall through evapotranspiration. Large-scale evaporation from the canopy feeds precipitation that falls back on the forest. Loop: forest cover → high evapotranspiration → regional precipitation → forest growth → forest cover. The Amazon partly makes its own rain.
- External stresses: deforestation (removes forest cover directly) + regional warming and drying (reduces precipitation, increases fire risk)
- Tipping point: if deforestation and drought reduce forest cover below ~20–25% of original area, the forest can no longer generate sufficient evapotranspiration to sustain regional rainfall. The moisture recycling loop breaks. Reduced rainfall → tree mortality → reduced evapotranspiration → further reduced rainfall. A reinforcing dieback loop.
- End state: large-scale savannification of the eastern Amazon. Roughly 30–40% of original Amazon area at risk under high-deforestation + 2°C warming scenarios. Carbon release: 50–90 GtC — a significant positive forcing on the global carbon cycle.
- Current state: deforestation is currently ~20% of original area. The system is close to, possibly past, the tipping zone in some regions.

**Human domain example:**
Athabasca River as a local tipping point system. The oil sands require large volumes of water from the Athabasca River for in-situ operations (SAGD) and tailings management. Regulatory frameworks set flow-based restrictions (operations must reduce or halt water withdrawals during low-flow periods). The low-flow threshold is itself affected by climate: reduced Rocky Mountain snowpack (the Athabasca's primary source) and earlier melt timing shift the river's seasonal flow regime. The tipping structure: if climate-driven low-flow periods become longer and more frequent, the operational feasibility of water-intensive in-situ production crosses a regulatory threshold that constrains output. The stock (river flow) has a seasonal balancing loop (snowpack accumulates in winter, melts in spring) that is being weakened by warming — exactly the tipping point structure from Ch 3.

**Data domain example:**
Early warning signals and satellite monitoring of tipping elements. The critical slowing down signature (Ch 3 Exercise 3.3) is detectable in satellite time series: as a system approaches a tipping point, variance increases and recovery rate after perturbation decreases. In practice: GRACE/-FO data for Greenland and WAIS show accelerating mass loss rates, indicating MISI may be in progress for some outlet glaciers. Vegetation index time series (NDVI from MODIS/Landsat) over the Amazon show increased variance and decreased seasonal amplitude in regions under high deforestation pressure — a data signature of declining forest resilience. The data pipeline challenge: detecting these signals requires long, consistent satellite records (decades), cross-sensor calibration, and careful separation of climate variability from structural change. This is exactly the observational monitoring problem covered in WH Computational Geography cryosphere and remote sensing modules.

**Diagram:** Mermaid 4.3 (permafrost-methane tipping point — the cleanest diagram representation, in the feedback section). For AMOC, a brief diagram showing the balancing self-sustaining loop and the freshwater stress pathway weakening it. See Section 4 (diagrams).

**Cross-link callout:** WH Computational Geography — cryosphere and environmental systems modules. The WAIS and Athabasca glacier examples in this section connect directly to the physical mechanisms modelled in the cryosphere laboratory. See Section 6.

**Target:** 1000–1200 words across all three tipping element subsections plus domain examples. Voice: technically grounded, not alarmist. State the mechanism. Quantify where possible. The author's former glaciologist identity should be legible in the specificity of the WAIS treatment.

**Separator:** `---`

---

### Section 5: Simulation — 3-box carbon cycle model

**Header:** `## Simulating the carbon cycle: three stocks, one perturbation`

**Purpose:** Build the simulation that makes the chapter's central claims tangible. Demonstrate (1) how the ocean and land biosphere buffer the atmospheric CO₂ pulse but only partially; (2) how atmospheric CO₂ overshoots any pre-industrial level; (3) what a reduced-emission scenario looks like versus business-as-usual. Make the reader feel the response time of the Earth system as a stock-flow system.

**Bridge paragraph content (for Writer):**
Exercise 5.X in the next section asks you to extend this model; the code below is the base case. Run it before reading the interpretation. The result — atmospheric CO₂ continuing to rise even in the reduced-emission scenario — is not a bug. It is what a stock does when inflows still exceed outflows. Run the equilibrium scenario first to verify the model is correctly initialised before modifying the emission trajectory.

Full simulation specification is in Section 3 of this document.

**Separator:** `---`

---

### Section 6: Exercises

**Header:** `## Exercises`

**Six exercises as specified below.**

---

## 3. Simulation Specification

### Model: 3-Box Carbon Cycle

**Method:** Euler integration, `dt = 1 year`, run 1750–2150 (400 steps).

**Boxes (stocks) and pre-industrial initial values:**

| Stock | Symbol | Pre-industrial value | Units |
|---|---|---|---|
| Atmosphere | A | 590 | GtC |
| Ocean (surface + deep combined, but split into surface exchange and deep buffering) | O | 38000 | GtC |
| Land biosphere (vegetation + soil) | L | 2150 | GtC |

Note: Ocean value of 38,000 GtC is the total ocean stock. In the simplified 3-box model, this large stock acts as a slow sink — the flow rate is what changes, not the total stock dramatically. The ocean stock changes by ~200 GtC over the 400-year run.

**Pre-industrial equilibrium flows (approximate, annual GtC/yr):**

| Flow | Symbol | Direction | Rate |
|---|---|---|---|
| Ocean-atmosphere gas exchange (gross out of ocean) | F_OA | Ocean → Atmosphere | 90.0 |
| Atmosphere-ocean gas exchange (gross into ocean) | F_AO | Atmosphere → Ocean | 90.0 |
| Land photosynthesis (GPP, into land biosphere) | F_AL | Atmosphere → Land | 120.0 |
| Land respiration/decomposition (into atmosphere) | F_LA | Land → Atmosphere | 120.0 |
| Weathering (lithosphere source, treated as constant background) | F_W | → Atmosphere | 0.2 |
| Volcanic outgassing (constant background) | F_V | → Atmosphere | 0.1 |

Pre-industrial equilibrium check: `dA/dt = F_OA + F_LA + F_W + F_V - F_AO - F_AL = 0`. With these values: `90 + 120 + 0.2 + 0.1 - 90 - 120 = 0.3` — close to zero (the small imbalance represents the natural net sink, acceptable for this model; can be adjusted to exact zero by setting weathering + volcanic = 0 in the equilibrium scenario).

**Perturbation (anthropogenic emission):**

Emit a time-varying flow `E(t)` from fossil fuel burning + land use change, added to the atmosphere stock. Approximate historical and projected trajectory:

```
1750–1850: E(t) = 0.5 GtC/yr (pre-industrial baseline emissions, effectively negligible)
1850–1950: E(t) = linear ramp from 0.5 to 6.0 GtC/yr (industrialisation)
1950–2023: E(t) = linear ramp from 6.0 to 11.0 GtC/yr (post-war expansion)
2023–2100: Scenario-dependent (see below)
2100–2150: Scenario-dependent
```

**Three scenarios:**

**Scenario 0 — Pre-industrial equilibrium (validation run)**
- E(t) = 0 throughout (or the 0.3 GtC/yr natural balance offset)
- All three stocks should hold steady (within numerical error)
- Purpose: verify model initialisation is correct before adding perturbation
- Plot: dashed lines showing stable stocks as a reference

**Scenario 1 — Historical + projected business-as-usual (BAU)**
- 1750–2023: historical trajectory as above
- 2023–2100: linear increase from 11 to 14 GtC/yr (continued fossil fuel growth)
- 2100–2150: held at 14 GtC/yr
- Expected result: atmospheric CO₂ reaches ~550–600 ppm by 2100; continues rising to 2150

**Scenario 2 — Reduced emissions**
- 1750–2023: identical to Scenario 1 (historical is fixed)
- 2023–2075: linear decline from 11 to 2 GtC/yr (aggressive decarbonisation)
- 2075–2150: held at 2 GtC/yr (residual: agriculture, aviation, cement)
- Expected result: atmospheric CO₂ levels off but does not return to pre-industrial; ocean carbon stock continues rising

**Flow equations (Euler update):**

The flow rates F_AO and F_AL are not constant — they respond to the atmospheric stock (the carbon system has concentration-dependent flux). Implement a simplified concentration-dependent uptake:

```
F_AO(t) = k_AO * A(t)   where k_AO = 90 / 590 = 0.1525 yr⁻¹  (ocean uptake rate constant, calibrated to pre-industrial)
F_AL(t) = k_AL * A(t)   where k_AL = 120 / 590 = 0.2034 yr⁻¹  (land uptake rate constant, calibrated to pre-industrial)
```

This makes the ocean and land uptake scale with atmospheric concentration — when the atmosphere is enriched, sinks take up more. This is the CO₂ fertilisation / partial pressure driving effect. It is a simplification but produces physically plausible behaviour.

Keep outflows from ocean and land as constants (ocean respiration and outgassing, land respiration) — or equivalently, keep F_OA and F_LA as fixed pre-industrial values. The asymmetry (uptake scales with atmosphere, outflow is fixed) is what causes the ocean and land stocks to grow when the atmosphere is enriched.

**Ocean acidification diagnostic:**

Compute ocean carbon stock at each time step. Ocean acidification risk rises as the ocean carbon stock increases — more dissolved CO₂ drives pH down. Do not model pH explicitly; annotate the ocean stock plot with a note that rising ocean carbon stock corresponds to decreasing pH.

**Land sink uncertainty:**

In Scenario 2, add a third variant where land uptake is reduced by 20% after 2050 (`k_AL` reduced by 0.2 × baseline from 2050 onward) to represent land sink saturation under warming and dieback. Plot this as a dashed line alongside Scenario 2 to show the land sink uncertainty range.

**Plot specification:**

Three-panel figure, `figsize=(12, 9)` (three rows, one column), `dpi=150`.

**Panel 1 (top): Atmospheric CO₂ in ppm**
- Convert GtC to ppm: 1 GtC = 0.471 ppm (standard conversion: 2.13 GtC per ppm)
- Y-axis: "Atmospheric CO₂ (ppm)", range 250–650
- X-axis: Year, 1750–2150
- Lines:
  - Equilibrium: `#888888`, dashed, `linewidth=1.0`, annotate "Pre-industrial equilibrium"
  - BAU (Scenario 1): `#d52a2a`, solid, `linewidth=1.8`, annotate "Business-as-usual"
  - Reduced (Scenario 2): `#111111`, solid, `linewidth=1.8`, annotate "Reduced emissions"
  - Reduced + land sink uncertainty: `#111111`, dashed, `linewidth=1.2`, annotate "Reduced (low land sink)"
- Horizontal reference at 280 ppm: dashed grey, annotate "Pre-industrial (280 ppm)"
- Vertical reference at 2023: dashed grey, annotate "2023"

**Panel 2 (middle): Ocean carbon stock (GtC)**
- Y-axis: "Ocean carbon stock (GtC)", range 37800–38400
- X-axis: Year, 1750–2150
- Lines: same colours as Panel 1
- Annotate: "Increasing ocean carbon → ocean acidification" (arrow pointing up, placed at 2100)

**Panel 3 (bottom): Land biosphere carbon stock (GtC)**
- Y-axis: "Land biosphere carbon stock (GtC)", range 2000–2400
- X-axis: Year, 1750–2150
- Lines: same colours as Panel 1
- Annotate: "Land sink saturates under warming" (dashed line divergence, 2050 onward)

**Code style:**
- numpy + matplotlib only. No scipy.
- Named constants block at top: `A0`, `O0`, `L0`, `k_AO`, `k_AL`, `F_OA_const`, `F_LA_const`, `F_W`, `F_V`, `dt`, `YEARS_START`, `YEARS_END`
- Docstring: `"""3-box carbon cycle model — Chapter 4. Euler method: atmosphere, ocean, land biosphere stocks. Perturbation: anthropogenic CO₂ emission added as flow into atmosphere from 1750 onward."""`
- Separate function for emission trajectory: `def emissions(t, scenario):` returning GtC/yr
- Three scenarios run in a loop over scenario names; results stored in a dict
- `plt.tight_layout()` before save
- Save: `plt.savefig("_assets/ch04-carbon-cycle.png", dpi=150, bbox_inches="tight")`
- Comment every logical block (parameter initialisation, equilibrium flows, emission function, Euler loop, plot construction)
- Approximate length: 80–110 lines

**Block header:**
```
#| label: fig-carbon-cycle
#| fig-cap: "Figure 4.5. 3-box carbon cycle model: atmosphere, ocean, and land biosphere stocks under three emission scenarios, 1750–2150. Top panel: atmospheric CO₂ rises in all scenarios but the rate depends on emission trajectory. The reduced-emission scenario stabilises CO₂ but does not return it to pre-industrial levels — the atmospheric stock does not empty when emissions fall; it simply accumulates more slowly. Centre panel: ocean carbon stock grows in all scenarios, corresponding to ongoing ocean acidification. Bottom panel: land biosphere carbon stock grows as the land sink takes up more carbon but is sensitive to assumptions about land sink saturation. The dashed line in the bottom panel shows the effect of a 20% reduction in land uptake from 2050."
#| fig-width: 12
#| fig-height: 9
```

**Figure caption (below code block):**
> Figure 4.5. 3-box carbon cycle model under three emission scenarios, 1750–2150. Top: atmospheric CO₂ (ppm) — the reduced-emission scenario slows accumulation but does not return the stock to pre-industrial levels, because inflows still exceed outflows. Centre: ocean carbon stock (GtC) — continues rising in all scenarios, reflecting ongoing ocean acidification. Bottom: land biosphere carbon stock (GtC) with land sink uncertainty shown as a dashed line from 2050. The key result: atmospheric overshoot is not a function of the emission peak alone; it is a function of the cumulative stock change, which integrates decades of past emissions into every future state.

**"What to try" callout:**

```markdown
::: {.callout-tip}
## What to try

1. **Set emissions to zero in 2050 in Scenario 2.** Does atmospheric CO₂ immediately start falling? Why or why not? How many years does it take for the atmospheric stock to begin declining, and what controls that timescale?

2. **Change `k_AO` (ocean uptake rate) to 0.80 × its pre-industrial value from 2050 onward** — simulating ocean sink saturation as the ocean surface acidifies. What happens to the atmospheric stock trajectory? How does this compare to the land sink saturation uncertainty in Panel 3?

3. **Map this model to a data pipeline.** In a large satellite data processing system: what plays the role of the atmosphere stock? The ocean stock? The anthropogenic emission flow? What would "ocean acidification" look like in a data pipeline context — a stock accumulating something that degrades future capacity? Write down the analogy explicitly before continuing.
:::
```

---

## 4. Diagram Specifications

### Diagram 4.0 — Earth system coupled subsystems (stock-flow overview)

**Type:** Mermaid `flowchart LR`
**Location:** `## Earth as coupled subsystems`, after the structural prose, before the three-domain examples.
**Purpose:** Give the reader a map of the Earth system as interacting stocks. Structural orientation, not causal loop detail.

**Nodes and edges:**
```
ATM[["Atmosphere\n(GHG, heat)"]]
OCN[["Ocean\n(heat, carbon, NADW)"]]
CRY[["Cryosphere\n(ice, permafrost)"]]
BIO[["Biosphere\n(biomass, soil C)"]]
LIT[["Lithosphere\n(rock carbon)"]]

ATM -->|"gas exchange\n(CO₂, H₂O)"| OCN
OCN -->|"gas exchange"| ATM
ATM -->|"precipitation"| CRY
CRY -->|"meltwater,\nalbedo"| ATM
ATM -->|"photosynthesis\nCO₂"| BIO
BIO -->|"respiration,\ndecomposition"| ATM
LIT -->|"weathering,\nvolcanism"| ATM
```

**Accent node:** `ATM` — the atmosphere is the central coupling stock in this chapter. `fill:#fff3f3,stroke:#d52a2a,stroke-width:2px`
**Standard node style:** `fill:#f5f5f5,stroke:#111111,stroke-width:2px`
**Figure number:** 4.1
**Caption:**
> Figure 4.1. Earth's five major subsystems as interacting stocks. Double-border rectangles (using `[[...]]` notation) represent stocks; solid arrows represent material or energy flows. The atmosphere is the central coupling medium: most cross-system flows pass through it or are driven by it. Each stock has a characteristic response time — the atmosphere responds on timescales of years to decades; the deep ocean on centuries to millennia; the lithosphere on millions of years. These mismatched response times are the source of the long delays that characterise Earth system behaviour.

---

### Diagram 4.1 — Carbon cycle 3-box stock-flow (Mermaid)

**Type:** Mermaid `flowchart LR`
**Location:** `## Biogeochemical cycles`, after the pre-industrial equilibrium prose, before the fossil fuel perturbation prose.
**Purpose:** Show the three-box stock-flow structure of the carbon cycle — the structural counterpart to the Python simulation.

**Nodes and edges:**
```
EM([Fossil fuel\nemissions\nGtC/yr])
ATM[["Atmosphere\n590 GtC\n(pre-industrial)"]]
OCN[["Ocean\n38,000 GtC"]]
LND[["Land Biosphere\n2,150 GtC"]]
WTH([Weathering +\nvolcanism\n~0.3 GtC/yr])

EM -->|"E(t)\n~10 GtC/yr\n(current)"| ATM
WTH -->|"background"| ATM
ATM -->|"gas exchange\n~90 GtC/yr"| OCN
OCN -->|"outgassing\n~90 GtC/yr"| ATM
ATM -->|"photosynthesis\n~120 GtC/yr"| LND
LND -->|"respiration +\ndecomp\n~120 GtC/yr"| ATM
```

**Accent node:** `EM([Fossil fuel\nemissions\nGtC/yr])` — the perturbation that breaks equilibrium. `fill:#fff3f3,stroke:#d52a2a,stroke-width:2px`
**Standard node styles:** Stocks `fill:#f5f5f5,stroke:#111111,stroke-width:2px`; source/sink nodes (rounded) standard grey
**Figure number:** 4.2
**Caption:**
> Figure 4.2. The 3-box carbon cycle. Double-border rectangles are stocks; rounded rectangles are external sources. Pre-industrial: gross atmosphere-ocean and atmosphere-land flows are nearly equal, and the atmospheric stock is stable. Perturbation: anthropogenic fossil fuel emissions add ~10 GtC/yr to the atmosphere — a new inflow with no corresponding natural outflow at that rate. Ocean and land uptake absorb roughly half; the remainder accumulates in the atmosphere. The atmospheric stock has risen from 590 GtC (~280 ppm) to ~870 GtC (~420 ppm) as a result.

---

### Diagram 4.2 — Water vapour reinforcing feedback loop

**Type:** Mermaid `graph LR`
**Location:** `## Climate feedbacks`, after the ice-albedo revisit paragraph, before the ocean heat uptake paragraph.
**Purpose:** Show the water vapour feedback as a reinforcing loop — a new diagram not drawn in Ch 2. This completes the feedback picture alongside the ice-albedo loop already established.

**Nodes and edges:**
```
ST["Surface\nTemperature"] -->|"+"| WV["Atmospheric\nWater Vapour"]
WV -->|"+"| DLW["Downwelling\nLongwave\nRadiation"]
DLW -->|"+ [R]"| ST
```

**Accent node:** `WV["Atmospheric\nWater Vapour"]` — the key intermediate stock that makes this loop work. `fill:#fff3f3,stroke:#d52a2a,stroke-width:2px`
**Standard node style:** `fill:#f5f5f5,stroke:#111111,stroke-width:2px`
**Figure number:** 4.3
**Caption:**
> Figure 4.3. Water vapour reinforcing feedback loop. Warmer surface temperatures increase atmospheric water vapour content (Clausius-Clapeyron: ~7% per 1°C). Water vapour absorbs outgoing longwave radiation and re-radiates it downward, further warming the surface. Zero − signs → reinforcing (R). This feedback roughly doubles the direct warming from CO₂ alone. It is the largest single amplifier in the climate system and operates on timescales of days to weeks — far faster than the ice-albedo feedback.

---

### Diagram 4.3 — Permafrost-methane tipping point

**Type:** Mermaid `graph LR`
**Location:** `## Climate feedbacks`, after the permafrost-methane feedback prose, immediately before the tipping point connection statement.
**Purpose:** Apply the Ch 3 tipping point loop structure (Fig 3.1) to a real Earth system. This diagram is the bridge from the feedbacks section to the tipping points section.

**Nodes and edges:**
```
PF["Permafrost\nCarbon Stock\n(~1,700 GtC)"] -->|"+"| BF["Balancing\nFeedback\n(frozen state)"]
BF -->|"− [B]"| PF
WM["Arctic\nWarming"] -->|"−"| BF
WM -->|"+"| RF["Permafrost\nThaw Rate"]
RF -->|"+"| CH4["CH₄ + CO₂\nRelease"]
CH4 -->|"+ [R]"| WM
```

**Accent node:** `PF["Permafrost\nCarbon Stock\n(~1,700 GtC)"]` — the stock at risk. `fill:#fff3f3,stroke:#d52a2a,stroke-width:2px`
**Standard node style:** `fill:#f5f5f5,stroke:#111111,stroke-width:2px`
**Figure number:** 4.4
**Caption:**
> Figure 4.4. Permafrost-methane tipping point structure. The frozen permafrost state is maintained by a balancing feedback (B): low temperatures keep organic carbon frozen, suppressing decomposition. Arctic warming weakens this balancing loop and activates a reinforcing loop (R): thaw → microbial decomposition → methane and CO₂ release → additional greenhouse warming → further thaw. The permafrost carbon stock (~1,700 GtC) is more than double the current atmospheric carbon content. If the reinforcing loop becomes self-sustaining, the carbon release is independent of further human emissions. This is a tipping point in the sense of Chapter 3: the transition switches which loop governs behaviour, and the new state is self-sustaining.

---

### Diagram 4.4 (optional) — AMOC weakening as balancing-loop collapse

**Type:** Mermaid `graph LR`
**Location:** `## Earth system tipping points`, `### AMOC` subsection, after the AMOC physical mechanism prose.
**Purpose:** Show how a self-sustaining balancing loop (the thermohaline circulation) can be collapsed by an external stress (freshwater forcing) into a weakened state. This is a structural variant on the Ch 3 tipping point diagram — the collapse of a balancing loop rather than the activation of a reinforcing one.
**Disposition:** Include if section length allows. If editorial space is tight, omit and rely on Diagram 4.4 (permafrost) to carry the tipping point diagrammatic burden for the section.

**Nodes and edges:**
```
AMOC["AMOC\nStrength"] -->|"+"| HT["Northward\nHeat Transport"]
HT -->|"+"| EVAP["North Atlantic\nEvaporation"]
EVAP -->|"+"| SAL["Surface\nSalinity"]
SAL -->|"+ [B]"| AMOC
FW["Greenland\nMeltwater\n(freshwater forcing)"] -->|"−"| SAL
FW -->|"+"| STR["Freshwater\nStress"]
STR -->|"−"| AMOC
```

**Accent node:** `FW["Greenland\nMeltwater\n(freshwater forcing)"]` — the external stress. `fill:#fff3f3,stroke:#d52a2a,stroke-width:2px`
**Standard node style:** `fill:#f5f5f5,stroke:#111111,stroke-width:2px`
**Figure number:** 4.6 (if included; 4.5 is the simulation figure)
**Caption:**
> Figure 4.6. AMOC self-sustaining balancing loop and freshwater stress. The thermohaline circulation maintains itself through a balancing loop (B): AMOC transports heat northward → increases evaporation → increases surface salinity → maintains the density contrast that drives AMOC. Greenland meltwater (left) dilutes North Atlantic surface salinity, weakening the loop. Past a threshold freshwater forcing, the density contrast drops below the level required to sustain deep water formation, and the loop collapses to a much weaker AMOC state.

---

## 5. Prose Section Assignments for Writer

### Assignment W4.0 — Opening puzzle

**Topic sentences:** The Keeling Curve contains two signals at once. The sawtooth is the land biosphere breathing. The rising baseline is a stock accumulating faster than its sinks can clear it.

**Mechanism to convey:**
1. Keeling Curve: observed 1958 to present at Mauna Loa. The sawtooth is seasonal Northern Hemisphere photosynthesis/respiration.
2. The mechanism: trees leaf out in spring (uptake flow increases, atmospheric stock falls); leaves fall and decompose in autumn (respiration flow increases, atmospheric stock rises). The amplitude (~6–8 ppm) is a stock-flow signal.
3. The baseline rises because the anthropogenic emission flow (fossil fuels) is adding carbon to the atmosphere faster than natural sinks remove it. The stock accumulates.
4. Close: this is a stock-flow system the reader already has the vocabulary to describe. The chapter applies that vocabulary to the Earth as a whole.

**Domain examples:** Earth only (this section is the puzzle — do not introduce human or data examples here).
**Target:** 300–400 words.
**Voice notes:** Do not use the phrase "climate change" in the first paragraph — arrive at the conclusion through the data. State the mechanism. Let the curve do the work.

---

### Assignment W4.1 — Earth as coupled subsystems

**Topic sentences:** The Earth system is not five subsystems. It is five stocks connected by flows — and the flows couple the stocks so that a change in one propagates through all the others on timescales that range from weeks to millennia.

**Mechanism to convey:**
1. Name the five stocks. One sentence each on what each stock holds.
2. The flows are what couple them — gas exchange, precipitation, photosynthesis, weathering. These are not background processes; they are the connections that make it a system.
3. Response times: mismatch is structural. Atmosphere: years. Ocean surface: decades. Deep ocean: centuries to millennia. Ice sheets: centuries to millennia. Lithosphere: millions of years. The same forcing applied to different stocks produces responses on completely different timescales.
4. Connect to Ch 1 boundary choice: drawing the boundary to exclude ocean-atmosphere coupling means missing the most important buffering mechanism for atmospheric CO₂.

**Domain examples:** All three as specified in Section 2.
**Target:** 600–750 words.
**Voice notes:** The oil sands example should be grounded in specific numbers (166 billion barrels recoverable; 1.4 trillion litres tailings; SAGD water requirements). This is the author's regional expertise — use it.

---

### Assignment W4.2 — Biogeochemical cycles

**Topic sentences:** The pre-industrial carbon cycle was a large-flow, near-equilibrium system. Hundreds of gigatonnes of carbon moved between stocks every year — and cancelled almost exactly. The fossil fuel perturbation added a new inflow that has no natural outflow at the same rate. The atmosphere is a stock. It is accumulating.

**Mechanism to convey:**
1. Pre-industrial equilibrium: the three-box structure. The flows are large (90 GtC/yr and 120 GtC/yr) but they cancel. The atmospheric stock is stable.
2. The fossil fuel perturbation: a new inflow. ~10 GtC/yr currently, started smaller in 1850. Ocean and land absorb roughly half. The rest stays.
3. Why the sinks cannot keep up: ocean uptake is limited by gas exchange kinetics and deep mixing rates. As ocean surface carbon rises, the partial pressure difference driving uptake decreases — the ocean sink weakens. This is the saturation structure that produces overshoot.
4. Connect to Ch 2 archetypes: this is overshoot in slow motion. The reinforcing perturbation (growing emissions) is running against a balancing sink (ocean and land uptake) that operates slowly — just like the overshoot archetype from Ch 2.
5. Industrial metabolism analogy: name the parallel to tailings ponds explicitly — a stock accumulating because the outflow is constrained, not because the inflow is out of control.

**Domain examples:** All three as specified in Section 2.
**Target:** 750–900 words.
**Voice notes:** The carbon flux numbers (590 GtC, 38,000 GtC, 90 GtC/yr exchange) should be stated with the confidence of someone who has worked with these values. Round numbers are fine; precision matters less than order of magnitude.

---

### Assignment W4.3 — Climate feedbacks

**Topic sentences:** The Earth's temperature response to a doubling of CO₂ is not 1°C. It is 2.5–4°C. The difference is feedbacks. The climate system contains reinforcing loops that amplify the initial forcing and balancing loops that partially dampen it. Understanding which loops are active, and on what timescales, is the difference between a 1.5°C outcome and a 4°C outcome.

**Mechanism to convey:**
1. Four feedbacks in sequence: ice-albedo (revisit briefly — the reader knows this), water vapour (the largest amplifier, new diagram), ocean heat uptake (the largest damper, with committed warming implication), permafrost methane (the tipping-point risk).
2. The feedback factor concept: direct forcing × amplification = total response. Name without algebra — "the feedback loops multiply the initial warming."
3. Committed warming: because the ocean has not yet fully warmed to equilibrium with current atmospheric CO₂, additional warming is already locked in. This is the delay structure of a very large stock (the ocean) with a slow response.
4. Oil sands as feedback amplifier: explicit structural description of the loop — oil sands production → natural gas combustion → CO₂ → warming → reduced Athabasca snowpack → operational water constraints → production pressure feedback. Name it as a feedback loop.

**Domain examples:** All three as specified in Section 2.
**Target:** 800–1000 words.
**Voice notes:** The permafrost treatment can be technically specific — active layer, thermokarst, SAGD thermal plumes in permafrost zones near oil sands operations. This is real expertise territory.

---

### Assignment W4.4 — Earth system tipping points

**Topic sentences:** The Ch 3 tipping point structure applies directly to three of the most consequential Earth systems: the Atlantic overturning circulation, the West Antarctic Ice Sheet, and the Amazon forest. Each has a self-sustaining current state, a weakening mechanism, and a reinforcing loop waiting to take over.

**Mechanism to convey:**
1. Brief reconnect to Fig 3.1 — "this is the same structure from Chapter 3, now grounded in geography and physics."
2. AMOC: the thermohaline self-sustaining loop; the freshwater stress; the density-driven collapse; the cooling of Western Europe; the palaeoclimate evidence. Current state: weakest in a millennium.
3. WAIS: Marine Ice Sheet Instability; the retrograde bed slope; the role of ice shelves; Thwaites specifically; the sea level implication; why this is the author's deepest area of expertise. The tipping point may already be in progress for some outlet glaciers.
4. Amazon: the moisture recycling self-sustaining loop; the deforestation threshold; the combined deforestation + warming stress; the savannification risk; the carbon release implication.
5. Athabasca water system as local analogue: brief, specific, connected to the structural framework.
6. Satellite early warning signals: critical slowing down in GRACE mass loss acceleration; NDVI variance increase in Amazon. Data pipeline challenge: long records, cross-sensor calibration.

**Domain examples:** All three as specified in Section 2.
**Target:** 1000–1200 words.
**Voice notes:** On WAIS: do not hedge. State the mechanism as a glaciologist would: retrograde bed, grounding line instability, ice shelf buttressing, MISI. This is the section where the author's former research identity should be most legible. On the human example: the Athabasca water constraint is not speculative — it is the subject of active regulatory and operational planning in the region.

---

### Assignment W4.5 — Simulation bridge paragraph

**Topic sentences:** Exercise 4.X asks you to extend this model; the code below is the base case. Run it before reading the interpretation. The result — atmospheric CO₂ continuing to rise even in the reduced-emission scenario — is not a bug in the code. It is what a stock does when inflows still exceed outflows.

**Target:** 2–3 sentences, ~50–60 words. Match Ch 2 register precisely.

---

### Assignment W4.6 — Bridge sentences before each diagram (four sentences)

Each 15–25 words. Name what the diagram shows before the reader sees it.

**Before Diagram 4.0 (five-subsystem overview, in Section 1):**
Name what it shows: the five Earth system stocks and the primary flow connections between them, with the atmosphere as the central coupling medium.

**Before Diagram 4.1 (3-box carbon cycle, in Section 2):**
Name what it shows: the three carbon stocks and the gross flows between them, plus the anthropogenic emission perturbation as a new inflow without a corresponding outflow at the same rate.

**Before Diagram 4.2 (water vapour R loop, in Section 3):**
Name what it shows: the reinforcing loop connecting surface temperature, atmospheric water vapour content, and downwelling longwave radiation — the largest amplifying feedback in the climate system.

**Before Diagram 4.3 (permafrost-methane tipping point, in Section 3):**
Name what it shows: the same two-loop tipping point structure from Chapter 3, applied to the permafrost carbon stock — with Arctic warming as the external stress that tips the system from the frozen balancing state into the thaw-methane reinforcing loop.

---

## 6. Cross-Link Callouts

### Callout 4.A — WH Maths (differential equations for Earth system models)

**Target:** WH Maths Vol 8, Ch 1 (Control, Feedback, Stability) and Ch 3 (Continuum Transport)
**Insertion point:** End of `## Climate feedbacks` section, after the permafrost-methane content and before `---` separator.

**Callout content to specify to Writer:**

The feedback parameters discussed in this section — the ice-albedo feedback parameter, the water vapour feedback parameter, the ocean heat uptake efficiency — are the empirical entries in the Jacobian of the linearised Earth system. The sum of feedback parameters determines the sign of the dominant eigenvalue of the system: negative sum (balancing dominant) → stable equilibrium → finite equilibrium climate sensitivity; positive sum (reinforcing dominant) → runaway. Earth system models are systems of coupled ordinary and partial differential equations, and the question of whether the climate will stabilise at a new equilibrium or continue warming is a question about eigenvalues.

WH Maths Vol 8, Ch 1 (Control, Feedback, and Stability) develops the eigenvalue treatment of feedback systems from first principles, using the same thermostat example from Chapter 2 as the entry point. Ch 3 (Continuum Transport) covers the partial differential equations that govern heat diffusion and mass transport — the mathematical substrate of the ocean heat uptake model and the permafrost active layer model.

**Format:**
```markdown
::: {.callout-note}
## Earth system models as dynamical systems

[text as above, ~100 words, precise mathematical pointer]

[WH Maths Vol 8, Ch 1](https://wayward.house/learn/maths/advanced/) develops the eigenvalue treatment of feedback systems — the same thermostat example from Chapter 2 is the entry point. [Ch 3 (Continuum Transport)](https://wayward.house/learn/maths/advanced/) covers the PDEs governing heat diffusion and mass transport in the ocean and permafrost active layer.
:::
```

---

### Callout 4.B — WH Computational Geography (cryosphere monitoring and remote sensing)

**Target:** WH Computational Geography — cryosphere and mountain systems module, specifically: `glacier-mass-balance.qmd`, `permafrost-thaw-geohazards.qmd`, `snow-accumulation-melt-modeling.qmd`; and environmental systems module: `land-atmosphere-coupling-and-feedbacks.qmd`, `net-radiation-and-albedo.qmd`
**Insertion point:** End of `## Earth system tipping points` section, after the satellite early warning signals data example and before `---` separator.

**Callout content to specify to Writer:**

The satellite monitoring examples in this section — GRACE/-FO for ice mass, MODIS/NDVI for Amazon resilience, AMSR-2 for sea ice — are specific data products produced by processing pipelines whose architecture and physical assumptions are covered in WH Computational Geography. The glacier mass balance methods, the energy balance models for snow and ice, the permafrost thermal models, and the land-atmosphere coupling frameworks are the computational geography counterparts to the systems thinking structures in this chapter.

The systems thinking question is *why* the Earth system exhibits tipping point behaviour. The computational geography question is *how to detect, measure, and model* it using spatial data. Both are necessary: the measurement without the mechanism cannot distinguish a trend that is approaching a tipping point from one that is not.

**Format:**
```markdown
::: {.callout-note}
## Monitoring Earth system tipping points with spatial data

[text as above, ~100 words]

[WH Computational Geography — Cryosphere and Mountain Systems](https://wayward.house/learn/computational-geography/cryosphere-and-mountain-systems/) covers glacier mass balance methods, permafrost thermal models, and snow accumulation/melt modelling — the physical detail behind the GRACE and active layer monitoring examples above. [Environmental Systems](https://wayward.house/learn/computational-geography/environmental-systems/) covers land-atmosphere coupling, net radiation, and vegetation feedbacks — the physical substrate of the Amazon resilience example. Comp Geo Part 4 (Hazards) extends these frameworks to wildfire, flood, and cascading risk.
:::
```

---

### Callout 4.C — WH Data Engineering (Earth observation data pipelines)

**Target:** WH Data Engineering Ch 3 (Pipelines and ETL) and Ch 5 (Streaming and Real-time)
**Insertion point:** End of `## Biogeochemical cycles` section, after the remote sensing / data pipeline domain example and before `---` separator.

**Callout content to specify to Writer:**

The Earth observation data pipeline described in this section — raw satellite imagery → Level-2 geophysical retrievals → Level-3 gridded products → scientific time series — is a multi-stage ETL pipeline at planetary scale. The latency between a real-world cryosphere change and its appearance in a published dataset (months to years) is a delay embedded in the data pipeline, not in the physical system. Understanding this delay matters for any application that tries to use satellite data for near-real-time monitoring: the processing pipeline's stock-flow structure determines how current the data product actually is.

For operational Earth monitoring applications (wildfire detection, flood response, oil spill tracking), streaming near-real-time data architectures have replaced batch processing — the latency has been reduced from days to minutes by redesigning the pipeline's flow structure. The same tradeoff between latency and data quality that governs Earth observation pipelines appears in all high-volume sensor networks.

**Format:**
```markdown
::: {.callout-note}
## Earth observation as a data pipeline problem

[text as above, ~100 words]

[WH Data Engineering Ch 3 (Pipelines and ETL)](https://wayward.house/learn/data-engineering/) covers the architecture of multi-stage data transformation pipelines — the same structure as the satellite data processing chain above, with the same latency-versus-quality tradeoffs. [Ch 5 (Streaming and Real-time)](https://wayward.house/learn/data-engineering/) covers the streaming architectures used for operational near-real-time Earth monitoring. The systems thinking framework is the diagnostic lens; Data Engineering Ch 3 and Ch 5 are the engineering response.
:::
```

---

## 7. Assembly Instructions

### 7.1 Final section order

```
[YAML front matter — as specified in §1]

## The puzzle                                              [NEW — W4.0]
---
## Earth as coupled subsystems                             [NEW — W4.1]
  [W4.6 bridge sentence before Diagram 4.0]
  [Diagram 4.0 — five-subsystem stock-flow Mermaid]
  [> Figure 4.1 caption]
  [Three-domain examples: Earth / Human (oil sands) / Data (EO pipeline)]
---
## Biogeochemical cycles                                   [NEW — W4.2]
  [W4.6 bridge sentence before Diagram 4.1]
  [Diagram 4.1 — 3-box carbon cycle Mermaid]
  [> Figure 4.2 caption]
  [Pre-industrial equilibrium prose]
  [Fossil fuel perturbation prose]
  [Three-domain examples: Earth (Keeling) / Human (industrial metabolism / tailings) / Data (carbon flux RS)]
  [Callout 4.C — WH Data Engineering]
---
## Climate feedbacks                                       [NEW — W4.3]
  [Ice-albedo feedback revisit (1 paragraph — brief)]
  [W4.6 bridge sentence before Diagram 4.2]
  [Diagram 4.2 — water vapour R loop Mermaid]
  [> Figure 4.3 caption]
  [Water vapour feedback prose]
  [Ocean heat uptake as B loop with delay prose]
  [W4.6 bridge sentence before Diagram 4.3]
  [Diagram 4.3 — permafrost-methane tipping point Mermaid]
  [> Figure 4.4 caption]
  [Permafrost-methane feedback prose and tipping point connection]
  [Feedback factor concept — brief]
  [Three-domain examples: Earth (four feedbacks) / Human (oil sands amplifier) / Data (feedback parameter estimation)]
  [Callout 4.A — WH Maths Vol 8]
---
## Earth system tipping points                             [NEW — W4.4]
  [Reconnect to Ch 3 Fig 3.1 — 1 paragraph]
  ### AMOC
    [AMOC prose — mechanism, current state, palaeoclimate evidence]
    [Diagram 4.4 / Fig 4.6 if included — AMOC balancing loop collapse]
  ### West Antarctic Ice Sheet
    [WAIS prose — MISI mechanism, Thwaites, sea level implication]
  ### Amazon dieback
    [Amazon prose — moisture recycling, deforestation threshold, savannification risk]
  [Human domain example: Athabasca water system — 1 paragraph]
  [Data domain example: satellite early warning signals — 1 paragraph]
  [Callout 4.B — WH Computational Geography]
---
## Simulating the carbon cycle: three stocks, one perturbation   [NEW]
  [W4.5 bridge paragraph — Writer]
  [{python} 3-box carbon cycle simulation block]
  [What to try callout]
  [> Figure 4.5 caption]
---
## Exercises                                               [NEW]
  [Exercise 4.1 — system identification]
  [Exercise 4.2 — response time estimation]
  [Exercise 4.3 — feedback identification]
  [Exercise 4.4 — tipping point analysis]
  [Exercise 4.5 — simulation extension]
  [Exercise 4.6 — leverage point analysis]

---
*Status: draft — ...*                                      [UPDATE at assembly]
```

### 7.2 Figure numbering register

| Figure | Type | Content | Location |
|---|---|---|---|
| 4.1 | Mermaid flowchart | Five-subsystem Earth stock-flow overview | `## Earth as coupled subsystems` |
| 4.2 | Mermaid flowchart | 3-box carbon cycle with emission perturbation | `## Biogeochemical cycles` |
| 4.3 | Mermaid graph LR | Water vapour reinforcing loop | `## Climate feedbacks` |
| 4.4 | Mermaid graph LR | Permafrost-methane tipping point structure | `## Climate feedbacks` |
| 4.5 | Python simulation | 3-panel carbon cycle time series | `## Simulating the carbon cycle` |
| 4.6 | Mermaid graph LR | AMOC balancing loop and freshwater stress (optional) | `## Earth system tipping points`, AMOC subsection |

---

## 8. Exercises

Six exercises, two per exercise type from the DESIGN-BRIEF taxonomy:

**4.1 — System identification**
Choose one of the following and draw a stock-flow diagram. Identify all stocks, inflows, outflows, and the variables that control flow rates.
a. The global nitrogen cycle (atmosphere, soil, ocean, and biosphere stocks; key flows: nitrogen fixation, denitrification, agricultural application, runoff)
b. A watershed: from mountain snowpack to river outflow (snowpack stock, groundwater stock, river discharge stock; flows: accumulation, melt, infiltration, evapotranspiration, streamflow)
c. The Athabasca oil sands system (bitumen in ground, pipeline inventory, tailings pond — three stocks; flows as described in this chapter)
d. A coral reef (coral cover, algae cover, grazer population — the three stocks from Figure 3.2 in Chapter 3, extended to include human fishing pressure as an additional outflow)

**4.2 — Response time estimation**
The West Antarctic Ice Sheet holds approximately 3.3 million km³ of ice. The current net outflow (calving + basal melt, net of accumulation) from the WAIS is approximately 150 km³/year and is accelerating.
a. Using the response time formula from Chapter 1 ($\tau = S / |F_{\text{net}}|$), estimate how long the WAIS would persist at the current net loss rate.
b. This answer is obviously wrong as an engineering estimate of when sea level will reach its full response — why? What does this tell you about applying the linear response time formula to a system near a tipping point?
c. What would the permafrost carbon stock's response time be if the current net emission rate from permafrost is approximately 0.5 GtC/yr (net decomposition minus new carbon added)? What happens to this response time if warming accelerates thaw to 2 GtC/yr?

**4.3 — Feedback identification**
For each of the following, identify whether the feedback is reinforcing or balancing, and draw a causal loop diagram:
a. Melting Arctic sea ice and the polar vortex: reduced sea ice → reduced temperature gradient between equator and pole → weaker polar vortex → more warm air intrusion into Arctic → more sea ice melt
b. Ocean acidification and coral calcification: higher atmospheric CO₂ → more dissolved CO₂ in ocean → lower pH → reduced carbonate ion availability → slower coral skeleton growth → reduced reef structural complexity → reduced fish habitat → reduced grazer population → more algae → more smothering of coral → less coral calcification
c. Carbon fertilisation: higher atmospheric CO₂ → higher photosynthesis rate → more biomass → more respiration when organisms die → more CO₂ released (note: this one requires you to identify whether the net loop is reinforcing or balancing)
d. Permafrost insulation: high permafrost carbon stock → intact tundra vegetation → insulating organic layer → lower ground temperatures → slower thaw → more carbon retained in permafrost

**4.4 — Tipping point analysis (connects to Ch 3 Exercise 3.3)**
The Atlantic Meridional Overturning Circulation (AMOC) is exhibiting possible early warning signals: the variance of proxy records (such as sea surface temperature fingerprints and sediment cores) has increased over the past century, and some analyses suggest reduced recovery rates after perturbation — consistent with "critical slowing down" theory.
a. Using the framework from Chapter 3 and Figure 4.6 in this chapter, describe the mechanism by which AMOC could cross a tipping point. What is the stock, the balancing feedback, the external stress, and the reinforcing loop that would take over?
b. If AMOC tips to a much weaker state, what are the downstream consequences for the other Earth system stocks described in this chapter? Trace at least two causal pathways.
c. What observational data would you monitor to track AMOC resilience — not just its current strength, but its proximity to the tipping point? (Hint: the answer is not just "observe AMOC strength.")

**4.5 — Simulation extension**
Using the carbon cycle simulation from this chapter as a base:
a. Add a fourth scenario — "net-zero by 2050" — where emissions follow the historical trajectory to 2023, then decline linearly to zero by 2050, and are held at zero from 2050 to 2150. What happens to the atmospheric CO₂ stock? Does it stabilise? Does it fall back toward pre-industrial levels? Why or why not?
b. Implement an ocean sink saturation effect: reduce `k_AO` by 0.5% per year from 2023 onward (compounding). This simulates the gradual reduction in ocean uptake efficiency as the surface ocean acidifies and carbonate chemistry shifts. How does this change the atmospheric CO₂ trajectory in Scenario 2 (reduced emissions)?
c. In the simulation, the land biosphere and ocean are modelled as passive sinks — they absorb more when the atmosphere is enriched, but they do not actively reduce their outflows in response to warming. How would you represent the Amazon dieback tipping point (Section 4.4) in this model? What change to the model structure — not just to a parameter — would be needed?

**4.6 — Leverage point analysis**
Apply Meadows' leverage point hierarchy (Chapter 8 preview) to the Earth's carbon cycle system:
a. Identify one intervention at the level of *flow rates* (e.g., increasing the rate of reforestation). What are the limits to this intervention? Why might it fail to return the atmospheric stock to pre-industrial levels even if implemented at scale?
b. Identify one intervention at the level of *feedback structure* (e.g., enhancing ocean carbon uptake). What would need to change in the Earth system's feedback structure for this to work? What are the risks of inadvertently strengthening a different reinforcing loop?
c. The most powerful leverage points in Meadows' hierarchy involve *goals* and *paradigms*. What would it mean to change the "goal" of the global economy as a stock-flow system? What paradigm shift would be required, and what feedback structures would need to be redesigned to reflect the new goal?

---

## 9. Deliverables Checklist

### Writer
- [ ] Opening puzzle prose — Keeling Curve, ~350 words (W4.0)
- [ ] Earth as coupled subsystems prose — three domains, ~700 words (W4.1)
- [ ] Biogeochemical cycles prose — three domains, ~850 words (W4.2)
- [ ] Climate feedbacks prose — four feedbacks + three domains, ~900 words (W4.3)
- [ ] Earth system tipping points prose — three elements + two domain examples, ~1100 words (W4.4)
- [ ] Simulation bridge paragraph — ~60 words (W4.5)
- [ ] Four bridge sentences before diagrams — ~20 words each (W4.6)
- [ ] Six exercises (4.1–4.6)

### Simulation Engineer
- [ ] `{python}` 3-box carbon cycle block with `#| label: fig-carbon-cycle` and `#| fig-cap:`
- [ ] Named constants block: `A0`, `O0`, `L0`, `k_AO`, `k_AL`, `F_OA_const`, `F_LA_const`, `F_W`, `F_V`, `dt`, `YEARS_START`, `YEARS_END`
- [ ] `def emissions(t, scenario):` function
- [ ] Three scenarios: equilibrium validation, BAU, reduced emissions (+ reduced with low land sink variant as dashed line)
- [ ] 3-panel figure: atmospheric CO₂ (ppm), ocean carbon (GtC), land carbon (GtC)
- [ ] `ax.annotate` annotations (no legend); WH palette (`#d52a2a`, `#111111`, `#888888`)
- [ ] `.callout-tip` "What to try" block (including pipeline mapping question)
- [ ] `> Figure 4.5` caption
- [ ] `plt.savefig("_assets/ch04-carbon-cycle.png", dpi=150, bbox_inches="tight")`

### Diagram Specifier
- [ ] Mermaid block: Diagram 4.0 — five-subsystem Earth stock-flow overview (Fig 4.1)
- [ ] Mermaid block: Diagram 4.1 — 3-box carbon cycle with emission perturbation (Fig 4.2)
- [ ] Mermaid block: Diagram 4.2 — water vapour reinforcing loop (Fig 4.3)
- [ ] Mermaid block: Diagram 4.3 — permafrost-methane tipping point (Fig 4.4)
- [ ] Mermaid block: Diagram 4.4 — AMOC balancing loop collapse (Fig 4.6, optional)
- [ ] `> Figure N.M.` caption for each

### Assembly and QA
- [ ] Three `.callout-note` cross-link callouts inserted at specified points (4.A, 4.B, 4.C)
- [ ] All `> Figure N.M.` captions present and numbered correctly (4.1–4.5, 4.6 if AMOC diagram included)
- [ ] YAML front matter updated with subtitle, axiom, rewrite, opens_to, destinations
- [ ] Status line updated to `draft`
- [ ] `DESIGN-BRIEF.md` status row for `04-earth-as-a-system` updated to `draft`

### QA notes for assembler
- Verify pre-industrial equilibrium: run Scenario 0 in isolation and confirm all three stocks hold steady (within ±1 GtC) before assembling the full simulation section
- Verify ppm conversion: 1 ppm CO₂ = 2.13 GtC; pre-industrial 590 GtC = 277 ppm — close to the accepted 280 ppm. Acceptable given simplified model structure
- Verify that `k_AO = 90/590` and `k_AL = 120/590` reproduce the pre-industrial equilibrium flows when multiplied by `A0 = 590`
- Mermaid diagrams: confirm `graph LR` (not `flowchart`) for causal loop diagrams (Figs 4.3, 4.4, 4.6); confirm `flowchart LR` for stock-flow diagrams (Figs 4.1, 4.2)
- Cross-check that the four feedbacks in `## Climate feedbacks` are consistent with the simulation's structure: ice-albedo and water vapour are *not* explicitly modelled in the 3-box carbon cycle simulation (they are climate feedbacks, not carbon cycle feedbacks); this distinction should be stated clearly in the prose to prevent reader confusion

---

*End of plan. Chapter 4 is the largest chapter in Phase 2. Estimated total prose: 4,000–5,000 words plus simulation code (~100 lines) and six diagrams. The simulation is the hardest deliverable — the equilibrium initialisation and the concentration-dependent uptake equations must be verified before the scenarios are run. Recommend the Simulation Engineer complete the equilibrium validation run first and share the equilibrium output before proceeding to the perturbation scenarios.*

---

### Critical Files for Implementation

- `/Users/pauldhobson/src/websites/waywardhouse-systems-thinking/04-earth-as-a-system.qmd` — the target file, currently empty; all deliverables are assembled here
- `/Users/pauldhobson/src/websites/waywardhouse-systems-thinking/DESIGN-BRIEF.md` — voice, palette, cross-link targets, and status table; status row for Ch 4 must be updated to `draft` on completion
- `/Users/pauldhobson/src/websites/waywardhouse-systems-thinking/02-feedback-structures.qmd` — reference for diagram style (graph LR, WH palette, inline node styling, `> Figure N.M.` caption format, `.callout-note` and `.callout-tip` structure)
- `/Users/pauldhobson/src/websites/waywardhouse-systems-thinking/03-complexity-and-emergence.qmd` — reference for tipping point section structure, Schelling simulation code style, and the three-callout cross-link pattern
- `/Users/pauldhobson/src/websites/waywardhouse-systems-thinking/_assets/` — target directory for `ch04-carbon-cycle.png`; simulation save path must match exactly