from __future__ import annotations

from typing import Protocol

from src.ml.training.training_dataset import TrainingDatasetSnapshot


class TrainingDatasetRepository(Protocol):

    def save(
        self,
        snapshot: TrainingDatasetSnapshot,
    ) -> None:
        ...