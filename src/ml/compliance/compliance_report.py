
from dataclasses import dataclass
from .compliance_schema import ComplianceSchema
from .compliance_finding import ComplianceFinding
import pandas as pd
from datetime import datetime
from typing import Any

@dataclass
class ComplianceReport:

    compliance_type: str

    generated_at: datetime

    overall_status: str

    findings: list[ComplianceFinding]

    summary: dict[str, Any]