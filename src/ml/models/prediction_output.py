from dataclasses import dataclass, field
from typing import Any
from datetime import datetime, UTC


@dataclass(frozen=True)
class PredictionOutput:
    """
    Prediction returned by a model.
    """

    prediction: Any

    #model_version: str

    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    score: float | None = None

    probabilities: dict[Any, float] | None = None

    