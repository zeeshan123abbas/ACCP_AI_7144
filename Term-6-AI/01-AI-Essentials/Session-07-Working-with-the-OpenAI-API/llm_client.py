"""Session 07 - Shared helper: talk to an OpenAI chat model, or a local mock.

If the `openai` package is installed AND the OPENAI_API_KEY environment
variable is set, real requests are sent. Otherwise a tiny offline mock
answers, so every example in this folder still runs in class.

Set the model with OPENAI_MODEL (default below). Model names change over
time, so check https://platform.openai.com/docs/models for current ones.
"""
import os

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def _mock_reply(messages):
    last = messages[-1]["content"]
    names = [m["content"] for m in messages if m["role"] == "user" and "my name is" in m["content"].lower()]
    if "name" in last.lower() and "?" in last and names:
        return f"(mock) You told me earlier: '{names[-1]}'."
    return f"(mock) I received {len(messages)} message(s). Last one was: {last[:60]!r}"


def chat(messages, model=DEFAULT_MODEL, temperature=0.7, max_tokens=300):
    """Send a list of {'role','content'} dicts and return the reply text."""
    key = os.getenv("OPENAI_API_KEY")
    try:
        from openai import OpenAI
    except ImportError:
        OpenAI = None
    if not key or OpenAI is None:
        return _mock_reply(messages)
    client = OpenAI()                       # reads OPENAI_API_KEY automatically
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    mode = "LIVE" if os.getenv("OPENAI_API_KEY") else "MOCK (no OPENAI_API_KEY set)"
    print("Mode:", mode, "| model:", DEFAULT_MODEL)
    print(chat([{"role": "user", "content": "Say hello to Aptech AI students in one line."}]))
