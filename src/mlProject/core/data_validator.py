# src/mlProject/core/data_validator.py

from abc import ABC, abstractmethod
import pandas as pd
from mlProject.entities.artifact_entity import ValidationResult

class IDataValidator(ABC):
    @abstractmethod
    def validate(self, data: pd.DataFrame) -> ValidationResult:
        raise NotImplementedError