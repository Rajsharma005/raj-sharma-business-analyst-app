"""CLI entrypoint for the Business Analyst Engine."""

from __future__ import annotations

import argparse
import json
import os
import sys
from importlib import metadata
from pathlib import Path

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app.engine.runtime import (
    render_output,
    run_engine,
    validate_config,
)
from app.utils.errors import (
    AppError,
    ConfigError,
    RuntimeAppError,
    ValidationError,
    format_error,
)
from app.utils.validate import (
    validate_file_path,
    validate_mode,
    validate_non_empty,
    validate_optional_text,
)


def build_parser() -> argparse.ArgumentParser:
    description = (
        "Business Analyst Decision Engine CLI for structured problem intake, "
        "analysis framing, and executive-ready outputs."
    )
    epilog = (
        "Examples:\n"
        "  ba-engine --mode analyst --problem \"Delivery productivity is down\"\n"
        "  ba-engine --mode executive --problem \"Churn is rising\" --industry \"Telecom\""
    )
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"ba-engine {get_version()}",
    )

    required = parser.add_argument_group("Required arguments")
    required.add_argument(
        "--mode",
        required=True,
        choices=["analyst", "executive", "portfolio"],
        help="Output mode",
    )
    required.add_argument(
        "--problem",
        required=True,
        help="Free-text business problem statement",
    )

    optional = parser.add_argument_group("Optional context")
    optional.add_argument("--context", help="Optional business context")
    optional.add_argument("--industry", help="Optional industry")

    config = parser.add_argument_group("Configuration")
    config.add_argument(
        "--config",
        default="app/config/default.json",
        help="Path to config JSON",
    )
    config.add_argument(
        "--verbose",
        action="store_true",
        help="Show details for unexpected errors",
    )
    return parser


def get_version() -> str:
    try:
        return metadata.version("ba-engine")
    except metadata.PackageNotFoundError:
        return "0.1.0"


def write_output(path: str, content: str) -> None:
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(content)
    except OSError as exc:
        raise RuntimeAppError(f"Failed to write output file: {exc}") from exc


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    mode = validate_mode(args.mode, ["analyst", "executive", "portfolio"])
    problem = validate_non_empty("Problem statement", args.problem)
    context = validate_optional_text("Context", args.context)
    industry = validate_optional_text("Industry", args.industry)
    config_path = validate_file_path("Config file", args.config)

    try:
        config = json.loads(Path(config_path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ConfigError(f"Config file is invalid JSON: {exc}") from exc

    validate_config(config)

    payload = run_engine(
        problem,
        context=context,
        industry=industry,
        config=config,
    )

    outputs_dir = os.path.join(
        "projects", "project_001_performance_gap_analysis", "outputs"
    )

    content, filename = render_output(mode, payload, config)
    write_output(os.path.join(outputs_dir, filename), content)

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValidationError, ConfigError, RuntimeAppError) as exc:
        print(format_error(exc), file=sys.stderr)
        sys.exit(exc.code)
    except AppError as exc:
        print(format_error(exc), file=sys.stderr)
        sys.exit(exc.code)
    except Exception as exc:
        message = "Unexpected error occurred. Please retry or report."
        if "--verbose" in sys.argv:
            message = f"{message} Details: {exc}"
        print(message, file=sys.stderr)
        sys.exit(1)
