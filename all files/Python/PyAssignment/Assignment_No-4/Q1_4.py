import re

def validate_mobile_number(mobile_number):
    pattern = r'^[1-9]\d{9}$'
    return re.match(pattern, mobile_number) is not None

# Example usage:
mobile_number = "1234567890"
if validate_mobile_number(mobile_number):
    print(f"{mobile_number} is a valid mobile number.")
else:
    print(f"{mobile_number} is not a valid mobile number.")
