# /src/mlProject/core/pipeline_stage.py

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mlProject.entities.pipeline_entity import PipelineContext, PipelineResult

class IPipelineStage(ABC):
    """Contract implemented by every pipeline stage."""

    @abstractmethod
    def run(self, context: "PipelineContext") -> "PipelineResult":
        raise NotImplementedError