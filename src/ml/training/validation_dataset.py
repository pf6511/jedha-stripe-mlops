from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

@dataclass(frozen=True)
class ValidationDataset:

    """
    Validation dataset used to evaluate a trained model.
    """
    X: pd.DataFrame

    y: pd.Series