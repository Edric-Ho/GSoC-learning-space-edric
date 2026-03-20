# Thinking Process: Needs-Based Behavioral Model

## 1. Motivation

After building Model 1 (interaction-based inequality), I wanted to explore a different dimension of behavior:

> Can Mesa naturally support agents with internal decision-making based on competing needs?

This led to implementing a minimal needs-based work–rest model.

---

## 2. Initial Design

The first version of the model used a simple rule:

- If energy is low → rest
- If energy is high → work

This produced stable behavior, but revealed a limitation:

> The model was effectively a threshold system, not a true behavioral tradeoff.

There was no meaningful tension between competing drives.

---

## 3. Introducing Competing Pressures

To make behavior more realistic, I introduced two internal pressures:

- Recovery pressure (from low energy)
- Reward-seeking pressure (from low accumulated reward)

The agent decision process became:

1. Compute pressures
2. Compare pressures
3. Choose action

This created a genuine behavioral conflict.

---

## 4. Observed Issue

In early experiments, the system converged to a state where:

- agents accumulated reward
- work pressure decayed rapidly
- agents mostly rested

This revealed an important modeling issue:

> The functional form of internal drives strongly affects emergent behavior.

---

## 5. Key Insight

Even in a minimal behavioral model:

- small design choices (eg. how reward pressure decays)
- can lead to qualitatively different system outcomes

This suggests that:

> Behavioral modeling is highly sensitive to internal state formulation, not just interaction structure.

---

## 6. Framework Observation

From an implementation perspective:

- all decision logic is embedded inside `agent.step()`
- there is no clear separation between:
    - observation
    - evaluation
    - decision
    - action

This becomes increasingly difficult to manage as behavior grows more complex.

---

## 7. Implication for Mesa

This model highlights a gap:

> Mesa provides flexible scheduling and interaction tools, but lacks explicit support for structuring agent decision processes.

This suggests a potential direction:

- introducing lightweight abstractions for behavioral pipelines
- or modular decision components that separate observation, evaluation, and action

Importantly, this suggestion emerges from implementation experience rather than being assumed a priori.

---

## 8. Relation to Model 1

Model 1:
- behavior implicit in interaction rules

Model 2:
- behavior explicit in internal decision structure

Together, they show:

> both interaction structure and internal decision logic are critical drivers of emergent behavior.

---

## 9. Next Steps

Possible future directions:

- extend to multiple competing needs
- compare with BDI-style agents
- test separation of decision logic from execution

---

## 10. Version Evolution

### Version 1: Threshold-Based Behavior

The initial model used simple energy thresholds:
- low energy → rest
- high energy → work

This produced stable behavior but lacked genuine behavioral tradeoffs.


### Version 2: Competing Internal Drives

To introduce meaningful behavioral structure, the model was extended to include:

- recovery pressure (from low energy)
- reward-seeking pressure (from low reward)

This transformed the model from a threshold system into a conflict-based decision system.

### Version 3: Calibrated Competing Drives

To restore a balanced behavioral regime, a minimum work pressure was introduced and increased.

This resulted in:

- sustained work–rest balance (~50/50)
- stable energy levels
- continued variability across agents

This confirms that:

> small changes in internal drive formulation can lead to qualitatively different emergent dynamics.

This highlights the sensitivity of behavioral models to design choices, even in minimal systems.

---

## 11. Modeling Lesson

This model demonstrates that:

- introducing behavioral structure (competing drives) is not sufficient on its own
- the specific formulation of internal drives (eg. decay rate, lower bounds) critically determines system behavior

In particular:

- rapidly decaying reward pressure led to rest-dominant collapse
- introducing a lower bound restored sustained behavioral tension

This suggests that:

> behavioral outcomes are highly sensitive to internal state design, even in minimal models

This is an important consideration when designing reusable behavioral frameworks.

---

## 12. Summary

This model demonstrates that:

- even simple behavioral systems require structured decision-making
- Mesa currently does not provide a natural abstraction for this
- this becomes more apparent as behavioral complexity increases

This progression from threshold rules to calibrated competing drives illustrates how behavioral structure must be both explicitly modeled and carefully parameterized to produce meaningful dynamics.
