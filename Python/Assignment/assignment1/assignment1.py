# 1.	A simple program that displays “Hello, World!”. It's often used to illustrate the syntax of the language.
print("Hello, World!")


# Q2.	Give the example of interactive mode and script mode
# 1. Interactive Mode

# $ python
# Python 3.9.1 (default, Jan 12 2021, 15:25:38) 
# [GCC 10.2.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print("Hello, World!")
# Hello, World!
# >>> 2 + 3
# 5
# >>> exit()

# 2. Script Mode

# File: hello.py
print("Hello, World!")

# $ python hello.py
# Hello, World!



# Q3.	Write a program on types of variable and also which type of variable is immutable or mutable
# Eg .List -> list=[1,2,3], int, boolean, …..etc.

integer_var = 5
float_var = 3.14
string_var = "Hello, World!"
bool_var = True
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
set_var = {7, 8, 9}
dict_var = {'a': 1, 'b': 2, 'c': 3}

print("Type of integer_var:", type(integer_var))
print("Type of float_var:", type(float_var))
print("Type of string_var:", type(string_var))
print("Type of bool_var:", type(bool_var))
print("Type of list_var:", type(list_var))
print("Type of tuple_var:", type(tuple_var))
print("Type of set_var:", type(set_var))
print("Type of dict_var:", type(dict_var))

print("Mutable variables:")
mutable_variables = [list_var, set_var, dict_var]
for var in mutable_variables:
    print(type(var))

print("Immutable variables:")
immutable_variables = [integer_var, float_var, string_var, bool_var, tuple_var]
for var in immutable_variables:
    print(type(var))


# Q4.	Write a program on operators with priority and associativity
result = 10 + 5 * 2  
print("Result of 10 + 5 * 2:", result)
x = 10
y = 5
z = 5
print("x > y:", x > y)  
print("y < z:", y < z)  
print("x == y:", x == y)  
print("y != z:", y != z)  
a = True
b = False
c = True
print("a and b:", a and b)  
print("a or b:", a or b)    
print("not b:", not b)      
x = 10
x += 5  
print("Value of x after x += 5:", x)
p = 60       
q = 13       
print("p & q:", p & q)   
print("p | q:", p | q)   
print("p ^ q:", p ^ q)   
print("~p:", ~p)         
print("p << 2:", p << 2) 
print("p >> 2:", p >> 2) 


list_var = [1, 2, 3, 4, 5]
print("3 in list_var:", 3 in list_var)   
print("6 not in list_var:", 6 not in list_var) 


# Q5.	Write a simple program for using comment.
print("Hello, World!") 

"""
This is a multi-line comment.
You can write multiple lines here
without using the # symbol repeatedly.
"""
print("Hello, World!")


# Q6.	A Simple program In Python Program to Add Two Numbers. Accept number from user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 + num2
print("The sum of", num1, "and", num2, "is:", result)

# Q7.	Write A Program in python language to Find the Square Root.
import math
num = float(input("Enter a number: "))
square_root = math.sqrt(num)
print("The square root of", num, "is:", square_root)

# Q8.	Write A Python Program to Calculate the Area of a Triangle.
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle with base", base, "and height", height, "is:", area)

# Q9.	Write A Python Program to Solve Quadratic Equation.
import math
a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The roots of the quadratic equation are:", root1, "and", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("The root of the quadratic equation is:", root)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print("The roots of the quadratic equation are:", real_part, "+", imaginary_part, "i and",
          real_part, "-", imaginary_part, "i")


# Q10.	Write A Python program to check if a number is positive, negative or zero
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Q11. Write A Python Program to Check if a Number is Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Q12.	Write A Python Program to Check Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# Q13.	Write A Python Program to Find the Largest Among Three Numbers 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number among", num1, ",", num2, ", and", num3, "is:", largest)


# Q14. Write A Python Program to Check Prime Number
def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")


# Q15. Write a program on complex number.
complex_num1 = 3 + 4j
complex_num2 = 2 - 5j
sum_complex = complex_num1 + complex_num2
print("Sum of", complex_num1, "and", complex_num2, "is:", sum_complex)
difference_complex = complex_num1 - complex_num2
print("Difference of", complex_num1, "and", complex_num2, "is:", difference_complex)

product_complex = complex_num1 * complex_num2
print("Product of", complex_num1, "and", complex_num2, "is:", product_complex)

quotient_complex = complex_num1 / complex_num2
print("Quotient of", complex_num1, "and", complex_num2, "is:", quotient_complex)
conjugate_complex = complex_num1.conjugate()
print("Conjugate of", complex_num1, "is:", conjugate_complex)
real_part = complex_num1.real
imaginary_part = complex_num1.imag
print("Real part of", complex_num1, "is:", real_part)
print("Imaginary part of", complex_num1, "is:", imaginary_part)
