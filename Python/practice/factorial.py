# Write a program to find the factorial of a number using recursion.

def main(n):
    if n == 0:
        return 1
    else:
        return n * main(n - 1)

try:
    n = int(input("Enter a number: "))
    print(main(n))

except ValueError as e:
    print("Please enter a valid number",e)