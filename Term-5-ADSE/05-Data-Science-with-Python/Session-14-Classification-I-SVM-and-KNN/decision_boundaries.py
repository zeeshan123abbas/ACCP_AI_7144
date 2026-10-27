# decision_boundaries.py - SEE how KNN and SVM split the space
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Two interleaving half-moons: a classic non-linear problem (2 features, 2 classes)
X, y = make_moons(n_samples=200, noise=0.25, random_state=3)

models = {
    "KNN (k=15)": KNeighborsClassifier(n_neighbors=15),
    "SVM linear": SVC(kernel="linear"),
    "SVM RBF": SVC(kernel="rbf", C=1),
}

# A fine grid of points covering the plot area
xx, yy = np.meshgrid(np.linspace(-2, 3, 300), np.linspace(-1.5, 2, 300))
grid = np.c_[xx.ravel(), yy.ravel()]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, (name, model) in zip(axes, models.items()):
    model.fit(X, y)
    zone = model.predict(grid).reshape(xx.shape)     # class of every grid point
    ax.contourf(xx, yy, zone, alpha=0.3, cmap="coolwarm")
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolor="k", s=20)
    ax.set_title(f"{name}  (accuracy {model.score(X, y):.2f})")

fig.tight_layout()
fig.savefig("decision_boundaries.png")
print("Saved decision_boundaries.png")
