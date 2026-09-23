from __future__ import annotations

from datetime import date

from airflow.sdk import task
from airflow.sdk import task_group

from src.ml.config.model_definition import ModelDefinition

from src.ml.infrastructure.ml_services import (
    MLServices,
)

from src.ml.training.training_dataset import (
    TrainingDatasetSnapshot,
)


@task_group(group_id="feature_dataset") # pyright: ignore[reportArgumentType]
def feature_dataset_group(
    model_definition: ModelDefinition,
    dataset_version: str,
    training_start: date,
    training_end: date,
):

    @task
    def create_training_dataset(
        model_definition: ModelDefinition,
        dataset_version: str,
        training_start: date,
        training_end: date,
    ) -> TrainingDatasetSnapshot:

        dataset_service = MLServices.dataset_service()

        return dataset_service.create_training_dataset(
            model_definition=model_definition,
            dataset_version=dataset_version,
            training_start=training_start,
            training_end=training_end,
        )

    return create_training_dataset(
        model_definition=model_definition,
        dataset_version=dataset_version,
        training_start=training_start,
        training_end=training_end,
    )