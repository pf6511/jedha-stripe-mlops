from dataclasses import dataclass
from typing import Any
from datetime import datetime


@dataclass(frozen=True)
class MonitoringReport:

    model_name: str
    model_version: str

    period_start: datetime
    period_end: datetime

    generated_at: datetime

    metrics: dict[str, Any]

    data_drift: float

    feature_drift: dict[str, float]

    drift_detected: bool

    alerts: list[str]