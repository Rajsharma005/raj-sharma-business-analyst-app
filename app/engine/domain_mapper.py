"""
Domain Mapping Engine (Domain-Agnostic)
--------------------------------------
This module maps a classified business problem + original statement to a likely
industry domain, subdomain, and context tags. It is intentionally heuristic
and interview-ready: simple, explainable, and easy to extend.

Why this matters:
- Domain mapping anchors KPI selection and benchmarking (e.g., churn in SaaS vs.
  churn in telecom uses different KPIs and data sources).
- Subdomain mapping helps align stakeholders, data systems, and operational
  process owners (e.g., payments vs. lending vs. collections).
- Context tags (B2B/B2C, regulated, subscription) guide hypothesis design and
  recommendation constraints.
"""

from __future__ import annotations

from typing import Dict, List

# Practical taxonomy of domains and subdomains used by BAs across industries.
DOMAIN_TAXONOMY = {
    "banking_finance": {
        "keywords": ["bank", "lending", "loan", "credit", "collections", "fintech"],
        "subdomains": {
            "lending_collections": ["loan", "delinquency", "collections"],
            "payments": ["payment", "transfer", "settlement"],
            "risk_compliance": ["risk", "fraud", "kyc", "aml"],
        },
    },
    "retail_ecommerce": {
        "keywords": ["retail", "store", "ecommerce", "cart", "checkout", "sku"],
        "subdomains": {
            "merchandising": ["assortment", "sku", "inventory"],
            "fulfillment": ["order", "shipping", "delivery"],
            "customer_support": ["returns", "refund", "support"],
        },
    },
    "saas_tech": {
        "keywords": ["saas", "subscription", "product", "platform", "user"],
        "subdomains": {
            "product_growth": ["activation", "adoption", "usage"],
            "customer_success": ["renewal", "retention", "csat"],
            "sales_ops": ["pipeline", "lead", "crm"],
        },
    },
    "telecom": {
        "keywords": ["telecom", "network", "mobile", "broadband", "carrier"],
        "subdomains": {
            "network_operations": ["outage", "latency", "coverage"],
            "billing": ["invoice", "bill", "charge"],
            "customer_retention": ["churn", "port-out", "retention"],
        },
    },
    "manufacturing": {
        "keywords": ["manufacturing", "plant", "production", "factory", "yield"],
        "subdomains": {
            "production_ops": ["throughput", "oee", "line"],
            "quality": ["defect", "scrap", "rework"],
            "supply_chain": ["supplier", "procurement", "inventory"],
        },
    },
    "healthcare": {
        "keywords": ["healthcare", "hospital", "patient", "clinic", "provider"],
        "subdomains": {
            "clinical_ops": ["patient", "care", "admission"],
            "revenue_cycle": ["claim", "billing", "denial"],
            "compliance": ["hipaa", "audit", "regulatory"],
        },
    },
    "logistics": {
        "keywords": ["logistics", "shipment", "warehouse", "delivery", "fleet"],
        "subdomains": {
            "warehouse_ops": ["warehouse", "pick", "pack"],
            "transportation": ["fleet", "route", "last mile"],
            "order_fulfillment": ["fulfillment", "sla", "delivery"],
        },
    },
    "education": {
        "keywords": ["education", "edtech", "student", "course", "learning"],
        "subdomains": {
            "student_success": ["completion", "retention", "engagement"],
            "content_delivery": ["course", "content", "curriculum"],
            "operations": ["enrollment", "admissions"],
        },
    },
    "hospitality": {
        "keywords": ["hotel", "hospitality", "booking", "guest", "occupancy"],
        "subdomains": {
            "reservations": ["booking", "occupancy", "rate"],
            "guest_experience": ["review", "service", "nps"],
            "operations": ["housekeeping", "staffing"],
        },
    },
}


