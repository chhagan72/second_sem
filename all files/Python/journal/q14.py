# Write a python program to validate the URL by using regular expression. 16] 
import re

def validate_url(url):
    # Regular expression pattern for URL validation
    pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    if re.match(pattern, url):
        return True
    else:
        return False

# Test cases
urls_to_test = [
    "http://www.example.com",
    "https://example.com/page",
    "ftp://ftp.example.com/file",
    "invalid-url",
    "http://www.invalid url.com",
    "https://www.invalid?url.com"
]

for url in urls_to_test:
    if validate_url(url):
        print(f"'{url}' is a valid URL.")
    else:
        print(f"'{url}' is not a valid URL.")
