from pydantic import BaseModel

class AirflowSettings(BaseModel):
    dag_name: str
    base_url: str