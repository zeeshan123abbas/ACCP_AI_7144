# hierarchical_clustering.py - build clusters step by step and draw a dendrogram
# Install once:  pip install scikit-learn scipy matplotlib

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Ten cities described by [average temperature C, yearly rainfall in 100 mm]
cities = ["Karachi", "Hyderabad", "Sukkur", "Lahore", "Faisalabad",
          "Multan", "Islamabad", "Murree", "Quetta", "Gilgit"]
weather = [[26, 2], [27, 2], [27, 1], [24, 6], [24, 4],
           [26, 2], [21, 11], [13, 17], [16, 2], [12, 1]]

# 1) Agglomerative clustering: start with 10 groups, keep merging the closest two
model = AgglomerativeClustering(n_clusters=3, linkage="ward")
labels = model.fit_predict(weather)
for city, label in zip(cities, labels):
    print(f"{city:<11} -> group {label}")

# 2) Dendrogram: a tree showing the order in which groups were merged
merges = linkage(weather, method="ward")
plt.figure(figsize=(8, 5))
dendrogram(merges, labels=cities, leaf_rotation=45)   # tilt names so they do not overlap
plt.title("Dendrogram of Pakistani cities by weather")
plt.ylabel("Merge distance")
plt.tight_layout()
plt.savefig("dendrogram.png")
plt.show()
