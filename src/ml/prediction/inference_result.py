from dataclasses import dataclass

from src.ml.features.common.context import FeatureContext
from src.ml.models.prediction_output import PredictionOutput


@dataclass(frozen=True)
class InferenceResult:

    context: FeatureContext

    prediction: PredictionOutput

    features: dict[str, object]

    model_name: str

    model_version: str