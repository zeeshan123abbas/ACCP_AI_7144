import unittest
from app import grade


class GradeTests(unittest.TestCase):
    def test_grades(self):
        self.assertEqual([grade(m) for m in (95, 75, 65, 55, 10)], ["A", "B", "C", "D", "F"])

    def test_invalid(self):
        with self.assertRaises(ValueError):
            grade(-5)


if __name__ == "__main__":
    unittest.main()
