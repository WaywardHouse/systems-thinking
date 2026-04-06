# CHAPTER-08-PLAN.md — Chapter 8 Production Plan: "Systems Intervention"

**Status at plan date:** 2026-04-05
**For agents:** Writer, Simulation Engineer, Diagram Specifier
**What exists:** Stub (`08-systems-intervention.qmd`, 3 lines) — full design required.
**Role in book:** Final chapter. Applies the complete vocabulary (Chs 1–7) to the question of change.
Every section should feel like a synthesis, not just new material.

---

## 1. Chapter-Level Design

### YAML Front Matter

```yaml
---
title: "Systems Intervention"
subtitle: "Where to change a system — and why the obvious place is usually wrong"
status: seed → draft
axiom: "The places where systems are most easily changed are the places where change has the least effect. The places where change matters most are the places that are hardest to reach."
rewrite: "Structural change is more durable than parameter adjustment. A rule that automatically corrects a stock is worth more than a quota that must be re-set each year by a committee under economic pressure."
opens_to:
  - course: ESDE 402
    relationship: anchors
  - text: "WH Computational Geography (all parts)"
    relationship: applies
destinations:
  - field: earth
    hook: "In 1992, the Canadian government declared an indefinite moratorium on cod fishing in the Grand Banks. Five centuries of the world's most productive fishery ended in a single announcement. Everyone who managed the fishery — biologists, regulators, politicians, fishing communities — had been doing their jobs. The collapse was not caused by ignorance or corruption. It was caused by intervening at the wrong place in the system: adjusting quota numbers while leaving intact the economic feedback loop that drove escalating effort regardless of what the quotas said."
  - field: human
    hook: "Rent control is one of the most studied policy interventions in economics. The short-run effect — lower rents for current tenants — is exactly what the policy targets. The long-run effects — reduced housing supply, decreased maintenance investment, reduced residential mobility — operate through feedback loops that the intervention did not touch. The intervention was applied at LP 12 (a number: the maximum allowable rent). The effects that undermined it operated at LP 10 and LP 8 (material flow structure and balancing loop strength)."
  - field: data
    hook: "Goodhart's Law: when a measure becomes a target, it ceases to be a good measure. A model accuracy metric used as a performance target for an ML team will be optimised — but not necessarily by improving the model. The team may adjust thresholds, select test sets, or filter evaluation data. Goodhart's Law is a systems dynamics result: intervening at LP 12 (the number: the accuracy score) while leaving intact the incentive structure that determines how the number is produced creates a new reinforcing loop that erodes the measurement signal."
---
```

### Opening Puzzle

**The Grand Banks cod collapse (1992).**

The Grand Banks off Newfoundland supported one of the most productive marine fisheries in human history. John Cabot's 1497 expedition reported cod so dense the sea could barely be crossed. By the 1960s, the annual harvest was still 250,000 tonnes. By 1992, the Canadian government declared an indefinite moratorium: the cod stock had collapsed to below 1% of its 1960s level. 30,000 jobs disappeared. The fishery has not meaningfully recovered in thirty years.

The puzzle is what did not cause the collapse. There was no fraud, no regulatory capture, no willful irrationality. Biologists assessed the stock annually using scientifically defensible methods. Regulators set quotas based on those assessments. Fishing industry representatives lobbied for higher quotas, as any economic actor in their position would. Politicians balanced conservation objectives against the economic survival of coastal communities, as politicians are expected to do. Fishers fished to the quota.

The management system did exactly what it was designed to do. The fishery collapsed anyway.

The explanation requires looking at the feedback structure, not the actors. Annual stock assessments fed into annual quota-setting processes, but the quota-setting process was subject to economic and political pressure that consistently produced quotas above what biologists recommended. The stock declined. Higher prices per tonne (scarcity premium) increased the economic incentive to fish. More effort was deployed. The stock declined further. The management system was in a reinforcing loop with the economic system — each year's decline made the economic pressure for higher quotas stronger, not weaker. The balancing loop that should have corrected the stock — lower quotas in response to declining surveys — was consistently overwhelmed by the reinforcing loop of economic pressure.

The quota was the intervention. It targeted the harvest rate — a number, a parameter. It did not address the economic feedback that drove the quota-setting process. It did not change the information structure (who gets the stock assessment, when, and how it is used). It did not change the rules (who has standing to set quotas and under what constraints). It did not change the goal (which was implicitly to maintain fishing industry income, not to maintain the fish stock). Every year, the intervention was applied at the least effective place in the system, while the most effective places remained untouched.

This is the subject of the chapter.

---

