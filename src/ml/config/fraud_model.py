from sklearn.ensemble import RandomForestClassifier

from src.ml.config.model_definition import ModelDefinition


FRAUD_MODEL = ModelDefinition(

    model_name="fraud",

    feature_set_name="fraud_features",
    feature_set_schema_version="1.0",

    estimator_class=RandomForestClassifier,

    estimator_params={
        "n_estimators": 200,
        "max_depth": 10,
        "random_state": 42,
        "n_jobs": -1,
    },

    registered_model_name="fraud_detection",

    target_column="is_fraud",

    prediction_column="prediction",

    confidence_column="confidence",

    minimum_precision=0.95,

    minimum_recall=0.80,

    minimum_f1_score=0.87,
)