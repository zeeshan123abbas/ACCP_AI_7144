"""Tiny module used to demonstrate a CI pipeline."""


def grade(marks: int) -> str:
    if not 0 <= marks <= 100:
        raise ValueError("marks must be 0-100")
    if marks >= 80:
        return "A"
    if marks >= 70:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 50:
        return "D"
    return "F"
