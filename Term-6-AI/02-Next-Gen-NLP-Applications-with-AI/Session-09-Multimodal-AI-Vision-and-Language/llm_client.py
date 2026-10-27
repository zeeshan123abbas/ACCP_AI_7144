"""Shared helper: send a prompt to an OpenAI chat model, or use a mock answer.

- If the `openai` package is installed AND the OPENAI_API_KEY environment
  variable is set, a real request is sent to the model.
- Otherwise the function simply returns the `mock_answer` you passed in,
  so every example still runs in class without a key or internet.

Choose the model with the OPENAI_MODEL environment variable.
Model names change over time: https://platform.openai.com/docs/models
"""
import os

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def is_live():
    """True when a real API call is possible."""
    try:
        import openai  # noqa: F401
    except ImportError:
        return False
    return bool(os.getenv("OPENAI_API_KEY"))


def chat(messages, mock_answer="No API key set.", temperature=0.2):
    """Send a list of {'role': ..., 'content': ...} messages and return the reply text."""
    # Step 1: no key? return the sample answer so the lesson can continue
    if not is_live():
        return "(mock) " + mock_answer

    # Step 2: create a client (it reads OPENAI_API_KEY by itself)
    from openai import OpenAI
    client = OpenAI()

    # Step 3: send the messages and return the text of the first reply
    response = client.chat.completions.create(
        model=MODEL, messages=messages, temperature=temperature
    )
    return response.choices[0].message.content


def ask_llm(prompt, mock_answer="No API key set.", system="You are a helpful assistant.",
            temperature=0.2):
    """Shortcut for one question: builds the messages list for you."""
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt},
    ]
    return chat(messages, mock_answer=mock_answer, temperature=temperature)


if __name__ == "__main__":
    print("Mode :", "LIVE" if is_live() else "MOCK (set OPENAI_API_KEY for real answers)")
    print("Model:", MODEL)
    print(ask_llm("Say hello to NLP students in one line.", mock_answer="Hello, NLP students!"))
