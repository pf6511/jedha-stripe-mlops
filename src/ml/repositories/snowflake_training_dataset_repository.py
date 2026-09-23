from __future__ import annotations

import pandas as pd

from src.ml.repositories.training_dataset_repository import (
    TrainingDatasetRepository,
)

from src.ml.training.training_dataset import (
    TrainingDatasetSnapshot,
)


class SnowflakeTrainingDatasetRepository(
    TrainingDatasetRepository,
):

    def save(
        self,
        snapshot: TrainingDatasetSnapshot,
    ) -> None:

        dataframe = self._to_dataframe(snapshot)

        self._write(
            dataframe=dataframe,
            dataset_version=snapshot.metadata.dataset_version,
        )

    @staticmethod
    def _to_dataframe(
        snapshot: TrainingDatasetSnapshot,
    ) -> pd.DataFrame:

        dataset = snapshot.dataset

        dataframe = dataset.features.copy()

        dataframe["target"] = dataset.target.values

        dataframe["dataset_version"] = (
            snapshot.metadata.dataset_version
        )

        return dataframe

    def _write(
        self,
        dataframe: pd.DataFrame,
        dataset_version: str,
    ) -> None:
        """
        Persist the snapshot into the model-specific
        Snowflake training dataset table.

        The concrete Snowflake write mechanism is intentionally
        isolated in this infrastructure implementation.
        """

        raise NotImplementedError