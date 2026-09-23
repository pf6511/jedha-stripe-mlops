from dataclasses import dataclass


@dataclass(frozen=True)
class ExperimentResult:
    """
    Result of a completed MLflow experiment.
    """

    run_id: str

    model_uri: str