"""Session 08 - Example 3: an LLM chatbot with short-term memory.

LLMs do not remember earlier messages by themselves. WE send the
conversation history every time. To control cost we keep only the
last few turns (a "sliding window").
Run: python chat_with_memory.py   (scripted turns, mock answers without a key)
"""
from llm_client import chat

MAX_TURNS = 3          # keep the last 3 user+assistant pairs

system_message = {"role": "system", "content": "You are a friendly study buddy for Python learners. Keep answers short."}
history = []           # list of {"role": ..., "content": ...}

def trimmed_history():
    """Keep only the last MAX_TURNS pairs (each pair = 2 messages)."""
    return history[-MAX_TURNS * 2:]

def ask(user_text, mock):
    history.append({"role": "user", "content": user_text})          # Step 1: remember the question
    messages = [system_message] + trimmed_history()                  # Step 2: build the request
    reply = chat(messages, mock_answer=mock)                         # Step 3: call the model
    history.append({"role": "assistant", "content": reply})          # Step 4: remember the answer
    return reply

# Scripted conversation: the 2nd question only makes sense with memory ("it")
turns = [
    ("My name is Hamza and I am learning lists.", "Nice to meet you, Hamza! Lists store many items in order."),
    ("How do I add an item to it?", "Use append, for example: fruits.append('mango')."),
    ("What is my name?", "Your name is Hamza."),
]
for text, mock in turns:
    print("You:", text)
    print("Bot:", ask(text, mock), "\n")

print("Messages stored:", len(history), "| messages sent last time:", len(trimmed_history()) + 1)
