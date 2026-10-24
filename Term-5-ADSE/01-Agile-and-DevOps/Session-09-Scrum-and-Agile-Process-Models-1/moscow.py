"""MoSCoW prioritisation helper for a fixed time-box (DSDM style).
Run: python moscow.py
"""
CAPACITY_DAYS = 20                     # what the team can deliver in this time-box

features = [
    ("Student login", "M", 3),
    ("View results", "M", 4),
    ("Download transcript PDF", "S", 3),
    ("Fee payment online", "M", 5),
    ("Dark mode", "C", 2),
    ("Chat with advisor", "W", 6),
    ("Push notifications", "S", 3),
    ("Profile photo upload", "C", 1),
]

order = {"M": 0, "S": 1, "C": 2, "W": 3}
plan, used = [], 0
for name, prio, days in sorted(features, key=lambda f: order[f[1]]):
    if prio == "W":
        continue                                   # agreed: not this time
    if used + days <= CAPACITY_DAYS:
        plan.append((name, prio, days))
        used += days

must = sum(d for _, p, d in features if p == "M")
print(f"Must-have effort: {must} of {CAPACITY_DAYS} days ({must / CAPACITY_DAYS:.0%})")
for name, prio, days in plan:
    print(f"  [{prio}] {name:<25} {days} d")
print(f"Planned {used}/{CAPACITY_DAYS} days")
if must / CAPACITY_DAYS > 0.6:
    print("Warning: Musts exceed 60% of capacity - little contingency left.")
