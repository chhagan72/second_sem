try:
    result = 5 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    variable = undefined_variable
except NameError as e:
    print(f"Error: {e}")

try:
    result = "5" + 2
except TypeError as e:
    print(f"Error: {e}")
