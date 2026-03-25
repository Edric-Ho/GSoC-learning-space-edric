from __future__ import annotations
import mesa
from .action import Action
from .engine import BehaviorEngine
from .evaluator import NeedsEvaluator
from .executor import ActionExecutor
from .observation import NeedsObservation
from .policy import GreedyPolicy


class WorkAction(Action):
    name = "work"

    def is_feasible(self, agent, observation) -> bool:
        return observation.energy >= 2

    def score(self, agent, observation) -> float:
        return 6.0 if observation.energy >= 5 else 2.0

    def start(self, agent) -> None:
        agent.action_progress = 0
        agent.last_action_event = "work(start)"

    def step(self, agent) -> None:
        agent.action_progress += 1

        # consume energy every step
        agent.energy = max(0, agent.energy - 2)

        if agent.action_progress < 3:
            agent.last_action_event = "work(continue)"
        else:
            agent.wealth += 3
            agent.last_action_event = "work(complete)"

    def abort(self, agent) -> None:
        agent.action_progress = 0

    def is_complete(self, agent) -> bool:
        return agent.action_progress >= 3


class RestAction(Action):
    name = "rest"

    def is_feasible(self, agent, observation) -> bool:
        return observation.energy < observation.max_energy

    def score(self, agent, observation) -> float:
        # prefer rest strongly when energy is low
        deficit = observation.max_energy - observation.energy
        return float(deficit + 3 if observation.energy <= 2 else deficit)

    def start(self, agent) -> None:
        agent.action_progress = 0
        agent.last_action_event = "rest(start)"

    def step(self, agent) -> None:
        agent.action_progress += 1
        agent.energy = min(agent.max_energy, agent.energy + 2)

    def abort(self, agent) -> None:
        agent.action_progress = 0

    def is_complete(self, agent) -> bool:
        return agent.action_progress >= 1


class EmergencyRestAction(Action):
    name = "emergency_rest"

    def is_feasible(self, agent, observation) -> bool:
        return observation.energy <= 1

    def score(self, agent, observation) -> float:
        return 100.0

    def start(self, agent) -> None:
        agent.action_progress = 0
        agent.last_action_event = "emergency_rest(start)"

    def step(self, agent) -> None:
        agent.action_progress += 1
        agent.energy = min(agent.max_energy, agent.energy + 4)

    def abort(self, agent) -> None:
        agent.action_progress = 0

    def is_complete(self, agent) -> bool:
        return agent.action_progress >= 1


class LeisureAction(Action):
    name = "leisure"

    def is_feasible(self, agent, observation) -> bool:
        return observation.energy >= 3

    def score(self, agent, observation) -> float:
        if 4 <= observation.energy <= 5:
            return 7.0
        return 1.0

    def start(self, agent) -> None:
        agent.action_progress = 0
        agent.last_action_event = "leisure(start)"

    def step(self, agent) -> None:
        agent.action_progress += 1
        agent.energy = max(0, agent.energy - 1)

        if agent.action_progress < 2:
            agent.last_action_event = "leisure(continue)"
        else:
            agent.wealth += 1
            agent.last_action_event = "leisure(complete)"

    def abort(self, agent) -> None:
        agent.action_progress = 0

    def is_complete(self, agent) -> bool:
        return agent.action_progress >= 2


class NeedsBehavioralAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.energy = 6
        self.max_energy = 10
        self.wealth = 0

        self.current_action = None
        self.action_progress = 0
        self.last_action_event = "none"

        self.actions = [EmergencyRestAction(), WorkAction(), RestAction()]

        self.behavior_engine = BehaviorEngine(
            observation_module=NeedsObservation(),
            evaluator=NeedsEvaluator(),
            decision_policy=GreedyPolicy(),
            action_executor=ActionExecutor(),
        )

    def step(self) -> None:
        self.behavior_engine.step(self)


class ExtendedNeedsBehavioralAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.energy = 4
        self.max_energy = 10
        self.wealth = 0

        self.current_action = None
        self.action_progress = 0
        self.last_action_event = "none"

        self.actions = [
            EmergencyRestAction(),
            WorkAction(),
            RestAction(),
            LeisureAction(),
        ]

        self.behavior_engine = BehaviorEngine(
            observation_module=NeedsObservation(),
            evaluator=NeedsEvaluator(),
            decision_policy=GreedyPolicy(),
            action_executor=ActionExecutor(),
        )

    def step(self) -> None:
        self.behavior_engine.step(self)
