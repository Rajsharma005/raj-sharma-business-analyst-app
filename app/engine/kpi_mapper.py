"""
KPI Mapping Engine (Domain-Agnostic)
----------------------------------
This module selects business-first KPIs based on a problem classification and
mapped domain context. The output is structured for analysis planning and
stakeholder communication.

Why this matters:
- KPIs translate ambiguous problems into measurable signals.
- The right KPIs prevent misdiagnosis (e.g., optimizing revenue while harming
  retention or compliance).
- KPI selection drives downstream hypothesis design and recommendation impact.
"""

from __future__ import annotations

from typing import Dict, List

# KPI framework keyed by problem type and domain family.
# Keep the taxonomy compact and extendable for interviews and real projects.
KPI_FRAMEWORK = {
    "churn": {
        "saas_tech": {
            "primary_kpis": [
                {
                    "name": "Gross Revenue Churn %",
                    "definition": "Revenue lost from churned customers / starting MRR",
                    "why_it_matters": "Measures direct revenue impact of churn.",
                },
                {
                    "name": "Logo Churn %",
                    "definition": "Customers lost / starting customer count",
                    "why_it_matters": "Shows customer attrition beyond revenue.",
                },
            ],
            "secondary_kpis": [
                {
                    "name": "Net Revenue Retention (NRR)",
                    "definition": "(Starting MRR + Expansion - Contraction - Churn) / Starting MRR",
                    "why_it_matters": "Captures expansion offset to churn.",
                },
                {
                    "name": "Product Adoption Rate",
                    "definition": "Active users / licensed users",
                    "why_it_matters": "Low adoption often precedes churn.",
                },
            ],
            "leading_indicators": ["Product adoption rate", "Support ticket volume"],
            "lagging_indicators": ["Gross revenue churn", "Logo churn"],
            "data_sources": ["CRM", "Billing", "Product Analytics", "Support"],
            "granularity": "monthly, customer-level",
            "operational": ["Support ticket volume"],
            "strategic": ["NRR", "Gross Revenue Churn %"],
        }
    },
    "efficiency": {
        "banking_finance": {
            "primary_kpis": [
                {
                    "name": "Collections Cycle Time",
                    "definition": "Average days from delinquency to resolution",
                    "why_it_matters": "Direct measure of operational efficiency.",
                },
                {
                    "name": "Promises-to-Pay Kept %",
                    "definition": "Kept promises / total promises",
                    "why_it_matters": "Shows effectiveness of collections outreach.",
                },
            ],
            "secondary_kpis": [
                {
                    "name": "Agent Productivity",
                    "definition": "Accounts handled per agent per day",
                    "why_it_matters": "Signals workload balance and process bottlenecks.",
                },
                {
                    "name": "Delinquency Roll Rate",
                    "definition": "% of accounts rolling to next delinquency bucket",
                    "why_it_matters": "Indicates early warning of collections leakage.",
                },
            ],
            "leading_indicators": ["Promises-to-Pay Kept %", "Agent Productivity"],
            "lagging_indicators": ["Collections Cycle Time", "Recovery Rate"],
            "data_sources": ["Collections System", "CRM", "Core Banking"],
            "granularity": "weekly, account-level",
            "operational": ["Agent Productivity"],
            "strategic": ["Collections Cycle Time"],
        }
    },
    "revenue": {
        "retail_ecommerce": {
            "primary_kpis": [
                {
                    "name": "Net Sales",
                    "definition": "Gross sales minus returns and discounts",
                    "why_it_matters": "Core revenue health indicator.",
                },
                {
                    "name": "Conversion Rate",
                    "definition": "Orders / sessions",
                    "why_it_matters": "Signals funnel performance.",
                },
            ],
            "secondary_kpis": [
                {
                    "name": "Average Order Value (AOV)",
                    "definition": "Total sales / total orders",
                    "why_it_matters": "Shows pricing and basket health.",
                },
                {
                    "name": "Return Rate",
                    "definition": "Returns / orders",
                    "why_it_matters": "High returns erode net revenue.",
                },
            ],
            "leading_indicators": ["Traffic", "Conversion Rate"],
            "lagging_indicators": ["Net Sales", "Gross Margin"],
            "data_sources": ["Ecommerce Platform", "Web Analytics", "ERP"],
            "granularity": "daily, SKU-level",
            "operational": ["Conversion Rate"],
            "strategic": ["Net Sales", "Gross Margin"],
        }
    },
}


def _fallback_kpis(problem_type: str) -> Dict[str, object]:
    """Provide a generic KPI set if no specific domain mapping exists."""
    return {
        "primary_kpis": [
            {
                "name": f"{problem_type.title()} Impact Metric",
                "definition": "Primary outcome metric aligned to the problem type",
                "why_it_matters": "Ensures analysis focuses on the core business outcome.",
            }
        ],
        "secondary_kpis": [],
        "leading_indicators": [],
        "lagging_indicators": [],
        "operational": [],
        "strategic": [],
        "data_sources": ["Finance", "Operations"],
        "granularity": "monthly",
    }


def map_kpis(problem_classification: Dict[str, str], domain_context: Dict[str, object]) -> Dict[str, object]:
    """
    Map problem classification + domain context to a structured KPI set.

    Returns:
    - primary_kpis, secondary_kpis
    - leading_indicators, lagging_indicators
    - operational_vs_strategic (split lists)
    - data_sources_needed, granularity
    - risks_if_wrong_kpis
    - confidence
    """
    problem_type = problem_classification.get("primary_category", "general")
    domain = domain_context.get("domain", "general_business")

    framework = KPI_FRAMEWORK.get(problem_type, {}).get(domain)
    confidence = 0.75 if framework else 0.4

    if framework is None:
        framework = _fallback_kpis(problem_type)

    operational = framework.get("operational", [])
    strategic = framework.get("strategic", [])

    return {
        "primary_kpis": framework.get("primary_kpis", []),
        "secondary_kpis": framework.get("secondary_kpis", []),
        "leading_indicators": framework.get("leading_indicators", []),
        "lagging_indicators": framework.get("lagging_indicators", []),
        "operational_vs_strategic": {
            "operational": operational,
            "strategic": strategic,
        },
        "data_sources_needed": framework.get("data_sources", []),
        "granularity": framework.get("granularity", "monthly"),
        "risks_if_wrong_kpis": [
            "May optimize the wrong outcome (e.g., growth at the expense of churn).",
            "May miss early warning signals leading to delayed interventions.",
            "Can cause stakeholders to disagree on problem severity and priorities.",
        ],
        "confidence": round(confidence, 2),
    }


# Examples:
# 1) SaaS churn problem
#    problem_classification = {"primary_category": "churn"}
#    domain_context = {"domain": "saas_tech"}
#    Expected => primary_kpis include Gross Revenue Churn %, Logo Churn %;
#               leading indicators include Product adoption rate.
#
# 2) Banking collections efficiency
#    problem_classification = {"primary_category": "efficiency"}
#    domain_context = {"domain": "banking_finance"}
#    Expected => primary_kpis include Collections Cycle Time, Promises-to-Pay Kept %;
#               lagging indicators include Recovery Rate.
#
# 3) Retail revenue decline
#    problem_classification = {"primary_category": "revenue"}
#    domain_context = {"domain": "retail_ecommerce"}
#    Expected => primary_kpis include Net Sales, Conversion Rate;
#               secondary_kpis include AOV, Return Rate.
