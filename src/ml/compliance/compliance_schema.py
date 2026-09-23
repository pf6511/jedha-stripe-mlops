from dataclasses import dataclass

@dataclass
class ComplianceSchema:

    identifier_columns: list[str]

    timestamp_column: str | None

    status_column: str | None

    metric_columns: list[str]