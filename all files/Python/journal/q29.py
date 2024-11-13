# 30]Write a Menu Driver Program to add, display, update, delete and exit in a student database
# containing Student_id,Student_name,Course through Python-MongoDB connectivity.
import pymongo

# Function to connect to MongoDB
def connect_to_mongodb():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["student_database"]
    collection = db["students"]
    return collection

# Function to add a student record
def add_student(collection):
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    student = {"Student_id": student_id, "Student_name": student_name, "Course": course}
    collection.insert_one(student)
    print("Student added successfully!")

# Function to display all student records
def display_students(collection):
    students = collection.find()
    for student in students:
        print(student)

# Function to update a student record
def update_student(collection):
    student_id = input("Enter Student ID to update: ")
    new_course = input("Enter new Course: ")
    collection.update_one({"Student_id": student_id}, {"$set": {"Course": new_course}})
    print("Student record updated successfully!")

# Function to delete a student record
def delete_student(collection):
    student_id = input("Enter Student ID to delete: ")
    collection.delete_one({"Student_id": student_id})
    print("Student record deleted successfully!")

# Main function
def main():
    collection = connect_to_mongodb()
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(collection)
        elif choice == "2":
            display_students(collection)
        elif choice == "3":
            update_student(collection)
        elif choice == "4":
            delete_student(collection)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
