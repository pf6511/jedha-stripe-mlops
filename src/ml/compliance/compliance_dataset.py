
from dataclasses import dataclass
from .compliance_schema import ComplianceSchema
import pandas as pd
from datetime import datetime


@dataclass
class ComplianceDataset:
    # ML_GOVERNANCE | GDPR | PCI_DSS...
    compliance_type: str
    period_start: datetime
    period_end: datetime
    schema: ComplianceSchema
    observations: pd.DataFrame