'''
Write a program to swap two numbers without using temporary variable
accept input from the user.
'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swapping: ", a, b)

a = a + b
b = a - b
a = a - b

print("After swapping: ", a, b)