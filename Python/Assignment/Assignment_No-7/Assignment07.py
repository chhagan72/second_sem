'''
1.	Create a student class with appropriate data members as per needed. Use public, protected, private at least one data members respectively. Create methods accept, display, calculateAverage of three subjects.
'''
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self._roll_number = roll_number
        self.__subject_scores = {'subject1': 0, 'subject2': 0, 'subject3': 0}

    def accept_details(self):
        print(f"\nEnter details for student {self.name} (Roll Number: {self._roll_number}):")
        self.name = input("Enter student name: ")
        self._roll_number = input("Enter roll number: ")
        self.__subject_scores['subject1'] = float(input("Enter marks for subject 1: "))
        self.__subject_scores['subject2'] = float(input("Enter marks for subject 2: "))
        self.__subject_scores['subject3'] = float(input("Enter marks for subject 3: "))

    def display_details(self):
        print(f"\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self._roll_number}")
        print(f"Subject Scores: {self.__subject_scores}")

    def calculate_average(self):
        average = sum(self.__subject_scores.values()) / len(self.__subject_scores)
        return average

student1 = Student(name="John Doe", roll_number="12345")
student1.accept_details()
student1.display_details()
average_score = student1.calculate_average()
print(f"\nAverage Score: {average_score}")

#OutPut
'''
Enter details for student John Doe (Roll Number: 12345):
Enter student name: Chhagan
Enter roll number: 67
Enter marks for subject 1: 76
Enter marks for subject 2: 88
Enter marks for subject 3: 89

Student Details:
Name: Chhagan
Roll Number: 67
Subject Scores: {'subject1': 76.0, 'subject2': 88.0, 'subject3': 89.0}

Average Score: 84.33333333333333
'''
'''
2.	Demonstrate the Inheritance – Single, Multiple, Multilevl 
'''
# Single
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak() 
dog.bark()


# Multiple
class Flyable:
    def fly(self):
        print("Flying high")

class Animal:
    def speak(self):
        print("Animal speaks")

class Bird(Animal, Flyable):
    def chirp(self):
        print("Bird chirps")

bird = Bird()
bird.speak() 
bird.fly()
bird.chirp()  


# Multilevl
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def play(self):
        print("Puppy plays")

puppy = Puppy()
puppy.speak()  
puppy.bark()
puppy.play()
#OutPut
'''
# Single
Animal speaks
Dog barks

# Multiple
Animal speaks
Flying high
Bird chirps

# Multilevl
Animal speaks
Dog barks
Puppy plays
'''
'''
'''