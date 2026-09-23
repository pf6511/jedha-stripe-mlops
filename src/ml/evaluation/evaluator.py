from __future__ import annotations

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

from src.ml.training.training_result import TrainingResult
from src.ml.evaluation.evaluation_result import EvaluationResult


class Evaluator:

    @staticmethod
    def evaluate(
        training: TrainingResult,
    ) -> EvaluationResult:

        predictions = training.estimator.predict(
            training.validation_dataset.X,
        )

        metrics = {
            "accuracy": accuracy_score(
                training.validation_dataset.y,
                predictions,
            ),
            "precision": precision_score(
                training.validation_dataset.y,
                predictions,
            ),
            "recall": recall_score(
                training.validation_dataset.y,
                predictions,
            ),
            "f1": f1_score(
                training.validation_dataset.y,
                predictions,
            ),
        }

        return EvaluationResult(
            metrics=metrics,
        )