from src.ml.features.common.definitions import FeatureDefinition
from ml.features.common.featureset import FeatureSet


CUSTOMER_FEATURE_SET = FeatureSet(

    name="customer_features",
    version="1.0",
    features=[

        #
        # Business identifiers
        #

        FeatureDefinition(
            name="subscription_id",
            data_type="string",
            description="Subscription identifier",
        ),

        FeatureDefinition(
            name="customer_id",
            data_type="string",
            description="Customer identifier",
        ),

        #
        # Current subscription
        #

        FeatureDefinition(
            name="created_at",
            data_type="datetime64[ns]",
            description="Subscription creation timestamp",
        ),

        FeatureDefinition(
            name="customer_tenure_days",
            data_type="int64",
            description="Customer tenure in days",
        ),

        FeatureDefinition(
            name="current_subscription_plan",
            data_type="string",
            description="Current subscription plan",
        ),

        #
        # Behaviour features
        #

        FeatureDefinition(
            name="transactions_last_30d",
            data_type="int64",
            description="Number of transactions during last 30 days",
        ),

        FeatureDefinition(
            name="total_spent_30d",
            data_type="float64",
            description="Total amount spent during last 30 days",
        ),

        FeatureDefinition(
            name="average_transaction_amount",
            data_type="float64",
            description="Average transaction amount during last 30 days",
        ),

        FeatureDefinition(
            name="preferred_merchant_type",
            data_type="string",
            description="Preferred merchant type",
        ),

        FeatureDefinition(
            name="renewal_count",
            data_type="int64",
            description="Number of subscription renewals",
        ),
    ]
)