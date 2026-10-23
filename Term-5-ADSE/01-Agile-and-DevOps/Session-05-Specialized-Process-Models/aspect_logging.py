"""A tiny taste of Aspect-Oriented ideas using Python decorators.

The logging/timing concern is written ONCE and applied to many functions.
Run: python aspect_logging.py
"""
import functools
import time


def log_and_time(func):
    """'Advice' that runs around every decorated function (a join point)."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] calling {func.__name__} args={args} kwargs={kwargs}")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"[LOG] {func.__name__} returned {result!r} in {elapsed:.2f} ms")
        return result
    return wrapper


@log_and_time
def calculate_fee(distance_km: float) -> float:
    return 120 + distance_km * 35          # base fare + per-km rate (PKR)


@log_and_time
def apply_discount(amount: float, percent: int) -> float:
    return round(amount * (1 - percent / 100), 2)


if __name__ == "__main__":
    fee = calculate_fee(8.5)
    apply_discount(fee, 10)
