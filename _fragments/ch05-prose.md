---
title: "Cities and Economies as Systems"
subtitle: "Agglomeration, lock-in, and why success breeds success"
status: seed
axiom: "Cities and economies concentrate because the feedback loops that make them valuable make them more valuable: reinforcing loops with no internal correction, limited only by congestion costs and the accidents of history."
rewrite: "Agglomeration is not an economic anomaly. It is a reinforcing feedback operating at urban scale — the same structure as ice-albedo, permafrost methane, and platform network effects."
opens_to:
  - chapter: 06-data-as-a-system
    relationship: enables
  - course: ESDE 304
    relationship: anchors
destinations:
  - field: earth
    hook: "The urban heat island effect is not incidental to city structure — it is a reinforcing feedback driven by the same impervious surface expansion that drives agglomeration. MODIS land surface temperature data makes it visible at 1km resolution."
  - field: human
    hook: "Calgary's economy contracted by roughly 8% in 18 months following the 2014 oil price collapse. Understanding why the contraction was so fast, and why recovery was slow, requires understanding the agglomeration structure that made the city vulnerable."
  - field: data
    hook: "A recommendation system that loses its user base does not degrade gracefully. It enters the Detroit feedback in reverse: fewer users, less training data, worse recommendations, more users leaving. The loop structure is identical to urban disinvestment."
---

---
### FRAGMENT 1 — The puzzle
---

## The puzzle

Every country, regardless of its geography, political history, or level of development, produces the same pattern in its city sizes. The largest city is roughly twice the population of the second-largest. The second is roughly twice the third. The relationship between a city's rank and its size follows a power law: population is proportional to rank raised to an exponent close to −1. This regularity was formalised by the linguist George Zipf in 1949 and bears his name. It has held in every dataset examined since.

Canada: Toronto at approximately 6 million, Montreal at 4.2 million, Vancouver at 2.6 million, Calgary at 1.6 million. The ratios are not exact. The pattern is. Japan produces the same distribution. So does Brazil, the United States, and France. The specific cities are different. The structural pattern is identical. No central planner produced it. No natural constraint imposed it. It emerged independently in thousands of cities competing for the same pool of migrants, capital, and economic activity.

The puzzle is not that large cities exist. The puzzle is why the distribution takes this specific mathematical form, why it is stable across centuries of urbanisation, and why it appears in places with no common institutional history. The usual economic explanations — comparative advantage, transportation costs, natural resources — are partial. They explain why some cities are larger than others. They do not explain why the ratio between them follows the same power law in Osaka and São Paulo.

The explanation lies in feedback structure. A city that is already larger offers more economic opportunity than a smaller city. That advantage attracts workers and firms. Their arrival makes the city larger. Making it larger makes it more attractive still. The reinforcing loop operates simultaneously in every city in every country. The Zipf distribution is what emerges from this process. The reader already has the vocabulary. Cities are stocks. Migration is a flow. Agglomeration is a feedback. The rank-size distribution is what emerges when reinforcing feedback operates simultaneously in thousands of cities competing for the same population.

---
### FRAGMENT 2 — Cities as stock-flow systems
---

## Cities as stock-flow systems

A city is a collection of coupled stocks. Population, housing, economic output, and infrastructure each accumulate and drain through their own flows. Each stock has its own characteristic response time. The coupling between them produces the dynamics that urban economists spend careers trying to explain.

Population is filled by in-migration and natural increase, drained by out-migration and natural decrease. The net migration flow responds to the wage differential between cities and the cost-of-living differential — workers move when the expected gain exceeds the expected cost of moving. This response operates on timescales of months to a few years. Housing is filled by new construction and drained by demolition and conversion. The construction flow responds to rent levels and vacancy rates, but with a delay: planning approval, financing, and physical construction take two to five years from the decision to build. Infrastructure — roads, transit, water systems, power grids — accumulates through public investment and drains through depreciation. Its response time is measured in decades. A city's traffic conditions today reflect infrastructure decisions made thirty years ago.

The mismatched response times produce characteristic pathologies. A city experiencing rapid population inflow fills its population stock faster than its housing stock can adjust. Rents rise. The rising rent signal eventually triggers a construction response, but the two-to-five year construction lag means the signal arrives into a market that may have already changed. Overbuilding follows a boom; underbuilding persists through a shortage. This oscillation pattern — driven by the response delay between a fast stock and a slower capacity stock — is the same structure as the commodity cycle in Chapter 2.

