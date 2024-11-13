import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Example usage:
email = "user@example.com"
if validate_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")