## 2. Section Structure

### Section overview

| # | Section title | Domain examples | Diagram? | Cross-link callout? |
|---|---|---|---|---|
| 0 | The puzzle (Grand Banks) | Earth only | None | No |
| 1 | Why interventions fail | Earth: quota failure; Human: rent control; Data: Goodhart | Mermaid 8.1 (Grand Banks reinforcing loop) | No |
| 2 | The leverage point hierarchy | All three domains across the 12 levels | Mermaid 8.2 (grouped hierarchy) | No |
| 3 | Leverage points applied | Earth: climate policy; Human: opioids/housing; Data: ML fairness | Mermaid 8.3 (same loop, three intervention depths) | WH Comp Geo |
| 4 | Unintended consequences | Earth: DDT; Human: cobra effect / rent control; Data: Goodhart | None (prose examples) | WH Maths Vol 8 |
| 5 | Principles for effective intervention | Synthesis across all chapters | None | WH Data Engineering |
| 6 | Simulation: fishery management | Earth/economic hybrid | Python fishery + Fig 8.4 | No |
| 7 | Exercises | — | — | — |

---

### Section 0: The puzzle

**Purpose:** Make visible the distinction between "the right actor doing the wrong thing" (ordinary failure) and "the right actor doing the right thing in the wrong place in the system" (systems failure). The Grand Banks is the cleanest example of the latter.

**Content:**
- Keeling Curve of cod production: 250,000 tonnes in 1960s → zero by 1992
- Who was doing their job: biologists, regulators, politicians, fishers
- The reinforcing loop that quota adjustments did not address: declining stock → scarcity premium → increased economic incentive → political pressure for higher quotas → declining stock
- Collapse was not the failure of an actor. It was the failure of an intervention targeted at LP 12.
- Close: the question is not "who is to blame?" The question is "where in the system could the intervention have been applied to produce a different outcome?"

**Target:** 500 words. Voice: precise, restrained. The drama is in the facts, not the adjectives.

**Separator:** `---`

---

### Section 1: Why interventions fail

**Header:** `## Why interventions fail`

**Purpose:** Establish three mechanisms of intervention failure that recur across domains.

**Three mechanisms:**

*Policy resistance.* The system pushes back against the intervention. Every balancing loop in the system has a goal, and interventions that adjust outputs without changing goals or feedback structures will be corrected by those loops. Raising the minimum wage (LP 12) without changing the labour market structure (LP 10) or the goal of profit maximisation (LP 3) is resisted by employment adjustments, automation, and geographic relocation of production — the balancing loops of the labour market. The intervention is real; the resistance is real; the long-run effect is smaller than the short-run effect and may be opposite in sign.

*Counterintuitive behaviour.* The most intuitively obvious intervention often makes the problem worse. Forrester's Urban Dynamics (1969): building more low-income housing in declining cities attracted low-income residents but did not create the jobs or services they needed, worsening the economic conditions that had driven them there. The counterintuitive result is not a paradox — it is a predictable consequence of reinforcing loops that the intervention strengthened rather than weakened.

*Fixes that fail.* From Chapter 2's archetype library: a symptomatic fix (adjusting a parameter to treat an output symptom) provides short-term relief while allowing the underlying structural problem to worsen. Quota adjustments in the Grand Banks were a fix that failed: each adjustment provided short-term relief to the fishing industry while the underlying structural problem (the reinforcing loop of economic pressure) continued. The fix delayed the confrontation with the structural problem — and by delaying it, made it more severe.

**Three-domain examples (brief, one paragraph each):**
- Earth: Annual catch quotas (LP 12) vs. ecosystem-based fisheries management (LP 5)
- Human: Rent control (LP 12 — the rent ceiling number) vs. housing supply reform (LP 4 — allowing new structures to be built)
- Data: Accuracy threshold monitoring (LP 12) vs. retraining trigger rules (LP 6 — changing the information structure) vs. optimisation objective redesign (LP 3)

**Diagram 8.1:** Grand Banks reinforcing loop — causal loop diagram showing:
- Cod stock → catches → revenue per vessel → fishing effort → catches (reinforcing)
- Annual quota → catches (balancing, but weak under pressure)
- Show the quota as a severed or bypassed balancing loop

**Target:** 700 words. Voice: analytical, pattern-focused. These are mechanisms, not morality tales.

**Separator:** `---`

---

### Section 2: The leverage point hierarchy

**Header:** `## The leverage point hierarchy`

**Purpose:** Introduce Meadows' 12 leverage points as the organising framework for the rest of the chapter. Make the hierarchy intuitive, not just a list.

