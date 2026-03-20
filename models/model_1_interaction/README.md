# From Effort to Inequality: A Local Competition Model in Mesa

## 0. Why I built this

I started with a simple question:

> If people put in similar effort, why do outcomes still end up so unequal?

My first instinct was to model this as a simple accumulation process:

$$
S_{i,t+1} = S_{i,t} + \alpha E_i + \varepsilon_{i,t}
$$

where effort contributes linearly and randomness adds noise.

But after thinking about it more, this didn’t really feel like an agent-based model anymore, agents weren’t interacting, they were just evolving independently.

So I shifted to something more **Mesa-native**: local interaction and competition.

---

## 1. What this model does

I place one agent on each grid cell. Each agent has:

- a fixed effort level $E_i$ (drawn from a small range)
- a success value $S_i(t)$ that evolves over time
- a fatigue term $F_i(t)$ that acts as a mild constraint

At every step, the process is:

1. Each agent computes a score:

$$
Z_i(t) = \beta E_i + \delta S_i(t) - \lambda F_i(t) + \varepsilon_i(t)
$$

   where:
   - $\beta$: weight on effort
   - $\delta$: strength of cumulative advantage
   - $\lambda$: fatigue penalty
   - $\varepsilon_i(t) \sim \mathcal{N}(0, \sigma^2)$: randomness

2. Each grid cell acts like a local “opportunity center”

3. Agents in the neighborhood compete using their scores

4. A winner is selected probabilistically using a softmax rule:

$$
P(i \text{ wins}) = \frac{\exp(Z_i)}{\sum_{j \in \mathcal{N}} \exp(Z_j)}
$$

5. The winner gains one unit of success:

$$
S_i(t+1) = S_i(t) + 1
$$

Everything is local — there is no global ranking or centralized decision.

---

## 1.5 Why this fits Mesa

This model is intentionally designed around Mesa’s core ideas:

- agents are autonomous and stateful
- interactions are local (grid-based neighborhoods)
- global outcomes emerge from repeated decentralized interactions

I avoided any global ranking or centralized allocation mechanism,
so all structure comes from agent interaction rather than external control.

This helped me better understand how Mesa’s abstractions
(space, agents, scheduler) support emergent behavior.

---

## 2. What I expected vs what actually happened

I expected:
- some inequality (due to randomness and feedback)
- but still a noticeable relationship between effort and success

What I actually got:

- Gini $≈ 0.78$
- top 10% share $≈ 0.70$
- effort-success correlation $≈ 0.19$

So:
- outcomes are highly concentrated
- effort only weakly explains success

---

## 3. How I measure inequality and structure

I track a few simple statistics:

### Gini coefficient

Used as the main inequality measure:

$$
G = \frac{2 \sum_{i=1}^{n} i x_i}{n \sum x_i} - \frac{n+1}{n}
$$

where values are sorted.

This gives a single number summary of inequality.

---

### Top 10% share

I also compute the fraction of total success held by the top 10% of agents.

This helps distinguish between:
- moderate inequality
- extreme concentration

---

### Effort–success correlation

I compute:

$$
\text{Corr}(E_i, S_i)
$$

This tells me how much final outcomes still reflect effort.

If this stays low, it means:
- randomness and interaction structure dominate
- effort alone does not explain outcomes

---

## 4. Mechanism behind the outcome

The results were significantly more extreme than expected.

From inspecting the model dynamics, a key mechanism appears to be:

> agents can win multiple overlapping contests in the same step

Because each grid cell hosts a contest and neighborhoods overlap,
a single agent can participate in multiple contests within one round.

This creates a compounding effect:

- winning increases success
- higher success increases future competitiveness
- increased competitiveness leads to more wins

This feedback loop operates within a single time step,
which accelerates inequality formation beyond what I initially expected.

---

## 5. What I think is causing this

The results were much more extreme than I expected.

After inspecting the model, I think the main driver is:

> agents can win multiple overlapping contests in the same step

Because:
- every cell runs a contest
- neighborhoods overlap
- the same agent can appear in many contests

So a strong agent can win multiple times in one round.

That creates a strong feedback loop:

- win → higher success
- higher success → higher score
- higher score → more wins

This compounds very quickly.

---

## 6. Refinement: limiting wins per step

To isolate the effect of overlapping contests, I modified the model so that:

- each agent can win **at most once per step**

Everything else in the model remains unchanged:
- same grid
- same parameters
- same scoring rule
- same stochasticity

This keeps the interaction local and decentralized,
but removes the strongest within-step amplification mechanism.

The goal of this change is not to make the model "better",
but to understand which part of the system is driving the extreme inequality.

---

## 7. Before vs after refinement

Baseline version (multiple wins per step allowed):
- Gini: 0.7810
- top 10% share: 0.6996
- effort-success correlation: 0.1920

Refined version (at most one win per agent per step):
- Gini: 0.0524
- top 10% share: 0.1068
- effort-success correlation: 0.0663

The difference between the two versions is striking.

In the baseline model, inequality becomes extreme: a small fraction of agents captures most of the total success. However, once each agent is restricted to at most one win per step, the system becomes nearly egalitarian.

This suggests that the dominant driver of inequality in the original model was not effort or randomness alone, but the ability of agents to accumulate multiple rewards within the same timestep due to overlapping local interactions.

In other words, inequality in this system is highly sensitive to how opportunities are structured and allocated in time, not just to individual attributes.

---

## 8. Why this model is useful (to me)

This model made something very clear:

> small local design choices can completely change global outcomes

In particular:
- overlapping opportunities
- reward frequency
- feedback strength

all matter more than I initially expected.

---
## 9. What felt awkward or limiting

While implementing this model, I noticed a few friction points:

- Behavior logic is tightly coupled with the agent class.
  As decision complexity grows, this becomes difficult to maintain or extend.

- The step/advance pattern works well for simple updates,
  but it is not expressive for multi-stage decision processes
  or interruptible actions.

- There is no clear abstraction for "decision systems"
  (e.g., separating belief, decision, and action layers).

These limitations did not affect this model heavily,
but they suggest potential challenges for more complex behavioral agents.

---
## 10. How I evaluate the model

Instead of relying on a single run, I:

- run multiple simulations with different seeds
- aggregate results across runs
- analyze sensitivity to parameters

This helps distinguish:
- structural effects (model design)
- vs randomness (noise)

---
## 11. Connection to behavioral frameworks

In this model, agent behavior is represented by a simple scoring function.
This makes the system easy to analyze, but it also highlights a limitation:

- decision-making is implicit (through a formula)
- rather than explicitly modeled (through structured reasoning)

Extending this model to behavioral frameworks would require:

- separating state (beliefs) from decision logic
- introducing explicit action selection processes
- supporting multi-stage or conditional decisions

For example:

- a needs-based agent would balance competing internal states (eg. fatigue vs reward)
- a BDI agent would explicitly represent goals and intentions
- a learning agent would update behavior based on past outcomes

While Mesa supports simple agent logic well, this model suggests that:
> more structured behavioral systems require additional design patterns
or abstractions that are not immediately available.

This aligns directly with the goal of evaluating Mesa’s support
for behavioral modeling through hands-on implementation.

---


## How to run

```bash
pip install -r requirements.txt
python run.py
