from __future__ import annotations

from datetime import date, datetime

from src.ml.repositories.dataset_repository import (
    DatasetRepository,
)


class SnowflakeDatasetRepository(DatasetRepository):

    def insert(
        self,
        model_name: str,
        dataset_version: str,
        feature_set: str,
        feature_set_schema_version: str,
        created_at: datetime,
        training_start: date,
        training_end: date,
        mlflow_run_id: str | None,
    ) -> None:

        raise NotImplementedError