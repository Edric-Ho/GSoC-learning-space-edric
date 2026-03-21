from mesa import Agent
from .pipeline import DecisionPipeline


class BehavioralBoltzmannWealthAgent(Agent):
    def __init__(self, model, initial_wealth: int = 1, risk_tolerance: float | None = None):
        super().__init__(model)
        self.wealth = initial_wealth
        self.risk_tolerance = (
            risk_tolerance if risk_tolerance is not None else self.random.uniform(0.8, 1.2)
        )
        self.pipeline = DecisionPipeline()

    def decide_transfer(self, partner) -> int:
        return self.pipeline.run(self, partner)
