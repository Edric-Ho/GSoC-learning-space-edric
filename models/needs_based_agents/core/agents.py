from __future__ import annotations
import mesa


class NeedsAgent(mesa.Agent):
    """
    The agent balances two competing pressures:
        - reward seeking: working increases reward
        - recovery: resting restores energy

    The goal is to make the decision structure
    explicit enough to expose how behavioral logic gets organized in Mesa.
    """

    def __init__(
            self,
            model: "NeedsBasedModel",
            initial_energy: int,
    ) -> None:
        super().__init__(model)
        self.energy = initial_energy
        self.reward = 0
        self.last_action = "none"

    def compute_rest_pressure(self) -> float:
        """
        Higher when energy is low.
        Ranges roughly from 0 to 1.
        """
        return 1.0 - (self.energy / self.model.max_energy)

    def compute_work_pressure(self) -> float:
        """
        Higher when accumulated reward is still low.
        This makes the agent feel some pressure to keep working early on,
        but that pressure weakens as reward builds up.
        """
        return max(0.3, 1.0 / (1.0 + self.reward))

    def decide_action(self) -> str:
        """
        Decision pipeline:
        1. Check hard constraints
        2. Compare internal pressures
        3. If neither side dominates, choose probabilistically
        """
        # Hard guard: if energy is critically low, rest.
        if self.energy <= self.model.low_threshold:
            return "rest"

        # Hard guard: if energy is very high and reward is still low, work.
        if self.energy >= self.model.high_threshold and self.reward <= self.model.reward_target:
            return "work"

        rest_pressure = self.compute_rest_pressure()
        work_pressure = self.compute_work_pressure()

        pressure_gap = work_pressure - rest_pressure

        # If one side clearly dominates, choose deterministically.
        if pressure_gap >= self.model.decision_margin:
            return "work"
        if pressure_gap <= -self.model.decision_margin:
            return "rest"

        # Otherwise, resolve the conflict probabilistically.
        # Shift pressure_gap from roughly [-margin, margin] into a probability.
        p_work = 0.5 + 0.5 * pressure_gap
        p_work = max(0.0, min(1.0, p_work))

        if self.random.random() < p_work:
            return "work"
        return "rest"

    def execute_action(self, action: str) -> None:
        """
        Apply the consequences of the chosen action.
        """
        if action == "work":
            self.reward += self.model.work_reward
            self.energy -= self.model.work_cost
        elif action == "rest":
            self.energy += self.model.rest_gain
        else:
            raise ValueError(f"Unknown action: {action}")

        self.energy = max(0, min(self.energy, self.model.max_energy))
        self.last_action = action

    def step(self) -> None:
        """
        Minimal behavioral cycle:
        observe internal state -> decide -> act

        Even in this simple model, behavior is already more structured than
        a single formula, which is exactly why this is useful for evaluating
        behavioral modeling in Mesa.
        """
        action = self.decide_action()
        self.execute_action(action)
