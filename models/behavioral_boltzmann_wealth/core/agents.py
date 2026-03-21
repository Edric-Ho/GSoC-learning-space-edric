from mesa import Agent
from .pipeline import DecisionPipeline


class BehavioralBoltzmannWealthAgent(Agent):
    def __init__(self, model, initial_wealth: int = 1):
        super().__init__(model)
        self.wealth = initial_wealth
        self.pipeline = DecisionPipeline()

    def decide_transfer(self, partner) -> int:
        return self.pipeline.run(self, partner)
