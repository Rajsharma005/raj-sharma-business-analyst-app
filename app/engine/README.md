# Engine Layer Architecture

## Purpose
The engine layer serves as the analytical brain of the Business Analyst system. It translates business problems into structured analytical components, aligns them to domains and KPIs, and produces hypothesis- and recommendation-ready outputs that can be used across industries.

## Module Roles
- `problem_classifier.py`: Interprets and categorizes incoming business problems into standardized problem types (e.g., productivity, churn, cost, growth).
- `domain_mapper.py`: Maps the classified problem to the appropriate industry domain(s) and contextualizes domain-specific considerations.
- `kpi_mapper.py`: Identifies the most relevant KPIs and metrics for the problem-domain pairing to guide analysis.
- `hypothesis_generator.py`: Proposes structured, testable hypotheses that explain the observed problem patterns.
- `recommendation_engine.py`: Synthesizes insight-ready themes into practical, prioritized recommendations for decision-makers.

## End-to-End Flow
1. A business problem is submitted to the engine layer.
2. The problem is classified into a standard problem type.
3. The engine maps the problem to the most relevant industry domain context.
4. Core KPIs are surfaced to anchor analysis.
5. Hypotheses are generated to guide data validation and analysis.
6. Recommendations are formed to translate validated insights into actionable decisions.
