# Behavioral El Farol Model

## Overview

This model implements a behavioral version of the classic El Farol Bar problem using a structured decision pipeline.

Agents repeatedly decide whether to attend a bar with limited capacity. If attendance exceeds capacity, the experience is negative, otherwise, it is positive. Since agents cannot coordinate directly, they must rely on past observations to make decisions.

Unlike standard implementations that embed decision logic implicitly, this model makes the agent decision process explicit and modular.

---

## Model Description

Each agent follows a five-stage decision pipeline:

1. **Observe**
    - Access past attendance history
    - Observe capacity and previous payoff

2. **Belief Update**
    - Predict future attendance using a moving average strategy

3. **Evaluation**
    - Compare predicted attendance with capacity
    - Compute a simple utility signal

4. **Decision**
    - Convert evaluation into a probabilistic choice

5. **Action**
    - Attend or stay home

This structure separates different components of decision-making and improves clarity and extensibility.

---

## Key Features

### Heterogeneous Agents

Agents use different prediction windows:
[3, 5, 8, 12]

This introduces diversity in beliefs and prevents synchronized behavior.

---

### Probabilistic Decision Rule

Instead of a deterministic threshold, agents use a smooth decision rule:

$$
p(go) = 1 / (1 + exp(-k * (capacity - predicted_attendance)))
$$

This reduces coordination failures caused by identical decisions.

---

### Payoff Structure

- Attend and not overcrowded → +1
- Attend and overcrowded → -1
- Stay home → 0

---

## Results
<p align="center">
  <img src="attendance_plot.png" width="400"/>
</p>

The model produces:

- Bounded fluctuations around capacity
- Noisy but stable attendance patterns
- Decentralized coordination among agents

In early steps, the system may exhibit extreme behavior due to lack of information, but it quickly stabilizes.

---

## Implementation Notes

- Built using Mesa
- Modular structure:
    - `agents.py` — agent definition
    - `pipeline.py` — decision process
    - `strategies.py` — prediction logic
    - `model.py` — environment and scheduling

---

## Testing

The model includes tests to verify:

- Correct initialization
- Valid attendance bounds
- Multi-step consistency
- Payoff correctness

---

## Discussion

A purely deterministic version of this model leads to pathological synchronization (all agents attend or none attend). Introducing probabilistic decisions and heterogeneous predictors resolves this issue and produces more realistic dynamics.

This highlights the importance of combining structure with diversity in agent-based models.

---

## Possible Extensions

- Alternative prediction strategies
- Reinforcement learning agents
- Social influence or network effects
- Multiple competing venues  
