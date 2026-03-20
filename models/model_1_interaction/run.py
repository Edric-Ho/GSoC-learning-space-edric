# This script runs a single simulation and prints summary statistics.
# I use it mainly for quick iteration and sanity checks.

from __future__ import annotations
from models.model_1_interaction.core import LocalInequalityModel


def main() -> None:
    """Run one baseline simulation and print a quick summary."""
    model = LocalInequalityModel(
        width=20,
        height=20,
        beta=1.0,
        delta=0.10,
        sigma=0.50,
        lambda_fatigue=0.00,
        effort_low=0.80,
        effort_high=1.20,
        radius=1,
        seed=42,
    )

    for _ in range(100):
        model.step()

    print(f"Steps completed: {model.steps}")
    print(f"Gini: {model.compute_gini():.4f}")
    print(f"Top 10% share: {model.compute_top10_share():.4f}")
    print(f"Mean success: {model.compute_mean_success():.4f}")
    print(f"Variance of success: {model.compute_variance_success():.4f}")
    print(f"Effort-success correlation: {model.compute_effort_success_correlation():.4f}")

    model_df = model.datacollector.get_model_vars_dataframe()
    print("\nLast 5 rows of model-level metrics:")
    print(model_df.tail())
    # I print the last few rows just to see whether the metrics
    # are still moving sharply near the end.


if __name__ == "__main__":
    main()
