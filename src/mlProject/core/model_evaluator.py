# src/mlProject/core/model_evaluator.py

from abc import ABC, abstractmethod
from typing import Any
from mlProject.entities.artifact_entity import EvaluationMetrics

class IModelEvaluator(ABC):
    @abstractmethod
    def evaluate(self, model: Any, test_data: Any) -> EvaluationMetrics:
        raise NotImplementedError

    @abstractmethod
    def log_metrics(self, metrics: EvaluationMetrics) -> None:
        raise NotImplementedError