# 16 Write a python program which consists of - try, except, else, finally blocks.
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print("Division successful.")
        print("Result:", result)
    finally:
        print("Executing 'finally' block.")


# Test cases
print("Test Case 1:")
divide(10, 2)

print("\nTest Case 2:")
divide(10, 0)