**Framing:**
In 1999, Donella Meadows published a short essay that has become one of the most-cited pieces in systems thinking: "Leverage Points: Places to Intervene in a System." The argument is that some places in a system are much more sensitive to intervention than others, and that the places most sensitive to intervention are not where we instinctively look.

The 12 leverage points, numbered from least effective (12) to most effective (1). Present them in four groups for coherence.

**Group 1 — Physical structure (LP 9–12): Hardest to change, lowest leverage**

*LP 12: Numbers — constants, parameters, subsidies, standards, taxes.* The most common intervention target. Adjusting the quota, changing the interest rate, setting a carbon tax. These matter — a poorly set number can cause real damage — but they rarely change the qualitative behaviour of a system. The system is the same system with a different knob setting.

*LP 11: Buffer stocks, relative to flows.* The size of a buffer determines how long a system can absorb shocks. Larger grain reserves make food supply more stable. Larger cash reserves make banks less fragile. Buffer sizes are expensive to change physically and politically.

*LP 10: Structure of material flows.* The transportation network, the age structure of a population, the layout of the electricity grid. These determine what flows are even possible. Very low leverage in the short term — infrastructure is expensive and slow to change.

*LP 9: Lengths of delays, relative to system change rate.* As established in Chapter 2 and Chapter 7: delays are load-bearing. Reducing a supply chain delay (Chapter 7) reduces the bullwhip amplitude more than proportionally. Delays are physically changeable — this is engineering — but often require significant investment.

**Group 2 — Feedback and information (LP 6–8): Designed, medium leverage**

*LP 8: Strength of negative feedback loops.* Balancing loops are what keep systems at their goals. A well-tuned thermostat is more effective than a poorly tuned one. Strengthening a weak balancing loop (adding sensors, improving actuation) is higher leverage than adjusting the setpoint (LP 12).

*LP 7: Gain around reinforcing loops.* Reducing the gain of a runaway reinforcing loop is high leverage. Removing the economic subsidy that makes fossil fuel extraction cheap is attacking the gain on a reinforcing loop (cheaper fuel → more extraction → more revenue → more investment in extraction). This is higher leverage than taxing the output.

*LP 6: Structure of information flows — who has access to what, and when.* This is one of the most accessible high-leverage points, and the most overlooked. Most systems failures involve agents making decisions without access to the information that would change their decisions. The annual cod stock assessment was available — but it was not embedded in the decision structure in a way that constrained the quota-setting process. Giving fishers real-time electronic stock monitoring (and making their quotas automatically scale with what they see) is a structural information change. It changes the feedback structure, not just a number.

*LP 5: Rules — incentives, constraints, punishments.* The rules of a system determine who can do what. Changing the rules is high leverage because it changes the behaviour of every agent simultaneously. Individual Transferable Quotas in fisheries (the structural change that saved the Icelandic fishery and the New Zealand fishery) are a rule change: they created a property right in the fish stock that gave every fisher an economic incentive to conserve it. The same economic agents, the same fishing grounds — different rules, different outcome.

**Group 3 — Goals and self-organisation (LP 3–4): High leverage, hard to access**

*LP 4: Power to add, change, evolve, or self-organise system structure.* The ability to change the feedback structure itself. Not setting a quota, not changing the rules about quotas — changing what kinds of management institutions are possible. This is the leverage point of institutional design.

*LP 3: Goals of the system.* The purpose or function of the system as it is embedded in a larger system. What is the fishery management system for? If its goal is "maintain fishing industry income," it will do that — to the detriment of the fish stock. If its goal is "maintain the marine ecosystem," the quota-setting process changes structurally, not just numerically. Goal changes are high leverage but require the entities in the system to accept the new goal, which is why they are rare and contested.

**Group 4 — Paradigm (LP 1–2): Transcendent, very rare**

*LP 2: Mindset or paradigm.* The shared ideas, beliefs, values, and assumptions from which the system arises. "Fisheries are a commons, and commons are to be maximally exploited" is a paradigm. "Fisheries are ecosystems we are embedded in" is a different paradigm. The transition from one to the other is not achieved by adjusting a quota. It is achieved by persistent evidence, cultural shift, and leadership.

*LP 1: The power to transcend paradigms.* To recognise that no paradigm is the final truth, and that any of them could be wrong. This is Meadows' highest leverage point, and the most difficult to describe. Its practical manifestation in governance: the institutional capacity to run controlled experiments, admit failure, change course. In data systems: treating model assumptions as hypotheses rather than facts.

