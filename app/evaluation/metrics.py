from dataclasses import dataclass
from statistics import mean


@dataclass(frozen=True)
class EvaluationSample:
    passed: bool
    latency_ms: float
    estimated_cost_usd: float


@dataclass(frozen=True)
class EvaluationSummary:
    pass_rate: float
    mean_latency_ms: float
    total_cost_usd: float


def summarize(
    samples: list[EvaluationSample],
) -> EvaluationSummary:

    if not samples:
        return EvaluationSummary(
            pass_rate=0.0,
            mean_latency_ms=0.0,
            total_cost_usd=0.0,
        )

    return EvaluationSummary(
        pass_rate=mean(
            float(sample.passed)
            for sample in samples
        ),
        mean_latency_ms=mean(
            sample.latency_ms
            for sample in samples
        ),
        total_cost_usd=sum(
            sample.estimated_cost_usd
            for sample in samples
        ),
    )
