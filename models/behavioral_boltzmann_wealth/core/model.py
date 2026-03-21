from mesa import Model
from mesa.datacollection import DataCollector
from .agents import BehavioralBoltzmannWealthAgent


class BehavioralBoltzmannWealthModel(Model):
    def __init__(self, n_agents: int = 100, initial_wealth: int = 1, seed=None):
        super().__init__(rng=seed)

        self.n_agents = n_agents
        self.initial_wealth = initial_wealth

        for _ in range(n_agents):
            BehavioralBoltzmannWealthAgent(self, initial_wealth=initial_wealth)

        self.datacollector = DataCollector(
            model_reporters={
                "Total Wealth": lambda m: sum(agent.wealth for agent in m.agents),
                "Mean Wealth": lambda m: (
                    sum(agent.wealth for agent in m.agents) / len(m.agents)
                    if len(m.agents) > 0
                    else 0
                ),
                "Max Wealth": lambda m: max(agent.wealth for agent in m.agents),
                "Min Wealth": lambda m: min(agent.wealth for agent in m.agents),
            }
        )

    def step(self):
        agents = list(self.agents)
        self.random.shuffle(agents)

        # pair agents randomly
        for i in range(0, len(agents) - 1, 2):
            a = agents[i]
            b = agents[i + 1]

            stake_a = a.decide_transfer(b)
            stake_b = b.decide_transfer(a)

            # Step 1 baseline:
            # if both can stake, randomly select one donor and one receiver
            if stake_a > 0 and stake_b > 0:
                donor, receiver = (a, b) if self.random.random() < 0.5 else (b, a)
                donor.wealth -= 1
                receiver.wealth += 1

            # if only one can stake, that agent gives 1 to the other
            elif stake_a > 0 and stake_b == 0:
                a.wealth -= 1
                b.wealth += 1
            elif stake_b > 0 and stake_a == 0:
                b.wealth -= 1
                a.wealth += 1

        self.datacollector.collect(self)
