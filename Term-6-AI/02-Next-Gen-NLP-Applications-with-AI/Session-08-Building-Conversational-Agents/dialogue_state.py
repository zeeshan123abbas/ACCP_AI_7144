"""Session 08 - Example 2: dialogue state tracking (slot filling).

A task bot must remember what it already knows and ask only for what is
missing. Here the bot books a counselling session and needs 3 slots.
Run: python dialogue_state.py   (uses a scripted conversation)
"""

# Step 1: the slots we must fill, and the question for each
REQUIRED_SLOTS = {
    "name": "May I have your name?",
    "course": "Which course are you interested in?",
    "day": "Which day suits you for the counselling session?",
}
COURSES = ["ai", "web", "python"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

def update_state(state, message):
    """Read the message and fill any slot we can recognise."""
    text = message.lower()
    for course in COURSES:
        if course in text.split():
            state["course"] = course
    for day in DAYS:
        if day in text:
            state["day"] = day
    if "my name is" in text:
        start = text.index("my name is") + len("my name is")   # position right after the phrase
        state["name"] = message[start:].strip().title()
    return state

def next_question(state):
    """Return the question for the first empty slot, or None when all are filled."""
    for slot, question in REQUIRED_SLOTS.items():
        if slot not in state:
            return question
    return None

# Step 2: a scripted user so the example runs without typing
user_turns = ["Hi, I want to learn AI", "My name is Ayesha Khan", "Saturday please"]

state = {}                                      # the dialogue state starts empty
for message in user_turns:
    print("User :", message)
    state = update_state(state, message)        # Step 3: track the state
    print("State:", state)
    question = next_question(state)             # Step 4: decide what to ask next
    if question:
        print("Bot  :", question, "\n")
    else:
        print(f"Bot  : Booked! {state['name']}, your {state['course'].upper()} counselling is on {state['day'].title()}.")
