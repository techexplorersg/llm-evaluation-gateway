import uuid
from dataclasses import dataclass

from app.providers.base import (
    GenerationRequest,
    GenerationResponse,
    LLMProvider,
)


@dataclass(frozen=True)
class GatewayResponse:
    request_id: str
    generation: GenerationResponse


class LLMGateway:

    def __init__(
        self,
        providers: dict[str, LLMProvider],
    ):
        if not providers:
            raise ValueError(
                "At least one provider is required"
            )

        self.providers = providers

    def generate(
        self,
        provider_name: str,
        request: GenerationRequest,
    ) -> GatewayResponse:

        provider = self.providers.get(
            provider_name
        )

        if provider is None:
            raise ValueError(
                f"Unknown provider: {provider_name}"
            )

        generation = provider.generate(
            request
        )

        return GatewayResponse(
            request_id=str(uuid.uuid4()),
            generation=generation,
        )
