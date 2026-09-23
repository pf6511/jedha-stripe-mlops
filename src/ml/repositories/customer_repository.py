from typing import Protocol
import pandas as pd

class CustomerRepository(Protocol):

    def find_customer_transactions(
        self,
        customer_id: str,
    ) -> pd.DataFrame: ...

    def find_customer_chargebacks(
        self,
        customer_id: str,
    ) -> pd.DataFrame: ...