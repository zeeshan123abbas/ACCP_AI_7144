"""Session 03 - Three kinds of AI agents in a two-room cleaning world.

Rooms "A" and "B" can be Dirty or Clean. The agent perceives
(current_room, status) and chooses an action: Suck, Left, Right, NoOp.
"""
import random

class Environment:
    def __init__(self, seed=3):
        random.seed(seed)
        self.status = {"A": random.choice(["Dirty", "Clean"]),
                       "B": random.choice(["Dirty", "Clean"])}
        self.location = "A"

    def percept(self):
        return self.location, self.status[self.location]

    def execute(self, action):
        if action == "Suck":
            self.status[self.location] = "Clean"
        elif action == "Right":
            self.location = "B"
        elif action == "Left":
            self.location = "A"


def simple_reflex_agent(percept):
    """Acts only on the current percept using condition-action rules."""
    room, status = percept
    if status == "Dirty":
        return "Suck"
    return "Right" if room == "A" else "Left"


class ModelBasedAgent:
    """Keeps an internal model (memory) of rooms it has already seen."""
    def __init__(self):
        self.model = {"A": None, "B": None}

    def __call__(self, percept):
        room, status = percept
        self.model[room] = status
        if status == "Dirty":
            self.model[room] = "Clean"
            return "Suck"
        if all(v == "Clean" for v in self.model.values()):
            return "NoOp"                       # knows the job is done
        return "Right" if room == "A" else "Left"


class GoalBasedAgent(ModelBasedAgent):
    """Same memory, but explicitly checks a goal test before acting."""
    goal = {"A": "Clean", "B": "Clean"}

    def __call__(self, percept):
        action = super().__call__(percept)
        if self.model == self.goal:
            print("    goal reached, stopping early")
        return action


def run(agent, name, steps=6):
    env = Environment()
    print(f"\n{name}  (start: {env.status})")
    for t in range(steps):
        p = env.percept()
        a = agent(p)
        print(f"  t={t} percept={p} -> action={a}")
        env.execute(a)
        if a == "NoOp":
            break

run(simple_reflex_agent, "Simple reflex agent")
run(ModelBasedAgent(), "Model-based agent")
run(GoalBasedAgent(), "Goal-based agent")
