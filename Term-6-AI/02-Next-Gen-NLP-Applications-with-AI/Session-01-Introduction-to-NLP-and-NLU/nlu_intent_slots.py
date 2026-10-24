"""Session 01 - From NLP to NLU: intent detection, slot filling and dialogue state.

A food-ordering assistant must understand WHAT the user wants (intent),
the DETAILS (slots), and remember them across turns (dialogue state).
"""
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

TRAIN = [
    ("I want to order a pizza", "order_food"), ("get me two burgers please", "order_food"),
    ("can I have biryani for dinner", "order_food"), ("order three shawarmas", "order_food"),
    ("where is my order", "track_order"), ("how long until my food arrives", "track_order"),
    ("is the rider close", "track_order"), ("track my delivery", "track_order"),
    ("cancel my order", "cancel_order"), ("I don't want the food anymore", "cancel_order"),
    ("please stop the delivery", "cancel_order"), ("cancel it", "cancel_order"),
    ("hello", "greet"), ("hi there", "greet"), ("assalam o alaikum", "greet"), ("good evening", "greet"),
]
texts, labels = zip(*TRAIN)
intent_model = make_pipeline(TfidfVectorizer(ngram_range=(1, 2)), LogisticRegression(max_iter=1000))
intent_model.fit(texts, labels)

NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
DISHES = ["pizza", "burger", "biryani", "shawarma", "karahi"]

def extract_slots(text):
    """Slot filling with simple rules: quantity, dish, time."""
    t = text.lower()
    slots = {}
    # a quantity counts only when it is directly followed by a dish name
    m = re.search(r"\b(\d+|one|two|three|four|five)\s+(?:%s)" % "|".join(DISHES), t)
    if m:
        slots["quantity"] = int(NUMBERS.get(m.group(1), m.group(1)))
    for dish in DISHES:
        if dish in t:
            slots["dish"] = dish
    m = re.search(r"\b(at \d{1,2}(:\d{2})?\s?(am|pm)?|tonight|now)\b", t)
    if m:
        slots["time"] = m.group(1)
    return slots

state = {"intent": None, "slots": {}}          # dialogue state tracking
conversation = ["Hi there", "I want to order two pizzas", "make it at 8 pm", "where is my order"]
for turn in conversation:
    intent = intent_model.predict([turn])[0]
    slots = extract_slots(turn)
    # a follow-up with only details keeps the previous intent
    if slots and not any(w in turn.lower() for w in ["order", "want", "get"]) and state["intent"]:
        intent = state["intent"]
    state["intent"] = intent
    state["slots"].update(slots)
    print(f"USER: {turn!r}\n   intent={intent:<13} new_slots={slots}  state={state['slots']}")
