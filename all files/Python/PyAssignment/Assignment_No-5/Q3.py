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