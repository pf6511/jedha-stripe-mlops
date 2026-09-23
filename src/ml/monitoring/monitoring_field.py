from dataclasses import dataclass
from src.ml.features.feature_type import FeatureType


@dataclass(frozen=True)
class MonitoringField:
    """
    Describes a column of the monitoring dataset.

    This metadata is used by the monitoring engine to interpret the
    semantics of the observations independently of any monitoring
    framework.
    """

    name: str

    type: FeatureType