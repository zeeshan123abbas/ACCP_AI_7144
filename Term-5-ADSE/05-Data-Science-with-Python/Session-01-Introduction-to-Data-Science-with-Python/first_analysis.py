# first_analysis.py - a tiny end-to-end data science workflow
# Question: "Do students who study more hours score higher?"

import pandas as pd
import matplotlib
matplotlib.use("Agg")            # draw to a file (works without a screen)
import matplotlib.pyplot as plt

# Step 1: collect data (here we type it in)
data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "score": [45, 50, 58, 62, 70, 74, 81, 88],
}

# Step 2: put it in a table (DataFrame)
df = pd.DataFrame(data)
print(df)

# Step 3: explore with simple statistics
print("\nAverage score:", df["score"].mean())
print("Correlation hours vs score:", round(df["hours"].corr(df["score"]), 3))

# Step 4: visualise
plt.scatter(df["hours"], df["score"], color="teal")
plt.title("Study hours vs exam score")
plt.xlabel("Hours studied per day")
plt.ylabel("Score")
plt.savefig("hours_vs_score.png")
print("\nChart saved as hours_vs_score.png")

# Step 5: communicate the insight
print("Insight: more study hours go with higher scores (strong positive correlation).")
