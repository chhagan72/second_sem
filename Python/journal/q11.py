# 11 Write a Python class named Student with two attributes student_name, marks. Modify the
# attribute values of the said class and print the original and modified values of the said
# attributes. 
class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

# Create an instance of the Student class
student = Student("John", 85)

# Print the original attribute values
print("Original Student Name:", student.student_name)
print("Original Marks:", student.marks)

# Modify the attribute values
student.student_name = "Alice"
student.marks = 90

# Print the modified attribute values
print("Modified Student Name:", student.student_name)
print("Modified Marks:", student.marks)