def _match_subdomain(statement: str, subdomains: Dict[str, List[str]]) -> str:
    for subdomain, keywords in subdomains.items():
        if any(keyword in statement for keyword in keywords):
            return subdomain
    return "general"


def _infer_context_tags(statement: str, classification: Dict[str, str]) -> List[str]:
    tags = []
    if any(term in statement for term in ["b2b", "enterprise", "client"]):
        tags.append("b2b")
    if any(term in statement for term in ["consumer", "b2c", "retail"]):
        tags.append("b2c")
    if any(term in statement for term in ["subscription", "renewal", "saas"]):
        tags.append("subscription")
    if any(term in statement for term in ["transaction", "checkout", "payment"]):
        tags.append("transactional")
    if any(term in statement for term in ["online", "digital", "app", "web"]):
        tags.append("online")
    if any(term in statement for term in ["store", "branch", "offline"]):
        tags.append("offline")
    if classification.get("primary_category") in {"risk", "compliance"}:
        tags.append("regulated")
    if classification.get("primary_category") in {"growth", "revenue"}:
        tags.append("growth_phase")
    if classification.get("primary_category") in {"cost", "efficiency"}:
        tags.append("stability_phase")
    return tags or ["unknown_context"]


def map_domain(problem_statement: str, classification: Dict[str, str]) -> Dict[str, object]:
    """
    Map a problem statement + classification output to domain, subdomain, and
    context tags. Returns a structured dictionary for downstream analytics.
    """
    normalized = problem_statement.strip().lower()
    assumptions = []
    clarifying_questions = []

    domain = "general_business"
    subdomain = "general"
    confidence = 0.3

    for domain_name, meta in DOMAIN_TAXONOMY.items():
        if any(keyword in normalized for keyword in meta["keywords"]):
            domain = domain_name
            subdomain = _match_subdomain(normalized, meta["subdomains"])
            confidence = 0.75 if subdomain != "general" else 0.6
            break

    # Use classification signals to adjust confidence and assumptions.
    if domain == "general_business":
        assumptions.append("Assumed no explicit industry markers in the statement.")
        clarifying_questions.append(
            "Which industry or business domain does this problem belong to?"
        )
    if classification.get("primary_category") in {"risk", "compliance"}:
        confidence = max(confidence, 0.6)

    context_tags = _infer_context_tags(normalized, classification)

    if confidence < 0.5:
        clarifying_questions.extend(
            [
                "Is the business model primarily subscription or transactional?",
                "Is this a B2B or B2C context?",
            ]
        )

    return {
        "domain": domain,
        "subdomain": subdomain,
        "context_tags": context_tags,
        "assumptions": assumptions,
        "clarifying_questions": clarifying_questions,
        "confidence": round(confidence, 2),
    }


# Examples:
# 1) Statement: "Churn is rising for SMB customers on our SaaS platform."
#    Classification: {"primary_category": "churn"}
#    Expected => {
#      "domain": "saas_tech",
#      "subdomain": "customer_success",
#      "context_tags": ["subscription", "b2b", "growth_phase"],
#      "assumptions": [],
#      "clarifying_questions": [],
#      "confidence": 0.75
#    }
#
# 2) Statement: "Delivery delays are hurting our last-mile SLAs in urban areas."
#    Classification: {"primary_category": "efficiency"}
#    Expected => {
#      "domain": "logistics",
#      "subdomain": "order_fulfillment",
#      "context_tags": ["stability_phase"],
#      "assumptions": [],
#      "clarifying_questions": [],
#      "confidence": 0.75
#    }
#
# 3) Statement: "Audit findings show KYC gaps in loan onboarding."
#    Classification: {"primary_category": "compliance"}
#    Expected => {
#      "domain": "banking_finance",
#      "subdomain": "risk_compliance",
#      "context_tags": ["regulated", "stability_phase"],
#      "assumptions": [],
#      "clarifying_questions": [],
#      "confidence": 0.75
#    }
