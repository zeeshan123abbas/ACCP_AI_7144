# plot_3d.py - show THREE numeric variables at once with a 3-D scatter
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
colours = df["result"].map({"Pass": "green", "Fail": "red"})   # colour by result

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(projection="3d")              # a 3-D axes

ax.scatter(df["study_hours"], df["attendance"], df["marks"], c=colours, s=25)
ax.set_xlabel("Study hours")
ax.set_ylabel("Attendance %")
ax.set_zlabel("Marks")
ax.set_title("3 variables: hours, attendance, marks")
ax.view_init(elev=20, azim=-60)                    # camera angle

fig.savefig("plot_3d.png")
print("Saved plot_3d.png  (green = Pass, red = Fail)")
