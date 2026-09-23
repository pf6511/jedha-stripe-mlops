from dataclasses import dataclass

from .monitoring_field import MonitoringField

@dataclass(frozen=True)
class MonitoringSchema:
    """
    Semantic description of a monitoring dataset.

    The schema identifies the feature columns and the prediction
    and target columns required by the monitoring engine.
    """

    feature_columns: list[MonitoringField]

    prediction_column: str

    target_column: str

    timestamp_column: str | None = None