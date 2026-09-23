from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class RegisteredModel:
    """
    Metadata describing a model registered in the ML model registry (MODEL_REGISTRY.MODEL_CATALOG).
    """

    # Model identity
    model_name: str
    registered_model_name: str
    model_version: int

    # MLflow references
    model_uri: str
    mlflow_run_id: str

    # Feature lineage
    feature_set_name: str
    feature_set_schema_version: str