from __future__ import annotations

from src.ml.config.model_definition import ModelDefinition

from src.ml.repositories.dataset_repository import (
    DatasetRepository,
)

from src.ml.training.training_dataset import (
    TrainingDatasetSnapshot,
)


class DatasetRegistry:

    def __init__(
        self,
        repository: DatasetRepository,
    ) -> None:

        self._repository = repository

    def register(
        self,
        model_definition: ModelDefinition,
        snapshot: TrainingDatasetSnapshot,
    ) -> None:

        metadata = snapshot.metadata

        self._repository.insert(
            model_name=model_definition.model_name,
            dataset_version=metadata.dataset_version,
            feature_set=model_definition.feature_set_name,
            feature_set_schema_version=(
                model_definition.feature_set_schema_version
            ),
            created_at=metadata.created_at,
            training_start=metadata.training_start,
            training_end=metadata.training_end,
            mlflow_run_id=metadata.mlflow_run_id,
        )