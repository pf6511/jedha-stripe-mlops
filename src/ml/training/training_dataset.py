from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from datetime import datetime, date

@dataclass(frozen=True)
class TrainingDatasetMetadata:

    dataset_version: str
    training_start: date
    training_end: date
    created_at: datetime
    mlflow_run_id: str | None = None

@dataclass(frozen=True)
class TrainingDataset:
    """
    Complete snapshot of the data selected for model training.
    """

    features: pd.DataFrame
    target: pd.Series

@dataclass(frozen=True)
class TrainingDatasetSnapshot:

    """
    Versioned training dataset together with its metadata.
    """

    dataset: TrainingDataset
    metadata: TrainingDatasetMetadata