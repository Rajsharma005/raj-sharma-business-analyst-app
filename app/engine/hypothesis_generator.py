"""
Hypothesis Generation Engine (Domain-Agnostic)
----------------------------------------------
This module generates structured, testable business hypotheses based on a
problem classification, domain context, and KPI map. It is designed to help
Business Analysts move from problem framing to actionable analysis plans.

Why this matters:
- Hypotheses convert business questions into testable statements.
- Tying hypotheses to KPIs ensures analysis stays outcome-focused.
- Clear, prioritized hypotheses accelerate stakeholder alignment and execution.
"""

from __future__ import annotations

from typing import Dict, List


def _extract_kpi_names(kpi_map: Dict[str, object]) -> List[str]:
    primary = [kpi.get("name") for kpi in kpi_map.get("primary_kpis", [])]
    secondary = [kpi.get("name") for kpi in kpi_map.get("secondary_kpis", [])]
    return [name for name in primary + secondary if name]


def _base_hypotheses(problem_type: str, domain: str) -> List[Dict[str, object]]:
    """Return a baseline hypothesis set tailored to problem type and domain."""
    if problem_type == "churn" and domain == "saas_tech":
        return [
            {
                "statement": "Lower product adoption is driving higher churn in the SMB segment.",
                "rationale": "Adoption is a leading indicator of retention in SaaS.",
                "expected_direction": "decrease",
                "test_method": "cohort analysis",
                "confidence": 0.7,
            },
            {
                "statement": "Support response times increased, leading to churn in high-value accounts.",
                "rationale": "Service quality issues often precede churn among premium segments.",
                "expected_direction": "increase",
                "test_method": "trend analysis",
                "confidence": 0.6,
            },
            {
                "statement": "Price increases reduced renewal rates in price-sensitive cohorts.",
                "rationale": "Pricing elasticity affects retention in competitive SaaS markets.",
                "expected_direction": "decrease",
                "test_method": "comparison",
                "confidence": 0.5,
            },
        ]

    if problem_type == "efficiency" and domain == "banking_finance":
        return [
            {
                "statement": "Workload imbalance across collections teams is increasing cycle time.",
                "rationale": "Uneven caseloads reduce throughput and delay resolution.",
                "expected_direction": "increase",
                "test_method": "variance analysis",
                "confidence": 0.65,
            },
            {
                "statement": "Manual verification steps are creating bottlenecks in collections workflows.",
                "rationale": "High manual touchpoints increase handling time.",
                "expected_direction": "increase",
                "test_method": "process analysis",
                "confidence": 0.6,
            },
        ]

    if problem_type == "efficiency" and domain in {"manufacturing", "logistics"}:
        return [
            {
                "statement": "Unplanned downtime is reducing throughput and productivity.",
                "rationale": "Downtime directly reduces output in ops-heavy environments.",
                "expected_direction": "decrease",
                "test_method": "trend analysis",
                "confidence": 0.7,
            },
            {
                "statement": "High rework rates are increasing cycle time and lowering throughput.",
                "rationale": "Rework adds non-value-added time to the process.",
                "expected_direction": "increase",
                "test_method": "correlation",
                "confidence": 0.6,
            },
        ]

    # Generic fallback hypotheses for other cases.
    return [
        {
            "statement": "Demand changes are driving shifts in core KPIs.",
            "rationale": "Market or customer behavior changes often explain KPI movement.",
            "expected_direction": "unknown",
            "test_method": "trend analysis",
            "confidence": 0.4,
        },
        {
            "statement": "Process inefficiencies are contributing to the observed performance gap.",
            "rationale": "Operational bottlenecks commonly explain performance declines.",
            "expected_direction": "increase",
            "test_method": "process analysis",
            "confidence": 0.5,
        },
    ]


