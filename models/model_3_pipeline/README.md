# Model 3: Behavioral Pipeline Model

## 1. Overview

This model explores a different question from the first two models:

> How naturally does Mesa support agents whose behavior is organized as an explicit decision pipeline?

The agent behavior here is intentionally simple. Agents balance two competing pressures:

- recovery (rest when energy is low)
- reward seeking (work when reward pressure is high)

The main difference is architectural rather than conceptual.

Instead of embedding all logic directly inside a single `step()` method, behavior is split into an explicit sequence:

1. observe
2. evaluate
3. decide
4. act

---

## 2. Why this model exists

Model 2 showed that once agent behavior becomes state-dependent and multi-stage, decision logic quickly starts to accumulate inside `agent.step()`.

This raised a more structural question:

> should Mesa provide clearer support for organizing decision processes, beyond just giving each agent a `step()` method?

This model is a minimal way of testing that question.

---

## 3. Behavioral Structure

Each agent maintains:

- energy
- reward
- last action

At each step, the agent:

1. observes internal state
2. evaluates competing internal drives
3. decides whether to work or rest
4. applies the consequences of that action

This makes the behavioral pipeline explicit and inspectable.

---

## 4. Key Observation

The main result is not that the dynamics are radically different from Model 2.

Instead, the key observation is:

> the same behavioral logic becomes much easier to reason about when the decision process is made explicit.

The output remains behaviorally meaningful:
- energy stays bounded
- reward continues to accumulate
- agents continue switching between work and rest

But the code is easier to interpret because the behavioral stages are separated.

---

## 5. Why this matters for Mesa

This model suggests that Mesa handles simple agent stepping well, but more structured behavioral systems benefit from clearer internal organization.

In particular, this model highlights a gap between:

- having a flexible `step()` method
- having an explicit behavioral pipeline abstraction

That gap becomes more important as agent behavior grows more complex.

---

## 6. Relation to the Behavioral Framework Project Idea

This model contributes to the behavioral framework idea by showing that the challenge is not only *when* agents are evaluated, but also *how* behavioral logic is organized.

In other words, behavioral modeling in Mesa involves at least two distinct concerns:

- evaluation timing
- decision structure

This model focuses on the second.

---

## 7. Summary

This model demonstrates that:

- explicit behavioral pipelines can improve clarity without changing the qualitative dynamics
- decision logic becomes easier to inspect when split into stages
- Mesa may benefit from lightweight abstractions for organizing behavioral pipelines
