"""Unit tests written FIRST (Red), then cart.py made them pass (Green).
Run: python -m unittest test_cart.py -v
"""
import unittest
from cart import Cart


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_new_cart_is_empty(self):
        self.assertEqual(self.cart.total(), 0)
        self.assertEqual(self.cart.count(), 0)

    def test_add_items_updates_total(self):
        self.cart.add("Biryani", 450, 2)
        self.cart.add("Raita", 80)
        self.assertEqual(self.cart.total(), 980)

    def test_adding_same_item_increases_quantity(self):
        self.cart.add("Tea", 60)
        self.cart.add("Tea", 60, 2)
        self.assertEqual(self.cart.count(), 3)

    def test_discount(self):
        self.cart.add("Pizza", 1000)
        self.assertEqual(self.cart.total(discount_percent=10), 900)

    def test_invalid_quantity_raises(self):
        with self.assertRaises(ValueError):
            self.cart.add("Juice", 150, 0)


if __name__ == "__main__":
    unittest.main()
