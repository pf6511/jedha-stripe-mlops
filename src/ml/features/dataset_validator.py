from __future__ import annotations

from src.ml.config.model_definition import ModelDefinition


class DatasetValidator:
    """
    Validate a generated training dataset.
    """

    @staticmethod
    def validate(
        model_config: ModelDefinition,
    ) -> None:
        """
        Validate dataset quality.

        Typical checks include:

        - row count
        - missing values
        - duplicate records
        - target distribution
        - schema consistency
        """

        pass