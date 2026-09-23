from dataclasses import dataclass

from src.ml.features.common.calculator import FeatureCalculator
from src.ml.features.common.featureset import FeatureSet


@dataclass(frozen=True)
class ModelFeatureComponents:

    """
    Domain components associated with a model.
    """
    model_name: str
    
    feature_calculator: FeatureCalculator

    feature_set: FeatureSet