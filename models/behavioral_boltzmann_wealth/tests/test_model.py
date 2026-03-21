from models.behavioral_boltzmann_wealth.core.model import BehavioralBoltzmannWealthModel


def test_model_initializes():
    model = BehavioralBoltzmannWealthModel(n_agents=20, initial_wealth=1, seed=42)
    assert len(model.agents) == 20
    assert model.initial_wealth == 1


def test_total_wealth_is_conserved():
    model = BehavioralBoltzmannWealthModel(n_agents=20, initial_wealth=1, seed=42)
    initial_total = sum(agent.wealth for agent in model.agents)

    for _ in range(10):
        model.step()

    final_total = sum(agent.wealth for agent in model.agents)
    assert initial_total == final_total


def test_wealth_never_negative():
    model = BehavioralBoltzmannWealthModel(n_agents=20, initial_wealth=1, seed=42)

    for _ in range(10):
        model.step()

    assert all(agent.wealth >= 0 for agent in model.agents)


def test_model_runs_multiple_steps():
    model = BehavioralBoltzmannWealthModel(n_agents=20, initial_wealth=1, seed=42)

    for _ in range(5):
        model.step()

    df = model.datacollector.get_model_vars_dataframe()
    assert len(df) == 5


def test_agents_have_risk_tolerance():
    model = BehavioralBoltzmannWealthModel(n_agents=20, initial_wealth=1, seed=42)
    assert all(hasattr(agent, "risk_tolerance") for agent in model.agents)
