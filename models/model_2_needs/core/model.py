from __future__ import annotations
import mesa
import numpy as np
from mesa.datacollection import DataCollector
from .agents import NeedsAgent


class NeedsBasedModel(mesa.Model):
    """
    Agents repeatedly choose between:
        - work: gain reward, lose energy
        - rest: regain energy, gain no immediate reward
    """

    def __init__(
            self,
            num_agents: int = 100,
            initial_energy: int = 6,
            max_energy: int = 10,
            low_threshold: int = 2,
            high_threshold: int = 7,
            reward_target: int = 8,
            decision_margin: float = 0.15,
            work_cost: int = 2,
            work_reward: int = 1,
            rest_gain: int = 1,
            seed: int | None = None,
    ) -> None:
        super().__init__(seed=seed)

        self.num_agents = num_agents
        self.initial_energy = initial_energy
        self.max_energy = max_energy
        self.low_threshold = low_threshold
        self.high_threshold = high_threshold
        self.reward_target = reward_target
        self.decision_margin = decision_margin
        self.work_cost = work_cost
        self.work_reward = work_reward
        self.rest_gain = rest_gain

        for _ in range(self.num_agents):
            NeedsAgent(self, initial_energy=self.initial_energy)

        self.datacollector = DataCollector(
            model_reporters={
                "AverageEnergy": self.compute_average_energy,
                "AverageReward": self.compute_average_reward,
                "WorkingFraction": self.compute_working_fraction,
                "RestingFraction": self.compute_resting_fraction,
            },
            agent_reporters={
                "energy": "energy",
                "reward": "reward",
                "last_action": "last_action",
            },
        )

        self.datacollector.collect(self)

    def compute_average_energy(self) -> float:
        return float(np.mean([agent.energy for agent in self.agents]))

    def compute_average_reward(self) -> float:
        return float(np.mean([agent.reward for agent in self.agents]))

    def compute_working_fraction(self) -> float:
        if len(self.agents) == 0:
            return 0.0
        working = sum(agent.last_action == "work" for agent in self.agents)
        return working / len(self.agents)

    def compute_resting_fraction(self) -> float:
        if len(self.agents) == 0:
            return 0.0
        resting = sum(agent.last_action == "rest" for agent in self.agents)
        return resting / len(self.agents)

    def step(self) -> None:
        self.agents.do("step")
        self.datacollector.collect(self)
