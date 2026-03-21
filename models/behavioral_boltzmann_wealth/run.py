from core import BehavioralBoltzmannWealthModel


def main() -> None:
    n_agents = 100
    initial_wealth = 1
    steps = 200
    seed = 42

    model = BehavioralBoltzmannWealthModel(
        n_agents=n_agents,
        initial_wealth=initial_wealth,
        seed=seed,
    )

    for _ in range(steps):
        model.step()

    wealths = [agent.wealth for agent in model.agents]

    print("Behavioral Boltzmann Wealth run complete.")
    print(f"Agents: {n_agents}")
    print(f"Initial wealth: {initial_wealth}")
    print(f"Steps: {steps}")
    print(f"Total wealth: {sum(wealths)}")
    print(f"Mean wealth: {sum(wealths) / len(wealths):.2f}")
    print(f"Min wealth: {min(wealths)}")
    print(f"Max wealth: {max(wealths)}")

    wealths = sorted(wealths)
    print("Top 10 wealth values:", wealths[-10:])

    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(6, 4))
        plt.hist(wealths, bins=20)
        plt.xlabel("Wealth")
        plt.ylabel("Number of Agents")
        plt.title("Behavioral Boltzmann Wealth Distribution")
        plt.show()
    except ImportError:
        print("matplotlib not installed; skipping plot.")


if __name__ == "__main__":
    main()
