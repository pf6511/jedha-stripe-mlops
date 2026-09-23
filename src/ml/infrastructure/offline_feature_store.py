from __future__ import annotations

import pandas as pd
from datetime import date, datetime

from src.ml.features.common.featureset import FeatureSet


class OfflineFeatureStore:
    """
    Gateway to the offline feature store.

    This class encapsulates access to the persisted feature datasets used
    during model training.
    """

    def load_snapshot(
        self,
        feature_set: FeatureSet,
        training_start: date,
        training_end: date,
    ) -> pd.DataFrame:
        """
        Load a versioned feature dataset.
        SELECT *
        FROM FEATURE_STORE.FRAUD_FEATURE_STORE
        WHERE created_at >= :training_start
        AND created_at < :training_end;

        Parameters
        ----------
        feature_set
            Feature set describing the snapshot to retrieve.

        Returns
        -------
        pd.DataFrame
            Materialized feature dataset.
        """

        #
        # TODO
        #
        # Replace this stub with the actual implementation:
        #
        # - Feast Offline Store
        # - Snowflake
        # - PostgreSQL
        # - Delta Lake
        # - Parquet
        #

        raise NotImplementedError(
            "Offline Feature Store not implemented."
        )