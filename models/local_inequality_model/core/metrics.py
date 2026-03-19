# These metrics are used to quantify inequality and structure of outcomes.
# I focus on simple, interpretable measures rather than complex ones.

from __future__ import annotations
import math
from typing import Sequence
import numpy as np


def gini(values: Sequence[float]) -> float:
    """Return the Gini coefficient of the input values.

    I use Gini as the main inequality summary because it is standard,
    compact, and easy to compare across runs.
    """
    arr = np.asarray(values, dtype=float)
    if arr.size == 0 or np.all(arr == 0):
        return 0.0
    if np.any(arr < 0):
        raise ValueError("Nonnegative values required.")

    arr_sorted = np.sort(arr)
    n = arr_sorted.size
    index = np.arange(1, n + 1)
    return float((2 * np.sum(index * arr_sorted)) / (n * np.sum(arr_sorted)) - (n + 1) / n)


def top_share(values: Sequence[float], top_fraction: float = 0.10) -> float:
    """Return the share held by the top fraction of values.

    I like this alongside Gini because it makes concentration at the top
    more visible.
    """
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return 0.0
    total = arr.sum()
    if total <= 0:
        return 0.0
    k = max(1, int(math.ceil(top_fraction * len(arr))))
    top_sum = np.sort(arr)[-k:].sum()
    return float(top_sum / total)


def safe_correlation(x: Sequence[float], y: Sequence[float]) -> float:
    """Return the correlation between two sequences if it is well-defined.

    Here I use it mainly to track how much final success still reflects effort.
    If the value stays low, the dynamics are being driven more by luck and feedback.
    """
    x_arr = np.asarray(x, dtype=float)
    y_arr = np.asarray(y, dtype=float)

    if x_arr.size == 0 or y_arr.size == 0 or x_arr.size != y_arr.size:
        return float("nan")
    if np.std(x_arr) == 0 or np.std(y_arr) == 0:
        return float("nan")
    return float(np.corrcoef(x_arr, y_arr)[0, 1])


def softmax_sample(weights: Sequence[float], rng: np.random.Generator) -> int:
    """Sample one index using softmax-transformed weights.

    I use this so higher-score agents are more likely to win,
    but never guaranteed to win.
    """
    w = np.asarray(weights, dtype=float)
    w = w - np.max(w)
    exp_w = np.exp(w)
    probs = exp_w / exp_w.sum()
    return int(rng.choice(len(weights), p=probs))
