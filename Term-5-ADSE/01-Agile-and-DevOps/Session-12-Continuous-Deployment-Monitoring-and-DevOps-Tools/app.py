"""Business logic (same as Session 11)."""


def grade(marks: int) -> str:
    if not 0 <= marks <= 100:
        raise ValueError("marks must be 0-100")
    for limit, letter in ((80, "A"), (70, "B"), (60, "C"), (50, "D")):
        if marks >= limit:
            return letter
    return "F"
