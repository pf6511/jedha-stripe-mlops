from datetime import datetime

from airflow.sdk import dag

from dags.task_groups.elt.airbyte_group import airbyte_group
from dags.task_groups.elt.dbt_group import dbt_group

from src.settings.settings_loader import SettingsLoader
from src.settings.environment import Environment


@dag(
    dag_id="stripe_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
)
def stripe_etl_pipeline():

    settings = SettingsLoader.load(Environment.get_current_env())
    ingestion = airbyte_group(settings.airbyte)

    transformation = dbt_group(settings.dbt)

    ingestion >> transformation


stripe_etl_pipeline()