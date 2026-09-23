from abc import ABC, abstractmethod

from src.ml.compliance.compliance_dataset import ComplianceDataset
from src.ml.compliance.compliance_finding import ComplianceFinding


class ComplianceRule(ABC):
    """
    Base class for a compliance rule.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def evaluate(
        self,
        dataset: ComplianceDataset,
    ) -> list[ComplianceFinding]:
        pass