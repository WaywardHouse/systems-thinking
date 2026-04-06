## Simulating the ML retraining loop under concept drift

Accuracy is a stock that decays as the world drifts away from what the model was trained on. The three scenarios below isolate how retraining frequency — none, fixed-schedule, and threshold-triggered — determines long-run model performance when the training data is itself a perishable resource.

```{python}
#| label: fig-concept-drift
#| fig-cap: "Figure 6.5. ML retraining loop under concept drift. Top: model accuracy over 10 years for three retraining policies. Bottom: training data freshness, with retraining events marked as vertical ticks. Without retraining, accuracy decays exponentially toward the random-chance floor. Periodic retraining produces a sawtooth — accuracy is always recovered, but always decays again on the same schedule. Adaptive retraining holds accuracy above the threshold with fewer events when drift is slow, but its advantage disappears when drift is fast and the trigger fires almost as often as the periodic schedule."
#| fig-width: 10
#| fig-height: 7
"""ML retraining loop under concept drift — Chapter 6.
Euler integration of two stocks: model accuracy and training data freshness.
Three scenarios: no retraining, periodic fixed-schedule, adaptive threshold-triggered."""
import numpy as np
import matplotlib.pyplot as plt

# -- Named constants -----------------------------------------------------------
ACCURACY_FLOOR     = 0.50   # random-chance baseline for binary classification
ACCURACY_CEILING   = 0.95   # best achievable accuracy with perfectly fresh data
ACCURACY_THRESHOLD = 0.80   # adaptive trigger: retrain when accuracy falls below this
D                  = 0.08   # drift rate (per year)
RETRAIN_PERIOD     = 1.0    # fixed-schedule retraining interval (years)
MIN_RETRAIN_GAP    = 0.25   # minimum time between retraining events (years, adaptive)
DT                 = 0.01   # Euler time-step (years)
T_START            = 0.0
T_END              = 10.0

# WH palette
COL_NONE     = "#888888"    # no retraining
COL_PERIODIC = "#111111"    # periodic retraining
COL_ADAPTIVE = "#d52a2a"    # adaptive retraining


# -- Euler simulation ----------------------------------------------------------
def run_simulation(retrain_policy):
    """
    Run one 10-year Euler simulation.

    retrain_policy: one of 'none', 'periodic', 'adaptive'

    Returns: (t, accuracy, freshness, retrain_times)
    """
    steps        = int((T_END - T_START) / DT) + 1
    t            = np.linspace(T_START, T_END, steps)
    accuracy     = np.empty(steps)
    freshness    = np.empty(steps)
    retrain_times = []

    # Initial conditions: well-trained model, perfectly fresh data
    accuracy[0]  = ACCURACY_CEILING
    freshness[0] = 1.0
    last_retrain = -999.0   # track time of last retraining event

    for i in range(1, steps):
        t_now = t[i]

        # -- Decay stocks via Euler step ----------------------------------------
        acc_prev   = accuracy[i - 1]
        fresh_prev = freshness[i - 1]

        # Accuracy decays exponentially toward the floor (concept drift)
        d_accuracy  = -D * (acc_prev - ACCURACY_FLOOR)
        # Data freshness decays exponentially toward zero (world changes)
        d_freshness = -D * fresh_prev

        acc_new   = acc_prev   + d_accuracy  * DT
        fresh_new = fresh_prev + d_freshness * DT

        # -- Check for a retraining event this step ----------------------------
        retrain_now = False

        if retrain_policy == "periodic":
            # Retrain on fixed schedule: at t = 1, 2, 3, ... years
            # Detect crossing of a schedule boundary inside this step
            prev_interval = (t[i - 1] - T_START) / RETRAIN_PERIOD
            curr_interval = (t_now    - T_START) / RETRAIN_PERIOD
            if int(curr_interval) > int(prev_interval):
                retrain_now = True

        elif retrain_policy == "adaptive":
            # Retrain when accuracy falls below threshold, subject to minimum gap
            elapsed_since_last = t_now - last_retrain
            if acc_new < ACCURACY_THRESHOLD and elapsed_since_last >= MIN_RETRAIN_GAP:
                retrain_now = True

        # -- Apply retraining effects ------------------------------------------
        if retrain_now:
            # Accuracy is restored in proportion to how fresh the training data is
            acc_new   = ACCURACY_FLOOR + (ACCURACY_CEILING - ACCURACY_FLOOR) * fresh_new
            # Data freshness is fully restored by ingesting new labels
            fresh_new = 1.0
            last_retrain = t_now
            retrain_times.append(t_now)

        accuracy[i]  = acc_new
        freshness[i] = fresh_new

    return t, accuracy, freshness, retrain_times


# -- Run all three scenarios ---------------------------------------------------
t0, acc0, fresh0, rt0 = run_simulation("none")
t1, acc1, fresh1, rt1 = run_simulation("periodic")
t2, acc2, fresh2, rt2 = run_simulation("adaptive")


# -- Figure: 2 panels ----------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), dpi=150)

# -- Panel 1: Model accuracy ---------------------------------------------------
ax1.plot(t0, acc0, color=COL_NONE,     linestyle="--", linewidth=1.2,
         label="No retraining")
ax1.plot(t1, acc1, color=COL_PERIODIC, linestyle="-",  linewidth=1.8,
         label="Periodic")
ax1.plot(t2, acc2, color=COL_ADAPTIVE, linestyle="-",  linewidth=1.8,
         label="Adaptive")

# Reference line at accuracy threshold
ax1.axhline(ACCURACY_THRESHOLD, color="#888888", linestyle="--",
            linewidth=0.7, zorder=0)

# Annotate threshold line
ax1.annotate("Threshold 0.80", xy=(0.12, ACCURACY_THRESHOLD),
             xytext=(0.12, ACCURACY_THRESHOLD + 0.015),
             fontsize=8, color="#888888", va="bottom")

# Annotate each scenario line at right edge
final_acc = {
    "No retraining": (t0[-1], acc0[-1], COL_NONE,     "right"),
    "Periodic":      (t1[-1], acc1[-1], COL_PERIODIC, "right"),
    "Adaptive":      (t2[-1], acc2[-1], COL_ADAPTIVE, "right"),
}
offsets = {
    "No retraining": -0.03,
    "Periodic":       0.02,
    "Adaptive":       0.02,
}
labels_data = [
    ("No retraining", t0, acc0, COL_NONE),
    ("Periodic",      t1, acc1, COL_PERIODIC),
    ("Adaptive",      t2, acc2, COL_ADAPTIVE),
]
for label, t_, acc_, col in labels_data:
    ax1.annotate(label,
                 xy=(t_[-1], acc_[-1]),
                 xytext=(t_[-1] - 0.1, acc_[-1] + offsets[label]),
                 fontsize=8.5, color=col, ha="right", va="center")

ax1.set_xlim(T_START, T_END)
ax1.set_ylim(0.40, 1.02)
ax1.set_ylabel("Model accuracy")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.grid(False)

# -- Panel 2: Training data freshness ------------------------------------------
ax2.plot(t0, fresh0, color=COL_NONE,     linestyle="--", linewidth=1.2)
ax2.plot(t1, fresh1, color=COL_PERIODIC, linestyle="-",  linewidth=1.8)
ax2.plot(t2, fresh2, color=COL_ADAPTIVE, linestyle="-",  linewidth=1.8)

# Mark retraining events as vertical tick marks
for rt in rt1:
    ax2.axvline(rt, color=COL_PERIODIC, alpha=0.3, linewidth=0.8)
for rt in rt2:
    ax2.axvline(rt, color=COL_ADAPTIVE, alpha=0.3, linewidth=0.8)

# Annotate scenario lines at right edge of panel 2
labels_fresh = [
    ("No retraining", t0, fresh0, COL_NONE,     -0.04),
    ("Periodic",      t1, fresh1, COL_PERIODIC,  0.03),
    ("Adaptive",      t2, fresh2, COL_ADAPTIVE,  0.03),
]
for label, t_, fresh_, col, yoff in labels_fresh:
    ax2.annotate(label,
                 xy=(t_[-1], fresh_[-1]),
                 xytext=(t_[-1] - 0.1, fresh_[-1] + yoff),
                 fontsize=8.5, color=col, ha="right", va="center")

ax2.set_xlim(T_START, T_END)
ax2.set_ylim(-0.05, 1.10)
ax2.set_xlabel("Year")
ax2.set_ylabel("Training data freshness")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.grid(False)

plt.tight_layout(pad=1.5)
plt.savefig("_assets/ch06-concept-drift.png", dpi=150, bbox_inches="tight")
plt.show()
```

