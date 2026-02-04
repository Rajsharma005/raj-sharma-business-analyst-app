"""Validation helpers for CLI inputs."""

from __future__ import annotations

from pathlib import Path

from app.utils.errors import ValidationError


def validate_mode(mode: str, allowed: list[str]) -> str:
    if mode not in allowed:
        raise ValidationError(
            f"Invalid mode '{mode}'. Allowed values: {', '.join(allowed)}."
        )
    return mode


def validate_non_empty(label: str, value: str, min_len: int = 5) -> str:
    if value is None or not value.strip():
        raise ValidationError(f"{label} is required.")
    if len(value.strip()) < min_len:
        raise ValidationError(f"{label} must be at least {min_len} characters.")
    return value.strip()


def validate_optional_text(
    label: str, value: str | None, max_len: int = 500
) -> str | None:
    if value is None:
        return None
    if len(value.strip()) > max_len:
        raise ValidationError(f"{label} must be {max_len} characters or fewer.")
    return value.strip() or None


def validate_file_path(label: str, path: str | None) -> str | None:
    if path is None:
        return None
    candidate = Path(path)
    if not candidate.exists():
        raise ValidationError(f"{label} does not exist: {candidate}")
    if not candidate.is_file():
        raise ValidationError(f"{label} must be a file: {candidate}")
    return str(candidate)
