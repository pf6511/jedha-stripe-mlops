from abc import ABC, abstractmethod

from src.ml.compliance.compliance_dataset import ComplianceDataset


class ComplianceRepository(ABC):
    """
    Loads compliance datasets prepared by dbt models.
    """

    @abstractmethod
    def load(
        self,
        compliance_type: str,
        **filters,
    ) -> ComplianceDataset:
        """
        Loads a compliance dataset.

        Parameters
        ----------
        compliance_type : str
            GDPR, PCI_DSS or ML_GOVERNANCE.
        filters :
            Optional filters (period, model, version...).

        Returns
        -------
        ComplianceDataset
        """
        pass