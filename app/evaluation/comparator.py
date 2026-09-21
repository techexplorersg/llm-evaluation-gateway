from dataclasses import dataclass


@dataclass(frozen=True)
class ModelMetrics:
    quality_score: float
    mean_latency_ms: float
    estimated_cost_usd: float


@dataclass(frozen=True)
class ModelComparison:
    quality_delta: float
    latency_delta_pct: float
    cost_delta_pct: float


def _percentage_change(
    baseline: float,
    candidate: float,
) -> float:
    if baseline == 0:
        return 0.0 if candidate == 0 else float("inf")

    return ((candidate - baseline) / baseline) * 100


def compare_models(
    baseline: ModelMetrics,
    candidate: ModelMetrics,
) -> ModelComparison:

    return ModelComparison(
        quality_delta=(
            candidate.quality_score
            - baseline.quality_score
        ),
        latency_delta_pct=_percentage_change(
            baseline.mean_latency_ms,
            candidate.mean_latency_ms,
        ),
        cost_delta_pct=_percentage_change(
            baseline.estimated_cost_usd,
            candidate.estimated_cost_usd,
        ),
    )
