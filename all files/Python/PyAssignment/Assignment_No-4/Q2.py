# 1.math Module:
# The math module provides mathematical functions.
import math

# Example: Calculate the square root of a number
number = 25
sqrt_result = math.sqrt(number)
print(f"Square root of {number}: {sqrt_result}")

# 2. datetime Module:
# The datetime module is used for working with dates and times.

from datetime import datetime

# Example: Get the current date and time
current_datetime = datetime.now()
print(f"Current date and time: {current_datetime}")

# 3. random Module:
# The random module is used for generating random numbers.

import random

# Example: Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")

# 4. os Module:
# The os module provides a way of using operating system-dependent functionality.

import os

# Example: Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# 5. json Module:
# The json module is used for encoding and decoding JSON data.

import json

# Example: Encode a Python dictionary into JSON format
data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data)
print(f"JSON representation of the data: {json_data}")