from app.utils.errors import (
    AppError,
    ConfigError,
    RuntimeAppError,
    ValidationError,
    format_error,
)


def test_error_codes():
    assert ValidationError("bad").code == 2
    assert ConfigError("bad").code == 3
    assert RuntimeAppError("bad").code == 1


def test_format_error_output():
    err = AppError(9, "Something went wrong")
    message = format_error(err)
    assert "Error (code 9)" in message
    assert "Something went wrong" in message
