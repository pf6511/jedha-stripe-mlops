from airflow.sdk import task_group

from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.airbyte.sensors.airbyte import AirbyteJobSensor

from src.settings.airbyte_settings import AirbyteSettings

@task_group(group_id="airbyte")
def airbyte_group(settings:AirbyteSettings):
    """
    Synchronise les données sources vers Snowflake via Airbyte.

    - PostgreSQL -> Snowflake
    - MongoDB -> Snowflake
    """

    #
    # PostgreSQL
    #
    trigger_postgres = AirbyteTriggerSyncOperator(
        task_id="trigger_postgres_sync",

        airbyte_conn_id=settings.airbyte_server_conn_id,

        connection_id=settings.stripe_postgresql_connection_id,
    )

    wait_postgres = AirbyteJobSensor(
        task_id="wait_postgres_sync",

        airbyte_conn_id=settings.airbyte_server_conn_id,

        airbyte_job_id=trigger_postgres.output, # type: ignore[arg-type]
    )

    #
    # MongoDB
    #
    trigger_mongodb = AirbyteTriggerSyncOperator(
        task_id="trigger_mongodb_sync",

        airbyte_conn_id=settings.airbyte_server_conn_id,

        connection_id=settings.stripe_mongodb_connection_id,
    )

    wait_mongodb = AirbyteJobSensor(
        task_id="wait_mongodb_sync",

        airbyte_conn_id=settings.airbyte_server_conn_id,

        airbyte_job_id=trigger_mongodb.output, # type: ignore[arg-type]
    )

    trigger_postgres >> wait_postgres
    trigger_mongodb >> wait_mongodb