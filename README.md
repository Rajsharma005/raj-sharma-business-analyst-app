# Business Analyst Decision Engine

A decision-thinking system that converts ambiguous business problems into
structured analysis, executive insights, and actionable recommendations.

This project demonstrates **how a Business Analyst should think** — not just
how to analyze data.

---

## Why This Project Exists

In real organizations, business problems are rarely clear.
Leaders don’t ask for dashboards — they ask for **decisions**.

Most analytics projects start with data.
This project starts with the **problem**.

The goal of this system is to show how a Business Analyst:
- Frames ambiguous business problems
- Identifies what truly matters (KPIs)
- Generates testable hypotheses
- Translates analysis into executive-ready recommendations

---

## What This App Does (At a Glance)

**Input:**  
A plain-English business problem

**Output:**  
Decision-ready artifacts tailored for different audiences

---

## Core Thinking Engine (How It Thinks)

The system follows a structured Business Analysis workflow:

1. **Problem Classification**
   - Identifies the true nature of the problem (growth, efficiency, risk, churn, etc.)
   - Avoids treating symptoms as root causes

2. **Domain & Context Mapping**
   - Maps the problem to the correct business domain
   - Applies realistic business assumptions

3. **KPI Mapping**
   - Selects decision-relevant KPIs (not vanity metrics)
   - Distinguishes leading vs lagging indicators

4. **Hypothesis Generation**
   - Produces testable, business-driven hypotheses
   - Explicitly states assumptions and risks

5. **Recommendation Engine**
   - Converts insights into prioritized actions
   - Balances impact, effort, and execution risk

---

## App Modes (Three Personas, One Engine)

The same engine powers three distinct outputs:

### 1. Analyst Mode
**Audience:** Business Analyst / Analytics Team  
**Output:**  
- Structured problem breakdown  
- KPI map  
- Hypotheses with testing logic  
- Detailed recommendations  

### 2. Executive Mode
**Audience:** Leadership / CXOs  
**Output:**  
- One-page executive summary  
- Business impact framing  
- Prioritized decisions (P1 / P2 / P3)  

### 3. Portfolio Mode
**Audience:** Hiring Managers / Interviewers  
**Output:**  
- Case story (STAR-style)  
- Resume-ready bullets  
- “Why trust this analyst?” signals  

---

## Example: One-Line Demo Command

```bash
python app/main.py \
  --mode executive \
  --problem "Delivery productivity is declining and project timelines are slipping" \
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
