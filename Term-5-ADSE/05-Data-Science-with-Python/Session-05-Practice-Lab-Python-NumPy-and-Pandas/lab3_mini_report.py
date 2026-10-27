# lab3_mini_report.py - Lab 3: turn the analysis into a saved report
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("cricket_scores.csv")

# Boundary runs: 4 runs per four, 6 runs per six
df["boundary_runs"] = df["fours"] * 4 + df["sixes"] * 6

# Per-player report
report = df.groupby("player")[["runs", "balls", "boundary_runs"]].sum()
report["strike_rate"] = (report["runs"] / report["balls"] * 100).round(1)
report["boundary_pct"] = (report["boundary_runs"] / report["runs"] * 100).round(1)
print(report)

# Save the report as CSV
report.to_csv("player_report.csv")
print("\nSaved player_report.csv")

# Save a chart of total runs
report["runs"].sort_values().plot(kind="barh", color="green",
                                  title="Total runs in 3 matches")
plt.xlabel("Runs")
plt.tight_layout()
plt.savefig("player_runs.png")
print("Saved player_runs.png")
