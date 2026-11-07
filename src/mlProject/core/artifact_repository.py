# src/mlProject/core/artifact_repository.py

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

class IArtifactRepository(ABC):
    @abstractmethod
    def save_artifact(self, name: str, obj: Any) -> Path:
        raise NotImplementedError

    @abstractmethod
    def load_artifact(self, path: str | Path) -> Any:
        raise NotImplementedError