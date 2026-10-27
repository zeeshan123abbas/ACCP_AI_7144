# lab2_contact_validator.py - validate user data with regex and custom exceptions
# Skills: functions, regex, raising and catching exceptions

import re


class InvalidDataError(Exception):
    """Our own exception type for bad user data."""


def check_email(email):
    if not re.fullmatch(r"[\w.]+@[\w]+\.[a-z.]{2,}", email):
        raise InvalidDataError(f"'{email}' is not a valid email")
    return email


def check_mobile(mobile):
    # Pakistani mobile format: 03XX-XXXXXXX
    if not re.fullmatch(r"03\d{2}-\d{7}", mobile):
        raise InvalidDataError(f"'{mobile}' should look like 0300-1234567")
    return mobile


# Test data: some good, some bad
people = [
    {"name": "Ali", "email": "ali@gmail.com", "mobile": "0300-1234567"},
    {"name": "Sara", "email": "sara.gmail.com", "mobile": "0321-7654321"},
    {"name": "Usman", "email": "usman@yahoo.com", "mobile": "300-123"},
]

for person in people:
    try:
        check_email(person["email"])
        check_mobile(person["mobile"])
        print(f"OK      {person['name']}")
    except InvalidDataError as error:
        print(f"INVALID {person['name']}: {error}")
