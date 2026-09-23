from __future__ import annotations

from datetime import date, datetime
from typing import Protocol


class DatasetRepository(Protocol):

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
        ...