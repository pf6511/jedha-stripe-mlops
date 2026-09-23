from src.ml.monitoring.model_monitor import ModelMonitor
from src.ml.monitoring.monitoring_report import MonitoringReport
from src.ml.repositories.monitoring_repository import MonitoringRepository


class MonitoringService:

    def __init__(
        self,
        repository: MonitoringRepository,
        monitor: ModelMonitor,
    ):
        self._repository = repository
        self._monitor = monitor

    def run_monitoring(
        self,
        model_name: str,
        model_version: str | None = None,
    ) -> MonitoringReport:

        dataset = self._repository.load_monitoring_dataset(
            model_name=model_name,
            model_version=model_version,
        )

        return self._monitor.evaluate(dataset)