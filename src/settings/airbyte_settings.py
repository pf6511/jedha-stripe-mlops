from pydantic import BaseModel


class AirbyteSettings(BaseModel):
    airbyte_server_conn_id: str
    stripe_postgresql_connection_id : str
    stripe_mongodb_connection_id:str