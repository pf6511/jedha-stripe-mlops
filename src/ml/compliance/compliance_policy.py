from abc import ABC, abstractmethod

from src.ml.compliance.compliance_rule import ComplianceRule


class CompliancePolicy(ABC):
    """
    Defines the rules composing a compliance framework.
    """

    @property
    @abstractmethod
    def compliance_type(self) -> str:
        pass

    @abstractmethod
    def rules(self) -> list[ComplianceRule]:
        pass