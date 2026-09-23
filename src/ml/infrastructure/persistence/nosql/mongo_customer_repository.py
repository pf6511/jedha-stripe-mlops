from src.ml.repositories.customer_repository import CustomerRepository

class MongoCustomerRepository(CustomerRepository):

    def __init__(self, database):
        self._database = database