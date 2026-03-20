from __future__ import annotations
import mesa


class NeedsAgent(mesa.Agent):
    """
    The agent balances two competing pressures:
    - reward seeking: working increases reward
    - recovery: resting restores energy

    Intentionally simple  to make the decision process
    explicit and easy to inspect.
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

    def decide_action(self) -> str:
        """
        A decision rule:
        - very low energy -> rest
        - high energy -> work
        - middle range -> probabilistic choice
        """
        if self.energy <= self.model.low_threshold:
            return "rest"

        if self.energy >= self.model.high_threshold:
            return "work"

        # In the middle range, agents are more likely to work if they have
        # more energy available.
        p_work = self.energy / self.model.max_energy
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

        # Clamp energy to a valid range.
        self.energy = max(0, min(self.energy, self.model.max_energy))
        self.last_action = action

    def step(self) -> None:
        """
        The behavioral pipeline is explicit here:

        observe internal state -> decide -> act

        One thing this model is meant to expose is that, even in this simple
        setup, all of this logic starts to accumulate inside the agent.
        """
        action = self.decide_action()
        self.execute_action(action)
