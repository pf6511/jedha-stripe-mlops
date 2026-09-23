from dataclasses import dataclass


@dataclass(frozen=True)
class FeatureDefinition:
    """
    Definition of a single feature.
    """

    name: str

    description: str

    data_type: str

    window: str | None = None

    nullable: bool = False