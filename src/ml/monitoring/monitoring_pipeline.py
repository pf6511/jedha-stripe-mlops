from src.ml.monitoring.monitoring_report import MonitoringReport
from src.ml.monitoring.monitoring_service import MonitoringService


class MonitoringPipeline:

    def __init__(
        self,
        monitoring_service: MonitoringService,
    ):
        self._monitoring_service = monitoring_service

    def run(
        self,
        model_name: str,
        model_version: str | None = None,
    ) -> MonitoringReport:

        return self._monitoring_service.run_monitoring(
            model_name=model_name,
            model_version=model_version,
        )