from airflow.sdk import task_group

from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator
from airflow.providers.standard.operators.bash import BashOperator

from src.settings.dbt_settings import DbtSettings


@task_group(group_id="dbt")
def dbt_group(settings: DbtSettings):
    """
    Execute dbt build Cloud puis dbt tests.
    """

    build = DbtCloudRunJobOperator(
        task_id="dbt_build",
        job_id=settings.job_id,
        conn_id=settings.conn_id,
    )

    test = BashOperator(
        task_id="dbt_test",
        bash_command="dbt test",
    )

    build >> test