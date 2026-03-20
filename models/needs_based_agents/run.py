from __future__ import annotations

from core import NeedsBasedModel


def main() -> None:
    model = NeedsBasedModel(
        num_agents=100,
        initial_energy=6,
        max_energy=10,
        low_threshold=2,
        high_threshold=7,
        reward_target=8,
        decision_margin=0.15,
        work_cost=2,
        work_reward=1,
        rest_gain=1,
        seed=42,
    )

    for _ in range(100):
        model.step()

    print(f"Steps completed: {model.steps}")
    print(f"Average energy: {model.compute_average_energy():.4f}")
    print(f"Average reward: {model.compute_average_reward():.4f}")
    print(f"Working fraction: {model.compute_working_fraction():.4f}")
    print(f"Resting fraction: {model.compute_resting_fraction():.4f}")

    model_df = model.datacollector.get_model_vars_dataframe()
    print("\nLast 5 rows of model-level metrics:")
    print(model_df.tail())


if __name__ == "__main__":
    main()
