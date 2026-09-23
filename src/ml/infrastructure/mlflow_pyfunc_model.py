from __future__ import annotations

from typing import Any, cast

import pandas as pd
from mlflow.pyfunc.model import PythonModel

from src.ml.models.mlflow_prediction_model import MLflowPredictionModel
from src.ml.models.prediction_estimator import PredictionEstimator, SupportsPredictProba


class MLflowPyFuncModel(PythonModel):
    """
    MLflow PyFunc adapter for the application prediction model.
    """

    def __init__(
        self,
        prediction_model: MLflowPredictionModel,
    ) -> None:
        self._prediction_model = prediction_model

    @property
    def estimator(self) -> PredictionEstimator:
        return self._prediction_model.estimator

    def predict(
        self,
        context: Any,
        model_input: pd.DataFrame,
        params: dict[str, Any] | None = None,
    ) -> Any:

        results: list[dict[str, Any]] = []

        for _, row in model_input.iterrows():

            features = cast(
                dict[str, object],
                row.to_dict(),
            )

            prediction_output = (
                self._prediction_model.predict_features(
                    features
                )
            )

            results.append(
                {
                    "prediction": prediction_output.prediction,
                    "score": prediction_output.score,
                    "probabilities": prediction_output.probabilities,
                }
            )

        return pd.DataFrame(results)