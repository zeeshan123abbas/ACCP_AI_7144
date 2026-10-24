"""Session 07 - A console chatbot that remembers the conversation.

The API is stateless: the model only "remembers" what you send again.
So we keep a `history` list and append every user and assistant turn.
We also trim old turns so the request never grows without limit.

Run interactively:  python chat_with_history.py
Run the demo only:  python chat_with_history.py --demo
"""
import sys
from llm_client import chat

MAX_TURNS = 10   # keep the system prompt + last 10 messages

history = [{"role": "system", "content": "You are StudyBot, a friendly helper for AI students. Keep answers short."}]

def ask(user_text):
    history.append({"role": "user", "content": user_text})
    trimmed = [history[0]] + history[1:][-MAX_TURNS:]
    reply = chat(trimmed)
    history.append({"role": "assistant", "content": reply})
    return reply

if "--demo" in sys.argv or not sys.stdin.isatty():
    for line in ["Hi, my name is Sana.", "What is a neural network in one line?", "What is my name?"]:
        print("You :", line)
        print("Bot :", ask(line))
else:
    print("Type 'quit' to exit.")
    while (text := input("You : ").strip()).lower() != "quit":
        print("Bot :", ask(text))
print(f"\n(history now holds {len(history)} messages)")
