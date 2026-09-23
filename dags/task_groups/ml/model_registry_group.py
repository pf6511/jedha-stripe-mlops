from airflow.sdk import task
from airflow.sdk import task_group

from src.ml.services.model_registry_service import ModelRegistryService
from src.ml.config.model_definition import ModelDefinition
from src.ml.experiment.experiment_result import ExperimentResult
from src.ml.repositories.model_repository import ModelRepository
from src.ml.registry.registered_model import RegisteredModel

@task_group(group_id="model_registry") # pyright: ignore[reportArgumentType]
def model_registry_group(
    experiment,
    model_definition: ModelDefinition,
    repository: ModelRepository,
):

    @task
    def register_model(
        experiment: ExperimentResult,
    ) -> RegisteredModel:

        return ModelRegistryService.register_model(
            experiment=experiment,
            model_definition=model_definition,
            repository=repository,
        )

    return register_model(experiment)