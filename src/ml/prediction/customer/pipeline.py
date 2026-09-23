from __future__ import annotations

import pandas as pd

from src.ml.models.base_prediction_model import BasePredictionModel
from src.ml.models.prediction_output import PredictionOutput
from src.ml.prediction.customer.feature_service import CustomerFeatureService


class CustomerPredictionPipeline:

    def __init__(
        self,
        feature_service: CustomerFeatureService,
        prediction_model: BasePredictionModel,
    ) -> None:

        self._feature_service = feature_service
        self._prediction_model = prediction_model

    def predict(
        self,
        subscription: pd.Series,
    ) -> PredictionOutput:
        """
        Execute the customer prediction pipeline.
        """

        context = self._feature_service.build_context(
            subscription,
        )

        return self._prediction_model.predict(
            context,
        )