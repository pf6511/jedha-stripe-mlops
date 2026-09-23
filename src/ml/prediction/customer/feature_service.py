from __future__ import annotations

from typing import Protocol

import pandas as pd

from src.ml.features.common.context import FeatureContext


class CustomerRepository(Protocol):

    def find_customer(
        self,
        customer_id: str,
    ) -> pd.DataFrame: ...

    def find_customer_transactions(
        self,
        customer_id: str,
    ) -> pd.DataFrame: ...

    def find_subscription_events(
        self,
        subscription_id: str,
    ) -> pd.DataFrame: ...


class CustomerFeatureService:

    def __init__(
        self,
        repository: CustomerRepository,
    ) -> None:
        self._repository = repository

    def build_context(
        self,
        subscription: pd.Series,
    ) -> FeatureContext:

        customer_id = subscription["customer_id"]
        subscription_id = subscription["subscription_id"]

        return FeatureContext(
            current_record=subscription,
            datasets={
                "customer": self._repository.find_customer(
                    customer_id,
                ),
                "transactions": self._repository.find_customer_transactions(
                    customer_id,
                ),
                "subscription_events": self._repository.find_subscription_events(
                    subscription_id,
                ),
            },
        )