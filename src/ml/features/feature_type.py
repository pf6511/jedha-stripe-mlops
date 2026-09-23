from dataclasses import dataclass
from enum import StrEnum


class FeatureType(StrEnum):
    NUMERICAL = "numerical"
    CATEGORICAL = "categorical"
    BOOLEAN = "boolean"
    DATETIME = "datetime"