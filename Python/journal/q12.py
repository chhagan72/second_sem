# 12 Write a Python program to match a string that contains only upper and lowercase
# letters, numbers, and underscores. 
import re

def match_string(text):
    pattern = r'^[a-zA-Z0-9_]*$'
    if re.match(pattern, text):
        return True
    else:
        return False

# Test cases
strings_to_test = ["Hello_World123", "abcDEF456", "123_456", "special@chars", "Spaces Not Allowed"]
for text in strings_to_test:
    if match_string(text):
        print(f"'{text}' matches the pattern.")
    else:
        print(f"'{text}' does not match the pattern.")
