from pydantic import BaseModel


class DbtSettings(BaseModel):
    job_id: int
    conn_id : str