Fort McMurray is the extreme case. The city exists almost entirely as a function of one industrial stock-flow system: oil sands extraction. In-migration tracked the oil price cycle because wages tracked oil revenues and labour demand tracked production throughput. Workers arrived when oil was above roughly $60 per barrel. They left when it was not. The 2016 Horse River Fire made the mechanism visible in accelerated form. The fire simultaneously depleted the city's population stock and its housing stock — both flows running hard in reverse within days. Population drained through emergency evacuation. Housing drained through physical destruction. Recovery required both stocks to refill simultaneously, with the housing stock constrained by construction capacity and the population stock constrained by housing availability. A city with more diverse economic structure — more decoupled stocks — would have shown more resilience. Fort McMurray's stock-flow structure has almost no decoupling.

**Earth domain: Urban heat island as a reinforcing stock-flow feedback**

Dense impervious surfaces — roads, buildings, parking structures — absorb more incoming solar radiation than the vegetated land they replace. They re-radiate heat at night rather than cooling through evapotranspiration. City cores run 2–5°C warmer than surrounding rural areas as a result. This temperature differential is not fixed. It is a feedback. Higher urban temperatures increase air conditioning demand. Air conditioning systems expel waste heat into the outdoor environment. That waste heat adds to the urban thermal stock. The loop is reinforcing: more impervious surface → higher temperatures → more mechanical cooling → more waste heat → higher temperatures. MODIS land surface temperature products at 1 km resolution make the heat island signal visible in every major city on Earth. The signal scales with city size.

**Data domain: Earth observation pipeline as city analogue**

Raw satellite telemetry arrives at ground stations at rates exceeding 2.5 petabytes per day — the data ingest flow. Processed geophysical products — calibrated, geolocated, atmospherically corrected — form the usable data stock downstream. Processing capacity is the analogue of housing stock: it is built slowly, through instrument characterisation campaigns, algorithm validation, and infrastructure procurement. When ingest rate exceeds processing capacity, a backlog accumulates. Latency between event and usable product grows. This is the same structural pattern as urban congestion: a fast inflow against a slow-building capacity stock. The remedy — more processing capacity — faces the same response delay that faces urban housing supply. Capital allocation, procurement, and deployment take years. The backlog accumulates in the meantime.

The stock-flow structure of a city and the stock-flow structure of an Earth observation pipeline are not analogous in a loose metaphorical sense. They are the same structure operating in different materials.

[DIAGRAM 5.1 GOES HERE]

::: {.callout-note}
## Equilibrium city size and linear stability

The agglomeration-congestion two-loop system has an equilibrium city size where attractiveness equals zero — the wage premium exactly offsets the cost-of-living penalty. Whether cities actually reach this equilibrium, and whether it is stable, depends on the relative rates of the two feedbacks. This is a fixed-point analysis: the equilibrium satisfies w(P) - c(P) = 0, and its stability depends on whether the derivative of net attractiveness with respect to population is negative (stable) or positive (unstable).

