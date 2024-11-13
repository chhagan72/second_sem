from Q4_1_a import MathsOperations

# Usage of the user-defined module
num1, num2, num3 = 10, 5, 8
math_operations_instance = MathsOperations()

# Find the maximum of three numbers
max_result = math_operations_instance.find_maximum(num1, num2, num3)
print(f"Maximum of {num1}, {num2}, and {num3} is: {max_result}")

# Find the minimum of three numbers
min_result = math_operations_instance.find_minimum(num1, num2, num3)
print(f"Minimum of {num1}, {num2}, and {num3} is: {min_result}")
