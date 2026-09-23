from airflow.sdk import task
from airflow.sdk import task_group
from airflow.sdk.definitions.xcom_arg import XComArg

from src.ml.config.model_definition import ModelDefinition
from src.ml.training.training_dataset import TrainingDatasetSnapshot

from src.ml.experiment.experiment_result import ExperimentResult

from src.ml.services.training_service import TrainingService
from airflow.sdk.definitions.xcom_arg import XComArg


@task_group(group_id="training") # pyright: ignore[reportArgumentType]
def training_group(
    training_dataset,
    model_definition: ModelDefinition,
):

    @task
    def train_model(
        training_dataset: TrainingDatasetSnapshot,
        model_definition: ModelDefinition,
    ) -> ExperimentResult:
        return TrainingService.train_model(
            training_dataset=training_dataset,
            model_definition=model_definition,
        )

    return train_model(
        training_dataset=training_dataset, # pyright: ignore[reportArgumentType]
        model_definition=model_definition,
    )