::: {.callout-tip}
## What to try

1. **Double the drift rate (`D = 0.16`).** How does this affect the performance of periodic retraining? How frequently would periodic retraining need to occur to maintain accuracy above 0.80? What does this imply about system design in rapidly changing environments — for example, a fraud detection model facing a novel attack campaign where the attacker adapts faster than the retraining cycle?

2. **Increase the retraining threshold to 0.88.** How does this change the retraining frequency in Scenario 2? Is the mean accuracy over the 10-year period higher or lower than with `ACCURACY_THRESHOLD = 0.80`? Does more frequent retraining always improve average performance, or does the freshness penalty from triggering early cut into gains?

3. **Simulate data freshness decay with a labelling lag.** In practice, fresh labels are not available the moment a threshold is crossed — human labellers or field validation campaigns introduce a delay. Add a 0.25-year lag: when the accuracy threshold is crossed, `data_freshness` continues to decay for 0.25 years before the retrain executes. How much does this delay degrade the post-retrain accuracy ceiling compared to instantaneous retraining, and does the gap widen or stay constant across the 10-year window?
:::

> Figure 6.5. ML retraining loop under concept drift across three retraining policies (D = 0.08 per year, accuracy floor = 0.50, accuracy ceiling = 0.95). Top panel: model accuracy over 10 years. Without retraining (grey dashed), accuracy decays exponentially toward random-chance baseline. Periodic retraining (black) produces a regular sawtooth — accuracy recovers fully after each event but always decays again on the same schedule regardless of how fast the world is drifting. Adaptive retraining (red) holds accuracy above the 0.80 threshold with events spaced by actual need rather than calendar time. Bottom panel: training data freshness, with individual retraining events shown as faint vertical ticks. The vertical ticks reveal that adaptive retraining fires less often than the fixed schedule when drift is slow — the policy is more efficient, not just faster. The stock-and-flow structure makes the core tradeoff explicit: accuracy is a stock that decays continuously, data freshness is a stock that decays continuously, and retraining is the inflow that refills both — subject to delay, minimum gap, and the freshness of the data at the moment of retraining.
