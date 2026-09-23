from __future__ import annotations

from typing import Any

import pandas as pd

from ml.features.common.calculator import FeatureCalculator
from ml.features.common.context import FeatureContext


class FraudFeatureCalculator(FeatureCalculator):
    """
    Computes fraud detection features.
    """

    def compute(
        self,
        context: FeatureContext,
    ) -> dict[str, Any]:

        transaction = context.current_record

        customer_transactions = context.datasets["customer_transactions"]

        customer_chargebacks = context.datasets["customer_chargebacks"]

        created_at = transaction["created_at"]

        transactions_last_24h = customer_transactions[
            customer_transactions["created_at"] >= (
                created_at - pd.Timedelta(hours=24)
            )
        ]

        transactions_last_30d = customer_transactions[
            customer_transactions["created_at"] >= (
                created_at - pd.Timedelta(days=30)
            )
        ]

        chargebacks_last_30d = customer_chargebacks[
            customer_chargebacks["created_at"] >= (
                created_at - pd.Timedelta(days=30)
            )
        ]

        return {

            #
            # Online features
            #
            "transaction_id":
                transaction["transaction_id"],

            "created_at":
                transaction["created_at"],

            "customer_id":
                transaction["customer_id"],

            "country_code":
                transaction["country_code"],

            "device_type_code":
                transaction["device_type_code"],

            "amount":
                transaction["amount"],

            "is_vpn_detected":
                transaction["is_vpn_detected"],

            #
            # Calculated features
            #
            "transactions_last_24h":
                len(transactions_last_24h),

            "avg_amount_30d":
                transactions_last_30d["amount"].mean(),

            "chargeback_count_30d":
                len(chargebacks_last_30d),

        }