'''
1.	Demonstrate ZeroDivisionError, NameError, TypeError.
'''
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

#OutPut
'''
Error: division by zero
Error: name 'undefined_variable' is not defined
Error: can only concatenate str (not "int") to str
'''
'''
2.	Demonstrate all keywords of exception with appropriate example.
'''
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"General Error: {e}")
else:
    print("No exception occurred.")
finally:
    print("Finally block executed.")
#OutPut
'''
Error: division by zero
Finally block executed.
'''
'''
3.	Create a class Student with attributes roll no, name, age and course. Initialize values through parameterized constructor. If age of student is not in between 15 and 21 then generate user-defined exception “AgeNotWithinRangeException”. If name contains numbers or special symbols raise exception “NameNotValidException”. Define the two exception classes.
'''
class AgeNotWithinRangeException(Exception):
    def __init__(self, message):
        self.message = message

class NameNotValidException(Exception):
    def __init__(self, message):
        self.message = message

class Student:
    def __init__(self, roll_no, name, age, course):
        if not name.isalpha():
            raise NameNotValidException("Name should not contain numbers or special symbols")
        if age < 15 or age > 21:
            raise AgeNotWithinRangeException("Age should be between 15 and 21")
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course

try:
    s = Student(1, "John Doe", 22, "Computer Science")
except AgeNotWithinRangeException as e:
    print(e)
except NameNotValidException as e:
    print(e)

try:
    s = Student(1, "John#Doe", 20, "Computer Science")
except AgeNotWithinRangeException as e:
    print(e)
except NameNotValidException as e:
    print(e)

try:
    s = Student(1, "John Doe", 14, "Computer Science")
except AgeNotWithinRangeException as e:
    print(e)
except NameNotValidException as e:
    print(e)
#OutPut
'''
Name should not contain numbers or special symbols
Name should not contain numbers or special symbols
Name should not contain numbers or special symbols
'''
'''

'''