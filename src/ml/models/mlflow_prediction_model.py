from __future__ import annotations

from typing import Any,cast

import pandas as pd

from .prediction_estimator import PredictionEstimator, SupportsPredictProba

from src.ml.catalog.model_feature_components import ModelFeatureComponents

from .base_prediction_model import BasePredictionModel
from .prediction_output import PredictionOutput


class MLflowPredictionModel(BasePredictionModel):
    """
    Prediction model backed by a trained estimator.

    The estimator is provided by the infrastructure layer.
    This class implements the application-level prediction
    contract independently of the underlying ML framework.
    """

    def __init__(
        self,
        estimator: PredictionEstimator,
        model_feature_components: ModelFeatureComponents,
    ) -> None:

        super().__init__(model_feature_components)

        self._estimator = estimator

    @property
    def estimator(self) -> PredictionEstimator:
        return self._estimator

    def _predict(
        self,
        features: pd.DataFrame,
    ) -> PredictionOutput:

        prediction = self._estimator.predict(features)[0]

        score: float | None = None
        probabilities: dict[Any, float] | None = None

        if hasattr(self._estimator, "predict_proba"):

            proba_estimator = cast(
                SupportsPredictProba,
                self._estimator,
            )
            
            proba = proba_estimator.predict_proba(features)[0]

            probabilities = {
                cls: float(probability)
                for cls, probability in zip(
                    proba_estimator.classes_,
                    proba,
                )
            }

            score = max(probabilities.values())

        return PredictionOutput(
            prediction=prediction,
            score=score,
            probabilities=probabilities,
        )