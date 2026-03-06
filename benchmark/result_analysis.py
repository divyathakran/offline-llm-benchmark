import csv
from collections import defaultdict

INPUT_FILE = "results\benchmark_results_cpu.csv" #run for bot cpu and gpu

data = defaultdict(lambda: {
    "ttft": [],
    "tps": [],
    "latency": [],
    "tokens": []
})

with open(INPUT_FILE, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        model = row["model"]

        data[model]["ttft"].append(float(row["ttft_sec"]))
        data[model]["tps"].append(float(row["tokens_per_sec"]))
        data[model]["latency"].append(float(row["total_latency_sec"]))
        data[model]["tokens"].append(float(row["tokens_generated"]))

print("\nMODEL PERFORMANCE SUMMARY\n")

print(f"{'Model':15} {'Avg TTFT':10} {'Tokens/sec':12} {'Avg Latency':12} {'Avg Tokens'}")
print("-" * 65)

for model, values in data.items():

    avg_ttft = sum(values["ttft"]) / len(values["ttft"])
    avg_tps = sum(values["tps"]) / len(values["tps"])
    avg_latency = sum(values["latency"]) / len(values["latency"])
    avg_tokens = sum(values["tokens"]) / len(values["tokens"])

    print(f"{model:15} {avg_ttft:<10.3f} {avg_tps:<12.2f} {avg_latency:<12.3f} {avg_tokens:.1f}")