**Diagram 8.2:** Vertical display of the 12 leverage points grouped into four tiers. Simple, clear. The numbers go from bottom (LP 12 = physical, low leverage) to top (LP 1 = paradigm, highest leverage). The groups are visually distinct.

**Target:** 900 words. Voice: expository but sharp. Do not list without explaining. Every leverage point should earn its place by reference to a real example.

**Separator:** `---`

---

### Section 3: Leverage points applied

**Header:** `## Leverage points applied`

**Purpose:** Show the hierarchy in action across all three domains using the same structural question applied at different leverage points.

**Climate policy (Earth domain):**

The behaviour of concern: atmospheric CO₂ continues to rise at ~2.4 ppm/year. The system: global energy economy with reinforcing loop of fossil fuel extraction, infrastructure investment, and consumer demand. What would interventions at each leverage point look like?

- LP 12 (carbon tax): adjusts the price of carbon. Higher cost → reduced demand at the margin. Resisted by economic competitiveness concerns. Effect eroded by substitution and efficiency gains that allow continued high absolute emissions. Useful but not sufficient alone.
- LP 9 (reducing energy system delays): faster permitting for renewables, faster grid interconnection. Reduces the construction lag that currently makes clean energy supply slow to respond to demand signals.
- LP 6 (information structure): transparent, real-time carbon accounting at the product level (lifecycle emissions embedded in prices). Gives buyers and producers the information to make different decisions without a mandate. High leverage because it changes decisions across the entire economy simultaneously.
- LP 5 (rules): fossil fuel subsidy removal (restructuring the rules that make fossil fuel competitive). Carbon budget law (making the goal — net zero by date — a legal constraint rather than a policy aspiration). Harder to implement than LP 12, much more durable.
- LP 3 (goal): reframing from "minimise economic cost of transition" to "maintain atmospheric carbon within safe operating boundaries." Goal changes at the international treaty level. The Paris Agreement is a partial goal-level change — it sets a goal but leaves the rules for achieving it to national governments.

**Opioid crisis (Human domain):**

The behaviour of concern: opioid overdose deaths rose from ~8,000/year in 1999 to >80,000/year by 2021 in the United States, driven by sequential shifts from prescription pills to heroin to illicit fentanyl.

- LP 12 (supply restriction): DEA scheduling changes, prescriber limits. The system responded by shifting demand to less regulated substitutes. Classic policy resistance.
- LP 9 (delay): rapid naloxone (overdose reversal) distribution shortens the delay between overdose and death. Not a structural fix, but buys time.
- LP 6 (information): fentanyl test strips, drug checking services. Changes the information available to users at the point of decision. High leverage relative to cost.
- LP 5 (rules): treatment-on-demand laws, removing prior authorisation requirements for addiction medication, reclassifying addiction as a chronic disease rather than a criminal status.
- LP 3 (goal): the treatment goal of the healthcare system in this domain was historically "abstinence." Harm reduction as a goal reframes what success looks like and enables a completely different set of interventions.

**ML system fairness (Data domain):**

The behaviour of concern: a loan approval model produces disparate outcomes across demographic groups that cannot be fully explained by creditworthiness factors.

- LP 12 (threshold adjustment): set different decision thresholds by group. Immediately implementable. Resisted because it requires explicit demographic classification, may not satisfy regulatory definitions of fairness, and does not address the training data problem.
- LP 10 (feature set): remove features that are proxies for protected characteristics. Changes the material flow structure of information into the model.
- LP 6 (information structure): require the model to produce explanations for each decision that are auditable. Changes the information available to the applicant and to regulators.
- LP 5 (rules): mandatory algorithmic audits, fairness certification requirements.
- LP 3 (goal): redefine the optimisation objective from "minimise default rate" to "minimise default rate subject to demographic parity constraint." Requires the goal of the model to change, which in turn requires the goal of the institution to change.

**Diagram 8.3:** A causal loop diagram with three different intervention arrows at LP 12, LP 6, and LP 3. Same underlying loop structure — three depths of intervention. Clean visual illustration of the hierarchy concept.

**Cross-link callout:** WH Computational Geography. The leverage point analysis applied to climate policy above — information structure, rules, and goal changes — maps directly to the policy instruments analysed in Comp Geo Parts 3 and 5. The systems thinking framework provides the structural rationale for why some instruments are more durable than others; Comp Geo provides the empirical case studies.

**Target:** 750 words. Voice: applied, specific. Name real policy instruments. The reader should feel they could apply this framework tomorrow.

**Separator:** `---`

---

### Section 4: Unintended consequences

**Header:** `## Unintended consequences`

