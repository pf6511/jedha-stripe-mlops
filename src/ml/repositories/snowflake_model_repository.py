from src.ml.registry.registered_model import RegisteredModel
from src.ml.repositories.model_repository import ModelRepository


class SnowflakeModelRepository(
    ModelRepository
):

    def insert(
        self,
        registered_model: RegisteredModel,
    ) -> None:

        # Persistance dans Snowflake
        raise NotImplementedError