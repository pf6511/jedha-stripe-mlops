from abc import ABC, abstractmethod

from src.ml.monitoring.monitoring_dataset import MonitoringDataset


class MonitoringRepository(ABC):

    @abstractmethod
    def load_monitoring_dataset(
        self,
        model_name: str,
        model_version: str | None = None,
    ) -> MonitoringDataset:
        """
        Loads the monitoring dataset associated with a deployed model.
        """
        pass