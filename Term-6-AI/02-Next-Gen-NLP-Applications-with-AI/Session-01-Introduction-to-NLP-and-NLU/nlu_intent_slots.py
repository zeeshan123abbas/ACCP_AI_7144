"""Session 01 - Example 4: NLU = intent detection + slot filling + dialogue state.

A food-ordering bot must know WHAT the user wants (intent),
the DETAILS (slots) and REMEMBER them across turns (dialogue state).
Run: python nlu_intent_slots.py
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# Step 1: a tiny training set of (sentence, intent)
training_sentences = [
    "I want to order a pizza", "get me two burgers", "can I have biryani", "order a shawarma",
    "where is my order", "track my delivery", "how long will my food take", "is the rider close",
    "cancel my order", "I do not want the food", "stop my delivery", "please cancel it",
]
training_intents = [
    "order_food", "order_food", "order_food", "order_food",
    "track_order", "track_order", "track_order", "track_order",
    "cancel_order", "cancel_order", "cancel_order", "cancel_order",
]

# Step 2: train an intent classifier (TF-IDF numbers + logistic regression)
intent_model = make_pipeline(TfidfVectorizer(), LogisticRegression())
intent_model.fit(training_sentences, training_intents)

# Step 3: slot filling with simple keyword rules
DISHES = ["pizza", "burger", "biryani", "shawarma"]
NUMBERS = {"one": 1, "two": 2, "three": 3}

def find_slots(sentence):
    slots = {}
    for word in sentence.lower().split():
        if word in NUMBERS:
            slots["quantity"] = NUMBERS[word]
        for dish in DISHES:
            if word.startswith(dish):          # "pizzas" also matches "pizza"
                slots["dish"] = dish
    return slots

# Step 4: dialogue state = what we remember so far in this conversation
state = {}

conversation = ["I want to order two pizzas", "where is my order", "please cancel it"]
for user_text in conversation:
    intent = intent_model.predict([user_text])[0]
    slots = find_slots(user_text)
    state.update(slots)                        # remember new details
    print(f"USER : {user_text}")
    print(f"  intent = {intent}, slots = {slots}, remembered = {state}")
