# dbscan_demo.py - DBSCAN finds clusters of ANY shape and marks outliers as -1

from sklearn.cluster import DBSCAN, KMeans
from sklearn.datasets import make_moons
from sklearn.metrics import adjusted_rand_score

# Two half-moon shapes - K-Means struggles with shapes like this
X, true_groups = make_moons(n_samples=200, noise=0.06, random_state=0)

kmeans_labels = KMeans(n_clusters=2, n_init=10, random_state=0).fit_predict(X)

# eps = how close points must be to count as neighbours
# min_samples = how many neighbours make a "dense" core point
dbscan_labels = DBSCAN(eps=0.2, min_samples=5).fit_predict(X)

# Compare with the real groups (1.0 = perfect match, 0 = random)
print("K-Means agreement:", round(adjusted_rand_score(true_groups, kmeans_labels), 2))
print("DBSCAN  agreement:", round(adjusted_rand_score(true_groups, dbscan_labels), 2))
print("DBSCAN clusters found:", sorted(set(dbscan_labels.tolist())))
print("Outliers (label -1):", list(dbscan_labels).count(-1))
