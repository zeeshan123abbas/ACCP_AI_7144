# lab5_cluster_employees.py - group employees by salary and rating with K-Means
# Run lab1_clean_explore.py first

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("employees_clean.csv")

# Step 1: choose the columns and scale them (salary is much bigger than rating)
features = df[["salary_k", "rating"]]
scaled = StandardScaler().fit_transform(features)

# Step 2: make 3 groups
kmeans = KMeans(n_clusters=3, n_init=10, random_state=0)
df["group"] = kmeans.fit_predict(scaled)

# Step 3: describe each group in plain numbers
summary = df.groupby("group")[["salary_k", "rating"]].mean().round(1)
summary["members"] = df["group"].value_counts().sort_index()
print(summary, "\n")

# Step 4: list the people in each group
for group_number, members in df.groupby("group"):
    print(f"Group {group_number}: {', '.join(members['name'])}")