def generate_hypotheses(
    problem_classification: Dict[str, str],
    domain_context: Dict[str, object],
    kpi_map: Dict[str, object],
) -> Dict[str, object]:
    """
    Generate structured hypotheses based on classification, domain, and KPI set.
    Returns primary and secondary hypotheses, null examples, and a hypothesis tree.
    """
    problem_type = problem_classification.get("primary_category", "general")
    domain = domain_context.get("domain", "general_business")
    kpi_names = _extract_kpi_names(kpi_map)

    base = _base_hypotheses(problem_type, domain)

    primary_hypotheses = []
    for hypothesis in base[:5]:
        primary_hypotheses.append(
            {
                "statement": hypothesis["statement"],
                "rationale": hypothesis["rationale"],
                "related_kpis": kpi_names[:2],
                "expected_direction": hypothesis["expected_direction"],
                "data_needed": [
                    "KPI trends", "Segment-level breakdowns", "Process timestamps"
                ],
                "test_method": hypothesis["test_method"],
                "confidence": hypothesis["confidence"],
                "risk_if_wrong": "May mis-prioritize root causes and delay corrective action.",
            }
        )

    secondary_hypotheses = [
        {
            "statement": "Data quality issues are exaggerating KPI declines.",
            "rationale": "Inconsistent data can create false signals in performance metrics.",
            "related_kpis": kpi_names[:1],
            "expected_direction": "unknown",
            "data_needed": ["Data completeness checks", "Audit logs"],
            "test_method": "validation",
            "confidence": 0.3,
            "risk_if_wrong": "May waste time on validation rather than real drivers.",
        },
        {
            "statement": "A specific segment or region is disproportionately driving the KPI decline.",
            "rationale": "Localized issues often explain aggregate KPI shifts.",
            "related_kpis": kpi_names[:2],
            "expected_direction": "decrease",
            "data_needed": ["Segment KPIs", "Region-level KPIs"],
            "test_method": "cohort analysis",
            "confidence": 0.5,
            "risk_if_wrong": "May over-focus on one segment and miss systemic issues.",
        },
    ]

    null_hypotheses = [
        "There is no statistically significant change in the primary KPI trend.",
        "Observed KPI shifts are within normal seasonal variation.",
        "The problem is not driven by operational factors but by external market shifts.",
    ]

    hypothesis_tree = {
        "people": [
            "Skill gaps or staffing shortfalls are reducing productivity.",
            "Training coverage is inconsistent across teams.",
        ],
        "process": [
            "Process bottlenecks are creating delays and rework.",
            "Hand-off points introduce wait time and errors.",
        ],
        "technology": [
            "Tooling limitations increase manual effort and error rates.",
            "System outages reduce throughput and SLA adherence.",
        ],
        "policy": [
            "Policy changes introduced additional approval steps.",
            "Compliance constraints reduce operational flexibility.",
        ],
    }

    return {
        "primary_hypotheses": primary_hypotheses,
        "secondary_hypotheses": secondary_hypotheses,
        "null_hypothesis_examples": null_hypotheses,
        "hypothesis_tree": hypothesis_tree,
    }


# Examples:
# 1) SaaS churn increase
#    problem_classification = {"primary_category": "churn"}
#    domain_context = {"domain": "saas_tech"}
#    kpi_map = {"primary_kpis": [{"name": "Gross Revenue Churn %"}]}
#    Expected => primary_hypotheses include adoption and support-related causes,
#               related_kpis include Gross Revenue Churn %.
#
# 2) Banking collections delay
#    problem_classification = {"primary_category": "efficiency"}
#    domain_context = {"domain": "banking_finance"}
#    kpi_map = {"primary_kpis": [{"name": "Collections Cycle Time"}]}
#    Expected => primary_hypotheses include workload imbalance and manual steps.
#
# 3) Operations productivity drop
#    problem_classification = {"primary_category": "efficiency"}
#    domain_context = {"domain": "logistics"}
#    kpi_map = {"primary_kpis": [{"name": "Throughput"}]}
#    Expected => primary_hypotheses include downtime and rework rates.
