from core import PipelineModel

def main():
    model = PipelineModel(
        num_agents=100,
        initial_energy=6,
        max_energy=10,
        decision_margin=0.15,
        work_cost=2,
        work_reward=1,
        rest_gain=1,
        seed=42,
    )

    for _ in range(100):
        model.step()

    print(f"Steps completed: {model.steps}")
    print(f"Average energy: {model.avg_energy():.4f}")
    print(f"Average reward: {model.avg_reward():.4f}")

    df = model.datacollector.get_model_vars_dataframe()
    print("\nLast 5 rows:")
    print(df.tail())


if __name__ == "__main__":
    main()
