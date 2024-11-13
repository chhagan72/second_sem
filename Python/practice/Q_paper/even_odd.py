# Write a program to check the number entered by user is even or odd.
# Program should accept integer digits only
try:
    def even_odd(num):
        if num % 2 == 0:
            print("even")
        else:
            print("odd")
    even_odd(int(input("Enter a number: "))) 
except ValueError:
    print("Invalid input")