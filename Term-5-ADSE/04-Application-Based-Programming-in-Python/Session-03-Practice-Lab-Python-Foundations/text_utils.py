# text_utils.py - Lab 4: a small module of string helper functions

def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count = count + 1
    return count

def is_palindrome(word):
    clean = word.lower().replace(" ", "")
    return clean == clean[::-1]      # [::-1] reverses a string

def word_frequency(sentence):
    freq = {}
    for word in sentence.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq

if __name__ == "__main__":
    print(count_vowels("Karachi"))          # 3
    print(is_palindrome("Madam"))           # True
    print(word_frequency("to be or not to be"))
