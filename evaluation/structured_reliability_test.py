import sys
import os
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from structured_generation.retry_logic import generate_with_retry
from structured_generation.generator import generate_structured


MODELS = [
    "llama3.2:1b",
    "phi3",
    "mistral",
    "llama3.1:8b"
]

PROMPTS = [
    "Explain machine learning in simple terms.",
    "What is the difference between AI and machine learning?",
    "Write a short paragraph about climate change.",
    "Explain the concept of recursion.",
    "What is a neural network?",
    "Explain overfitting in machine learning.",
    "Write a haiku about technology.",
    "What is Python used for?",
    "Explain blockchain in simple terms.",
    "Describe how the internet works.",
    "What are the advantages of renewable energy?",
    "Explain the concept of gravity.",
    "Write a short story about a robot.",
    "What is a database?",
    "Explain the importance of cybersecurity.",
    "What is cloud computing?",
    "Describe the water cycle.",
    "Explain object-oriented programming.",
    "What is a REST API?",
    "Explain the concept of supply and demand.",
    "What is a data structure?",
    "Describe photosynthesis.",
    "Explain the difference between RAM and storage.",
    "What is the purpose of an operating system?",
    "Explain reinforcement learning.",
    "Write a motivational quote.",
    "Explain the role of GPUs in AI.",
    "What is a compiler?",
    "Describe the process of evolution.",
    "Explain the concept of entropy."
]


STRUCTURED_PROMPT = """
Answer the question and return ONLY valid JSON.

Format:
{{
 "topic": "string",
 "summary": "string",
 "confidence": number between 0 and 1
}}

Question:
{}
"""

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_FILE = os.path.join(BASE_DIR, "results", "json_reliability_phase3.csv")


def test_model(model, temperature):

    success = 0
    results = []

    for i, p in enumerate(PROMPTS, start=1):

        prompt = STRUCTURED_PROMPT.format(p)

        result = generate_with_retry(
            lambda x: generate_structured(model, x, temperature),
            prompt
        )

        valid = 1 if result else 0
        success += valid

        results.append({
            "model": model,
            "prompt_id": i,
            "temperature": temperature,
            "json_valid": valid
        })

    print(f"Temperature {temperature} → JSON success rate: {success}/{len(PROMPTS)}")

    return results


def main():

    os.makedirs(os.path.join(BASE_DIR, "results"), exist_ok=True)

    print("Saving results to:", OUTPUT_FILE)

    all_results = []

    for model in MODELS:

        print(f"\nTesting {model}")

        for temp in [0, 0.7]:

            results = test_model(model, temp)
            all_results.extend(results)

    with open(OUTPUT_FILE, "w", newline="") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=["model", "prompt_id", "temperature", "json_valid"]
        )

        writer.writeheader()
        writer.writerows(all_results)

    print("\nResults saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    main()