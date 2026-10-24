"""Session 04 - Uninformed vs informed search on a simplified Pakistan road map.

Distances are rounded, approximate road kilometres for teaching only.
Heuristic h(n) = rough straight-line km from the city to Islamabad.
"""
import heapq
from collections import deque

GRAPH = {
    "Karachi":    {"Hyderabad": 165, "Quetta": 690},
    "Hyderabad":  {"Karachi": 165, "Sukkur": 330},
    "Sukkur":     {"Hyderabad": 330, "Multan": 470, "Quetta": 390},
    "Quetta":     {"Karachi": 690, "Sukkur": 390, "D.I.Khan": 520},
    "Multan":     {"Sukkur": 470, "Lahore": 340, "Faisalabad": 240, "D.I.Khan": 330},
    "Faisalabad": {"Multan": 240, "Lahore": 180, "Islamabad": 300},
    "Lahore":     {"Multan": 340, "Faisalabad": 180, "Islamabad": 375},
    "D.I.Khan":   {"Quetta": 520, "Multan": 330, "Islamabad": 400},
    "Islamabad":  {"Lahore": 375, "Faisalabad": 300, "D.I.Khan": 400},
}
H_TO_ISLAMABAD = {"Karachi": 1140, "Hyderabad": 1000, "Sukkur": 730, "Quetta": 700,
                  "Multan": 450, "Faisalabad": 250, "Lahore": 270, "D.I.Khan": 280,
                  "Islamabad": 0}

def path_cost(path):
    return sum(GRAPH[a][b] for a, b in zip(path, path[1:]))

def bfs(start, goal):
    frontier, seen, expanded = deque([[start]]), {start}, 0
    while frontier:
        path = frontier.popleft(); expanded += 1
        if path[-1] == goal:
            return path, expanded
        for nb in GRAPH[path[-1]]:
            if nb not in seen:
                seen.add(nb); frontier.append(path + [nb])

def dfs(start, goal):
    stack, seen, expanded = [[start]], set(), 0
    while stack:
        path = stack.pop(); node = path[-1]
        if node in seen:
            continue
        seen.add(node); expanded += 1
        if node == goal:
            return path, expanded
        for nb in GRAPH[node]:
            if nb not in seen:
                stack.append(path + [nb])

def best_first(start, goal, use_g, use_h):
    """use_g only -> Uniform Cost; use_h only -> Greedy; both -> A*."""
    frontier = [(0, 0, [start])]
    best_g, expanded = {start: 0}, 0
    while frontier:
        _, g, path = heapq.heappop(frontier); node = path[-1]
        if g > best_g.get(node, float("inf")):
            continue
        expanded += 1
        if node == goal:
            return path, expanded
        for nb, km in GRAPH[node].items():
            g2 = g + km
            if g2 < best_g.get(nb, float("inf")):
                best_g[nb] = g2
                f = (g2 if use_g else 0) + (H_TO_ISLAMABAD[nb] if use_h else 0)
                heapq.heappush(frontier, (f, g2, path + [nb]))

algorithms = {
    "BFS (uninformed)": lambda s, t: bfs(s, t),
    "DFS (uninformed)": lambda s, t: dfs(s, t),
    "Uniform Cost (uninformed)": lambda s, t: best_first(s, t, True, False),
    "Greedy Best-First (informed)": lambda s, t: best_first(s, t, False, True),
    "A* (informed)": lambda s, t: best_first(s, t, True, True),
}
for name, algo in algorithms.items():
    path, expanded = algo("Karachi", "Islamabad")
    print(f"{name:<30} cost={path_cost(path):5d} km  expanded={expanded}  path={' -> '.join(path)}")
