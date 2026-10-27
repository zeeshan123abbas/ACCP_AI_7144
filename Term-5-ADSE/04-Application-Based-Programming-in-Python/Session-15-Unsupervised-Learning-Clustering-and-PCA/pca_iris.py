# pca_iris.py - Principal Component Analysis: squeeze 4 columns into 2 for a picture

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data                     # 150 rows x 4 features
print("Original shape:", X.shape)

# Step 1: scale - PCA is sensitive to the size of numbers
X_scaled = StandardScaler().fit_transform(X)

# Step 2: keep 2 principal components
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)
print("New shape:", X_2d.shape)

# Step 3: how much information (variance) does each component keep?
for number, share in enumerate(pca.explained_variance_ratio_, start=1):
    print(f"PC{number} keeps {share:.1%} of the variance")
print(f"Total kept: {pca.explained_variance_ratio_.sum():.1%}")

# Step 4: plot - colours are the real species (PCA itself never saw them)
for species_number, name in enumerate(iris.target_names):
    points = X_2d[iris.target == species_number]
    plt.scatter(points[:, 0], points[:, 1], label=name)
plt.xlabel("Principal component 1")
plt.ylabel("Principal component 2")
plt.title("Iris flowers after PCA (4D -> 2D)")
plt.legend()
plt.savefig("pca_iris.png")
plt.show()
