from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class FeatureContext:
    """
    Context required to compute online features.

    Attributes
    ----------
    current_record:
        Current entity for which features are computed
        (transaction, customer, ...).

    datasets:
        Additional datasets required for feature computation.
        Each dataset is identified by a logical name.
    """

    current_record: pd.Series

    datasets: dict[str, pd.DataFrame]