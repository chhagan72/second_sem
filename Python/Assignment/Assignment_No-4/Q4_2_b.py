from Q4_1_a import MathsOperations
from Q4_2_a import StatsOperations

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

math_operations_instance = MathsOperations()
stats_operations_instance = StatsOperations()

max_result = math_operations_instance.find_maximum(num1, num2, num3)
min_result = math_operations_instance.find_minimum(num1, num2, num3)

average_result = stats_operations_instance.find_average(num1, num2, num3)
median_result = stats_operations_instance.find_median(num1, num2, num3)

print(f"\nMath Operations:")
print(f"Maximum of {num1}, {num2}, and {num3} is: {max_result}")
print(f"Minimum of {num1}, {num2}, and {num3} is: {min_result}")

print(f"\nStats Operations:")
print(f"Average of {num1}, {num2}, and {num3} is: {average_result}")
print(f"Median of {num1}, {num2}, and {num3} is: {median_result}")
