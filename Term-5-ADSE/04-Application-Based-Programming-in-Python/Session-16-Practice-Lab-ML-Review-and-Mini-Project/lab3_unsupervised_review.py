# lab3_unsupervised_review.py - PCA + K-Means on the wine dataset, then check the groups
# Wine dataset: 13 chemical measurements of 178 wines from 3 farms

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.preprocessing import StandardScaler

wine = load_wine()
X_scaled = StandardScaler().fit_transform(wine.data)

# Step 1: PCA from 13 columns to 2
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)
print(f"2 components keep {pca.explained_variance_ratio_.sum():.1%} of the variance")

# Step 2: choose K with the silhouette score
for k in range(2, 6):
    labels = KMeans(n_clusters=k, n_init=10, random_state=0).fit_predict(X_scaled)
    print(f"K={k}  silhouette={silhouette_score(X_scaled, labels):.3f}")

# Step 3: cluster with the best K and compare with the real farms
clusters = KMeans(n_clusters=3, n_init=10, random_state=0).fit_predict(X_scaled)
print("\nAgreement with real farms (ARI):",
      round(adjusted_rand_score(wine.target, clusters), 3))
print(pd.crosstab(wine.target, clusters, rownames=["real farm"], colnames=["cluster"]))
