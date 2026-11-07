# src/mlProject/core/config_manager.py

from abc import ABC, abstractmethod
from typing import Any

class IConfigManager(ABC):
    @abstractmethod
    def get_stage_config(self, stage_name: str) -> Any:
        raise NotImplementedError