**Purpose:** Show that unintended consequences are not random — they are predictable from the leverage point level of the intervention.

**The mechanism:**

LP 12 interventions (adjusting a number) produce the most predictable unintended consequences, because the system structure that remains unchanged continues to operate. The consequences are the other outputs of the same unchanged structure, now driven by the adjusted parameter. Higher carbon tax → energy poverty in low-income households (who spend a larger fraction of income on energy). Minimum wage increase → reduced entry-level hiring in price-competitive sectors. These are not surprises — they are predictable from the model.

Higher leverage interventions (LP 5, LP 3) produce less predictable consequences, because changing rules or goals activates feedback loops that were previously dormant or suppressed. These are harder to anticipate from the model because the model's own structure is changing. This is not an argument against high-leverage intervention — it is an argument for careful monitoring when high-leverage intervention is used.

**Three examples:**

*The cobra effect.* British colonial administration in India offered bounties for dead cobras to reduce the snake population. Enterprising citizens bred cobras for the bounty. When the programme was cancelled, they released the cobras. The cobra population increased. LP 12 intervention (the bounty = a number) created a new reinforcing loop (profit → breeding) that the original model did not include. The unintended consequence was predictable once the reinforcing loop was visible, but the policy was designed without modelling the system it was intervening in.

*Jevons paradox.* In 1865, William Stanley Jevons observed that more efficient steam engines, rather than reducing coal consumption, dramatically increased it: lower cost per unit of work made coal-powered machinery economically attractive for more uses. Every major efficiency improvement in the 20th century has shown the same pattern: more efficient cars → more driving; more efficient buildings → larger buildings. LP 12 (efficiency standards) is consistently undermined by the feedback loop at LP 7 (gain of reinforcing loop: cheaper energy use → more energy use → more investment in energy-using systems). The paradox is a direct consequence of intervening at LP 12 without addressing the reinforcing loop at LP 7.

*Goodhart's Law.* In data systems: any metric used as a target will be optimised — but optimisation of the metric and optimisation of the underlying reality it was measuring are only the same thing when there is no feedback between the metric and the decision-making process. When there is feedback (as there always is, in production), the metric drifts from the reality. This is the LP 12 failure mode in measurement systems. The structural fix is LP 6: change the information structure so that decision-makers cannot see the metric they are being evaluated on while they are making decisions — or change LP 5 so the rules for evaluation use multiple independent metrics that cannot all be simultaneously optimised.

**Cross-link callout:** WH Maths Vol 8 (Bifurcation Theory). The stability threshold identified in Chapter 7 — the point at which a system transitions from one qualitative behaviour mode to another — is also the point at which a leverage point intervention may have a qualitatively different effect than expected. Near a bifurcation, small changes in LP 12 (parameter values) can produce large, discontinuous changes in system behaviour. The formal theory of what happens to system behaviour near bifurcation points — and what that implies for intervention design — is the subject of WH Maths Vol 8, Ch 3.

**Target:** 650 words. Voice: analytical. Unintended consequences are a feature of the system, not the failure of the intervener.

**Separator:** `---`

---

### Section 5: Principles for effective intervention

**Header:** `## Principles for effective intervention`

**Purpose:** Synthesise the chapter's lessons into five durable principles. This section also serves as a closing synthesis for the entire book — the reader has built up the vocabulary over eight chapters; this section shows what that vocabulary is for.

**Five principles:**

1. **Intervene at the highest leverage point you can access.** LP 12 is the most accessible leverage point. LP 3 is the most effective. The gap between accessible and effective is where most policy failure lives. The task is not to intervene only at LP 1 — it is to identify the highest leverage point that the intervention can actually reach, and to understand why it is the highest.

2. **Structural changes are more durable than parameter adjustments.** A rule that automatically adjusts a flow in response to a stock level (LP 6: information structure) continues to work even when conditions change. A quota set at a single number (LP 12) requires re-setting every year by a committee under economic pressure. The Grand Banks and the Icelandic fishery received nearly identical biological pressures; the Icelandic fishery survived because its management rules were structural (ITQs), not parametric (annual quotas).

3. **Expect and monitor for adaptation.** Systems respond to interventions. The response is not random — it follows the feedback structure of the system. Map the likely adaptation paths before deploying an intervention, and build monitoring for those specific pathways from the start. When the cobra effect occurs, it is not a surprise to someone who modelled the system; it is only a surprise to someone who did not.

