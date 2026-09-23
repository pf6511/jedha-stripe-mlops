from src.ml.repositories.fraud_repository import FraudRepository


class MongoFraudRepository(FraudRepository):
    """MongoDB implementation of FraudRepository."""

    def __init__(self, database):
        self._database = database