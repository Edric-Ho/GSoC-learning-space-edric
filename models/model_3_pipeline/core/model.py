from __future__ import annotations
import mesa
import numpy as np
from mesa.datacollection import DataCollector
from .agents import PipelineAgent


class PipelineModel(mesa.Model):

    def __init__(
            self,
            num_agents=100,
            initial_energy=6,
            max_energy=10,
            decision_margin=0.15,
            work_cost=2,
            work_reward=1,
            rest_gain=1,
            seed=None,
    ):
        super().__init__(seed=seed)

        self.num_agents = num_agents
        self.max_energy = max_energy
        self.decision_margin = decision_margin
        self.work_cost = work_cost
        self.work_reward = work_reward
        self.rest_gain = rest_gain

        for _ in range(self.num_agents):
            PipelineAgent(self, initial_energy)

        self.datacollector = DataCollector(
            model_reporters={
                "AvgEnergy": self.avg_energy,
                "AvgReward": self.avg_reward,
                "WorkingFraction": self.working_fraction,
                "RestingFraction": self.resting_fraction,
            }
        )

        self.datacollector.collect(self)

    def avg_energy(self):
        return np.mean([a.energy for a in self.agents])

    def avg_reward(self):
        return np.mean([a.reward for a in self.agents])

    def step(self):
        self.agents.do("step")
        self.datacollector.collect(self)

    def working_fraction(self):
        working = sum(a.last_action == "work" for a in self.agents)
        return working / len(self.agents)

    def resting_fraction(self):
        resting = sum(a.last_action == "rest" for a in self.agents)
        return resting / len(self.agents)
