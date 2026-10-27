# pca_digits_speed.py - use PCA to shrink 64 pixel features and still classify well

from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1797 small images of handwritten digits, each 8x8 = 64 pixel values
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.25, random_state=0)

# Model 1: all 64 features
full_model = LogisticRegression(max_iter=3000).fit(X_train, y_train)
print("64 features  -> accuracy", round(full_model.score(X_test, y_test), 3))

# Model 2: keep only enough components for 90% of the variance
pca = PCA(n_components=0.90)                 # a fraction means "keep this much variance"
X_train_small = pca.fit_transform(X_train)   # fit PCA on training data only
X_test_small = pca.transform(X_test)
print("Components needed for 90% variance:", pca.n_components_)

small_model = LogisticRegression(max_iter=3000).fit(X_train_small, y_train)
print(f"{pca.n_components_} features  -> accuracy", round(small_model.score(X_test_small, y_test), 3))
