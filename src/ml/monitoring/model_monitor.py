from abc import ABC, abstractmethod

from src.ml.monitoring.monitoring_dataset import MonitoringDataset
from src.ml.monitoring.monitoring_report import MonitoringReport


class ModelMonitor(ABC):

    @abstractmethod
    def evaluate(
        self,
        dataset: MonitoringDataset,
    ) -> MonitoringReport:
        """
        Evaluates the monitoring dataset and produces a monitoring report.
        """
        pass