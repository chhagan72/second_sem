# a. Create dictionary
my_dict = {'apple': 5, 'banana': 3, 'cherry': 8, 'date': 2}

# Display the initial dictionary
print("Initial Dictionary:", my_dict)

# b. Access elements from dictionary
banana_count = my_dict['banana']
print("Number of bananas:", banana_count)

# c. Traversing, Appending, Updating, and Deleting elements
# Traverse and print key-value pairs
print("\nTraversing and Updating:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Append new key-value pair
my_dict['grape'] = 4
print("\nDictionary after appending 'grape':", my_dict)

# Update the value for an existing key
my_dict['cherry'] = 10
print("Dictionary after updating 'cherry':", my_dict)

# Delete a key-value pair
removed_value = my_dict.pop('date')
print("Dictionary after removing 'date':", my_dict)
print("Removed value:", removed_value)

# d. Appending element to dictionary
new_fruit = 'kiwi'
new_count = 6
my_dict[new_fruit] = new_count
print("\nDictionary after appending 'kiwi':", my_dict)
