"""
Runtime orchestrator for the Business Analyst Engine.
Runs the end-to-end flow: classify -> map domain -> map KPIs -> hypotheses -> recommendations.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable

from app.engine.domain_mapper import map_domain
from app.engine.hypothesis_generator import generate_hypotheses
from app.engine.kpi_mapper import map_kpis
from app.engine.problem_classifier import classify_problem
from app.engine.recommendation_engine import generate_recommendations
from app.utils.errors import ConfigError


def _get_config_section(config: Dict[str, object], key: str, default: object) -> object:
    value = config.get(key)
    return value if value is not None else default


def _format_list(items: Iterable[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def _format_kpis(kpis: Iterable[Dict[str, str]]) -> str:
    lines = []
    for kpi in kpis:
        lines.append(f"- **{kpi.get('name', 'KPI')}**: {kpi.get('definition', '')}")
        if kpi.get("why_it_matters"):
            lines.append(f"  - Why it matters: {kpi['why_it_matters']}")
    return "\n".join(lines)


def run_engine(
    problem_statement: str,
    context: str | None = None,
    industry: str | None = None,
    config: Dict[str, object] | None = None,
) -> Dict[str, object]:
    combined = " ".join(
        part for part in [problem_statement, context or "", industry or ""] if part
    ).strip()

    config = config or {}
    classification = classify_problem(combined)
    domain_context = map_domain(combined, classification)
    kpi_map = map_kpis(classification, domain_context)
    hypotheses = generate_hypotheses(classification, domain_context, kpi_map)
    recommendations = generate_recommendations(hypotheses, domain_context)

    return {
        "problem_statement": problem_statement,
        "context": context,
        "industry": industry,
        "classification": classification,
        "domain_context": domain_context,
        "kpi_map": kpi_map,
        "hypotheses": hypotheses,
        "recommendations": recommendations,
        "config": config,
    }


def _build_sections(payload: Dict[str, object], config: Dict[str, object]) -> Dict[str, str]:
    classification = payload["classification"]
    domain_context = payload["domain_context"]
    kpi_map = payload["kpi_map"]
    hypotheses = payload["hypotheses"]
    recommendations = payload["recommendations"]

    hypotheses_lines = []
    for idx, hypothesis in enumerate(hypotheses.get("primary_hypotheses", []), start=1):
        hypotheses_lines.extend(
            [
                f"### H{idx}. {hypothesis['statement']}",
                f"- Rationale: {hypothesis['rationale']}",
                f"- Related KPIs: {', '.join(hypothesis['related_kpis'])}",
                f"- Expected direction: {hypothesis['expected_direction']}",
                f"- Data needed: {', '.join(hypothesis['data_needed'])}",
                f"- Test method: {hypothesis['test_method']}",
                "- Potential confounders: scope changes, client-driven variability, data quality gaps",
                f"- Risk if wrong: {hypothesis['risk_if_wrong']}",
                "",
            ]
        )

    quick_wins = []
    for rec in recommendations.get("quick_wins", []):
        quick_wins.extend(
            [
                f"- {rec['action_statement']} (Owner: {rec['implementation_owner']}, Priority: {rec['priority_rank']})",
                f"  - Impact: {rec['expected_business_impact']}",
                f"  - Effort: {rec['estimated_effort']} | Timeframe: {rec['estimated_timeframe']}",
            ]
        )

    strategic_bets = []
    for rec in recommendations.get("strategic_bets", []):
        strategic_bets.extend(
            [
                f"- {rec['action_statement']} (Owner: {rec['implementation_owner']}, Priority: {rec['priority_rank']})",
                f"  - Impact: {rec['expected_business_impact']}",
                f"  - Effort: {rec['estimated_effort']} | Timeframe: {rec['estimated_timeframe']}",
            ]
        )

    priorities = []
    for rec in recommendations.get("quick_wins", []):
        priorities.append(f"- P1: {rec['action_statement']} (Owner: {rec['implementation_owner']})")
    for rec in recommendations.get("strategic_bets", []):
        priorities.append(f"- P2: {rec['action_statement']} (Owner: {rec['implementation_owner']})")
    if recommendations.get("risk_mitigation_actions"):
        p3 = recommendations["risk_mitigation_actions"][0]
        priorities.append(f"- P3: {p3['action_statement']} (Owner: {p3['implementation_owner']})")

    return {
        "problem_statement": payload["problem_statement"],
        "context": payload.get("context") or "Not provided",
        "industry": payload.get("industry") or "Not provided",
        "primary_category": classification.get("primary_category"),
        "secondary_subcategory": classification.get("secondary_subcategory"),
        "problem_nature": classification.get("problem_nature"),
        "domain": domain_context.get("domain"),
        "subdomain": domain_context.get("subdomain"),
        "context_tags": ", ".join(domain_context.get("context_tags", [])),
        "primary_kpis": _format_kpis(kpi_map.get("primary_kpis", [])),
        "secondary_kpis": _format_kpis(kpi_map.get("secondary_kpis", [])),
        "hypotheses": "\n".join(hypotheses_lines).strip(),
        "quick_wins": "\n".join(quick_wins).strip(),
        "strategic_bets": "\n".join(strategic_bets).strip(),
        "executive_priorities": "\n".join(priorities).strip(),
        "portfolio_resume_bullets": _format_list(
            [
                f"Delivered a quick-win initiative: {rec['action_statement']} (Owner: {rec['implementation_owner']})."
                for rec in recommendations.get("quick_wins", [])
            ]
        ),
    }


def _load_template(path: Path) -> str:
    if not path.exists():
        raise ConfigError(f"Template file not found: {path}")
    return path.read_text(encoding="utf-8")


def render_output(mode: str, payload: Dict[str, object], config: Dict[str, object]) -> tuple[str, str]:
    templates_dir = Path("app/templates")
    template_map = {
        "analyst": templates_dir / "analyst.md",
        "executive": templates_dir / "executive.md",
        "portfolio": templates_dir / "portfolio.md",
    }
    filename_map = {
        "analyst": "analyst_report.md",
        "executive": "executive_summary.md",
        "portfolio": "portfolio_story.md",
    }

    template_path = template_map[mode]
    template = _load_template(template_path)
    sections = _build_sections(payload, config)

    output_settings = _get_config_section(config, "output_settings", {})
    include_sections = output_settings.get("include_sections", {}).get(mode, {})

    if include_sections:
        for key, enabled in include_sections.items():
            if not enabled and key in sections:
                sections[key] = ""

    content = template.format(**sections)
    return content.strip() + "\n", filename_map[mode]


def validate_config(config: Dict[str, object]) -> None:
    required_keys = ["domain_taxonomy", "keyword_hints", "kpi_library", "output_settings"]
    for key in required_keys:
        if key not in config:
            raise ConfigError(f"Config file is invalid: missing key '{key}'.")
