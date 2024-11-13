import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or access the "company" database
db = client["company"]

# Create or access the "employees" collection
collection = db["employees"]

# i) Display all employees in "Accounts" department
def display_accounts_department():
    accounts_employees = collection.find({"dept": "Accounts"})
    print("Employees in Accounts department:")
    for employee in accounts_employees:
        print(employee)

# ii) Delete employee with ID - 210345
def delete_employee_by_id(employee_id):
    collection.delete_one({"ID": employee_id})
    print(f"Employee with ID {employee_id} deleted successfully.")

# iii) Update phone with new phone for employee ID - 123
def update_phone(employee_id, new_phone):
    collection.update_one({"ID": employee_id}, {"$set": {"phone": new_phone}})
    print(f"Phone updated successfully for employee with ID {employee_id}.")

if __name__ == "__main__":
    # Insert sample data
    employees_data = [
        {"ID": 123, "name": "Alice", "address": "123 Main St", "phone": "123-456-7890", "email": "alice@example.com", "dept": "Accounts"},
        {"ID": 210345, "name": "Bob", "address": "456 Elm St", "phone": "456-789-0123", "email": "bob@example.com", "dept": "HR"},
        {"ID": 567, "name": "Charlie", "address": "789 Oak St", "phone": "789-012-3456", "email": "charlie@example.com", "dept": "Accounts"}
    ]
    collection.insert_many(employees_data)

    # i) Display all employees in "Accounts" department
    display_accounts_department()

    # ii) Delete employee with ID - 210345
    delete_employee_by_id(210345)

    # iii) Update phone with new phone for employee ID - 123
    update_phone(123, "987-654-3210")

    # Display updated Accounts department
    print("\nUpdated Accounts department:")
    display_accounts_department()
