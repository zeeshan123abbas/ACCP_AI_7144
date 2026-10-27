# unsupervised_kmeans.py - UNSUPERVISED learning: group customers with K-Means
# Install once:  pip install scikit-learn matplotlib

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Customer data: [monthly visits, average spend in thousand Rs]
# NOTE: there are NO labels - we do not tell the model the groups
customers = [[2, 3], [3, 4], [2, 5], [3, 3],          # rare visitors, low spend
             [10, 4], [11, 5], [12, 3], [10, 6],      # frequent, low spend
             [9, 20], [11, 22], [10, 18], [12, 21]]   # frequent, high spend

# Step 1: ask for 3 groups (clusters)
kmeans = KMeans(n_clusters=3, n_init=10, random_state=0)

# Step 2: fit_predict finds the groups and returns a cluster number for each customer
groups = kmeans.fit_predict(customers)
print("Cluster of each customer:", groups)
print("Cluster centres:\n", kmeans.cluster_centers_.round(1))

# Step 3: which group would a new customer join?
print("New customer [11, 19] belongs to cluster", kmeans.predict([[11, 19]])[0])

# Step 4: plot - each cluster gets its own colour
visits = [c[0] for c in customers]
spend = [c[1] for c in customers]
plt.scatter(visits, spend, c=groups, cmap="viridis", s=80)
centres = kmeans.cluster_centers_
plt.scatter(centres[:, 0], centres[:, 1], color="red", marker="X", s=200, label="centres")
plt.xlabel("Visits per month")
plt.ylabel("Average spend (k Rs)")
plt.title("K-Means customer groups")
plt.legend()
plt.savefig("kmeans_customers.png")
plt.show()
