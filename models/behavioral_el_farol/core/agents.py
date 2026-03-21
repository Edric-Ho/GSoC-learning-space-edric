from mesa import Agent
from .pipeline import DecisionPipeline
from .strategies import MovingAveragePredictor


class BehavioralElFarolAgent(Agent):
    def __init__(self, model, strategy=None):
        super().__init__(model)
        if strategy is None:
            agent_window = self.random.choice([3, 5, 8, 12])
            self.strategy = MovingAveragePredictor(window=agent_window)
        else:
            self.strategy = strategy
        self.pipeline = DecisionPipeline()
        self.predicted_attendance = 0.0
        self.intends_to_go = False
        self.last_payoff = 0
        self.total_payoff = 0

    def step(self):
        self.pipeline.run(self)

    def finalize_round(self, realized_attendance: int):
        if self.intends_to_go:
            self.last_payoff = 1 if realized_attendance <= self.model.capacity else -1
        else:
            self.last_payoff = 0
        self.total_payoff += self.last_payoff
