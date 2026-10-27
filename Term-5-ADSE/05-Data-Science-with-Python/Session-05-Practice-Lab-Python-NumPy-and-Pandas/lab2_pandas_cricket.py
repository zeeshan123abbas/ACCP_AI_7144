# lab2_pandas_cricket.py - Lab 2: explore and summarise cricket scores with pandas
import pandas as pd

df = pd.read_csv("cricket_scores.csv", parse_dates=["date"])

# Task 1: explore
print("Shape:", df.shape)
print(df.head(4))

# Task 2: new column - strike rate = runs per 100 balls
df["strike_rate"] = (df["runs"] / df["balls"] * 100).round(1)

# Task 3: filter - innings of 50 or more runs
fifties = df[df["runs"] >= 50]
print("\nFifty-plus innings:\n", fifties[["match", "player", "runs"]])

# Task 4: player summary with groupby + agg
summary = df.groupby("player").agg(
    total_runs=("runs", "sum"),
    average=("runs", "mean"),
    best=("runs", "max"),
    sixes=("sixes", "sum"),
).sort_values("total_runs", ascending=False)
print("\nPlayer summary:\n", summary.round(1))

# Task 5: team total per match
team_match = df.groupby(["match", "team"])["runs"].sum()
print("\nTeam runs per match:\n", team_match)

# Task 6: use loc to read one value
print("\nBabar's best score:", summary.loc["Babar", "best"])
