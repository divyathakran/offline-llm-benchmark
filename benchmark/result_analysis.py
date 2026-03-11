import csv
from collections import defaultdict

# CHANGE THIS depending on experiment
INPUT_FILE = "results/benchmark_results_phase3_gpu.csv"
OUTPUT_FILE = "results/performance_summary_phase3_gpu.csv"

data = defaultdict(lambda: {
    "ttft": [],
    "tps": [],
    "latency": [],
    "tokens": []
})

with open(INPUT_FILE, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:

        # Skip cold start prompt
        if int(row["prompt_id"]) == 1:
            continue

        model = row["model"]

        data[model]["ttft"].append(float(row["ttft_sec"]))
        data[model]["tps"].append(float(row["tokens_per_sec"]))
        data[model]["latency"].append(float(row["total_latency_sec"]))
        data[model]["tokens"].append(float(row["tokens_generated"]))

print("\nMODEL PERFORMANCE SUMMARY\n")

print(f"{'Model':15} {'Avg TTFT':10} {'Tokens/sec':12} {'Avg Latency':12} {'Avg Tokens'}")
print("-" * 65)

summary_rows = []

for model, values in data.items():

    avg_ttft = sum(values["ttft"]) / len(values["ttft"])
    avg_tps = sum(values["tps"]) / len(values["tps"])
    avg_latency = sum(values["latency"]) / len(values["latency"])
    avg_tokens = sum(values["tokens"]) / len(values["tokens"])

    print(f"{model:15} {avg_ttft:<10.3f} {avg_tps:<12.2f} {avg_latency:<12.3f} {avg_tokens:.1f}")

    summary_rows.append({
        "model": model,
        "avg_ttft_sec": round(avg_ttft, 3),
        "avg_tokens_per_sec": round(avg_tps, 2),
        "avg_latency_sec": round(avg_latency, 3),
        "avg_tokens_generated": round(avg_tokens, 1)
    })


# Save summary CSV
with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=summary_rows[0].keys())
    writer.writeheader()
    writer.writerows(summary_rows)

print(f"\nSummary saved to: {OUTPUT_FILE}")