# Business Analyst Decision Engine (CLI)

A production-ready, portfolio-grade CLI that converts ambiguous business problems into:
1) structured analysis,  
2) executive summaries, and  
3) portfolio-ready case narratives.

## Why this exists
Most analytics projects stop at charts. This tool demonstrates **decision engineering**:
- problem taxonomy → domain mapping → KPI selection → hypothesis tree → recommendations
- output formats aligned to stakeholder needs (analyst / executive / portfolio)

## Features
- Domain-agnostic problem classification (growth, churn, cost, risk, efficiency, etc.)
- Context-aware domain + KPI mapping (with confidence + rationale)
- Hypothesis generation with confounders + test methods
- Recommendation engine with prioritization (impact vs effort) + owners + risks
- 3 stakeholder modes:
  - `analyst` → structured diagnostic report
  - `executive` → C-suite style 1-pager
  - `portfolio` → interview/storytelling narrative
- Production hardening: validation, clean errors, templates, config system
- Tests: pytest coverage for CLI validation and behavior
- Packaging: installable CLI (`ba-engine`) + version flag + license + changelog

## Quickstart

### Run locally (repo)
```bash
python app/main.py --mode analyst \
  --problem "Delivery productivity is down and timelines are slipping" \
  --context "Service-based project delivery" \
  --industry "Professional services"
```

## Configuration & Templates

Run with a custom config file:

```bash
python app/main.py --mode executive --problem "..." --config app/config/default.json
```

Templates live in `app/templates/` and can be edited to change output style for each mode.

## Error Handling

Exit codes:
- `0` success
- `1` unexpected runtime error
- `2` input validation error
- `3` config error

Use `--verbose` to include short details for unexpected errors.

Example validation errors:

```bash
python app/main.py --mode analyst --problem "Hi"
```

```bash
python app/main.py --mode executive --problem "Valid problem statement" --config app/config/missing.json
```

## Testing

Install dev dependency:

```bash
pip install pytest
```

Run tests:

```bash
pytest
```

Coverage includes CLI validation, error handling, exit codes, and a happy-path CLI run.

## Installation

```bash
pip install -e .
```

## Usage

```bash
ba-engine --mode analyst --problem "Delivery productivity is down and timelines are slipping"
```

## Development Workflow

```bash
pip install -e .
pytest
ba-engine --help
ba-engine --mode analyst --problem "Delivery productivity is down and timelines are slipping"
```

## Local Validation (Documented)
- `pip install -e .`
- `ba-engine --help`
- `ba-engine --mode analyst --problem "Delivery productivity is down and timelines are slipping"`
