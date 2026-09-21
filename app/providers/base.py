from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class GenerationRequest:
    prompt: str
    temperature: float = 0.0
    max_tokens: int = 512


@dataclass(frozen=True)
class GenerationResponse:
    provider: str
    model: str
    text: str

    input_tokens: int
    output_tokens: int

    latency_ms: float

    estimated_cost_usd: float | None = None


class LLMProvider(ABC):

    @abstractmethod
    def generate(
        self,
        request: GenerationRequest,
    ) -> GenerationResponse:
        """Generate a model response."""
        raise NotImplementedError
