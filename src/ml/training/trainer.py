from __future__ import annotations

from sklearn.model_selection import train_test_split

from src.ml.training.training_dataset import TrainingDataset
from src.ml.training.training_model import TrainingModel
from src.ml.training.training_result import TrainingResult
from src.ml.training.validation_dataset import ValidationDataset


class Trainer:
    """
    Train a machine learning model using a complete training dataset snapshot.
    """

    @staticmethod
    def train(
        model: TrainingModel,
        training_dataset: TrainingDataset,
    ) -> TrainingResult:
        """
        Split the training dataset into training and validation subsets,
        fit the model and return the estimator together with the validation
        dataset.
        """

        X_train, X_valid, y_train, y_valid = train_test_split(
            training_dataset.features,
            training_dataset.target,
            test_size=0.2,
            random_state=42,
        )

        validation_dataset = ValidationDataset(
            X=X_valid,
            y=y_valid,
        )

        estimator = model.fit(
            X_train,
            y_train,
        )

        return TrainingResult(
            estimator=estimator,
            validation_dataset=validation_dataset,
        )