import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import ollama
from structured_generation.retry_logic import generate_with_retry
from structured_generation.generator import generate_structured


MODEL = [
    "llama3.2:1b",
    "phi3",
    "mistral",
    "llama3.1:8b"
]

PROMPT = [
    "Explain machine learning in simple terms.",
    "Explain neural networks.",
    "What is cloud computing?"
]


STRUCTURED_PROMPT = """
Answer the question and return ONLY valid JSON.

Format:
{
 "topic": "string",
 "summary": "string",
 "confidence": number between 0 and 1
}

Question:
{}
"""


def test_model(model, temperature):

    success = 0
    total = len(PROMPT)

    for p in PROMPT:

        prompt = f"{STRUCTURED_PROMPT}\nQuestion:\n{p}"

        result = generate_with_retry(
            lambda x: generate_structured(model, x, temperature),
            prompt
        )

        if result:
            success += 1

    return success, total


def main():

    for model in MODEL:

        print(f"\nTesting {model}")

        for temp in [0, 0.7]:

            success, total = test_model(model, temp)

            print(
                f"Temperature {temp} → JSON success rate: {success}/{total}"
            )


if __name__ == "__main__":
    main()