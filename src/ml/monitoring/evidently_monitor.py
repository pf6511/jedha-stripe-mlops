from src.ml.monitoring.model_monitor import ModelMonitor
from src.ml.monitoring.monitoring_dataset import MonitoringDataset
from src.ml.monitoring.monitoring_report import MonitoringReport


class EvidentlyMonitor(ModelMonitor):
    """
    Monitoring engine based on Evidently.

    This implementation is responsible for configuring the monitoring
    metrics, executing the monitoring workflow and transforming the
    results into a framework-independent MonitoringReport.
    """

    def evaluate(
        self,
        dataset: MonitoringDataset,
    ) -> MonitoringReport:
        """
        Evaluates a monitoring dataset.

        The implementation is expected to:
        - interpret the MonitoringSchema;
        - configure the Evidently metrics;
        - execute the monitoring workflow;
        - convert the Evidently results into a MonitoringReport.
        """

        #
        # 1. Retrieve the semantic description of the dataset
        #
        schema = dataset.schema

        #
        # 2. Configure the monitoring engine
        #
        # report = Report(
        #     metrics=[
        #         ...
        #     ]
        # )

        #
        # 3. Execute the monitoring
        #
        # report.run(
        #     current_data=...,
        #     reference_data=...,
        # )

        #
        # 4. Build the framework-independent report
        #
        # return MonitoringReport(
        #     model_name=dataset.model_name,
        #     model_version=dataset.model_version,
        #     generated_at=datetime.now(),
        #     metrics=...,
        #     drift_detected=...,
        #     alerts=...,
        # )

        raise NotImplementedError