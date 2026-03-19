# This script runs multiple simulations to see how results vary across runs.
# Single runs can be noisy, so batch runs give a more reliable picture.

from __future__ import annotations
import itertools
import pandas as pd
from models.local_inequality_model.core import LocalInequalityModel


def run_one_replication(
    sigma: float,
    delta: float,
    effort_low: float,
    effort_high: float,
    steps: int,
    seed: int,
) -> dict:
    """Run one simulation and return the final summary statistics."""
    model = LocalInequalityModel(
        width=20,
        height=20,
        beta=1.0,
        delta=delta,
        sigma=sigma,
        lambda_fatigue=0.00,
        effort_low=effort_low,
        effort_high=effort_high,
        radius=1,
        seed=seed,
    )

    for _ in range(steps):
        # Advance one simulation for the chosen number of steps.
        model.step()

    return {
        "sigma": sigma,
        "delta": delta,
        "effort_low": effort_low,
        "effort_high": effort_high,
        "steps": steps,
        "seed": seed,
        "gini": model.compute_gini(),
        "top10_share": model.compute_top10_share(),
        "mean_success": model.compute_mean_success(),
        "variance_success": model.compute_variance_success(),
        "effort_success_corr": model.compute_effort_success_correlation(),
    }


def main() -> None:
    # I keep the grid small and readable here.
    # The point is not exhaustive search, just seeing how the main parameters
    # change the shape of inequality.
    sigma_values = [0.10, 0.50, 1.00]
    delta_values = [0.00, 0.10, 0.30]
    effort_ranges = [(0.95, 1.05), (0.80, 1.20)]
    seeds = [11, 22, 33, 44, 55]
    steps = 100

    rows = []
    for sigma, delta, (effort_low, effort_high), seed in itertools.product(
        sigma_values,
        delta_values,
        effort_ranges,
        seeds,
    ):
        rows.append(
            run_one_replication(
                sigma=sigma,
                delta=delta,
                effort_low=effort_low,
                effort_high=effort_high,
                steps=steps,
                seed=seed,
            )
        )

    df = pd.DataFrame(rows)
    summary = (
        df.groupby(["sigma", "delta", "effort_low", "effort_high"], as_index=False)
        .agg(
            mean_gini=("gini", "mean"),
            sd_gini=("gini", "std"),
            mean_top10_share=("top10_share", "mean"),
            mean_effort_success_corr=("effort_success_corr", "mean"),
        )
        .sort_values(["sigma", "delta", "effort_low", "effort_high"])
    )

    output_csv = "batch_results.csv"
    summary.to_csv(output_csv, index=False)

    print("Saved summarized parameter sweep results to:", output_csv)
    print("\nPreview:")
    print(summary.head(12))


if __name__ == "__main__":
    main()
