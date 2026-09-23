from __future__ import annotations

from typing import Any, Protocol

import pandas as pd


class PredictionEstimator(Protocol):
    """
    Contract implemented by prediction estimators.
    """

    @property
    def classes_(self) -> list[Any]:
        ...

    def predict(
        self,
        X: pd.DataFrame,
    ) -> Any:
        ...

    def predict_proba(
        self,
        X: pd.DataFrame,
    ) -> Any:
        ...

class SupportsPredictProba(Protocol):

    @property
    def classes_(self) -> list[Any]:
        ...

    def predict_proba(
        self,
        X: pd.DataFrame,
    ) -> Any:
        ...