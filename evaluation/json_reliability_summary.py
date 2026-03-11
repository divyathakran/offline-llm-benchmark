import pandas as pd

df = pd.read_csv("results/json_reliability_phase3.csv")

summary = (
    df.groupby(["model", "temperature"])["json_valid"]
    .mean()
    .reset_index()
)

summary["json_success_rate"] = summary["json_valid"] * 100
summary = summary.drop(columns=["json_valid"])

summary.to_csv(
    "results/json_reliability_summary.csv",
    index=False
)

print(summary)
print("\nSaved to results/json_reliability_summary.csv")