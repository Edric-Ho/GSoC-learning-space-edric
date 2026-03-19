# Thought Process: Building the Local Inequality Model

This file documents how my thinking evolved while building this model.  
I’m writing this mainly to keep track of decisions, mistakes, and what I learned.

---

## 1. Starting point: effort vs luck

I began with a very simple idea:

> outcomes = effort + randomness

Something like:

$$
S_{i,t+1} = S_{i,t} + \alpha E_i + \varepsilon_{i,t}
$$

At first this felt reasonable:
- effort contributes consistently
- randomness creates variation

But after thinking more carefully, I realized something important:

👉 there is no interaction between agents

Each agent is basically evolving independently.

That doesn’t really use Mesa at all.

---

## 2. Realization: this is not an ABM yet

Mesa is about:
- agents interacting
- local rules
- emergence

My initial version had:
- no competition
- no scarcity
- no interaction

So even if inequality appeared, it would just be from accumulated noise.

That felt unsatisfying. This made me realize something more specific about Mesa:

Mesa doesn’t just provide agents as a data structure.  
It assumes that the model’s behavior should come from interactions between agents.

In my initial version, even though I used agents, the system behavior did not depend on interaction at all. That meant I was not actually using Mesa in a meaningful way.

---

## 3. Shift: introduce competition

To make it more “agent-based”, I asked:

> what if agents compete for opportunities?

This introduces:
- interaction
- scarcity
- dependence on others

Instead of everyone accumulating independently, agents now:
- influence each other
- compete for limited rewards

---

## 4. Design choice: local vs global

At this point I had two options:

### Option A: global competition
- rank all agents
- pick top ones

### Option B: local competition (chosen)
- each agent only interacts with neighbors

I chose local competition because:
- it aligns better with Mesa philosophy
- it allows spatial structure
- it creates overlapping interactions

---

## 5. Building the local competition model

I placed agents on a grid.

Each step:
- every cell becomes an “opportunity center”
- agents in that neighborhood compete

Each agent computes a score:

$$
Z_i(t) = \beta E_i + \delta S_i(t) + \varepsilon_i(t)
$$

Later I added fatigue:

$$
Z_i(t) = \beta E_i + \delta S_i(t) - \lambda F_i(t) + \varepsilon_i(t)
$$

I kept the function linear on purpose:
- easier to interpret
- easier to debug

---

## 6. Decision: probabilistic selection

Instead of always picking the highest score, I used softmax:

$$
P(i \text{ wins}) = \frac{\exp(Z_i)}{\sum_j \exp(Z_j)}
$$

Reason:
- keeps randomness meaningful
- avoids deterministic “winner always wins” behavior
- allows weaker agents to occasionally win

---

## 7. First implementation result (unexpected)

After running the model, I got:

- Gini ≈ 0.78
- top 10% share ≈ 0.70
- effort-success correlation ≈ 0.19

This was surprising.

I expected:
- moderate inequality
- some correlation between effort and success

But instead:
- inequality was very high
- effort barely explained outcomes

---

## 8. Debugging the cause

I tried to understand what was driving this.

The key realization:

> agents can win multiple overlapping contests in the same step

Because:
- every grid cell runs a contest
- neighborhoods overlap
- agents appear in multiple neighborhoods

So one agent can:
- win multiple times in a single round

This effect was not obvious from the model definition itself,  it emerged from how interactions were implemented.

---

## 9. Insight: hidden amplification mechanism

This created a feedback loop:

1. agent wins
2. success increases
3. score increases (via $\delta S_i(t)$)
4. higher chance to win again
5. possibly multiple wins per round

This compounds very quickly.

So inequality is not just from:
- effort
- randomness

but also from:
👉 **structure of opportunity allocation**

---

## 10. Important modeling lesson

The most important takeaway so far is:

> interaction structure can dominate individual attributes

I initially thought outcomes would mainly reflect:
- effort (ability)
- randomness (luck)

But in this model, the structure of interaction, specifically how opportunities are distributed and how often agents can win, had a stronger effect than either.

This suggests that when building agent-based models, it is not enough to specify agent attributes correctly. The way interactions are structured can completely change the system-level outcome.

---

## 11. Statistical tracking decisions

To understand the model, I added:

### Gini coefficient
- overall inequality summary

### Top 10% share
- captures concentration at the top

### Effort-success correlation
- measures how much effort actually matters

These helped reveal that:
- inequality was extreme
- effort had weak explanatory power

---

## 12. Next refinement idea

To isolate the effect of overlapping contests, I plan to:

> restrict each agent to at most one win per step

This keeps:
- local interaction
- decentralized structure

but removes:
- multiple rewards per round

---

## 13. What I expect after the change

If my reasoning is correct:

- Gini should decrease
- top 10% share should decrease
- effort-success correlation should increase

If not, then:
- something else is driving inequality

---

## 14. Broader takeaway

This project made me realize:

> inequality is not just about individual differences (effort or luck)

It can also come from:
- how opportunities are structured
- how often agents interact
- how rewards are distributed

---

## 15. What I would explore next

Some possible extensions:

- network instead of grid
- dynamic effort (agents adapt behavior)
- limited number of opportunities per step
- removing cumulative advantage ($\delta = 0$)
- comparing deterministic vs probabilistic selection

---

## 16. Reflection on Mesa

Building this helped me understand:

- Mesa is not just about defining agents as objects
- it is about explicitly modeling how agents interact and influence each other

Also:

- small implementation choices matter a lot
- emergent behavior is very sensitive

---
## 17. Early thoughts on framework limitations

While building this model, I started to notice some limitations that may become more important for more complex behavior:

- decision logic is embedded directly inside the agent, making it harder to separate "state" from "decision process"
- the step/advance structure works for simple updates, but may not scale well to multi-stage or conditional decisions
- there is no clear abstraction for representing decision systems (eg. separating belief, decision, and action)

These did not block this model, but they suggest that building more structured behavioral agents may require additional design patterns or framework support.

---

## Final thought

This started as a simple idea about effort vs luck.

It turned into something more interesting:

> the structure of interaction can matter more than effort or luck themselves.
