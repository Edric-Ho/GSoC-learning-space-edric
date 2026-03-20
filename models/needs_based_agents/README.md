# Model 2: Needs-Based Work–Rest Behavior

## 1. Overview

This model implements a minimal needs-based behavioral system in Mesa.

Agents repeatedly choose between:
- **Work**: increases reward but consumes energy
- **Rest**: restores energy but yields no reward

My goal is to evaluate how naturally Mesa supports agents with **explicit internal state and decision-making logic**.

---

## 2. Behavioral Framing

This model is inspired by **needs-based behavioral theories**, where agents must balance competing internal drives.

Each agent maintains:

- Energy (resource constraint)
- Reward (accumulated success)

Behavior emerges from the tension between:

- **Recovery pressure** (low energy → rest)
- **Reward-seeking pressure** (low reward → work)

---

## 3. Decision Structure

At each step, agents follow a simple behavioral pipeline:

1. Observe internal state
2. Evaluate competing pressures
3. Choose action (work or rest)
4. Update internal state

Unlike Model 1, behavior is **explicitly structured**, rather than embedded in interaction rules.

---

## 4. Model Dynamics

Typical outcomes:

- Agents self-regulate energy levels
- Work/rest cycles emerge endogenously
- Population-level behavior stabilizes into a dynamic balance

---

## 5. Key Insight

Even in this minimal model, behavioral logic quickly becomes structured and multi-stage:

- state evaluation
- decision rules
- action execution

This reveals a limitation:

> Mesa does not provide a native abstraction for organizing decision logic beyond `agent.step()`.

---

## 6. Relation to Project Goal

This model contributes to evaluating Mesa’s support for behavioral frameworks by:

- implementing a **needs-based architecture**
- exposing how decision logic is currently embedded in agents
- highlighting potential need for structured decision pipelines

---

## 7. Future Extensions

Possible extensions include:

- adding multiple competing needs (eg. hunger, safety)
- introducing learning or adaptation
- separating decision logic from execution (eg. decision modules)

---

## 8. How to Run

```bash
python run.py
