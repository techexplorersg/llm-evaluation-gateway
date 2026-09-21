from app.evaluation.comparator import (
    ModelMetrics,
    compare_models,
)
from app.evaluation.release_gate import (
    ReleasePolicy,
    evaluate_release,
)


def test_candidate_is_approved():

    baseline = ModelMetrics(
        quality_score=0.85,
        mean_latency_ms=500,
        estimated_cost_usd=0.010,
    )

    candidate = ModelMetrics(
        quality_score=0.87,
        mean_latency_ms=520,
        estimated_cost_usd=0.0105,
    )

    comparison = compare_models(
        baseline,
        candidate,
    )

    decision = evaluate_release(
        comparison,
        ReleasePolicy(),
    )

    assert decision.approved
    assert decision.reasons == []


def test_quality_regression_blocks_release():

    baseline = ModelMetrics(
        quality_score=0.90,
        mean_latency_ms=500,
        estimated_cost_usd=0.010,
    )

    candidate = ModelMetrics(
        quality_score=0.82,
        mean_latency_ms=450,
        estimated_cost_usd=0.008,
    )

    decision = evaluate_release(
        compare_models(
            baseline,
            candidate,
        ),
        ReleasePolicy(),
    )

    assert not decision.approved


def test_latency_regression_blocks_release():

    baseline = ModelMetrics(
        quality_score=0.85,
        mean_latency_ms=500,
        estimated_cost_usd=0.010,
    )

    candidate = ModelMetrics(
        quality_score=0.87,
        mean_latency_ms=750,
        estimated_cost_usd=0.010,
    )

    decision = evaluate_release(
        compare_models(
            baseline,
            candidate,
        ),
        ReleasePolicy(),
    )

    assert not decision.approved
