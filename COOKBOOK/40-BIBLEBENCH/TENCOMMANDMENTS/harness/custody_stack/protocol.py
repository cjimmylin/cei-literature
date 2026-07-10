"""Strict single-action response protocol."""

from .schema import Action, CustodyError, SchemaValidationError, strict_json_loads


class ProtocolError(CustodyError, ValueError):
    """Raised when a model response is not exactly one valid action object."""


def parse_action(raw_response):
    """Parse exactly ``kind``, ``tool`` and ``arguments`` from one JSON object."""

    try:
        decoded = strict_json_loads(raw_response)
        if type(decoded) is not dict:
            raise SchemaValidationError("action response must be a JSON object")
        return Action.from_dict(decoded)
    except SchemaValidationError as exc:
        raise ProtocolError(str(exc)) from exc


__all__ = ["ProtocolError", "parse_action"]
