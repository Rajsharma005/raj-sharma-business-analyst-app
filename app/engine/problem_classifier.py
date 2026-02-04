"""
Problem Classification Engine (Domain-Agnostic)
----------------------------------------------
This module provides a lightweight, reusable way to translate an unstructured
business problem statement into structured categories used by Business Analysts.

Why this matters:
- Classification standardizes ambiguous problem statements so they can be routed
  to the right KPI sets, analytical techniques, and stakeholder expectations.
- It bridges business language ("deliveries are late") to analytic framing
  ("Efficiency -> Cycle Time -> Operational"), enabling faster hypothesis
  generation and recommendation design.
- It improves consistency across domains, so BA outputs are comparable and
  repeatable across portfolios and interviews.
"""

from __future__ import annotations

from typing import Dict

# A compact, interview-ready taxonomy that is intentionally domain-agnostic.
# Primary categories reflect common BA mandates across functions and industries.
PROBLEM_TAXONOMY = {
    "growth": {
        "keywords": ["grow", "expansion", "new market", "acquire", "scale"],
        "subcategories": {
            "market_expansion": ["new market", "geography", "segment"],
            "product_growth": ["upsell", "cross-sell", "adoption"],
        },
        "nature": "strategic",
    },
    "revenue": {
        "keywords": ["revenue", "sales", "pipeline", "conversion", "pricing"],
        "subcategories": {
            "conversion": ["conversion", "win rate", "close rate"],
            "pricing": ["price", "discount", "margin"],
        },
        "nature": "strategic",
    },
    "cost": {
        "keywords": ["cost", "expense", "overspend", "budget", "burn"],
        "subcategories": {
            "cost_overrun": ["overrun", "overspend", "variance"],
            "unit_economics": ["cost per", "unit cost"],
        },
        "nature": "tactical",
    },
    "efficiency": {
        "keywords": ["delay", "cycle time", "throughput", "productivity", "bottleneck"],
        "subcategories": {
            "delivery_delay": ["delay", "late", "sla"],
            "process_bottleneck": ["bottleneck", "handoff", "rework"],
        },
        "nature": "operational",
    },
    "churn": {
        "keywords": ["churn", "attrition", "retention", "renewal"],
        "subcategories": {
            "customer_churn": ["customer", "renewal"],
            "employee_attrition": ["employee", "talent", "resignation"],
        },
        "nature": "strategic",
    },
    "risk": {
        "keywords": ["risk", "exposure", "fraud", "downtime", "incident"],
        "subcategories": {
            "operational_risk": ["downtime", "incident"],
            "fraud_risk": ["fraud", "abuse"],
        },
        "nature": "operational",
    },
    "compliance": {
        "keywords": ["compliance", "audit", "regulatory", "policy"],
        "subcategories": {
            "audit_findings": ["audit", "finding"],
            "regulatory_change": ["regulatory", "law", "policy"],
        },
        "nature": "tactical",
    },
}


def _match_subcategory(statement: str, subcategories: Dict[str, list[str]]) -> str:
    """Return the first matching subcategory based on keywords, else 'general'."""
    for subcategory, keywords in subcategories.items():
        if any(keyword in statement for keyword in keywords):
            return subcategory
    return "general"


def classify_problem(statement: str) -> Dict[str, str]:
    """
    Classify a plain-English business problem statement into a structured form.

    Returns a dictionary with:
    - primary_category: highest-level taxonomy bucket
    - secondary_subcategory: more specific analytical focus
    - problem_nature: strategic / operational / tactical

    The output is intentionally structured for downstream modules:
    - KPI mapping can use the category/subcategory to surface metrics
    - Hypothesis generation can align to the nature and focus area
    - Recommendations can prioritize strategic vs operational interventions
    """
    normalized = statement.strip().lower()

    for category, meta in PROBLEM_TAXONOMY.items():
        if any(keyword in normalized for keyword in meta["keywords"]):
            return {
                "primary_category": category,
                "secondary_subcategory": _match_subcategory(
                    normalized, meta["subcategories"]
                ),
                "problem_nature": meta["nature"],
            }

    # Default fallback keeps the engine robust for ambiguous inputs.
    return {
        "primary_category": "unclassified",
        "secondary_subcategory": "general",
        "problem_nature": "operational",
    }


# Example problem statements and expected outputs:
# 1) "Delivery timelines are slipping and throughput is down across teams."
#    => {"primary_category": "efficiency", "secondary_subcategory": "delivery_delay",
#        "problem_nature": "operational"}
#
# 2) "Customer renewals have declined and churn is rising in SMB accounts."
#    => {"primary_category": "churn", "secondary_subcategory": "customer_churn",
#        "problem_nature": "strategic"}
#
# 3) "We are overspending on marketing and costs per lead are increasing."
#    => {"primary_category": "cost", "secondary_subcategory": "unit_economics",
#        "problem_nature": "tactical"}
