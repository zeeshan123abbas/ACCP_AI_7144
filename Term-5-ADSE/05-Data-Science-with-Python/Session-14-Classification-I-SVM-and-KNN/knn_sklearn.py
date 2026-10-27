# knn_sklearn.py - KNN with scaling and choosing the best k
from sklearn.datasets import load_wine          # small dataset bundled with scikit-learn
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 178 wines, 13 chemical measurements, 3 grape types (labels 0, 1, 2)
X, y = load_wine(return_X_y=True, as_frame=True)
print("Data shape:", X.shape, "| classes:", sorted(y.unique().tolist()))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0, stratify=y)

# Without scaling vs with scaling (k = 5)
plain = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
scaled = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)).fit(X_train, y_train)
print("Accuracy without scaling:", round(plain.score(X_test, y_test), 3))
print("Accuracy with scaling   :", round(scaled.score(X_test, y_test), 3))

# Choose k with 5-fold cross-validation on the TRAINING data only
# (the test set stays untouched until the very end)
k_values = range(1, 21)
scores = []
for k in k_values:
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k))
    cv_scores = cross_val_score(model, X_train, y_train, cv=5)   # 5 mini train/test rounds
    scores.append(cv_scores.mean())

best_k = k_values[scores.index(max(scores))]
print("Best k by cross-validation:", best_k, "| CV accuracy:", round(max(scores), 3))

# Final check on the test set with the chosen k
final = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=best_k)).fit(X_train, y_train)
print("Test accuracy with best k:", round(final.score(X_test, y_test), 3))

plt.plot(list(k_values), scores, marker="o")
plt.title("KNN: cross-validation accuracy for each k")
plt.xlabel("k (number of neighbours)")
plt.ylabel("mean CV accuracy")
plt.xticks(list(k_values))
plt.savefig("knn_choose_k.png")
print("Saved knn_choose_k.png")
