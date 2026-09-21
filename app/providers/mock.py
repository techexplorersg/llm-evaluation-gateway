import time

from app.providers.base import (
    GenerationRequest,
    GenerationResponse,
    LLMProvider,
)


class MockLLMProvider(LLMProvider):

    def __init__(
        self,
        model: str = "mock-model-v1",
    ):
        self.model = model

    def generate(
        self,
        request: GenerationRequest,
    ) -> GenerationResponse:

        start = time.perf_counter()

        response_text = (
            f"Mock response for: {request.prompt}"
        )

        latency_ms = (
            time.perf_counter() - start
        ) * 1000

        return GenerationResponse(
            provider="mock",
            model=self.model,
            text=response_text,
            input_tokens=len(
                request.prompt.split()
            ),
            output_tokens=len(
                response_text.split()
            ),
            latency_ms=latency_ms,
            estimated_cost_usd=0.0,
        )
