from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EvaluationResult:
    """
    Result produced by model evaluation.
    """

    metrics: dict[str, float]