import os
import pandas as pd
import matplotlib.pyplot as plt

# Ensure results folder exists
os.makedirs("results", exist_ok=True)

# Load benchmark summary
df = pd.read_csv("results/performance_summary_phase3_gpu.csv")

models = df["model"]
tokens_per_sec = df["avg_tokens_per_sec"]
latency = df["avg_latency_sec"]

# -----------------------------
# Throughput Comparison
# -----------------------------
plt.figure()

plt.bar(models, tokens_per_sec)

plt.title("Model Throughput Comparison (GPU)")
plt.xlabel("Model")
plt.ylabel("Tokens per Second")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("results/tokens_per_sec_comparison_gpu.png")

print("Saved: results/tokens_per_sec_comparison_gpu.png")


# -----------------------------
# Latency Comparison
# -----------------------------
plt.figure()

plt.bar(models, latency)

plt.title("Model Latency Comparison (GPU)")
plt.xlabel("Model")
plt.ylabel("Average Latency (seconds)")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("results/latency_comparison_gpu.png")

print("Saved: results/latency_comparison_gpu.png")


plt.show()