from dataclasses import dataclass
from typing import Optional

@dataclass
class ComplianceFinding:

    severity: str
    rule: str
    description: str
    recommendation: str | None = None

    @staticmethod
    def info(
        rule: str,
        description: str = "Compliance check passed."
    ) -> "ComplianceFinding":
        return ComplianceFinding(
            severity="INFO",
            rule=rule,
            description=description,
        )

    @staticmethod
    def warning(
        rule: str,
        description: str,
        recommendation: str | None = None,
    ) -> "ComplianceFinding":
        return ComplianceFinding(
            severity="WARNING",
            rule=rule,
            description=description,
            recommendation=recommendation,
        )

    @staticmethod
    def error(
        rule: str,
        description: str,
        recommendation: str | None = None,
    ) -> "ComplianceFinding":
        return ComplianceFinding(
            severity="ERROR",
            rule=rule,
            description=description,
            recommendation=recommendation,
        )