from __future__ import annotations

from datetime import date, datetime

import pandas as pd

from src.ml.catalog.model_catalog import ModelCatalog
from src.ml.config.model_definition import ModelDefinition
from src.ml.features.common.featureset import FeatureSet

from src.ml.infrastructure.offline_feature_store import (
    OfflineFeatureStore,
)
from src.ml.repositories.training_dataset_repository import (
    TrainingDatasetRepository,
)
from src.ml.registry.dataset_registry import DatasetRegistry
from src.ml.training.training_dataset import (
    TrainingDataset,TrainingDatasetMetadata, TrainingDatasetSnapshot,
)


class DatasetService:

    _catalog = ModelCatalog()
    _offline_store = OfflineFeatureStore()

    def __init__(
        self,
        training_dataset_repository: TrainingDatasetRepository,
        dataset_registry: DatasetRegistry,
    ) -> None:

        self._training_dataset_repository = (
            training_dataset_repository
        )

        self._dataset_registry = dataset_registry

    def _load_feature_set_dataframe(
        self,
        model_definition: ModelDefinition,
        training_start: date,
        training_end: date,
    ) -> tuple[pd.DataFrame, FeatureSet]:

        feature_set = self.select_feature_set(
            model_definition,
        )

        dataframe = self._offline_store.load_snapshot(
            feature_set,training_start,training_end
        )

        return dataframe, feature_set

    def select_feature_set(
        self,
        model_definition: ModelDefinition,
    ) -> FeatureSet:

        components = self._catalog.get(
            model_definition,
        )

        return components.feature_set

    def snapshot_training_dataset(
        self,
        model_definition: ModelDefinition,
        dataset_version: str,
        training_start: date,
        training_end: date,
    ) -> TrainingDatasetSnapshot:
        """
        Build a complete immutable training dataset snapshot.
        """
        dataframe, feature_set = (
            self._load_feature_set_dataframe(
            model_definition=model_definition,
            training_start=training_start,
            training_end=training_end,
            )
        )
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

    def validate_training_dataset(
        self,
        model_definition: ModelDefinition,
        snapshot: TrainingDatasetSnapshot,
    ) -> None:

        feature_set = self.select_feature_set(
            model_definition,
        )

        missing_features = (
            set(feature_set.feature_names)
            - set(snapshot.dataset.features.columns)
        )

        if missing_features:
            raise ValueError(
                "Missing features: "
                f"{sorted(missing_features)}"
            )

    def persist_training_dataset(
        self,
        snapshot: TrainingDatasetSnapshot,
    ) -> None:

        self._training_dataset_repository.save(
            snapshot,
        )

    def register_training_dataset(
        self,
        model_definition: ModelDefinition,
        snapshot: TrainingDatasetSnapshot,
    ) -> None:

        self._dataset_registry.register(
            model_definition=model_definition,
            snapshot=snapshot,
        )

    def create_training_dataset(
        self,
        model_definition: ModelDefinition,
        dataset_version: str,
        training_start: date,
        training_end: date,
    ) -> TrainingDatasetSnapshot:
        """
        Build, validate, persist and catalogue an immutable
        training dataset snapshot.
        """

        snapshot = self.snapshot_training_dataset(
            model_definition=model_definition,
            dataset_version=dataset_version,
            training_start=training_start,
            training_end=training_end,
        )

        self.validate_training_dataset(
            model_definition=model_definition,
            snapshot=snapshot,
        )

        self.persist_training_dataset(
            snapshot,
        )

        self.register_training_dataset(
            model_definition=model_definition,
            snapshot=snapshot,
        )

        return snapshot