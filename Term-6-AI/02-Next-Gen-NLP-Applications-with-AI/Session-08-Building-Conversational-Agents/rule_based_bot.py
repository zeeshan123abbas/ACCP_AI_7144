"""Session 08 - Example 1: a simple rule-based chatbot.

Before LLMs, many bots matched keywords to intents and replied from
templates. This is still useful for small, predictable tasks.
Run: python rule_based_bot.py   (type 'bye' to quit)
"""

# Step 1: each intent has some keywords and a fixed reply
INTENTS = {
    "greeting": (["hello", "hi", "salam", "assalam"], "Hello! How can I help you today?"),
    "timings":  (["time", "timing", "open", "close"], "We are open Monday to Saturday, 9 am to 9 pm."),
    "fees":     (["fee", "fees", "cost", "price"], "The monthly fee is PKR 25,000."),
    "goodbye":  (["bye", "goodbye", "khuda hafiz"], "Goodbye! Have a great day."),
}

def detect_intent(message):
    """Return the first intent whose keyword appears in the message."""
    text = message.lower().replace("?", "").replace("!", "")
    words = text.split()                                  # list of single words
    for intent, (keywords, _reply) in INTENTS.items():
        for keyword in keywords:
            if " " in keyword:                            # two-word keyword, e.g. "khuda hafiz"
                if keyword in text:
                    return intent
            elif keyword in words:                        # one-word keyword must match a whole word
                return intent
    return "unknown"

def reply_to(message):
    intent = detect_intent(message)
    if intent == "unknown":
        return intent, "Sorry, I did not understand. Ask me about fees or timings."
    return intent, INTENTS[intent][1]

# Step 2: the chat loop
if __name__ == "__main__":
    print("Bot: Hi! Ask me about fees or timings. Type 'bye' to quit.")
    while True:
        user = input("You: ")
        intent, answer = reply_to(user)
        print(f"Bot: {answer}   [intent={intent}]")
        if intent == "goodbye":
            break
