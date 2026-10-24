"""Shopping cart built with TDD (see test_cart.py)."""


class Cart:
    def __init__(self):
        self._items = {}                      # name -> (price, qty)

    def add(self, name: str, price: float, qty: int = 1) -> None:
        if price < 0 or qty <= 0:
            raise ValueError("price must be >= 0 and qty > 0")
        old_price, old_qty = self._items.get(name, (price, 0))
        self._items[name] = (price, old_qty + qty)

    def total(self, discount_percent: float = 0) -> float:
        subtotal = sum(p * q for p, q in self._items.values())
        return round(subtotal * (1 - discount_percent / 100), 2)

    def count(self) -> int:
        return sum(q for _, q in self._items.values())
