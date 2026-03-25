from behavioral_execution.model import SimpleNeedsModel
from baseline_monolithic import MonolithicNeedsAgent


def extract_monolithic_trace(steps=10):
    agent = MonolithicNeedsAgent()
    trace = []
    for _ in range(steps):
        agent.step()
        trace.append((agent.last_event, agent.energy, agent.wealth))
    return trace


def extract_behavioral_trace(steps=10):
    model = SimpleNeedsModel(n_agents=1, seed=100)
    agent = list(model.agents)[0]
    trace = []
    for _ in range(steps):
        model.step()
        trace.append((agent.last_action_event, agent.energy, agent.wealth))
    return trace


def test_behavioral_matches_monolithic_trace():
    assert extract_behavioral_trace() == extract_monolithic_trace()


def test_behavioral_model_runs_multiple_steps():
    model = SimpleNeedsModel(n_agents=1, seed=100)
    for _ in range(5):
        model.step()
    agent = list(model.agents)[0]
    assert 0 <= agent.energy <= agent.max_energy


def test_work_action_is_multi_step():
    model = SimpleNeedsModel(n_agents=1, seed=100)
    agent = list(model.agents)[0]

    model.step()
    first_event = agent.last_action_event
    current_action = agent.current_action.name if agent.current_action else None

    assert "work" in first_event or current_action == "work"


def test_completion_and_recovery_appear_in_trace():
    trace = extract_behavioral_trace()
    events = [event for event, _, _ in trace]

    assert "work(complete)" in events
    assert "emergency_rest(complete)" in events or "rest(complete)" in events


def test_interrupt_appears_when_energy_starts_low_during_work():
    model = SimpleNeedsModel(n_agents=1, seed=100)
    agent = list(model.agents)[0]

    work_action = next(action for action in agent.actions if action.name == "work")
    agent.current_action = work_action
    agent.action_progress = 2
    agent.energy = 1
    agent.last_action_event = "none"

    model.step()

    assert agent.last_action_event == "work(interrupt)"
    assert agent.current_action is None


def test_agent_never_exceeds_max_energy():
    model = SimpleNeedsModel(n_agents=1, seed=100)
    for _ in range(20):
        model.step()
        agent = list(model.agents)[0]
        assert 0 <= agent.energy <= agent.max_energy


def test_leisure_action_executes_in_extended_model():
    from behavioral_execution.model import ExtendedNeedsModel

    model = ExtendedNeedsModel(n_agents=1, seed=100)
    agent = list(model.agents)[0]

    found = False
    for _ in range(12):
        model.step()
        if "leisure" in agent.last_action_event:
            found = True
            break

    assert found
