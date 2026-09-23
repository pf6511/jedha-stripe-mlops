from src.ml.config.model_definition import ModelDefinition

from src.ml.features.fraud.calculator import FraudFeatureCalculator
from src.ml.features.customer.calculator import CustomerFeatureCalculator

from src.ml.features.fraud.featureset import FRAUD_FEATURE_SET
from src.ml.features.customer.featureset import CUSTOMER_FEATURE_SET

from .model_feature_components import ModelFeatureComponents


class ModelCatalog:
    """
    Returns the domain components associated with a model.
    """

    def get(
        self,
        model_config: ModelDefinition,
    ) -> ModelFeatureComponents:

        match model_config.model_name:

            case "fraud":

                return ModelFeatureComponents(
                    model_name=model_config.model_name,
                    feature_calculator=FraudFeatureCalculator(),
                    feature_set=FRAUD_FEATURE_SET,
                )

            case "customer":

                return ModelFeatureComponents(
                    model_name=model_config.model_name,
                    feature_calculator=CustomerFeatureCalculator(),
                    feature_set=CUSTOMER_FEATURE_SET,
                )

            case _:

                raise ValueError(
                    f"Unknown model '{model_config.model_name}'."
                )