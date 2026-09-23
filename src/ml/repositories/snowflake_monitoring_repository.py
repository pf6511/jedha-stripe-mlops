from src.ml.monitoring.monitoring_dataset import MonitoringDataset
from src.ml.repositories.monitoring_repository import MonitoringRepository


class SnowflakeMonitoringRepository(MonitoringRepository):

    def load_monitoring_dataset(
        self,
        model_name: str,
        model_version: str | None = None,
    ) -> MonitoringDataset:
        """
        Loads a monitoring dataset from Snowflake.
        """

        raise NotImplementedError