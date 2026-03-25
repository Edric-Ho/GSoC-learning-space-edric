from __future__ import annotations
import mesa
from .action import Action
from .engine import BehaviorEngine
from .evaluator import NeedsEvaluator
from .executor import ActionExecutor
from .observation import NeedsObservation
from .policy import GreedyPolicy


class BehavioralAgent(mesa.Agent):
    def __init__(
            self,
            model,
            behavior_engine: BehaviorEngine,
            actions: list[Action],
    ) -> None:
        super().__init__(model)
        self.behavior_engine = behavior_engine
        self.actions = actions
        self.current_action: Action | None = None
        self.last_action_event = "none"

    def step(self) -> None:
        self.behavior_engine.step(self)


class WorkAction(Action):
    name = "work"

    def is_feasible(self, agent, observation) -> bool:
        return observation.energy >= 2

    def start(self, agent) -> None:
        super().start(agent)
        agent.last_action_event = "work(start)"

    def step(self, agent) -> None:
        self.progress += 1
        agent.energy = max(0, agent.energy - 2)

        if self.progress < 3:
            agent.last_action_event = "work(continue)"
        else:
            agent.wealth += 3
            agent.last_action_event = "work(complete)"

    def abort(self, agent) -> None:
        super().abort(agent)

    def is_complete(self, agent) -> bool:
        return self.progress >= 3


class RestAction(Action):
    name = "rest"

    def is_feasible(self, agent, observation) -> bool:
        return observation.energy < observation.max_energy

    def start(self, agent) -> None:
        super().start(agent)
        agent.last_action_event = "rest(start)"

    def step(self, agent) -> None:
        self.progress += 1
        agent.energy = min(agent.max_energy, agent.energy + 2)
        agent.last_action_event = "rest(complete)"

    def abort(self, agent) -> None:
        super().abort(agent)

    def is_complete(self, agent) -> bool:
        return self.progress >= 1


class EmergencyRestAction(Action):
    name = "emergency_rest"

    def is_feasible(self, agent, observation) -> bool:
        return observation.energy <= 1

    def start(self, agent) -> None:
        super().start(agent)
        agent.last_action_event = "emergency_rest(start)"

    def step(self, agent) -> None:
        self.progress += 1
        agent.energy = min(agent.max_energy, agent.energy + 4)
        agent.last_action_event = "emergency_rest(complete)"

    def abort(self, agent) -> None:
        super().abort(agent)

    def is_complete(self, agent) -> bool:
        return self.progress >= 1


class LeisureAction(Action):
    name = "leisure"

    def is_feasible(self, agent, observation) -> bool:
        return observation.energy >= 3

    def start(self, agent) -> None:
        super().start(agent)
        agent.last_action_event = "leisure(start)"

    def step(self, agent) -> None:
        self.progress += 1
        agent.energy = max(0, agent.energy - 1)

        if self.progress < 2:
            agent.last_action_event = "leisure(continue)"
        else:
            agent.wealth += 1
            agent.last_action_event = "leisure(complete)"

    def abort(self, agent) -> None:
        super().abort(agent)

    def is_complete(self, agent) -> bool:
        return self.progress >= 2


class NeedsBehavioralAgent(BehavioralAgent):
    def __init__(self, model):
        actions = [
            EmergencyRestAction(),
            WorkAction(),
            RestAction(),
        ]

        behavior_engine = BehaviorEngine(
            observation_module=NeedsObservation(),
            evaluator=NeedsEvaluator(),
            decision_policy=GreedyPolicy(),
            action_executor=ActionExecutor(),
        )

        super().__init__(
            model=model,
            behavior_engine=behavior_engine,
            actions=actions,
        )

        self.energy = 6
        self.max_energy = 10
        self.wealth = 0


class ExtendedNeedsBehavioralAgent(BehavioralAgent):
    def __init__(self, model):
        actions = [
            EmergencyRestAction(),
            WorkAction(),
            RestAction(),
            LeisureAction(),
        ]

        behavior_engine = BehaviorEngine(
            observation_module=NeedsObservation(),
            evaluator=NeedsEvaluator(),
            decision_policy=GreedyPolicy(),
            action_executor=ActionExecutor(),
        )

        super().__init__(
            model=model,
            behavior_engine=behavior_engine,
            actions=actions,
        )

        self.energy = 4
        self.max_energy = 10
        self.wealth = 0

    def step(self) -> None:
        self.behavior_engine.step(self)
