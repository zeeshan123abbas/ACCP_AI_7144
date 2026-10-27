"""Session 13 - Example 5: collaborative filtering ("students like you also took...").

No text needed: we only use who rated what. Similar users -> similar tastes.
Install: pip install numpy
Run:     python collaborative_filtering.py
"""
import numpy as np

courses = ["Python", "ML", "Deep Learning", "HTML/CSS", "React", "NLP"]
students = ["Ali", "Sana", "Bilal", "Hira", "Usman"]

# Step 1: ratings matrix (rows = students, columns = courses), 0 = not taken yet
ratings = np.array([
    [5, 4, 0, 1, 0, 5],   # Ali
    [4, 5, 5, 0, 1, 4],   # Sana
    [1, 0, 0, 5, 5, 0],   # Bilal
    [0, 1, 1, 4, 5, 1],   # Hira
    [5, 0, 4, 0, 0, 0],   # Usman  <- we recommend for him
])

def cosine(a, b):
    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))

target = students.index("Usman")

# Step 2: how similar is Usman to every other student?
similarities = []
for i in range(len(students)):
    if i != target:
        similarities.append((float(cosine(ratings[target], ratings[i])), i))
similarities.sort(reverse=True)
print("Most similar students:", [(students[i], round(s, 2)) for s, i in similarities])

# Step 3: predict Usman's rating for each course he has NOT taken
#         = weighted average of other students' ratings (weights = similarity)
predictions = {}
for c in range(len(courses)):
    if ratings[target, c] == 0:
        weighted_sum = sum(s * ratings[i, c] for s, i in similarities if ratings[i, c] > 0)
        weight_total = sum(s for s, i in similarities if ratings[i, c] > 0)
        predictions[courses[c]] = weighted_sum / weight_total if weight_total else 0

# Step 4: recommend the highest predicted ratings
for course, score in sorted(predictions.items(), key=lambda item: item[1], reverse=True):
    print(f"Predicted rating for {course:<9}: {score:.2f}")
