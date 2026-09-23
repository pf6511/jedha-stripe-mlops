from datetime import datetime

from src.ml.compliance.compliance_dataset import ComplianceDataset
from src.ml.compliance.compliance_policy import CompliancePolicy
from src.ml.compliance.compliance_report    import (
    ComplianceFinding,
    ComplianceReport,
)


class ComplianceService:
    """
    Executes compliance policies.
    """

    def evaluate(
        self,
        dataset: ComplianceDataset,
        policy: CompliancePolicy,
    ) -> ComplianceReport:

        findings: list[ComplianceFinding] = []

        for rule in policy.rules():
            findings.extend(rule.evaluate(dataset))

        overall_status = self._compute_status(findings)

        return ComplianceReport(
            compliance_type=policy.compliance_type,
            generated_at=datetime.utcnow(),
            overall_status=overall_status,
            findings=findings,
            summary=self._build_summary(findings),
        )

    def _compute_status(
        self,
        findings: list[ComplianceFinding],
    ) -> str:

        if any(f.severity == "ERROR" for f in findings):
            return "NON_COMPLIANT"

        if any(f.severity == "WARNING" for f in findings):
            return "UNDER_REVIEW"

        return "COMPLIANT"

    def _build_summary(
        self,
        findings: list[ComplianceFinding],
    ) -> dict:

        return {
            "errors": sum(f.severity == "ERROR" for f in findings),
            "warnings": sum(f.severity == "WARNING" for f in findings),
            "checks": len(findings),
        }