from __future__ import annotations

from datetime import date, datetime

import pandas as pd

from src.ml.config.model_definition import ModelDefinition
from src.ml.features.common.featureset import FeatureSet

from src.ml.training.training_dataset import (
    TrainingDataset,
    TrainingDatasetMetadata,
    TrainingDatasetSnapshot,
)

@DeprecationWarning
class TrainingDatasetBuilder:

    @staticmethod
    def build_snapshot(
        dataframe: pd.DataFrame,
        model_definition: ModelDefinition,
        feature_set: FeatureSet,
        dataset_version: str,
        training_start: date,
        training_end: date,
    ) -> TrainingDatasetSnapshot:

        features = dataframe[
            feature_set.feature_names
        ].copy()

        target = dataframe[
            model_definition.target_column
        ].copy()

        dataset = TrainingDataset(
            features=features,
            target=target,
        )

        metadata = TrainingDatasetMetadata(
            dataset_version=dataset_version,
            training_start=training_start,
            training_end=training_end,
            created_at=datetime.utcnow(),
        )

        return TrainingDatasetSnapshot(
            dataset=dataset,
            metadata=metadata,
        )