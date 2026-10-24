"""Session 04 - A* on the 8-puzzle with two heuristics.

State: a tuple of 9 numbers read row by row, 0 = blank.
h1 = number of misplaced tiles, h2 = total Manhattan distance.
Both are admissible, but h2 is better informed, so A* expands fewer nodes.
"""
import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def neighbours(state):
    i = state.index(0)
    r, c = divmod(i, 3)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            s = list(state); s[i], s[j] = s[j], s[i]
            yield tuple(s)

def misplaced(state):
    return sum(1 for a, b in zip(state, GOAL) if a and a != b)

def manhattan(state):
    total = 0
    for idx, tile in enumerate(state):
        if tile:
            g = GOAL.index(tile)
            total += abs(idx // 3 - g // 3) + abs(idx % 3 - g % 3)
    return total

def astar(start, h):
    frontier = [(h(start), 0, start, [start])]
    best_g, expanded = {start: 0}, 0
    while frontier:
        f, g, state, path = heapq.heappop(frontier)
        if g > best_g[state]:
            continue
        expanded += 1
        if state == GOAL:
            return path, expanded
        for nxt in neighbours(state):
            if g + 1 < best_g.get(nxt, 1e9):
                best_g[nxt] = g + 1
                heapq.heappush(frontier, (g + 1 + h(nxt), g + 1, nxt, path + [nxt]))

def show(state):
    for r in range(3):
        print("   ", " ".join(str(x) if x else "_" for x in state[r * 3:r * 3 + 3]))

start = (7, 2, 4, 5, 0, 6, 8, 3, 1)   # solvable; try (8, 6, 7, 2, 5, 4, 3, 0, 1) for a 31-move challenge
print("Start state:"); show(start)
for name, h in (("misplaced tiles", misplaced), ("Manhattan distance", manhattan)):
    path, expanded = astar(start, h)
    print(f"A* with {name:<20}: {len(path) - 1} moves, {expanded} nodes expanded")
