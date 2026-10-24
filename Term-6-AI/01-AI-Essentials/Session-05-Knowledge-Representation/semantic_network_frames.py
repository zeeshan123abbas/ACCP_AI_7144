"""Session 05 - Semantic networks and frames.

A semantic network stores knowledge as (subject, relation, object) triples.
"is_a" links allow inheritance: properties flow down from general to specific.
Frames group the slots (attributes) of one concept, with defaults.
"""

TRIPLES = [
    ("Animal", "can", "breathe"),
    ("Bird", "is_a", "Animal"),
    ("Bird", "can", "fly"),
    ("Bird", "has", "feathers"),
    ("Penguin", "is_a", "Bird"),
    ("Penguin", "cannot", "fly"),          # exception overrides inheritance
    ("Parrot", "is_a", "Bird"),
    ("Mithu", "instance_of", "Parrot"),
]

def parents(node):
    return [o for s, r, o in TRIPLES if s == node and r in ("is_a", "instance_of")]

def can(node, ability):
    """Walk up the is_a chain; the most specific fact wins."""
    for s, r, o in TRIPLES:
        if s == node and o == ability and r in ("can", "cannot"):
            return r == "can"
    return any(can(p, ability) for p in parents(node))

for who in ("Mithu", "Penguin", "Bird"):
    print(f"Can {who} fly? {can(who, 'fly')}   breathe? {can(who, 'breathe')}")

# ---------------- Frames ----------------
class Frame:
    def __init__(self, name, parent=None, **slots):
        self.name, self.parent, self.slots = name, parent, slots

    def get(self, slot):
        if slot in self.slots:
            return self.slots[slot]
        return self.parent.get(slot) if self.parent else None

course = Frame("Course", duration_hours=2, delivery="classroom")
ai_session = Frame("AI_Session", parent=course, module="AI Essentials", lab=True)
online_ai = Frame("Online_AI_Session", parent=ai_session, delivery="online")

print("\nFrame lookup with inheritance and overriding:")
for slot in ("module", "duration_hours", "delivery", "lab"):
    print(f"  {online_ai.name}.{slot} = {online_ai.get(slot)}")
