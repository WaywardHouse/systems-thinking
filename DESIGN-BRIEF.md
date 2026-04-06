# Design Brief: Systems Thinking for Engineers

## What this book is

A book for engineers who need to reason about systems that push back. Glaciers, supply chains, cities, machine learning pipelines, wildfire fronts, housing markets — these are systems with feedback, delays, nonlinearity, and emergent behaviour. Standard engineering training teaches you to optimise components. This book teaches you to understand the whole.

## Intellectual lineage

- **Donella Meadows** — *Thinking in Systems* (2008): the accessible entry point, stocks/flows/feedback, archetypes, leverage points. The prose voice this book aspires to: dry, precise, occasionally wry.
- **Jay Forrester** — system dynamics: stock-flow simulation, policy resistance, counterintuitive behaviour of complex systems. The mathematical machinery beneath Meadows.
- **Santa Fe Institute** — complexity science: emergence, phase transitions, adaptive systems, fitness landscapes.
- **W. Ross Ashby** — cybernetics: requisite variety, homeostasis. The engineering control theory connection.
- **Norbert Wiener** — feedback and control as a unifying idea across biology, engineering, and society.

## What it is not

- Not a soft "systems thinking" course that replaces rigour with diagrams and buzzwords
- Not a survey of complexity science for its own sake
- Not a programming manual (though simulation code is included)
- Not a management textbook with "systems thinking" rebranded

## Core design principle

Every chapter opens with a real system that behaves counterintuitively. The reader should feel the puzzle before they see the framework. The framework is earned by the puzzle, not front-loaded.

Three examples per chapter: one from earth systems, one from human/economic systems, one from data/AI systems. This is the ESDE program in miniature — the same conceptual move works across all three domains.

## Voice

Dry. Precise. Occasionally terse. Like Meadows at her best: the prose does not oversell. It states the mechanism and lets the reader feel its force.

Avoid:
- Jargon that hasn't been earned by the surrounding explanation
- Optimism about systems thinking as a magic tool ("if everyone just thought in systems...")
- Bullet-pointed lists where prose reasoning belongs

Use:
- Numbered list only for procedural sequences (steps in building a model)
- Tables for comparisons that would be tedious in prose
- Code blocks for all simulation implementations

## Repeating visual threads

1. **Causal loop diagrams** — standard notation (+ / − arrows, R / B loop labels, delays as double lines). Introduced in Ch 1, used throughout. Never decorative — every diagram earns its place by showing something the prose cannot.

2. **Stock-flow diagrams** — introduced in Ch 1 alongside causal loops. Shown in Stella/Vensim style, then implemented in Python. By Ch 7, readers can build their own.

3. **Time-series archetypes** — plots showing the signature behaviour of each feedback archetype: exponential growth, goal-seeking, oscillation, overshoot and collapse. Real data examples wherever possible.

4. **Phase portraits** — introduced in Ch 2 (feedback) and again in Ch 3 (complexity). Connects to WH Maths Vol 8 (control theory, dynamical systems).

## Mathematical register

- **Ch 1–3:** No calculus required. Systems thinking is diagram-first and accessible to Year 1 students.
- **Ch 4–5:** Light differential equations (rate of change, equilibrium, linearisation). Connects to WH Maths Vols 5–7.
- **Ch 6–8:** Stock-flow simulation in Python. Differential equations as the mathematical substrate. Students who want depth are pointed to WH Maths Vol 8 (Ch 1: Control, Feedback, Stability).

## Exercise types (per chapter)

1. **System identification:** Given a description of a real system, draw the causal loop diagram. Identify all feedback loops and label them.

2. **Archetype recognition:** Given a time-series plot or a news story, identify which system archetype is operating.

3. **Simulation build:** Given a verbal description, implement a stock-flow model in Python (using the `pysd` or `pystock` library, or a raw ODE solver). Run it. Vary one parameter. What changes?

4. **Leverage point analysis:** Given a system diagram, apply Meadows' leverage point hierarchy. Which interventions would be most effective? Which would have unintended consequences?

## Cross-links to other WH books

- **→ WH Maths Vol 8 (Ch 1: Control, Feedback, Stability):** The same mathematics in engineering control theory language. Students who want formal treatment of eigenvalues and stability in feedback systems should go here.
- **→ Comp Geo Part 4 (Hazards):** Ch 4 of this book (Earth as a System) is the conceptual precursor to wildfire spread and flood feedback dynamics in Comp Geo.
- **→ Comp Geo Part 5 (Economic Systems):** Ch 5 (Cities and Economies as Systems) is the systems thinking lens on the models in Comp Geo Part 5.
- **→ Data-AI Ch 3 (Optimisation):** Loss landscapes in ML are energy landscapes in system dynamics terms. Ch 6 of this book makes the connection.
- **→ Data Engineering Ch 7–8 (Governance, ML Platforms):** Concept drift = system failure from feedback starvation. Ch 6 of this book is the framework; Data Engineering Ch 7–8 are the engineering response.

## Build priority

**Phase 1 (now — ESDE 106, Semester 1):** Ch 1–3  
**Phase 2 (Year 3 support):** Ch 4–5  
**Phase 3 (Year 4 support):** Ch 6–8  

## Status tracking

| Chapter | Status | Notes |
|---------|--------|-------|
| 01-what-is-a-system | draft | Simulation, Mermaid diagrams, cross-links assembled |
| 02-feedback-structures | draft | Reinforcing/balancing loops, five archetypes, delay dynamics, thermostat simulation, five Mermaid causal loop diagrams assembled |
| 03-complexity-and-emergence | draft | Tipping points (3 examples, 3 Mermaid diagrams), Schelling simulation, emergence/complexity distinction, data/AI resilience example, 3 cross-link callouts assembled |
| 04-earth-as-a-system | draft | Keeling Curve puzzle, five Earth system stocks (Fig 4.1–4.2), four climate feedbacks (Figs 4.3–4.4), AMOC/WAIS/Amazon tipping points (Fig 4.6), oil sands + EO pipeline examples throughout, 3-box carbon cycle simulation four scenarios 1750–2150 (Fig 4.5), three cross-link callouts, six exercises assembled |
| 05-cities-and-economies-as-systems | draft | Zipf's Law puzzle, seven sections, four Mermaid diagrams (Figs 5.1–5.4), two-city agglomeration simulation three scenarios (Fig 5.5), Alberta oil sands + Fort McMurray + Detroit inversion examples, three cross-link callouts, six exercises assembled |
| 06-data-as-a-system | draft | Spam filter puzzle, data pipelines as stock-flow, four ML feedback loop types, loss landscapes as energy landscapes, concept drift taxonomy (data/label/prior), retraining simulation three scenarios (Fig 6.5), GRACE gap + Arctic classifier + COVID credit scoring examples, three cross-link callouts, six exercises assembled |
| 07-modelling-and-simulation | draft | World3/Limits to Growth puzzle, modelling cycle (Fig 7.1), glacier mass balance CLD+SFD (Figs 7.2–7.3), supply chain bullwhip simulation (Fig 7.5), wrong-boundary diagram (Fig 7.4), three cross-link callouts, six exercises assembled |
| 08-systems-intervention | draft | Grand Banks puzzle, policy resistance archetypes (Fig 8.1), Meadows 12 leverage points (Fig 8.2), three-domain intervention hierarchy (Fig 8.3), Gordon-Schaefer fishery simulation three scenarios (Fig 8.4), cobra effect + Jevons + Goodhart, three cross-link callouts, six exercises + capstone assembled |
