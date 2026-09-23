from datetime import date

from airflow import DAG

from src.ml.config.fraud_model import FRAUD_MODEL
from src.ml.config.model_definition import ModelDefinition

from dags.task_groups.ml.feature_dataset_group import (
    feature_dataset_group,
)
from dags.task_groups.ml.training_group import training_group

from dags.task_groups.ml.model_registry_group import (
    model_registry_group,
)
from dags.task_groups.ml.deployment_group import deployment_group

from src.ml.repositories.snowflake_model_repository import (
    SnowflakeModelRepository,
)


def create_ml_pipeline(
    model_definition: ModelDefinition,
    dataset_version: str,
    training_start: date,
    training_end: date,
) -> DAG:

    model_repository = SnowflakeModelRepository()

    with DAG(
        dag_id=f"train_{model_definition.model_name}",
    ) as dag:

        training_dataset = feature_dataset_group(
            model_definition=model_definition,
            dataset_version=dataset_version,
            training_start=training_start,
            training_end=training_end,
        )

        experiment_result = training_group(
            training_dataset=training_dataset,
            model_definition=model_definition,
        )


        registry = model_registry_group(
            experiment=experiment_result,
            model_definition=model_definition,
            repository=model_repository,
        )

        deployment = deployment_group(
            model_definition,
        )

        (
            training_dataset
            >> experiment_result
            >> registry
            >> deployment
        )

    return dag


dag = create_ml_pipeline(
    model_definition=FRAUD_MODEL,
    dataset_version="fraud_ds_v1",
    training_start=date(2025, 1, 1),
    training_end=date(2025, 12, 31),
)