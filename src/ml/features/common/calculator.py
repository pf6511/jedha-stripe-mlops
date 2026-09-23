from abc import ABC
from abc import abstractmethod
from typing import Any

from src.ml.features.common.context import FeatureContext


class FeatureCalculator(ABC):
    """
    Computes features from a FeatureContext.
    """

    @abstractmethod
    def compute(
        self,
        context: FeatureContext,
    ) -> dict[str, Any]:
        """
        Returns computed features.
        """
        ...