[WH Maths Vol 8, Ch 1 (Control, Feedback, Stability)](https://wayward.house/learn/maths/advanced/) develops this as a general eigenvalue problem for linear feedback systems — the same framework that governs climate sensitivity in Chapter 4.
:::

---
### FRAGMENT 3 — Agglomeration — the reinforcing loop
---

## Agglomeration — the reinforcing loop

A larger city is a more productive city. This is not a claim about scale economies within individual firms. A single factory operating in Calgary does not produce more output per worker than the same factory operating in Red Deer because Calgary is larger. The claim is about what happens when many firms and workers concentrate in the same place. Three mechanisms drive the effect. All three are reinforcing loops.

**1. Labour market pooling.** A larger city contains more workers with more diverse and specialised skills. A firm with an unusual technical requirement — a methane sensor calibration engineer for an emissions monitoring startup, a Cree-language court interpreter for a northern legal aid clinic — has a higher probability of finding that person in Calgary than in Red Deer. The probability is higher not because individual workers are better but because the labour pool is larger and more differentiated. Workers benefit symmetrically: a specialised worker in a thick labour market has more outside options, which reduces unemployment risk and increases bargaining power. The feedback is direct. A thicker labour market attracts more firms. More firms attract more workers. The market grows thicker.

**2. Knowledge spillovers.** Ideas propagate through proximity. Patent citation data shows that inventors cite patents from their own metropolitan area at significantly higher rates than patents from elsewhere, controlling for industry and technology class. The excess citation rate decays with distance. The mechanism is face-to-face interaction: accidental conversations in coffee shops, movement of workers between firms, shared attendance at industry events. These interactions are not plannable in advance — they are a product of density. The feedback: more firms generating ideas in the same location produces more recombination events, which produces higher innovation rates, which attracts more firms. The density of the agglomeration is self-amplifying.

**3. Input sharing.** Firms in a dense urban economy share specialised suppliers, infrastructure, and intermediate services that cannot survive at smaller scale. A film production ecosystem requires not just studios and actors but lighting rental houses, costume manufacturers, location scouts, catering contractors, post-production facilities, and insurance specialists. These intermediate industries require a minimum volume of core-industry demand to be financially viable. The feedback: a larger cluster of core-industry firms sustains a larger supplier ecosystem. A larger supplier ecosystem reduces per-unit costs for core firms. Lower costs attract more core firms. The cluster grows.

All three channels are reinforcing loops. None contains an internal corrective mechanism. Left alone, each would drive concentration toward a single enormous city. What limits them is the congestion balancing loop described in the next section.

**Human domain: Alberta oil sector lock-in**

The Alberta oil sands represent the most concentrated regional agglomeration in Canadian economic history. By 2014, oil and gas extraction directly and indirectly accounted for approximately 25% of provincial GDP. The sector had attracted a dense ecosystem of engineering firms, environmental consultants, heavy equipment manufacturers, geophysical service providers, pipeline contractors, and specialised financial services. The ecosystem is the agglomeration externality made concrete. It creates lock-in through a mechanism that operates on the labour market pooling and knowledge spillover channels simultaneously.

A new renewable energy firm establishing operations in Calgary in 2015 faced a structural paradox. Calgary's agglomeration advantage was real: deep pools of engineers, project managers, environmental specialists, and procurement professionals. But those workers had been trained in and for the oil sector. Their technical knowledge, their professional networks, their certification structures — all were calibrated to bitumen extraction and pipeline construction. The agglomeration advantage that attracted the renewable firm also imported a workforce trained for a different technology. The lock-in is not maintained by superior performance of the incumbent technology. It is maintained by the ecosystem that grew up around it.

[DIAGRAM 5.2 GOES HERE]

[DIAGRAM 5.3 GOES HERE]

---
### FRAGMENT 4 — Congestion and the cost of city size
---

## Congestion and the cost of city size

The reinforcing loop does not produce infinite concentration. A mechanism limits it. That mechanism is congestion: costs that rise with city size and reduce the city's attractiveness to marginal workers and firms.

Four channels drive congestion costs. Housing costs rise as land near the city centre becomes scarce and expensive; denser cities command land premiums that translate directly into reduced real wages for workers paying urban rents. Commute times increase as road and transit networks saturate — a worker in Toronto spends on average 33 minutes commuting each way, versus 17 minutes in a city of 200,000. Wage competition among firms rises as later arrivals bid for workers in a tightening labour market, compressing profit margins. Pollution and livability costs — air quality degradation, noise, per-capita crime rates — tend to rise with density in the absence of specific interventions, adding a quality-of-life penalty to the cost calculation.

The balancing loop operates through net attractiveness. As city size increases, congestion costs rise for the marginal worker and firm. Net attractiveness — the wage premium minus the cost-of-living penalty — declines. In-migration slows. The city approaches an equilibrium size where net attractiveness reaches zero for the marginal entrant. This equilibrium is not necessarily socially optimal. Individual migrants decide based on the wage and cost signals they observe. They do not account for the congestion costs they impose on existing residents: the fractionally longer commutes, the fractionally higher rents, the fractionally lower air quality. These are negative externalities. The city in the absence of planning intervention will exceed the social optimum. The gap between private optimum and social optimum is the efficiency cost of uncoordinated migration.

The balance between the two loops — agglomeration strength versus congestion costs — determines the shape of the city size distribution. Strong agglomeration and weak congestion produce sharp concentration in a few very large cities. Weak agglomeration and strong congestion produce a more even distribution. Countries with high housing supply flexibility — where construction can respond to demand signals with short delays — tend to have flatter city size distributions because the congestion feedback engages less forcefully. Countries where planning restrictions slow housing construction have sharper concentration: London, Sydney, San Francisco. The feedback structures are the same. The parameters differ.

**Data domain: Platform network effects and content saturation**

A recommendation platform exhibits the same two-loop structure. The agglomeration equivalent is Metcalfe's Law: network value scales roughly as N², where N is the number of active users, because each new user creates new potential connections for all existing users. More users make the platform more valuable, which attracts more users. The congestion equivalent is content saturation: more users generate more content, which increases the signal-to-noise ratio problem, which requires increasingly sophisticated recommendation infrastructure to maintain content quality. Beyond a threshold, more content degrades the average content experience. The platform's effective user base — users who find the platform genuinely valuable, not merely habitual — may stop growing even as nominal user counts rise.

The platform's equilibrium user base is where marginal user value, measured as engagement quality, equals the marginal congestion cost, measured as recommendation noise. Beyond that threshold, success begins to degrade the experience that produced the success. The loop structure is identical to the urban case. Only the material differs.

---
### FRAGMENT 5 — Urban scaling laws
---

## Urban scaling laws

A city of 10 million does not have ten times the economic output of a city of 1 million. It has roughly fifteen times the output. The relationship is a power law: Y ∝ N^β, where β ≈ 1.15 for GDP, average wages, patents filed, and — less encouragingly — rates of violent crime. The exponent β > 1 means that per-capita output rises with city size. A person in a city of 10 million earns more, on average, than a person in a city of 1 million in the same country doing comparable work. The agglomeration premium is not just total but per-capita.

The mechanism behind the exponent is interaction rate. In a city of N people, the number of possible pairwise interactions scales as N(N−1)/2, proportional to N² for large N. Not all pairwise interactions are productive. But if the fraction that are productive — knowledge exchanges, business transactions, labour market matches — is roughly constant, then total productive interactions scale faster than N. Total economic output follows. Bettencourt, West, and colleagues at the Santa Fe Institute formalised this in a series of papers beginning in 2007: the superlinear scaling emerges from the social network structure of cities, which increases interaction rates faster than population grows. The implication is that agglomeration is not a second-order effect added onto a linear base economy. It is the primary mechanism through which cities generate value.

Infrastructure scales differently. Roads, water pipes, electrical cables, and sewage systems scale sublinearly with population: β ≈ 0.85. A city of 10 million requires fewer lane-kilometres of road per capita than a city of 1 million, because density allows infrastructure sharing. A single water main serves many apartments stacked vertically; dispersed single-family housing requires a main for each. Large cities are simultaneously more productive per capita and more efficient per capita. Both advantages compound with size. This compounding is the quantitative expression of why the reinforcing agglomeration loop is so difficult to reverse.

**Human domain: Calgary versus Edmonton**

Alberta's two major cities offer a rare natural experiment in agglomeration structure. Both cities are roughly equal in population — approximately 1.6 million versus 1.5 million in the 2021 census. Calgary specialised in oil sector headquarters, financial services, and engineering firm clusters. Edmonton specialised in government and public sector services, retail, and oil sector operations and processing. Despite near-equal populations, Calgary historically commanded a private-sector wage premium over Edmonton, reflecting the higher agglomeration density of its specific cluster. The oil sector is a high-productivity cluster; its agglomeration externalities transmit into wages.

Following the 2014 oil price collapse, Calgary's per capita GDP advantage over Edmonton contracted sharply. The superlinear advantage of the oil cluster partially reversed. The mechanism was direct: the oil sector cluster began to thin. Firms left or contracted. The labour market pooling advantage weakened. Knowledge spillover intensity fell as engineering firm density declined. The scaling premium is not a fixed property of city size. It is a property of the active agglomeration structure. When that structure weakens, the premium weakens with it.

**Earth domain: Urban heat island scaling**

Urban heat island intensity scales superlinearly with city size. Larger cities are hotter relative to their rural surroundings not merely because they contain more impervious surface in absolute terms, but because they concentrate it at higher densities. The same interaction-rate logic applies: a denser city generates more waste heat per unit area, because more energy-consuming activities — transportation, HVAC systems, industrial processes, human metabolism — occur per square kilometre. The heat island intensity, measured as the temperature differential between urban core and rural surroundings, grows with city population at an exponent above 1. The same feedback that makes large cities more economically productive per capita makes them hotter per capita.

::: {.callout-note}
## Economic geography: from loops to spatial models

The agglomeration and lock-in mechanisms described here have formal counterparts in economic geography. The Krugman core-periphery model shows how transport costs and scale economies interact to produce spatial concentration. Gravity models of trade quantify how economic mass and distance jointly determine trade flows — the economic analogue of the migration rate function in the simulation below.

[WH Computational Geography Part 5 (Economic Systems)](https://wayward.house/learn/computational-geography/) covers these models in detail: core-periphery simulation, gravity model calibration, and spatial autocorrelation analysis of GDP. The systems thinking framework in this chapter explains *why* concentration emerges; the Comp Geo models quantify *how much* and *where*.
:::

---
### FRAGMENT 6 — Lock-in and path dependence
---

## Lock-in and path dependence

The agglomeration reinforcing loop creates a structural advantage for incumbents. Once a sector achieves sufficient scale in a place, the ecosystem of supporting industries, specialised labour, and calibrated infrastructure tilts subsequent investment toward that sector. New entrants in different sectors face a disadvantage not because their technology is inferior but because the supporting system has been optimised for something else. The cost of entry into a new sector is not just the firm's own startup cost. It is the cost of building or reorienting an entire ecosystem.

This is path dependence. The long-run equilibrium of the system depends on its history, not just on current fundamentals. The QWERTY keyboard is the canonical small-scale example: a key layout refined for nineteenth-century typewriter mechanics persists not because it is optimal for contemporary typing but because switching costs are prohibitive. Retraining millions of typists to a more efficient layout — Dvorak, for instance — costs more in lost productivity during the transition than the efficiency gain is worth to any individual. The coordination problem cannot be solved by individual rational actors. It requires collective action.

At regional scale, the Alberta oil sector lock-in is maintained by an ecosystem of approximately 200,000 oil sector workers, more than 10,000 supplier firms, twenty-plus engineering and geoscience programmes training petroleum engineers, and a regulatory environment calibrated over decades to the sector's specific environmental, safety, and royalty requirements. A new clean energy sector in Alberta does not enter a neutral environment. It enters one structured around something else. It must either persuade existing institutions to retrain and reorient — a slow process with uncertain outcomes — or build a parallel ecosystem largely from scratch.

Dutch Disease is the macro-economic version of the same mechanism. When a resource boom increases export revenues, it raises the country's exchange rate. A higher exchange rate makes other export industries — manufacturing, agriculture, tradeable services — less competitive on world markets. Their margins fall. They contract. The resource sector expands further. The economy concentrates in the resource sector not because that sector is intrinsically more productive in some permanent sense, but because the exchange rate mechanism has structurally weakened everything else. The reinforcing loop: larger resource sector → higher exchange rate → weaker manufacturing → relative growth of resource sector.

The structural consequence operates asymmetrically in time. During the boom, the rest of the economy atrophies gradually — slowly enough that the process is rarely described as a crisis. When the resource sector contracts, the rest of the economy lacks the agglomeration density to absorb displaced workers. The supporting ecosystems for alternative sectors no longer exist at sufficient scale. Recovery is slow not primarily because of labour market rigidity or policy failure — though both may contribute — but because agglomeration ecosystems, once dismantled, take years to decades to rebuild. The lock-in operates in both phases: it concentrates during the boom and constrains recovery after the bust.

[DIAGRAM 5.4 GOES HERE]

---
### FRAGMENT 7 — Urban system collapse and the Detroit inversion
---

## Urban system collapse and the Detroit inversion

The agglomeration reinforcing loop runs in reverse. A city that loses its core industry does not shrink proportionally. The agglomeration mechanism inverts, and the collapse follows the same reinforcing structure as the growth — only downward.

Detroit's trajectory makes the mechanism legible. At its peak in 1950, Detroit was the fourth-largest city in the United States, with a per-capita income above the national average and an auto-sector agglomeration of extraordinary density — assembly plants, steel suppliers, rubber manufacturers, tool-and-die shops, design studios, and the financial infrastructure to support all of them. As the US auto industry lost market share through the 1960s, 70s, and 80s, the city shed manufacturing employment. The agglomeration externalities did not simply shrink. They inverted. The labour market thinned: workers left, reducing the skill pool available to remaining firms, which accelerated further departure. Knowledge spillovers weakened: fewer firms meant fewer interactions, lower innovation rates, and less reason for new entrants to locate there. Supplier networks contracted: as core firms left, the intermediate industries that depended on them became unviable and closed. As the economic base contracted, tax revenues fell. City services deteriorated. Population left in response to deteriorating services, further contracting the tax base. The loop: economic decline → population loss → tax base fall → service deterioration → further population loss → further economic decline.

Detroit lost 60% of its population between 1950 and 2010. That figure is not the result of a smooth linear adjustment. It is the result of a reinforcing collapse — the same loop structure as the tipping points in Chapter 3, operating through an economic stock rather than a physical one. The structure of the collapse was predictable from the loop structure of the growth. The same mechanism that made the city valuable made it vulnerable.

**Human domain: Fort McMurray as single-industry extreme**

Fort McMurray — officially part of the Regional Municipality of Wood Buffalo — is the most concentrated single-industry agglomeration in Canada. Approximately 80% of economic activity is directly linked to oil sands extraction and upgrading. The 2016 Horse River Fire evacuated roughly 90,000 residents in less than 24 hours. Physical recovery was relatively rapid: the industry and its capital infrastructure were largely intact, the economic agglomeration was not structurally disrupted, and reconstruction proceeded at pace. The oil price collapse of 2014–2016 caused a slower, structurally different contraction. Firms cancelled or deferred projects. Workers left. The agglomeration thinned — not catastrophically, but measurably. Recovery from that contraction was slower than recovery from the fire, because the thinning of the agglomeration cannot be reversed by insurance payouts and reconstruction contracts. It requires the investment and hiring decisions of thousands of independent actors. And those actors are making decisions in an energy sector under secular pressure from the energy transition. The fire was an acute shock to stocks that could refill. The oil price collapse was a signal about the long-run trajectory of the flows.

**Data domain: Platform collapse and the Detroit inversion**

A social platform that loses critical mass of users enters the Detroit reinforcing collapse directly. The loop: fewer users → weaker network value → lower new user acquisition rate → further user loss. The threshold at which upward recovery becomes self-sustaining is the same threshold below which downward collapse becomes self-sustaining. This symmetry is structural. The Metcalfe's Law network effect that drives growth also drives collapse once the direction reverses. Friendster reached a peak of 115 million users before losing most of them to MySpace within eighteen months. MySpace reached a peak before losing most of them to Facebook. Neither collapse was gradual. Both were fast once the inflection point was crossed. The collapse is fast because the reinforcing loop that built the platform runs at the same speed in reverse.

::: {.callout-note}
## Detecting platform feedback reversal

A platform entering the Detroit inversion will show early warning signals before collapse becomes self-sustaining: declining engagement metrics, rising churn rates, falling content creation rates. These are the critical slowing down signatures from Chapter 3, applied to an economic system.

[WH Data Engineering Ch 7–8 (Governance and ML Platform Architecture)](https://wayward.house/learn/data-engineering/) covers the monitoring infrastructure required to detect this feedback reversal — instrumentation of engagement funnels, anomaly detection on training data distributions, and circuit breakers that trigger intervention before the collapse reinforcing loop becomes self-sustaining.
:::

---
### FRAGMENT 8 — Simulation bridge
---

## Two cities, one feedback

The two-city model below makes path dependence visible without additional abstraction. Two cities start with nearly equal populations. The same agglomeration and congestion feedbacks operate in both, with identical parameters. A small random perturbation to initial conditions — noise on the order of 1% — determines which city gains the initial advantage. Run the model multiple times: the outcome is not predictable from the starting state. The identity of the dominant city varies across runs. But the structure of the outcome — one city dominant, one residual — is predictable from the loop structure alone. The feedback guarantees concentration. History determines which city concentrates.

This is the formal content of path dependence. The equilibrium is not unique. The system has multiple attractors, one for each possible dominant city. Which attractor the system reaches depends on the trajectory, not just the parameters. And the trajectory depends on small initial perturbations that are effectively random from the perspective of any planner or policymaker. Policy can influence the parameters — agglomeration strength, congestion costs, infrastructure investment rates. It cannot, in general, determine the outcome from a position of near-symmetry. The feedback does that.

[SIMULATION BLOCK GOES HERE]

---
### FRAGMENT 9 — Exercises
---

## Exercises

**5.1 — Housing market stock-flow**

A growing mid-sized Canadian city is experiencing a housing shortage. The housing market consists of two stocks (housing supply and population seeking housing) connected by several flows.

a. Draw the full stock-flow diagram. Identify all stocks, flows, and the primary balancing loop that governs long-run equilibrium between housing supply and demand.
b. The primary delay in the housing market is the construction lag: from approval to completion takes 3–5 years. How does this delay affect the behaviour of rents? Sketch the time-series archetype you would expect for rents in response to a step increase in population inflow.
c. City policy proposes upzoning — allowing higher-density construction in existing residential areas. Which flow in your diagram does this intervention primarily affect? What is the leverage of this intervention relative to other possible interventions (e.g., rent controls, foreign buyer taxes)?

---

**5.2 — Scaling law analysis**

The following pairs are approximate GDP (billions CAD) and population for seven Canadian cities:
Toronto: 480, 6.2M | Montreal: 220, 4.2M | Vancouver: 180, 2.6M | Calgary: 130, 1.6M | Ottawa-Gatineau: 90, 1.4M | Edmonton: 110, 1.5M | Quebec City: 55, 0.85M

a. Plot log(GDP) vs log(population) for these seven cities. Fit a line. What is the slope β?
b. Is β above or below 1? What does this imply about per-capita productivity scaling with city size in Canada?
c. Ottawa-Gatineau has a high per-capita GDP relative to its population. Propose a mechanism — consistent with the agglomeration framework — that could produce this result. Hint: consider the nature of the primary agglomeration in Ottawa.

---

**5.3 — Dutch Disease causal loop diagram**

Section 5.4 describes the Dutch Disease mechanism connecting resource sector growth, exchange rate, and manufacturing competitiveness.

a. Draw the full causal loop diagram. Include: resource sector scale, resource export revenues, exchange rate, manufacturing competitiveness, manufacturing employment, labour flows between sectors, and any other nodes you identify as necessary.
b. Label every link as + or −. Identify all complete loops and label each as R or B.
c. The Dutch Disease model predicts that a resource boom weakens manufacturing. But empirically, some resource-rich economies manage to maintain manufacturing competitiveness. Identify one structural change to your diagram — a new link, a modified link, or a new feedback — that could explain how a country could avoid Dutch Disease despite a resource boom.

---

**5.4 — Path dependence simulation**

Using the two-city agglomeration model from this chapter:

a. Set both cities to exactly equal populations (zero noise). Run the model. What happens? Explain why in terms of the loop structure.
b. Add 1% random noise to initial conditions. Run the model 20 times. What fraction of runs end with City A holding more than 60% of total population? Plot the distribution of final City A population shares across runs.
c. Now double the agglomeration strength parameter α. Repeat (b). How does increasing agglomeration strength affect (i) the speed of divergence and (ii) the variance of final outcomes across runs?

---

**5.5 — Leverage points in Alberta's energy transition**

Using Meadows' leverage point hierarchy (from Chapter 1), identify three leverage points in the Alberta oil sector lock-in system.

a. Identify one low-leverage intervention (below the level of feedback structure in Meadows' hierarchy). Describe what it changes and why the effect is limited.
b. Identify one medium-leverage intervention (at the level of feedback structure). Describe the specific feedback loop it modifies and the mechanism by which it would reduce lock-in.
c. Identify one high-leverage intervention (at the level of goals or paradigm). Describe what it would require — institutionally, politically, and economically — and what resistance to change would arise.
d. For the medium-leverage intervention: what unintended consequence might arise from changing that feedback, and how would you monitor for it?

---

**5.6 — Platform resilience**

A large recommendation platform loses 20% of its user base in 6 months following a privacy scandal.

a. Map this to the platform network effect loop diagram from Section 5.5. Which link or links are weakened? Describe the mechanism.
b. Describe two distinct feedback dynamics that could follow: one leading to recovery, one leading to collapse. For each, identify which loop dominates.
c. You are the platform's data engineering lead. Propose three metrics you would instrument to distinguish early recovery from the beginning of a collapse spiral. For each metric, describe: (i) what it measures in system terms, (ii) the expected trajectory in recovery vs. collapse, and (iii) the threshold that would trigger an escalation response.
