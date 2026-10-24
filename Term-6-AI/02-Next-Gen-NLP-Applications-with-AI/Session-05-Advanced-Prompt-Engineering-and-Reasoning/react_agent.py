"""Session 05 - Example 4: a tiny ReAct loop (Reason + Act).

The model writes a Thought, then an Action (a tool call). Our code runs the
tool and sends back an Observation. This repeats until a Final Answer.
Run: python react_agent.py   (mock mode replays a sample conversation)
"""
from llm_client import chat

# Step 1: the tools our program can run
def calculator(expression):
    allowed = "0123456789+-*/(). "
    if all(ch in allowed for ch in expression):        # only allow simple maths
        return str(eval(expression))
    return "error: only numbers and + - * / allowed"

def fee_lookup(course):
    fees = {"ACCP AI": 25000, "Web Design": 12000}       # fees per month (sample data)
    return str(fees.get(course, "unknown course"))

TOOLS = {"calculator": calculator, "fee_lookup": fee_lookup}

# Step 2: the system prompt teaches the model the ReAct format
system = """Answer the question using this format:
Thought: what you should do next
Action: tool_name[input]      (tools: calculator, fee_lookup)
Wait for an Observation after each Action.
When you know the answer write:  Final Answer: <answer>"""

question = "What is the total fee for 6 months of the ACCP AI course?"
messages = [{"role": "system", "content": system}, {"role": "user", "content": question}]

# Sample model replies used only in mock mode, one per loop round
mock_steps = [
    "Thought: I need the monthly fee first.\nAction: fee_lookup[ACCP AI]",
    "Thought: Now multiply the monthly fee by 6.\nAction: calculator[25000*6]",
    "Thought: I have the total.\nFinal Answer: The total fee is Rs. 150,000.",
]

# Step 3: the loop - at most 5 rounds so it can never run forever
for step in range(5):
    reply = chat(messages, mock_answer=mock_steps[min(step, 2)], temperature=0)
    print(reply.replace("(mock) ", ""))
    messages.append({"role": "assistant", "content": reply})

    if "Final Answer:" in reply:                     # finished
        break

    # Step 4: read the Action line, e.g. "Action: calculator[25000*6]"
    action_lines = [line for line in reply.splitlines() if line.startswith("Action:")]
    if not action_lines:                             # model broke the format: stop safely
        print("No Action found - stopping.")
        break
    action_line = action_lines[0]
    tool_name = action_line.split(":")[1].split("[")[0].strip()
    tool_input = action_line.split("[")[1].rstrip("]")

    # Step 5: run the tool and send the result back as an Observation
    if tool_name in TOOLS:
        observation = TOOLS[tool_name](tool_input)
    else:
        observation = f"unknown tool {tool_name}"
    print("Observation:", observation)
    messages.append({"role": "user", "content": f"Observation: {observation}"})
