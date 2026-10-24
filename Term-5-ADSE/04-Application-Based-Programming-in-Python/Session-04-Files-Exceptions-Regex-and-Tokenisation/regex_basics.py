# regex_basics.py - finding patterns in text with the re module

import re

text = "Call 0300-1234567 or 0321-7654321. Email: info@aptech.pk, admin@example.com"

# search(): first match only
first = re.search(r"\d{4}-\d{7}", text)
print("First phone:", first.group())

# findall(): every match, returned as a list
phones = re.findall(r"\d{4}-\d{7}", text)
print("All phones:", phones)

emails = re.findall(r"[\w.]+@[\w.]+\.\w+", text)
print("Emails:", emails)

# match(): checks only at the START of the string
print("Starts with 'Call'?", bool(re.match(r"Call", text)))

# sub(): replace matches (hide phone numbers)
hidden = re.sub(r"\d{4}-\d{7}", "XXXX-XXXXXXX", text)
print("Hidden:", hidden)

# fullmatch(): validate a whole value
cnic = "42101-1234567-1"
if re.fullmatch(r"\d{5}-\d{7}-\d", cnic):
    print(cnic, "is a valid CNIC format")
