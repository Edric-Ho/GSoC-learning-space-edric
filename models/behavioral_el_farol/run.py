from core import BehavioralElFarolModel


def main() -> None:
    # Basic configuration
    n_agents = 100
    capacity = 60
    steps = 50
    seed = 42

    model = BehavioralElFarolModel(
        n_agents=n_agents,
        capacity=capacity,
        seed=seed,
    )

    for _ in range(steps):
        model.step()

    print("Behavioral El Farol run complete.")
    print(f"Agents: {n_agents}")
    print(f"Capacity: {capacity}")
    print(f"Steps: {steps}")
    print(f"Final attendance: {model.current_attendance}")

    if model.attendance_history:
        avg_attendance = sum(model.attendance_history) / len(model.attendance_history)
        overcrowded_steps = sum(1 for x in model.attendance_history if x > capacity)

        print(f"Average attendance: {avg_attendance:.2f}")
        print(f"Overcrowded steps: {overcrowded_steps}/{steps}")
        print("Attendance history:")
        print(model.attendance_history)

    try:
        import matplotlib.pyplot as plt

        plt.plot(model.attendance_history)
        plt.axhline(y=capacity, linestyle="--")
        plt.xlabel("Step")
        plt.ylabel("Attendance")
        plt.title("Behavioral El Farol Attendance Over Time")
        plt.show()
    except ImportError:
        print("matplotlib not installed; skipping plot.")


if __name__ == "__main__":
    main()
