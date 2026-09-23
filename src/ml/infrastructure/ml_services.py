from src.ml.repositories.snowflake_dataset_repository import (
    SnowflakeDatasetRepository,
)

from src.ml.repositories.snowflake_training_dataset_repository import (
    SnowflakeTrainingDatasetRepository,
)

from src.ml.registry.dataset_registry import DatasetRegistry
from src.ml.services.dataset_service import DatasetService


class MLServices:

    @staticmethod
    def dataset_service() -> DatasetService:

        dataset_registry = DatasetRegistry(
            repository=SnowflakeDatasetRepository(),
        )

        return DatasetService(
            training_dataset_repository=(
                SnowflakeTrainingDatasetRepository()
            ),
            dataset_registry=dataset_registry,
        )