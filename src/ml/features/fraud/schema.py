from dataclasses import dataclass

@dataclass(frozen=True)
class FraudFeatureSchema:
    """
    Schema describing the fraud feature vector.
    """

    transaction_count_24h: int

    total_amount_24h: float

    average_amount_30d: float

    merchant_count_30d: int

    chargeback_rate_90d: float

    fraud_label: bool