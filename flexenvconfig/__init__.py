import os
from typing import Optional, TypeVar

from abs import ABC, abstractmethod


class BaseFlexEnvConfig(ABC):
    @abstractmethod
    def __init__(self) -> None:
        """
        Abstact constructor, define your configuration values as attributes
        """
        pass

    @classmethod
    def get_env(cls, key: str, default: Optional[str] = None) -> Optional[str]:
        """
        Helper method to fetch values from the environment when building config
        objects
        """
        return os.getenv(key, default)

    @abstractmethod
    def validate(self) -> bool:  # type: ignore[empty-body]
        """
        Implement logic that validates that a config object contains the require
        attributes
        """
        pass
