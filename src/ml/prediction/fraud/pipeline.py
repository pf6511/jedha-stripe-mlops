from __future__ import annotations

import pandas as pd

from src.ml.models.base_prediction_model import BasePredictionModel
from src.ml.prediction.fraud.feature_service import FraudFeatureService

from src.ml.prediction.inference_result import InferenceResult


class FraudInferencePipeline:

    def __init__(
        self,
        feature_service: FraudFeatureService,
        prediction_model: BasePredictionModel,
    ) -> None:

        self._feature_service = feature_service
        self._prediction_model = prediction_model

    def predict(
        self,
        transaction: pd.Series,
    ) -> InferenceResult:
        """
        Execute the complete fraud inference pipeline.
        """

        #
        # Build context
        #
        context = self._feature_service.build_context(
            transaction
        )

        #
        # Compute features once
        #
        features = self._prediction_model.compute_features(
            context
        )

        #
        # Predict from computed features
        #
        prediction = self._prediction_model.predict_features(
            features
        )

        return InferenceResult(
            context=context,
            features=features,
            prediction=prediction,
            model_name="fraud_detection",
            model_version="fraud-v1",
        )