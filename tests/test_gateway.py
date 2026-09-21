from app.gateway.service import LLMGateway
from app.providers.base import GenerationRequest
from app.providers.mock import MockLLMProvider


def test_gateway_routes_request():

    gateway = LLMGateway(
        providers={
            "mock": MockLLMProvider()
        }
    )

    response = gateway.generate(
        provider_name="mock",
        request=GenerationRequest(
            prompt="Explain retrieval evaluation."
        ),
    )

    assert response.request_id
    assert (
        response.generation.provider
        == "mock"
    )
    assert (
        response.generation.model
        == "mock-model-v1"
    )


def test_gateway_rejects_unknown_provider():

    gateway = LLMGateway(
        providers={
            "mock": MockLLMProvider()
        }
    )

    try:
        gateway.generate(
            provider_name="unknown",
            request=GenerationRequest(
                prompt="test"
            ),
        )

        assert False

    except ValueError:
        assert True
