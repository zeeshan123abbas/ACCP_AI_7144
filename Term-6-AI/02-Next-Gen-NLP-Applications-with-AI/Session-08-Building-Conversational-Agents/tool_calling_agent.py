"""Session 08 - Example 4: an agent that calls Python functions (tools).

Modern LLM APIs support "tool calling": we describe our functions, the
model decides which one to call and with what arguments, our code runs
it, and the model writes the final reply using the result.
Run: python tool_calling_agent.py
  - with OPENAI_API_KEY: real tool calling
  - without a key      : a simple keyword router plays the model's part
"""
import json
from llm_client import is_live, MODEL

# Step 1: the real Python tools
def get_fee(course):
    fees = {"ai": 25000, "web": 12000, "python": 9000}
    return {"course": course, "monthly_fee_pkr": fees.get(course.lower(), "unknown")}

def get_class_time(course):
    times = {"ai": "5 pm - 7 pm", "web": "9 am - 11 am", "python": "11 am - 1 pm"}
    return {"course": course, "time": times.get(course.lower(), "unknown")}

TOOLS = {"get_fee": get_fee, "get_class_time": get_class_time}

# Step 2: describe the tools in the JSON format the API expects
TOOL_SPECS = [
    {"type": "function", "function": {
        "name": name,
        "description": description,
        "parameters": {"type": "object",
                       "properties": {"course": {"type": "string", "description": "ai, web or python"}},
                       "required": ["course"]}}}
    for name, description in [("get_fee", "Monthly fee of a course"),
                              ("get_class_time", "Class timing of a course")]
]

def mock_router(question):
    """Offline stand-in for the model: pick a tool and argument with keywords."""
    course = next((c for c in ["ai", "web", "python"] if c in question.lower().split()), "ai")
    tool = "get_fee" if "fee" in question.lower() else "get_class_time"
    result = TOOLS[tool](course)
    return f"(mock) I called {tool}({course!r}) and got {result}"

def run_agent(question):
    if not is_live():
        return mock_router(question)

    from openai import OpenAI
    client = OpenAI()
    messages = [{"role": "user", "content": question}]

    # Step 3: first call - the model may ask for a tool
    response = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOL_SPECS)
    message = response.choices[0].message
    if not message.tool_calls:                     # no tool needed
        return message.content

    # Step 4: run every requested tool and send the results back
    messages.append(message)
    for call in message.tool_calls:
        args = json.loads(call.function.arguments)
        result = TOOLS[call.function.name](**args)
        messages.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result)})

    # Step 5: second call - the model writes the final answer using the tool results
    final = client.chat.completions.create(model=MODEL, messages=messages)
    return final.choices[0].message.content

if __name__ == "__main__":
    for q in ["What is the fee for the web course?", "When is the python class?"]:
        print("Q:", q)
        print("A:", run_agent(q), "\n")
