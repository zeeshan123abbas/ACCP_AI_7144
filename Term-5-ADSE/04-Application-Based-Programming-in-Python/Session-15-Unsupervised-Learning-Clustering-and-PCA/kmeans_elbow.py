# kmeans_elbow.py - choose the number of clusters with the elbow method and silhouette score
# Install once:  pip install scikit-learn matplotlib

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

# Step 1: make 300 sample points that secretly form 4 groups
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.9, random_state=7)

# Step 2: try K = 1..8 and record two scores
inertias = []
print("K | inertia | silhouette")
for k in range(1, 9):
    model = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    inertias.append(model.inertia_)          # total distance of points to their centre
    if k > 1:                                # silhouette needs at least 2 clusters
        sil = silhouette_score(X, model.labels_)
        print(f"{k} | {model.inertia_:8.1f} | {sil:.3f}")
    else:
        print(f"{k} | {model.inertia_:8.1f} |   -")

# Step 3: plot the elbow curve - look for the "bend"
plt.plot(range(1, 9), inertias, marker="o")
plt.xlabel("Number of clusters (K)")
plt.ylabel("Inertia (lower = tighter clusters)")
plt.title("Elbow method")
plt.savefig("elbow.png")
plt.show()
