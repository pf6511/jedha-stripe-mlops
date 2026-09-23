from enum import Enum


class Environment(str, Enum):
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"

    @staticmethod
    def get_current_env():
        return Environment.DEV