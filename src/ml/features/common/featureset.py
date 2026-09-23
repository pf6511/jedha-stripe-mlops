from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd

from .definitions import FeatureDefinition


@dataclass(frozen=True)
class FeatureSet:
    name: str

    version: str

    features: list[FeatureDefinition]

    @property
    def feature_names(self) -> list[str]:
        return [feature.name for feature in self.features]

    def align(
        self,
        values: pd.Series,
        fill_value: Any | None = None
    ) -> pd.Series:
        """
        Retourne les features dans l'ordre attendu par le modèle.
        Les features manquantes sont ajoutées avec fill_value.
        Les features supplémentaires sont ignorées.
        """
        return values.reindex(
            self.feature_names,
            fill_value=fill_value,
        )

    def to_dataframe(
        self,
        values: pd.Series,
        fill_value: Any = 0,
    ) -> pd.DataFrame:
        """
        Construit le DataFrame attendu par scikit-learn.
        """
        return (
            self.align(values, fill_value)
            .to_frame()
            .T
        )