4. **Match intervention timescale to system response time.** An intervention that operates on a short timescale in a system with long delays will be evaluated on its short-term effect and abandoned before its long-term effect is visible. Urban reforestation: costs are immediate, benefits in urban temperature and air quality emerge over decades. If the policy evaluation window is three years, the intervention will always appear to have failed. The delay mismatch from Chapter 2 applies to policy evaluation as much as to feedback control.

5. **Model before intervening.** Chapter 7 showed how to build the minimum model that captures the load-bearing feedback structure of a system. That model, run before the intervention is deployed, will reveal which leverage point the intervention is actually targeting, what adaptation pathways are likely, and what feedback loops may be strengthened as side effects. The model does not need to be precise. It needs to have the right structure. A rough model of the right system is more useful than no model.

**Closing the book:**

Chapters 1 through 7 built a vocabulary: stocks, flows, feedback, delays, tipping points, emergence, modelling methodology. This chapter applies that vocabulary to the question that motivated building it: how do you change a system that is producing outcomes you do not want?

The answer is not "push harder on the obvious intervention." Pushing harder at LP 12 makes the system push back harder. The answer is to understand the feedback structure — which loops are driving the behaviour you want to change, what leverage points they are most sensitive to, and which of those points you can actually reach. That understanding is what the vocabulary is for. The rest is engineering.

**Target:** 700 words. Voice: synthesis, slightly more expansive than the preceding sections. This is the conclusion to the chapter and the book. It should feel complete.

**Separator:** `---`

---

### Section 6: Simulation — fishery management

**Header:** `## Simulating fishery management`

**Purpose:** Demonstrate the leverage point hierarchy using the fishery as a simulation. Three management regimes, three leverage points. The result shows that the same economic dynamics produce different outcomes depending on the structural intervention applied.

**The Gordon-Schaefer model:**

Fish stock dynamics (logistic growth + harvest):
```
dF/dt = r * F * (1 - F/K) - H(F, E)
```

Fishing effort dynamics (profit-driven, open-access):
```
dE/dt = φ * E * (price * q * F - unit_cost)
```

Where E grows when fishing is profitable (revenue per unit effort > cost per unit effort) and shrinks when it is not.

Harvest: H = q * E * F (catchability × effort × stock)

**Three scenarios:**

Scenario 1 — Fixed quota (LP 12): H = H_target (constant, set below MSY)
Scenario 2 — Open access (no effective management): dE driven purely by profit
Scenario 3 — Harvest Control Rule (LP 6: information + feedback structure): H = min(q*E*F, HCR(F))

Where the HCR is:
```
HCR(F) = H_max                          if F >= F_target
HCR(F) = H_max * (F - F_floor) / (F_target - F_floor)   if F_floor <= F < F_target
HCR(F) = 0                              if F < F_floor
```

The HCR automatically reduces the harvest cap as the stock falls below the target level. Effort dynamics operate in scenario 3 exactly as in scenario 2 — the same economic incentives — but the harvest is capped by the stock-responsive rule.

**The leverage point lesson:**
- Scenario 1 uses LP 12: set a quota number. Works if set correctly; fails under pressure.
- Scenario 2 has no structural intervention: the reinforcing economic loop collapses the stock.
- Scenario 3 uses LP 6/5: change the information flow (harvest is now a function of stock level) and the rule (no one can exceed the HCR cap). Same economic actors; different structural arrangement; different outcome.

**Parameters:**
- r = 0.30/yr
- K = 1000 Gt
- q = 0.0012 (catchability)
- price = 3.0 (normalized, per Gt)
- unit_cost = 0.50 (per unit effort)
- φ = 0.50 (effort adjustment speed)
- F_0 = 800 Gt (initial stock — heavily fished but viable)
- E_0 = 80 (initial effort)
- T_END = 80 years
- DT = 0.05 years
- MSY = r*K/4 = 75 Gt/yr; H_target = 0.70 * MSY = 52.5 (scenario 1)
- F_OA = unit_cost/(price*q) = 0.50/(3.0*0.0012) = 139 Gt (open-access equilibrium)
- HCR parameters: H_max = 0.65*MSY = 48.75; F_target = 500; F_floor = 150

**Figure 8.4:** Two panels
- Panel 1: Fish stock F(t), three scenarios, 80 years. Vertical reference lines at F_MSY=500 and F_OA=139.
- Panel 2: Harvest rate H(t), three scenarios. Shows: scenario 1 flat, scenario 2 high then declining (economic response to stock decline), scenario 3 adaptive (declining as stock falls, then recovering)

**Cross-link callout:** None on this simulation — the callouts have been distributed across earlier sections.

---

## 3. Simulation Code Specification

