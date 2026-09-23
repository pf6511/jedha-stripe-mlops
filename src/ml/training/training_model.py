from __future__ import annotations

from typing import Protocol

import pandas as pd

from src.ml.models.prediction_estimator import PredictionEstimator


class TrainingModel(Protocol):
    """
    Contract implemented by trainable machine learning models.
    """

    def fit(
        self,
        X: pd.DataFrame,
        y: pd.Series,
    ) -> PredictionEstimator:
        """
        Train the model and return a prediction estimator.
        """
        ...