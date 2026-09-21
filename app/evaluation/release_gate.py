from dataclasses import dataclass

from app.evaluation.comparator import (
    ModelComparison,
)


@dataclass(frozen=True)
class ReleasePolicy:
    max_quality_regression: float = 0.02
    max_latency_increase_pct: float = 20.0
    max_cost_increase_pct: float = 15.0


@dataclass(frozen=True)
class ReleaseDecision:
    approved: bool
    reasons: list[str]


def evaluate_release(
    comparison: ModelComparison,
    policy: ReleasePolicy,
) -> ReleaseDecision:

    reasons = []

    if (
        comparison.quality_delta
        < -policy.max_quality_regression
    ):
        reasons.append(
            "Candidate exceeds allowed quality regression."
        )

    if (
        comparison.latency_delta_pct
        > policy.max_latency_increase_pct
    ):
        reasons.append(
            "Candidate exceeds allowed latency increase."
        )

    if (
        comparison.cost_delta_pct
        > policy.max_cost_increase_pct
    ):
        reasons.append(
            "Candidate exceeds allowed cost increase."
        )

    return ReleaseDecision(
        approved=not reasons,
        reasons=reasons,
    )