```python
# Parameters
r = 0.30; K = 1000.0; q = 0.0012
price = 3.0; unit_cost = 0.50; phi = 0.50
F_0 = 800.0; E_0 = 80.0
T_END = 80.0; DT = 0.05
MSY = r * K / 4  # = 75

# Scenarios
H_FIXED = 0.70 * MSY  # = 52.5 Gt/yr

HCR_H_MAX  = 0.65 * MSY  # = 48.75 Gt/yr
HCR_F_TGT  = 500.0        # = F_MSY
HCR_F_FLOOR = 150.0

def hcr(F):
    if F >= HCR_F_TGT:
        return HCR_H_MAX
    elif F >= HCR_F_FLOOR:
        return HCR_H_MAX * (F - HCR_F_FLOOR) / (HCR_F_TGT - HCR_F_FLOOR)
    else:
        return 0.0

def run(scenario):
    F, E = F_0, E_0
    # record arrays
    ...
    for i in steps:
        growth = r * F * (1 - F/K)
        
        if scenario == 1:
            H = H_FIXED
            dE = 0  # no effort dynamics — externally managed
        elif scenario == 2:
            H = q * E * F
            dE = phi * E * (price * q * F - unit_cost)
        elif scenario == 3:
            H = min(q * E * F, hcr(F))
            dE = phi * E * (price * q * F - unit_cost)
        
        F = max(0, F + (growth - H) * DT)
        E = max(0, E + dE * DT)
```

**WH palette:**
- Scenario 1 (fixed quota): `#888888` dashed
- Scenario 2 (open access): `#d52a2a` solid
- Scenario 3 (HCR): `#111111` solid

---

## 4. Diagram Specifications

### Diagram 8.1 — Grand Banks reinforcing loop

Causal loop diagram showing:
- Cod stock → catches → revenue → fishing effort → catches (back to cod stock via harvest)
- Annual quota intervention as a weak balancing arrow being bypassed
- Label the dominant loop R (reinforcing)

### Diagram 8.2 — Leverage point hierarchy

Simple vertical grouping:
- Group 4 (top): Paradigm (LP 1-2)
- Group 3: Goals, self-organisation (LP 3-4)
- Group 2: Rules, information, feedback (LP 5-8)
- Group 1 (bottom): Physical structure, numbers (LP 9-12)
- Arrow from bottom to top labelled "increasing leverage, increasing difficulty of change"

### Diagram 8.3 — Three intervention depths on the same loop

A single causal loop diagram with three intervention arrows at different points:
- LP 12 arrow: pointing at the harvest flow (adjusting the quota number)
- LP 6 arrow: pointing at the information link (making harvest a function of stock level)
- LP 3 arrow: pointing at the goal node (changing what the system is trying to maintain)
- Caption explains why each deeper intervention is more robust

---

## 5. Exercise Specifications

**8.1 — System identification.** A freshwater aquifer underlies a farming region. Farmers draw water from the aquifer for irrigation. When water prices are low and crops are profitable, irrigation intensity increases. As the aquifer depletes, well depths must increase (higher pumping cost) — but technology improvements have consistently reduced pumping costs faster than depletion increases them. Draw the causal loop diagram. Identify all feedback loops. Which leverage point is being inadvertently employed by the technology improvement, and why is it making the problem worse rather than better?

**8.2 — Archetype recognition.** The Aral Sea, once the world's fourth-largest lake, lost 90% of its volume between 1960 and 2000 due to Soviet-era irrigation diversion of the rivers feeding it. The diversion was a deliberate intervention to expand cotton production. Map this as a leverage point problem: at what leverage point was the intervention applied? What higher-leverage intervention might have produced a different outcome? (Hint: consider what the goal of the Central Asian agricultural system was, and what goal would have been required to conserve the sea.)

**8.3 — Simulation build.** Add a minimum viable population effect to the fishery simulation from Section 6. Below a minimum population threshold F_min = 100 Gt, cod reproductive success declines (the fish cannot find each other in sparse populations). Model this as: `r_effective(F) = r * max(0, (F - F_min) / (F_MSY - F_min))` for F < F_MSY. This is the Allee effect from Chapter 3. Run all three scenarios. Which management regime prevents the stock from entering the F < F_min danger zone? How does this change the design requirements for the Harvest Control Rule?

**8.4 — Leverage point analysis.** You are advising a city government on its housing affordability problem. Median house price has been rising at 8% per year for fifteen years. The government has implemented: (a) a buyers' subsidy programme, (b) a stamp duty reduction for first-home buyers, (c) a foreign buyer tax. Using the leverage point hierarchy, classify each intervention. For each, predict the most likely unintended consequence. What would a leverage point 5 intervention look like in this context? What would a leverage point 3 intervention require?

