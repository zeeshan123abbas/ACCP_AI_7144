"""Session 12 - Example 1: test a model for bias with counterfactual sentences.

Idea: keep the sentence the same and change ONLY a group word (a name,
gender or city). A fair model should give (almost) the same score.
Our "model" is a deliberately biased toy scorer so you can see a failure.
Run: python bias_probe.py
"""

def toy_hiring_scorer(text):
    """A pretend CV-screening model that learned bad habits from biased data."""
    score = 0.5
    if "experienced" in text:
        score += 0.3
    if "he" in text.lower().split():    # BIAS: learned from past hiring data
        score += 0.1
    if "Lahore" in text:                # BIAS: favours one city
        score += 0.05
    return round(score, 2)

# Step 1: one template, many groups
template = "{pronoun} is an experienced Python developer from {city}."
pronouns = ["he", "she"]
cities = ["Karachi", "Lahore", "Quetta"]

# Step 2: score every combination
results = {}
for pronoun in pronouns:
    for city in cities:
        sentence = template.format(pronoun=pronoun.capitalize(), city=city)
        score = toy_hiring_scorer(sentence)
        results[(pronoun, city)] = score
        print(f"{score:.2f}  {sentence}")

# Step 3: the gap between the best and worst group is a simple bias signal
gap = max(results.values()) - min(results.values())
print(f"\nLargest score gap between groups: {gap:.2f}")
print("Possible bias detected!" if gap > 0.05 else "Scores look consistent.")
