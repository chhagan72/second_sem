# 17 Write a python program which raises the exception with a message. 
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed!")
    else:
        return x / y

# Test cases
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)
else:
    print("Result:", result)
