"""Session 13 - Example 1: the simplest search - count matching words.

Run: python keyword_search.py
"""
from courses import COURSES

def keyword_search(query, top_k=3):
    query_words = set(query.lower().split())
    results = []
    for course in COURSES:
        # Step 1: put title and description together and split into words
        course_words = set((course["title"] + " " + course["text"]).lower().replace(",", "").replace(".", "").split())
        # Step 2: score = how many query words appear in the course
        score = len(query_words & course_words)
        if score > 0:
            results.append((score, course["title"]))
    # Step 3: highest score first
    results.sort(reverse=True)
    return results[:top_k]

for query in ["python models", "build websites", "teach a computer to talk"]:
    print(f"\nQuery: {query}")
    print(keyword_search(query) or "  no results")
