"""Session 13 - Example 4: content-based recommendations ("more like this").

If a student liked one course, recommend courses whose DESCRIPTIONS are similar.
Install: pip install scikit-learn
Run:     python content_recommender.py
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from courses import COURSES

# Step 1: vectors for every course description
documents = [c["title"] + ". " + c["text"] for c in COURSES]
vectors = TfidfVectorizer(stop_words="english").fit_transform(documents)

# Step 2: course-to-course similarity table (8 x 8)
similarity = cosine_similarity(vectors)

def recommend(course_id, top_k=3):
    row = course_id - 1                               # ids start at 1, rows at 0
    ranked = similarity[row].argsort()[::-1]
    picks = [i for i in ranked if i != row][:top_k]   # skip the course itself
    return [(round(float(similarity[row][i]), 2), COURSES[i]["title"]) for i in picks]

for liked in [1, 4]:
    print(f"\nBecause you liked '{COURSES[liked - 1]['title']}':")
    for score, title in recommend(liked):
        print(f"  {score:.2f}  {title}")
