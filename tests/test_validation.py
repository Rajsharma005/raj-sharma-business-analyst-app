import pytest

from app.utils.errors import ValidationError
from app.utils.validate import (
    validate_file_path,
    validate_mode,
    validate_non_empty,
)


def test_validate_mode_accepts_valid():
    assert validate_mode("analyst", ["analyst", "executive"]) == "analyst"


def test_validate_mode_rejects_invalid():
    with pytest.raises(ValidationError):
        validate_mode("invalid", ["analyst", "executive"])


def test_validate_non_empty_rejects_empty():
    with pytest.raises(ValidationError):
        validate_non_empty("Problem", "")


def test_validate_non_empty_rejects_short():
    with pytest.raises(ValidationError):
        validate_non_empty("Problem", "abc", min_len=5)


def test_validate_non_empty_accepts_valid():
    assert validate_non_empty("Problem", "Valid problem statement") == "Valid problem statement"


def test_validate_file_path_allows_none():
    assert validate_file_path("Config", None) is None


def test_validate_file_path_rejects_missing():
    with pytest.raises(ValidationError):
        validate_file_path("Config", "does/not/exist.json")


def test_validate_file_path_accepts_existing(tmp_path):
    file_path = tmp_path / "config.json"
    file_path.write_text("{}", encoding="utf-8")
    assert validate_file_path("Config", str(file_path)) == str(file_path)
