import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/json_reliability_summary.csv")

models = df["model"]
rates = df["json_success_rate"]

plt.figure()
plt.bar(models, rates)

plt.title("Structured JSON Reliability Across Models")
plt.xlabel("Model")
plt.ylabel("JSON Success Rate (%)")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("results/json_reliability_comparison.png")

plt.show()