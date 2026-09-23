from __future__ import annotations

from src.ml.config.model_definition import ModelDefinition

from src.ml.experiment.experiment_result import ExperimentResult
from src.ml.registry.registered_model import RegisteredModel

import mlflow


class ModelRegistry:
    '''
    ModelRegistry is responsible for the technical registering of a model into MLFlow
    '''
    def register_model(
        self,
        experiment: ExperimentResult,
        model_definition: ModelDefinition,
    ) -> RegisteredModel:

        registered  = mlflow.register_model(
            model_uri=experiment.model_uri,
            name=model_definition.registered_model_name,

        )
        return RegisteredModel(
            model_name=model_definition.model_name,
            registered_model_name=model_definition.registered_model_name,
            model_version=int(registered.version),
            model_uri=experiment.model_uri,
            mlflow_run_id=experiment.run_id,
            feature_set_name=model_definition.feature_set_name,
            feature_set_schema_version=model_definition.feature_set_schema_version,
        )