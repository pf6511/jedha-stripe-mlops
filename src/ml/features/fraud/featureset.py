from src.ml.features.common.definitions import FeatureDefinition
from src.ml.features.common.featureset import FeatureSet


FRAUD_FEATURE_SET = FeatureSet(
            name="fraud_features",
            version="1.0",
 features=[

        FeatureDefinition(
            name="transaction_id",
            data_type="string",
            description="Unique transaction identifier",
        ),

        FeatureDefinition(
            name="created_at",
            data_type="datetime64[ns]",
            description="Transaction timestamp",
        ),

        FeatureDefinition(
            name="customer_id",
            data_type="string",
            description="Customer identifier",
        ),

        FeatureDefinition(
            name="country_code",
            data_type="string",
            description="Customer country",
        ),

        FeatureDefinition(
            name="device_type_code",
            data_type="string",
            description="Device type",
        ),

        FeatureDefinition(
            name="amount",
            data_type="float64",
            description="Transaction amount",
        ),

        FeatureDefinition(
            name="is_vpn_detected",
            data_type="bool",
            description="VPN detected",
        ),

        FeatureDefinition(
            name="transactions_last_24h",
            data_type="int64",
            description="Number of customer transactions during the last 24 hours",
        ),

        FeatureDefinition(
            name="avg_amount_30d",
            data_type="float64",
            description="Average transaction amount during the last 30 days",
        ),

        FeatureDefinition(
            name="chargeback_count_30d",
            data_type="int64",
            description="Number of chargebacks during the last 30 days",
        ),

    ]
    )
    