import subprocess
import sys
from pathlib import Path
import shutil


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLI_PATH = PROJECT_ROOT / "app" / "main.py"
CONFIG_PATH = PROJECT_ROOT / "app" / "config" / "default.json"


def run_cli(args, cwd):
    return subprocess.run(
        [sys.executable, str(CLI_PATH), *args],
        cwd=cwd,
        capture_output=True,
        text=True,
    )


def test_cli_invalid_mode_exit_code(tmp_path):
    result = run_cli(
        ["--mode", "invalid", "--problem", "Valid problem statement", "--config", str(CONFIG_PATH)],
        cwd=tmp_path,
    )
    assert result.returncode == 2
    assert "invalid" in result.stderr.lower()


def test_cli_missing_problem_exit_code(tmp_path):
    result = run_cli(["--mode", "analyst", "--config", str(CONFIG_PATH)], cwd=tmp_path)
    assert result.returncode == 2
    assert "--problem" in result.stderr


def test_cli_valid_analyst_run(tmp_path):
    templates_src = PROJECT_ROOT / "app" / "templates"
    templates_dest = tmp_path / "app" / "templates"
    templates_dest.mkdir(parents=True, exist_ok=True)
    for template in templates_src.iterdir():
        shutil.copy(template, templates_dest / template.name)

    result = run_cli(
        [
            "--mode",
            "analyst",
            "--problem",
            "Delivery productivity is down and timelines are slipping",
            "--config",
            str(CONFIG_PATH),
        ],
        cwd=tmp_path,
    )
    assert result.returncode == 0
    output_path = tmp_path / "projects" / "project_001_performance_gap_analysis" / "outputs" / "analyst_report.md"
    assert output_path.exists()
