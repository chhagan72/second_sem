# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30

# Modifying values
my_dict["age"] = 35
print(my_dict["age"])   # Output: 35

# Adding new key-value pairs
my_dict["email"] = "alice@example.com"
print(my_dict)          # Output: {'name': 'Alice', 'age': 35, 'city': 'New York', 'email': 'alice@example.com'}

# Deleting a key-value pair
del my_dict["city"]
print(my_dict)          # Output: {'name': 'Alice', 'age': 35, 'email': 'alice@example.com'}
