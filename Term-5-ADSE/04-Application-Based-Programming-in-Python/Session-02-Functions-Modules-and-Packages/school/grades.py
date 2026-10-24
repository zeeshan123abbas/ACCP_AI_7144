# school/grades.py - a module inside the "school" package

def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    return "F"
