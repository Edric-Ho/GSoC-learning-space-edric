from models.needs_based_agents.core import NeedsBasedModel

def main() -> None:
    model = NeedsBasedModel(num_agents=20, seed=123)

    for _ in range(5):
        model.step()

    assert len(model.agents) == 20
    assert model.compute_average_energy() >= 0.0
    assert model.compute_average_reward() >= 0.0
    print("Smoke test passed.")


if __name__ == "__main__":
    main()