**8.5 — Leverage point analysis (data domain).** A social media platform's engagement algorithm optimises for click-through rate. A government regulator requires the platform to reduce hate speech, measured by a classifier operating on content. The platform implements: (a) a minimum confidence threshold for the classifier, (b) a shadow-banning policy for borderline content, (c) a human review queue for appeals. Classify each intervention on the leverage point hierarchy. Predict which intervention the platform will prefer, and why. What higher-leverage intervention would address the underlying goal misalignment?

**8.6 — Capstone: full vocabulary.** You have been asked to advise on the management of a commercial salmon fishery in British Columbia. The fishery has exhibited a 40-year cycle of boom and bust — high catches in some years, near-zero catches in others — that has been attributed to a combination of ocean temperature cycles, predator dynamics, and fishing pressure. (a) Draw the full causal loop diagram including at least three feedback loops. (b) Identify all stocks, their time constants, and the dominant feedback loop in each phase of the cycle. (c) Build a stock-flow diagram and write the differential equations for the two most important stocks. (d) Apply the leverage point hierarchy: list three interventions at different levels, predict the most likely unintended consequence of each, and recommend which you would implement first and why. (e) Describe the structural validation test you would apply to any model used to inform management decisions for this fishery.

---

## 6. Cross-Link Callout Specifications

### Callout 1 (Section 3) — WH Computational Geography

**Header:** `## Resource management and the leverage point hierarchy`
**Location:** After the climate/opioid/ML examples section
**Content:** The leverage point analysis applied here maps directly to the policy instruments examined in WH Computational Geography Parts 3 (Land Use and Policy) and 5 (Economic Systems). Those chapters provide empirical case studies with spatial data — fisheries, forestry, water allocation — for the systems analysed conceptually here. The framework provides the structural rationale for why some instruments are durable and others are not; the Computational Geography chapters provide the data and the domain specifics.

### Callout 2 (Section 4) — WH Maths Vol 8

**Header:** `## Bifurcation points and intervention design`
**Location:** After the unintended consequences examples
**Content:** The tipping points from Chapter 3 and the stability thresholds from Chapter 7 appear in a unified framework in WH Maths Vol 8, Ch 3 (Bifurcation Theory). Near a bifurcation point, LP 12 interventions (parameter changes) can have discontinuous, qualitatively different effects — small parameter changes can push the system across a stability boundary, producing outcomes completely out of proportion to the intervention. Formal bifurcation analysis can identify these danger zones before intervention, providing a mathematical foundation for the caution recommended in this chapter.

### Callout 3 (Section 5) — WH Data Engineering

**Header:** `## Technical debt as a managed stock`
**Location:** After the principles section
**Content:** The fishery management framework translates directly to software engineering. Codebase health is a stock — it accumulates through good engineering practices and depletes through shortcuts, accumulated dependencies, and deferred refactoring (technical debt). The economic feedback is the same: short-term delivery pressure drives high-rate depletion; no management rule → depletion to dysfunction. The LP 5 intervention is a structural one: definition-of-done policies that cap the rate of technical debt accumulation relative to estimated debt repayment capacity. The LP 3 intervention is a goal change: treating codebase health as a first-class engineering output, not a residual after feature delivery. WH Data Engineering, Ch 8 applies this framing to platform governance.

---

## 7. Assembly Instructions

Write in order: Section 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7.

Section 5 (Principles) is the book's conclusion. Write it last-of-prose, with awareness that it is the final analytical section of the entire book. It should feel resolved, not open-ended.

The simulation (Section 6) should run cleanly. Verify:
- Scenario 2 stabilises near F_OA = 139 Gt (not zero — plain logistic with this model)
- Scenario 1 stabilises near 774 Gt
- Scenario 3 stabilises near 796 Gt (but along a different path — through F_target management)
- Harvest panel shows the clear difference between fixed, collapsing, and adaptive

**Checklist before handoff:**
- [ ] YAML front matter complete
- [ ] All seven sections present
- [ ] Three Mermaid diagrams (Grand Banks loop, leverage hierarchy, three intervention depths)
- [ ] Fishery simulation: three scenarios, 2-panel figure, callout-tip with three "What to try" items
- [ ] Three cross-link callouts at specified locations
- [ ] Six exercises with capstone exercise 8.6
- [ ] Section 5 reads as the book's conclusion — complete, not summary
- [ ] Status table in DESIGN-BRIEF.md updated to reflect Ch 8 as draft
