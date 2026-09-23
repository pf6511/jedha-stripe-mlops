from pydantic import BaseModel

from .dbt_settings import DbtSettings
from .airbyte_settings import AirbyteSettings
from .airflow_settings import AirflowSettings

class Settings(BaseModel):
    dbt: DbtSettings
    airbyte:AirbyteSettings
    airflow: AirflowSettings