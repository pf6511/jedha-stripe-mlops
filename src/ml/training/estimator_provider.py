from __future__ import annotations

from typing import Protocol

from src.ml.config.model_definition import ModelDefinition
from src.ml.models.prediction_estimator import PredictionEstimator


class EstimatorProvider(Protocol):
    """
    Factory responsible for creating untrained prediction estimators.
    """

    def create(
        self,
        model_config: ModelDefinition,
    ) -> PredictionEstimator:
        """
        Create a new estimator associated with the model.
        """
        ...

class SklearnEstimatorProvider(EstimatorProvider):
    """
    Default estimator provider.

    TODO
    ----
    Instantiate the estimator associated with the model.
    """

    def create(
        self,
        model_config: ModelDefinition,
    ) -> PredictionEstimator:

        raise NotImplementedError(
            "Estimator creation must be implemented."
        )