"""Session 03 - Formulating and solving a problem: the water jug puzzle.

You have a 4-litre jug and a 3-litre jug, no markings, and a tap.
Goal: get exactly 2 litres in the 4-litre jug.

Problem formulation
  State        : (a, b) litres in the 4L and 3L jug
  Initial state: (0, 0)
  Actions      : fill, empty, or pour one jug into the other
  Goal test    : a == 2
  Path cost    : 1 per action
"""
from collections import deque

CAP_A, CAP_B, TARGET = 4, 3, 2

def successors(state):
    a, b = state
    pour_ab = min(a, CAP_B - b)
    pour_ba = min(b, CAP_A - a)
    return {
        "Fill 4L": (CAP_A, b),
        "Fill 3L": (a, CAP_B),
        "Empty 4L": (0, b),
        "Empty 3L": (a, 0),
        "Pour 4L->3L": (a - pour_ab, b + pour_ab),
        "Pour 3L->4L": (a + pour_ba, b - pour_ba),
    }

def solve(start=(0, 0)):
    frontier = deque([(start, [])])
    visited = {start}
    while frontier:
        state, path = frontier.popleft()
        if state[0] == TARGET:                       # goal test
            return path
        for action, nxt in successors(state).items():
            if nxt not in visited:
                visited.add(nxt)
                frontier.append((nxt, path + [(action, nxt)]))
    return None

steps = solve()
print(f"Solved in {len(steps)} steps:")
print("  start      -> (0, 0)")
for action, state in steps:
    print(f"  {action:<11}-> {state}")
