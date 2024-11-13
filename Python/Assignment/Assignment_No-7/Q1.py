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
