from models.behavioral_el_farol.core.model import BehavioralElFarolModel


def test_model_initializes():
    model = BehavioralElFarolModel(n_agents=20, capacity=12, seed=42)
    assert len(model.agents) == 20
    assert model.capacity == 12
    assert model.current_attendance == 0
    assert model.attendance_history == []


def test_model_runs_one_step():
    model = BehavioralElFarolModel(n_agents=20, capacity=12, seed=42)
    model.step()

    assert isinstance(model.current_attendance, int)
    assert 0 <= model.current_attendance <= 20
    assert len(model.attendance_history) == 1


def test_model_runs_multiple_steps():
    model = BehavioralElFarolModel(n_agents=20, capacity=12, seed=42)

    for _ in range(5):
        model.step()

    assert len(model.attendance_history) == 5
    assert all(isinstance(x, int) for x in model.attendance_history)
    assert all(0 <= x <= 20 for x in model.attendance_history)


def test_agent_payoffs_are_updated():
    model = BehavioralElFarolModel(n_agents=20, capacity=12, seed=42)
    model.step()

    payoffs = [agent.last_payoff for agent in model.agents]
    assert all(p in (-1, 0, 1) for p in payoffs)
