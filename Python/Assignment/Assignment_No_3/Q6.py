# Create a dictionary
my_dict = {'apple': 5, 'banana': 3, 'cherry': 8, 'date': 2}

# a. cmp() - Not valid in Python 3
# b. len()
length = len(my_dict)
print("Length of the dictionary:", length)

# c. clear()
my_dict.clear()
print("Dictionary after clear:", my_dict)

# d. get()
value = my_dict.get('apple', 'Not found')
print("Value for 'apple':", value)

# e. has_key() - Not valid in Python 3
# f. values()
values = list(my_dict.values())
print("Values in the dictionary:", values)

# g. items()
items = list(my_dict.items())
print("Key-Value pairs:", items)

# h. key() - Not valid in Python 3
# i. update()
my_dict.update({'grape': 4, 'kiwi': 6})
print("Dictionary after updating:", my_dict)

# j. values() (repeated)
values_updated = list(my_dict.values())
print("Updated values in the dictionary:", values_updated)

# k. items() (repeated)
items_updated = list(my_dict.items())
print("Updated Key-Value pairs:", items_updated)

# l. key() - Not valid in Python 3
# m. update() (repeated)
my_dict.update({'orange': 3})
print("Dictionary after additional update:", my_dict)
