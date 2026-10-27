# knn_by_hand.py - how K-Nearest Neighbours decides, step by step
import math

# Known fruits: (weight in grams, sweetness 1-10) -> label
known = [
    ((150, 7), "Apple"), ((170, 6), "Apple"), ((140, 8), "Apple"),
    ((120, 9), "Mango"), ((200, 9), "Mango"), ((210, 8), "Mango"),
    ((300, 3), "Melon"), ((320, 4), "Melon"),
]
new_fruit = (190, 8)
k = 3

# Step 1: distance from the new fruit to every known fruit (straight-line / Euclidean)
distances = []
for (weight, sweet), label in known:
    d = math.sqrt((weight - new_fruit[0]) ** 2 + (sweet - new_fruit[1]) ** 2)
    distances.append((d, label))

# Step 2: sort by distance and keep the k closest
distances.sort()
nearest = distances[:k]
print("Nearest neighbours:")
for d, label in nearest:
    print(f"  {label:<6} distance = {d:.1f}")

# Step 3: majority vote
votes = {}
for _, label in nearest:
    votes[label] = votes.get(label, 0) + 1
print("Votes:", votes)
print("Prediction:", max(votes, key=votes.get))

# Note: weight (grams) is much bigger than sweetness (1-10), so weight dominates the
# distance. That is why we SCALE features before KNN (see knn_sklearn.py).
