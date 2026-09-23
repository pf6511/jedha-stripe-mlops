from src.ml.monitoring.evidently_monitor import EvidentlyMonitor
from src.ml.monitoring.monitoring_pipeline import MonitoringPipeline
from src.ml.monitoring.monitoring_service import MonitoringService
from src.ml.repositories.monitoring_repository import MonitoringRepository


class MonitoringPipelineBuilder:

    @classmethod
    def build(
        cls,
        repository: MonitoringRepository,
    ) -> MonitoringPipeline:

        monitor = EvidentlyMonitor()

        monitoring_service = MonitoringService(
            repository=repository,
            monitor=monitor,
        )

        return MonitoringPipeline(
            monitoring_service=monitoring_service,
        )