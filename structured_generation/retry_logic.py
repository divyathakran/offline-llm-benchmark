from structured_generation.validator import validate_output


def generate_with_retry(generate_fn, prompt, retries=1):

    for attempt in range(retries + 1):

        response = generate_fn(prompt)

        validated = validate_output(response)

        if validated:
            return validated

        print("Invalid JSON output. Retrying...")

    return None