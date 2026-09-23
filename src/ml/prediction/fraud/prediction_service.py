from __future__ import annotations

from datetime import UTC, datetime

import pandas as pd

from src.ml.prediction.fraud.pipeline import FraudInferencePipeline
from src.ml.repositories.mongodb_repository import (
    MongoDbRepository,
)


class FraudPredictionService:

    def __init__(
        self,
        inference_pipeline: FraudInferencePipeline,
        repository: MongoDbRepository,
    ) -> None:

        self._pipeline = inference_pipeline
        self._repository = repository

    def predict(
        self,
        transaction: pd.Series,
    ):

        result = self._pipeline.predict(
            transaction
        )

        ml_node = {
            "featureSets": {
                "fraud_features": {
                    "featureSetVersion": "1.0",
                    "metadata": {
                        "generator": "FraudFeatureService",
                        "generatorVersion": "1.0",
                        "generatedAt": datetime.now(
                            UTC
                        ).isoformat(),
                        "featureSchemaVersion": "1.0",
                    },
                    "data": result.features,
                }
            },
            "predictions": {
                "fraud_detection": {
                    "modelName": result.model_name,
                    "modelVersion": result.model_version,
                    "predictionTimestamp":
                        result.prediction.timestamp.isoformat(),
                    "outputs": {
                        "prediction":
                            result.prediction.prediction,
                        "score":
                            result.prediction.score,
                        "probabilities":
                            result.prediction.probabilities,
                    },
                }
            },
        }

        self._repository.update_field(
            collection="transactions",
            document_id=transaction["transaction_id"],
            field_name="ml",
            field_value=ml_node,
        )

        return result.prediction