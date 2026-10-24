"""Score-based SDLC model recommender.
Run: python model_selector.py
"""
QUESTIONS = {
    "clear_requirements": "Requirements are clear and stable (0-5): ",
    "regulated": "Heavy regulation / audit needed (0-5): ",
    "risk": "Technical or business risk (0-5): ",
    "customer_time": "Customer available every week (0-5): ",
    "speed": "Need to release something fast (0-5): ",
}


def recommend(a: dict) -> str:
    scores = {
        "Waterfall / V-Model": a["clear_requirements"] + a["regulated"] - a["risk"],
        "Spiral": a["risk"] * 2 + a["regulated"] - a["speed"],
        "Scrum / XP": a["customer_time"] + a["speed"] + a["risk"] - a["clear_requirements"],
        "RAD": a["speed"] * 2 + a["customer_time"] - a["regulated"] - a["risk"],
    }
    for model, s in sorted(scores.items(), key=lambda kv: -kv[1]):
        print(f"{model:<22} score {s:>3}")
    return max(scores, key=scores.get)


if __name__ == "__main__":
    demo = {"clear_requirements": 1, "regulated": 1, "risk": 4, "customer_time": 4, "speed": 5}
    print("Demo project (startup app):")
    print("Recommended ->", recommend(demo))
