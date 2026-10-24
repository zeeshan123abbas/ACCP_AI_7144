# test_text_utils.py - Lab 5: check our functions with simple assert tests
# If every assert is True, nothing happens. If one fails, Python shows an AssertionError.

from text_utils import count_vowels, is_palindrome, word_frequency

assert count_vowels("Python") == 1
assert count_vowels("AEIOU") == 5
assert is_palindrome("Race car") is True
assert is_palindrome("Flutter") is False
assert word_frequency("a b a") == {"a": 2, "b": 1}

print("All tests passed!")
