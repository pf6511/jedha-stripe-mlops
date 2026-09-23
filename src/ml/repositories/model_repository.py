
from abc import ABC, abstractmethod
from src.ml.registry.registered_model import RegisteredModel
class ModelRepository(ABC):

    @abstractmethod
    def insert(
        self,
        registered_model: RegisteredModel,
    ) -> None:
        ...