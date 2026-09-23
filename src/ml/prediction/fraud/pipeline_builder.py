from .pipeline import FraudInferencePipeline
from src.ml.catalog.model_feature_components import ModelFeatureComponents

from src.ml.config.fraud_model import FRAUD_MODEL

from src.ml.models.mlflow_prediction_model import MLflowPredictionModel

from src.ml.prediction.fraud.feature_service import FraudFeatureService
from src.ml.repositories.fraud_repository import FraudRepository

import mlflow

from src.ml.models.prediction_estimator import PredictionEstimator
from typing import cast

from src.ml.infrastructure.mlflow_pyfunc_model import MLflowPyFuncModel

class FraudInferencePipelineBuilder:

    def build(
        self,
        repository: FraudRepository,
        model_uri: str,
        model_feature_components: ModelFeatureComponents,
    ) -> FraudInferencePipeline:
        """
        Build a fully initialized fraud prediction pipeline.

        The production model is loaded from the MLflow Model Registry
        before constructing the prediction pipeline.
        """

        #
        # Load the production model from the MLflow Model Registry.
        # The loaded model is expected to satisfy the PredictionEstimator protocol.
        #
        mlflow_pyfunc_model = cast(
            MLflowPyFuncModel,
            mlflow.pyfunc.load_model(model_uri),
        )

        estimator = mlflow_pyfunc_model.estimator

        prediction_model = MLflowPredictionModel(
            estimator=estimator,
            model_feature_components=model_feature_components,
        )

        feature_service = FraudFeatureService(
            repository=repository,
        )

        return FraudInferencePipeline(
            feature_service=feature_service,
            prediction_model=prediction_model,
        )