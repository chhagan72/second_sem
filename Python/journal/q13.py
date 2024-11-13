# 13] Write a python program to validate the password by using regular expression.
# a. Complexity requirement is that we need at least one capital letter, one number and one
# special character.
# b. We also need the length of the password to be between 8 and 18.
import re

def validate_password(password):
    # Ensure length is between 8 and 18 characters
    if len(password) < 8 or len(password) > 18:
        return False

    # Ensure at least one capital letter, one number, and one special character
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}|:<>?]).+$'
    if re.match(pattern, password):
        return True
    else:
        return False

# Test cases
passwords_to_test = ["Abc123!@#", "Password123", "short", "Toolongpassword123456", "NoSpecialCharacter123"]
for password in passwords_to_test:
    if validate_password(password):
        print(f"'{password}' is a valid password.")
    else:
        print(f"'{password}' is not a valid password.")
