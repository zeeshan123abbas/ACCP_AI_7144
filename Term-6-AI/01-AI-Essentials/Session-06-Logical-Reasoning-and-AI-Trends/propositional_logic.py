"""Session 06 - Propositional logic: truth tables and entailment by model checking.

Knowledge base (KB):
  R  : "It is raining"
  W  : "The road is wet"
  S  : "The match is suspended"
  KB = (R -> W) AND (W -> S) AND R
Question: does KB entail S?   (KB |= S)
"""
from itertools import product

def implies(a, b):
    return (not a) or b

SYMBOLS = ["R", "W", "S"]

def kb(m):
    return implies(m["R"], m["W"]) and implies(m["W"], m["S"]) and m["R"]

def entails(kb_fn, query_fn):
    """KB |= query if query is true in EVERY model where KB is true."""
    for values in product([True, False], repeat=len(SYMBOLS)):
        m = dict(zip(SYMBOLS, values))
        if kb_fn(m) and not query_fn(m):
            return False
    return True

print(" R     W     S    | KB")
for values in product([True, False], repeat=3):
    m = dict(zip(SYMBOLS, values))
    print(" ".join(f"{str(v):<5}" for v in values), "|", kb(m))

print("\nKB |= S ?      ", entails(kb, lambda m: m["S"]))
print("KB |= not R ?  ", entails(kb, lambda m: not m["R"]))

# Inference rules shown as code
print("\nModus Ponens   : from R and (R -> W) conclude W")
print("Modus Tollens  : from not S and (W -> S) conclude not W")

# A taste of predicate (first-order) logic: "All students who pass get a certificate"
students = {"Ayesha": 82, "Bilal": 45, "Hamza": 67}
passes = lambda x: students[x] >= 50                 # Passes(x)
certificate = {x for x in students if passes(x)}     # forall x: Passes(x) -> Certificate(x)
print("\nforall x Passes(x) -> Certificate(x):", sorted(certificate))
print("exists x not Passes(x)?", any(not passes(x) for x in students))
