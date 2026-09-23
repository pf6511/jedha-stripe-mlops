
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ModelDefinition:
    """
    Configuration describing an ML pipeline.

    A ModelConfig contains all information required to train,
    register and deploy a specific ML model.
    """

    # General
    model_name: str

    # Dataset
    feature_set_name: str
    feature_set_schema_version: str

    # Estimator
    estimator_class: type
    estimator_params: dict[str, Any]

    # Registry
    registered_model_name: str

    # Evaluation
    target_column: str
    prediction_column: str
    confidence_column: str

    # Acceptance criteria
    minimum_precision: float
    minimum_recall: float
    minimum_f1_score: float