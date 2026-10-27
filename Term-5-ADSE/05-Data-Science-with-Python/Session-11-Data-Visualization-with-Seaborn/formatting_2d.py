# formatting_2d.py - formatting features that make a 2-D plot professional
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")

# Theme, context and palette change the whole look in one place
sns.set_theme(style="darkgrid", context="talk", palette="muted")

plt.figure(figsize=(9, 6))
ax = sns.scatterplot(data=df, x="attendance", y="marks", hue="campus",
                     size="study_hours", sizes=(20, 200), alpha=0.7)

ax.set_title("Marks vs attendance by campus", fontsize=18, weight="bold")
ax.set_xlabel("Attendance (%)")
ax.set_ylabel("Marks (out of 100)")
ax.set_xlim(50, 102)                                # control the axis range
ax.axhline(60, color="red", linestyle="--", linewidth=1)   # pass line
ax.text(51, 61, "pass mark", color="red", fontsize=12)
ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=11)  # legend outside

plt.tight_layout()
plt.savefig("formatted_plot.png", dpi=120)
print("Saved formatted_plot.png")
