from __future__ import annotations

from src.ml.features.common.context import FeatureContext
from src.ml.repositories.fraud_repository import FraudRepository

import pandas as pd



class FraudFeatureService:

    def __init__(
        self,
        repository: FraudRepository,
    ) -> None:
        self._repository = repository

    def build_context(
        self,
        transaction: pd.Series,
    ) -> FeatureContext:

        customer_id = transaction["customer_id"]

        return FeatureContext(
            current_record=transaction,
            datasets={
                "transactions": self._repository.find_customer_transactions(
                    customer_id,
                ),
                "chargebacks": self._repository.find_customer_chargebacks(
                    customer_id,
                ),
            },
        )