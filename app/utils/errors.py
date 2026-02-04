"""Error types and formatting for CLI validation and runtime handling."""

from __future__ import annotations


class AppError(Exception):
    def __init__(self, code: int, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


class ValidationError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(2, message)


class ConfigError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(3, message)


class RuntimeAppError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(1, message)


def format_error(err: AppError) -> str:
    return f"Error (code {err.code}): {err.message}"
