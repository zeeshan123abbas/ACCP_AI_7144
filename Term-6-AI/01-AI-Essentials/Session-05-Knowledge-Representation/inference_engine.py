"""Session 05 - Rule-based knowledge representation with forward and backward chaining.

Domain: a tiny "first-aid advisor" knowledge base (for teaching only, not medical advice).
Facts are strings. Rules are IF all(conditions) THEN conclusion.
"""

RULES = [
    ({"fever", "cough"}, "possible_flu"),
    ({"possible_flu", "body_ache"}, "likely_flu"),
    ({"sneezing", "itchy_eyes"}, "possible_allergy"),
    ({"likely_flu"}, "advice_rest_and_fluids"),
    ({"possible_allergy"}, "advice_avoid_dust"),
    ({"fever", "stiff_neck"}, "advice_see_doctor_now"),
]

def forward_chain(facts):
    """Data-driven: keep firing rules until no new fact appears."""
    facts = set(facts)
    fired = True
    while fired:
        fired = False
        for conditions, conclusion in RULES:
            if conditions <= facts and conclusion not in facts:
                print(f"  rule fired: IF {sorted(conditions)} THEN {conclusion}")
                facts.add(conclusion)
                fired = True
    return facts

def backward_chain(goal, facts, depth=0):
    """Goal-driven: to prove a goal, prove all conditions of a rule that concludes it."""
    pad = "  " * (depth + 1)
    if goal in facts:
        print(f"{pad}{goal}: known fact")
        return True
    for conditions, conclusion in RULES:
        if conclusion == goal:
            print(f"{pad}trying to prove {goal} via {sorted(conditions)}")
            if all(backward_chain(c, facts, depth + 1) for c in conditions):
                return True
    print(f"{pad}{goal}: cannot be proven")
    return False

patient = {"fever", "cough", "body_ache"}
print("FORWARD CHAINING from facts:", sorted(patient))
derived = forward_chain(patient)
print("  advice:", sorted(f for f in derived if f.startswith("advice")))

print("\nBACKWARD CHAINING: is 'advice_rest_and_fluids' supported?")
print("  result:", backward_chain("advice_rest_and_fluids", patient))
