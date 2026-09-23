from src.ml.experiment.experiment_result import ExperimentResult
from src.ml.config.model_definition import ModelDefinition
from src.ml.registry.model_registry import ModelRegistry
from src.ml.registry.registered_model import RegisteredModel
from src.ml.repositories.model_repository import ModelRepository

class ModelRegistryService:

    @staticmethod
    def register_model(
        experiment: ExperimentResult,
        model_definition: ModelDefinition,
        repository: ModelRepository,
    ) -> RegisteredModel:

        registered_model = ModelRegistry().register_model(
            experiment,
            model_definition,
        )

        repository.insert(registered_model)

        return registered_model