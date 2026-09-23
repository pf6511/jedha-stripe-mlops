from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from src.ml.models.prediction_estimator import PredictionEstimator
from src.ml.training.validation_dataset import ValidationDataset

@dataclass(frozen=True)
class TrainingResult:
    """
    Result produced by a completed model training.

    The object transports the trained estimator together with
    the validation dataset required by the evaluation phase.
    """

    estimator: PredictionEstimator

    validation_dataset: ValidationDataset