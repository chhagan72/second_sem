# Write a python program to validate an email address by using regular expression. 
import re

def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Test cases
emails_to_test = [
    "example@example.com",
    "user123@example.co.uk",
    "user.name@example.org",
    "invalid-email",
    "invalid@.com",
    "@example.com",
    "user@examplecom"
]

for email in emails_to_test:
    if validate_email(email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is not a valid email address.")
