# make_students_csv.py - create a practice dataset (run once)
import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=7)
n = 120                                            # number of students

study_hours = rng.uniform(1, 8, n).round(1)        # hours per day
attendance = rng.uniform(55, 100, n).round()       # percent
gender = rng.choice(["Female", "Male"], n)
campus = rng.choice(["North", "Gulshan", "Saddar"], n)

# Marks depend on study hours and attendance, plus some random noise
marks = (20 + study_hours * 6 + attendance * 0.35 + rng.normal(0, 6, n)).clip(0, 100).round()

df = pd.DataFrame({
    "gender": gender, "campus": campus, "study_hours": study_hours,
    "attendance": attendance, "marks": marks,
})
df["result"] = np.where(df["marks"] >= 60, "Pass", "Fail")
df.to_csv("students.csv", index=False)
print(df.head())
print("Saved students.csv with", len(df), "rows")
