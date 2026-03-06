import time
import ollama
import csv

# Models to benchmark
MODEL = [
    "llama3.2:1b",
    "phi3",
    "mistral",
    "llama3.1:8b"
]

# Standardised prompt set (30 prompts taken from AI itself)
PROMPT = [
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

OUTPUT_FILE = "benchmark_results_cpu.csv"

def benchmark_model(model,prompt):
    token_count = 0
    first_token_time=None

    start_time= time.time()

    stream = ollama.chat(
        model=model,
        messages= [{"role":"user","content":prompt}],
        stream = True
    )

    for chunk in stream:
        if first_token_time is None:
            first_token_time = time.time()
        token = chunk["message"]["content"]
        token_count +=1

    end_time = time.time()

    ttft = first_token_time - start_time
    generation_time = end_time - first_token_time
    total_latency = end_time - start_time

    tokens_per_second = token_count / generation_time if generation_time > 0 else 0

    return ttft, tokens_per_second, total_latency, token_count

def main():
    results = []

    print("\nStarting benchmark...\n")

    for model in MODEL:
        print(f"\nTesting model: {model}\n")

        for i, prompt in enumerate(PROMPT):
            print(f"Prompt {i+1}/{len(PROMPT)}")

            ttft, tps, latency, tokens = benchmark_model(model, prompt)

            results.append({
                "model": model,
                "prompt_id": i + 1,
                "ttft_sec": round(ttft, 3),
                "tokens_per_sec": round(tps, 3),
                "total_latency_sec": round(latency, 3),
                "tokens_generated": tokens
            })

    print("\nWriting results to CSV...\n")

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "model",
            "prompt_id",
            "ttft_sec",
            "tokens_per_sec",
            "total_latency_sec",
            "tokens_generated"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in results:
            writer.writerow(row)

    print("Benchmark complete.")
    print(f"Results saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()