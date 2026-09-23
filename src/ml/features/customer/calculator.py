from __future__ import annotations

from typing import Any

import pandas as pd

from ml.features.common.calculator import FeatureCalculator
from ml.features.common.context import FeatureContext


class CustomerFeatureCalculator(FeatureCalculator):
    """
    Computes customer-related features.
    """

    def compute(
        self,
        context: FeatureContext,
    ) -> dict[str, Any]:

        subscription = context.current_record

        customer = context.datasets["customer"]

        transactions = context.datasets["transactions"]

        subscription_events = context.datasets["subscription_events"]

        created_at = subscription["created_at"]

        #
        # Transactions during last 30 days
        #
        transactions_30d = transactions.loc[
            transactions["created_at"].between(
                created_at - pd.Timedelta(days=30),
                created_at,
            )
        ]

        #
        # Preferred merchant
        #
        preferred_merchant = "UNKNOWN"

        if not transactions_30d.empty:

            preferred_merchant = (
                transactions_30d["merchant_type_code"]
                .mode()
                .iloc[0]
            )

        #
        # Renewal events
        #
        renewal_count = len(
            subscription_events.loc[
                subscription_events[
                    "subscription_event_type_code"
                ] == "SubscriptionRenewed"
            ]
        )

        return {

            #
            # Business identifiers
            #
            "subscription_id":
                subscription["subscription_id"],

            "customer_id":
                subscription["customer_id"],

            "created_at":
                created_at,

            #
            # Customer information
            #
            "customer_tenure_days":
                (
                    created_at -
                    customer["effective_from"]
                ).days,

            "current_subscription_plan":
                subscription["subscription_plan"],

            #
            # Behaviour features
            #
            "transactions_last_30d":
                len(transactions_30d),

            "total_spent_30d":
                transactions_30d["transaction_amount"].sum(),

            "average_transaction_amount":
                transactions_30d["transaction_amount"].mean(),

            "preferred_merchant_type":
                preferred_merchant,

            "renewal_count":
                renewal_count,

        }