from datetime import datetime

from airflow.sdk import DAG, task

from src.ml.monitoring.monitoring_pipeline_builder import (
    MonitoringPipelineBuilder,
)
from src.ml.repositories.snowflake_monitoring_repository import (
    SnowflakeMonitoringRepository,
)
from src.ml.monitoring.deployed_models import DeployedModel


@task
def run_model_monitoring():

    repository = SnowflakeMonitoringRepository()

    pipeline = MonitoringPipelineBuilder.build(
        repository=repository,
    )

    for model_name in DeployedModel:
        pipeline.run(model_name=model_name)


with DAG(
    dag_id="daily_model_monitoring",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["mlops", "monitoring"],
):

    run_model_monitoring()