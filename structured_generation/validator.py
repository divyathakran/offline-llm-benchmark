import json
from structured_generation.schema import StructuredResponse


def validate_output(response_text):

    try:
        data = json.loads(response_text)

        validated = StructuredResponse(**data)

        return validated

    except Exception:
        return None