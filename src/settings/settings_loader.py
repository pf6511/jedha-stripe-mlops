from pathlib import Path

from .environment import Environment
from .settings import Settings


class SettingsLoader:

    @staticmethod
    def load(environment: Environment) -> Settings:

        path = Path("config") / f"{environment.value}.json"

        return Settings.model_validate_json(path.read_text())