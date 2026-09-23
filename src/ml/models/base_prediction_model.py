from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd

from src.ml.catalog.model_feature_components import ModelFeatureComponents
from src.ml.features.common.context import FeatureContext

from .prediction_output import PredictionOutput


class BasePredictionModel(ABC):

    def __init__(
        self,
        model_feature_components: ModelFeatureComponents,
    ) -> None:

        self._model_feature_components = model_feature_components

    def compute_features(
        self,
        context: FeatureContext,
    ) -> dict[str, object]:
        """
        Compute online features from the provided context.
        """

        return self._model_feature_components.feature_calculator.compute(
            context
        )

    def predict_features(
        self,
        features: dict[str, object],
    ) -> PredictionOutput:
        """
        Perform prediction from an already computed feature set.
        """

        dataframe = self._model_feature_components.feature_set.to_dataframe(
            pd.Series(features)
        )

        return self._predict(dataframe)

    def predict(
        self,
        context: FeatureContext,
    ) -> PredictionOutput:
        """
        Convenience method computing features then predicting.
        """

        features = self.compute_features(
            context
        )

        return self.predict_features(
            features
        )

    @abstractmethod
    def _predict(
        self,
        features: pd.DataFrame,
    ) -> PredictionOutput:
        ...