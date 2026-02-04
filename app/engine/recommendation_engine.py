"""
Recommendation & Decision-Support Engine (Domain-Agnostic)
---------------------------------------------------------
This module converts validated/high-confidence hypotheses into structured,
executive-ready recommendations. It balances impact, effort, risk, and timing
so leaders can make clear decisions.

Why this matters:
- Recommendations translate analysis into action.
- Explicit trade-offs (impact vs. effort) prevent unrealistic roadmaps.
- Clear linkage to hypotheses and KPIs preserves analytical rigor.
"""

from __future__ import annotations

from typing import Dict, List


def _default_constraints() -> Dict[str, object]:
    return {
        "risk_appetite": "medium",
        "budget_constraint": "moderate",
        "timeline_pressure": "moderate",
        "change_capacity": "medium",
    }


def _prioritize(impact_score: int, effort_score: int) -> str:
    if impact_score >= 4 and effort_score <= 2:
        return "P1"
    if impact_score >= 4 and effort_score <= 4:
        return "P2"
    return "P3"


def _build_recommendation(
    action_statement: str,
    linked_hypothesis: str,
    expected_business_impact: str,
    impacted_kpis: List[str],
    implementation_owner: str,
    estimated_effort: str,
    estimated_timeframe: str,
    risks_and_dependencies: str,
    success_criteria: str,
    impact_score: int,
    effort_score: int,
) -> Dict[str, object]:
    return {
        "action_statement": action_statement,
        "linked_hypothesis": linked_hypothesis,
        "expected_business_impact": expected_business_impact,
        "impacted_kpis": impacted_kpis,
        "implementation_owner": implementation_owner,
        "estimated_effort": estimated_effort,
        "estimated_timeframe": estimated_timeframe,
        "risks_and_dependencies": risks_and_dependencies,
        "success_criteria": success_criteria,
        "impact_score": impact_score,
        "effort_score": effort_score,
        "priority_rank": _prioritize(impact_score, effort_score),
    }


def generate_recommendations(
    hypotheses: Dict[str, object],
    domain_context: Dict[str, object],
    business_constraints: Dict[str, object] | None = None,
) -> Dict[str, object]:
    """
    Generate structured recommendations from hypotheses, domain context,
    and business constraints.
    """
    constraints = business_constraints or _default_constraints()
    primary_hypotheses = hypotheses.get("primary_hypotheses", [])
    top_hypothesis = primary_hypotheses[0]["statement"] if primary_hypotheses else ""
    impacted_kpis = []
    if primary_hypotheses:
        impacted_kpis = primary_hypotheses[0].get("related_kpis", [])

    quick_wins = [
        _build_recommendation(
            action_statement="Tighten operational playbooks in the highest-impact segment",
            linked_hypothesis=top_hypothesis,
            expected_business_impact="Stabilize KPIs quickly by reducing preventable leakage",
            impacted_kpis=impacted_kpis,
            implementation_owner="Ops",
            estimated_effort="Low",
            estimated_timeframe="2-4 weeks",
            risks_and_dependencies="Requires frontline adoption and manager enforcement",
            success_criteria="Short-term KPI stabilization and SLA adherence",
            impact_score=4,
            effort_score=2,
        )
    ]

    strategic_bets = [
        _build_recommendation(
            action_statement="Redesign the core process to remove high-friction steps",
            linked_hypothesis=top_hypothesis,
            expected_business_impact="Sustained improvement in efficiency and quality",
            impacted_kpis=impacted_kpis,
            implementation_owner="Ops",
            estimated_effort="High",
            estimated_timeframe="3-6 months",
            risks_and_dependencies="Cross-functional alignment, funding, and change capacity",
            success_criteria="Structural KPI uplift sustained across two quarters",
            impact_score=5,
            effort_score=4,
        )
    ]

    risk_mitigation_actions = [
        _build_recommendation(
            action_statement="Introduce governance checks for high-risk decisions",
            linked_hypothesis=top_hypothesis,
            expected_business_impact="Reduce downside risk without halting progress",
            impacted_kpis=impacted_kpis,
            implementation_owner="Finance",
            estimated_effort="Medium",
            estimated_timeframe="4-6 weeks",
            risks_and_dependencies="Requires clear thresholds and ownership",
            success_criteria="No critical control breaches during rollout",
            impact_score=3,
            effort_score=3,
        )
    ]

    experiments_and_pilots = [
        _build_recommendation(
            action_statement="Run a pilot in a controlled segment before scaling",
            linked_hypothesis=top_hypothesis,
            expected_business_impact="Validate impact assumptions before full rollout",
            impacted_kpis=impacted_kpis,
            implementation_owner="Product",
            estimated_effort="Medium",
            estimated_timeframe="4-8 weeks",
            risks_and_dependencies="Pilot design must isolate variables",
            success_criteria="Pilot shows statistically meaningful KPI lift",
            impact_score=4,
            effort_score=3,
        )
    ]

    executive_summary = [
        "Focus on the top hypothesis and stabilize KPIs within 4-6 weeks.",
        "Deploy one high-confidence quick win while designing a longer-term fix.",
        "Pilot the strategic change in a controlled segment before scaling.",
        "Guardrails are required given current risk appetite and constraints.",
    ]

    return {
        "quick_wins": quick_wins,
        "strategic_bets": strategic_bets,
        "risk_mitigation_actions": risk_mitigation_actions,
        "experiments_and_pilots": experiments_and_pilots,
        "executive_summary": executive_summary,
        "business_constraints": constraints,
        "domain_context": domain_context,
    }


# Examples:
# 1) SaaS churn reduction roadmap
#    hypotheses = {"primary_hypotheses": [{"statement": "Low adoption drives churn", "related_kpis": ["NRR"]}]}
#    domain_context = {"domain": "saas_tech"}
#    Expected => quick_wins around adoption playbooks; strategic bets around product onboarding redesign.
#
# 2) Banking collections improvement plan
#    hypotheses = {"primary_hypotheses": [{"statement": "Manual verification slows collections", "related_kpis": ["Cycle Time"]}]}
#    domain_context = {"domain": "banking_finance"}
#    Expected => quick wins on workflow simplification; strategic bets on automation.
#
# 3) Operations cost-efficiency initiative
#    hypotheses = {"primary_hypotheses": [{"statement": "Downtime reduces throughput", "related_kpis": ["Throughput"]}]}
#    domain_context = {"domain": "manufacturing"}
#    Expected => pilots for preventive maintenance; strategic bets for process redesign.
