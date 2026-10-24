"""Run: python -m unittest -v"""
import unittest
from app import grade


class GradeTests(unittest.TestCase):
    def test_boundaries(self):
        self.assertEqual(grade(80), "A")
        self.assertEqual(grade(79), "B")
        self.assertEqual(grade(50), "D")
        self.assertEqual(grade(49), "F")

    def test_invalid(self):
        with self.assertRaises(ValueError):
            grade(101)


if __name__ == "__main__":
    unittest.main()
