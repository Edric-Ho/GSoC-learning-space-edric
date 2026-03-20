from __future__ import annotations
import mesa


class PipelineAgent(mesa.Agent):
    """
    Agent with explicit behavioral pipeline:
    observe -> evaluate -> decide -> act
    """
    def __init__(self, model: "PipelineModel", initial_energy: int) -> None:
        super().__init__(model)
        self.energy = initial_energy
        self.reward = 0
        self.last_action = "none"

        # internal temporary state
        self.rest_pressure = 0.0
        self.work_pressure = 0.0
        self.action = None

    # --- PIPELINE STAGES ---
    def observe(self) -> None:
        """Read internal state (placeholder for future extensions)."""
        pass

    def evaluate(self) -> None:
        """Compute internal drives."""
        self.rest_pressure = 1.0 - (self.energy / self.model.max_energy)
        self.work_pressure = max(0.3, 1.0 / (1.0 + self.reward))

    def decide(self) -> None:
        """Resolve conflict between drives."""
        gap = self.work_pressure - self.rest_pressure

        if gap > self.model.decision_margin:
            self.action = "work"
        elif gap < -self.model.decision_margin:
            self.action = "rest"
        else:
            p_work = 0.5 + 0.5 * gap
            if self.random.random() < p_work:
                self.action = "work"
            else:
                self.action = "rest"

    def act(self) -> None:
        """Apply consequences."""
        if self.action == "work":
            self.reward += self.model.work_reward
            self.energy -= self.model.work_cost
        else:
            self.energy += self.model.rest_gain

        self.energy = max(0, min(self.energy, self.model.max_energy))
        self.last_action = self.action

    def step(self) -> None:
        self.observe()
        self.evaluate()
        self.decide()
        self.act()
