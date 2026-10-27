# encoding_demo.py - why character encoding matters
# Text is stored as bytes; the ENCODING is the rule that maps characters to bytes.
import pandas as pd

text = "Karachi کراچی"                    # English + Urdu

# 1. Encode to bytes with UTF-8 (supports every language)
data = text.encode("utf-8")
print("UTF-8 bytes:", data)
print("Decoded back:", data.decode("utf-8"))

# 2. The wrong encoding gives "mojibake" (garbled text)
print("Wrong decoding:", data.decode("latin-1"))

# 3. Saving and reading a CSV with Urdu text
df = pd.DataFrame({"city": ["Karachi", "Lahore"], "urdu": ["کراچی", "لاہور"]})
df.to_csv("cities_utf8.csv", index=False, encoding="utf-8")
print(pd.read_csv("cities_utf8.csv", encoding="utf-8"))

# 4. If a file fails with UnicodeDecodeError, try another encoding
try:
    pd.read_csv("cities_utf8.csv", encoding="ascii")
except UnicodeDecodeError as error:
    print("\nASCII cannot read Urdu:", type(error).__name__)
# Tip: Excel on Windows likes encoding="utf-8-sig" when you save CSVs
