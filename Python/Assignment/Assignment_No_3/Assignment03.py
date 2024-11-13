'''
LIST
1.	Write a program for demonstration of List using following functions - :
Create a list as per needed
a.	Create a list and display each on single line using looping statement.
'''
my_list = ["Apple", "Banana", "Cherry", "Date", "Fig"]
for item in my_list:
    print(item)
#OutPut
'''
Apple
Banana
Cherry
Date  
Fig
'''

'''
b.	Initialize the first list to second list.
'''
first_list = [1, 2, 3, 4, 5]
second_list = list(first_list)
print(second_list)
#OutPut
'''
[1, 2, 3, 4, 5]
'''

'''
c.	Access the specific element of list from user entered position.
'''
my_list = ["Apple", "Banana", "Cherry", "Date", "Fig"]
position = int(input("Enter the position to access (1 to {}): ".format(len(my_list))))
if 1 <= position <= len(my_list):
    selected_element = my_list[position - 1]
    print("Element at position {}: {}".format(position, selected_element))
else:
    print("Invalid position. Please enter a valid position.")
#OutPut
'''
Enter the position to access (1 to 5): 2
Element at position 2: Banana
'''

'''
d.	Delete the specific elements of from user entered position and elements.
'''
my_list = ["Apple", "Banana", "Cherry", "Date", "Fig"]
print("Current List:", my_list)
position = int(input("Enter the position to delete (1 to {}): ".format(len(my_list))))
if 1 <= position <= len(my_list):
    del my_list[position - 1]
    print("Element at position {} deleted.".format(position))
    print("Updated List:", my_list)
else:
    print("Invalid position. Please enter a valid position.")
#OutPut
'''
Current List: ['Apple', 'Banana', 'Cherry', 'Date', 'Fig']
Enter the position to delete (1 to 5): 3
Element at position 3 deleted.
Updated List: ['Apple', 'Banana', 'Date', 'Fig']
'''

'''
e.	Concatenate the first list to second list.
'''
first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9, 10]
con_list = second_list + first_list
print("Concatenated List:", con_list)
#OutPut
'''
Concatenated List: [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
'''

'''
f.	Repeats a list from user entered times.
'''
my_list = ["Apple", "Banana", "Cherry"]
r_count = int(input("Enter the number of times to repeat the list: "))
r_list = my_list*r_count
print(my_list)
print(r_list)
#OutPut
'''
Enter the number of times to repeat the list: 2
['Apple', 'Banana', 'Cherry']
['Apple', 'Banana', 'Cherry', 'Apple', 'Banana', 'Cherry']
'''

'''
g.	Operates the all membership operators on list.
'''
my_list = ["Apple", "Banana", "Cherry", "Date", "Fig"]
element_to_check = input("Enter an element to check if it's in the list: ")
if element_to_check in my_list:
    print(f"{element_to_check} is in the list.")
else:
    print(f"{element_to_check} is not in the list.")
element_to_check_not_in = input("Enter an element to check if it's not in the list: ")
if element_to_check_not_in not in my_list:
    print(f"{element_to_check_not_in} is not in the list.")
else:
    print(f"{element_to_check_not_in} is in the list.")
#OutPut
'''
Enter an element to check if it's in the list: Banana
Banana is in the list.
Enter an element to check if it's not in the list: Cherry
Cherry is not in the list.
'''

'''
h.	Perform the slicing operation on the list – [:n],[n:],[:],[n:m],[:-n],[-n:]
'''
my_list = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Honeydew"]
n = 3
m = 6
slice_1 = my_list[:n]
slice_2 = my_list[n:]
slice_3 = my_list[:]
slice_4 = my_list[n:m]
slice_5 = my_list[:-n]
slice_6 = my_list[-n:]
print("Original List:", my_list)
print("Slice [:n]:", slice_1)
print("Slice [n:]:", slice_2)
print("Slice [:]:", slice_3)
print("Slice [n:m]:", slice_4)
print("Slice [:-n]:", slice_5)
print("Slice [-n:]:", slice_6)
#OutPut
'''
Original List: ['Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grape', 'Honeydew']
Slice [:n]: ['Apple', 'Banana', 'Cherry']
Slice [n:]: ['Date', 'Fig', 'Grape', 'Honeydew']
Slice [:]: ['Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grape', 'Honeydew']
Slice [n:m]: ['Date', 'Fig', 'Grape']
Slice [:-n]: ['Apple', 'Banana', 'Cherry', 'Date']
Slice [-n:]: ['Fig', 'Grape', 'Honeydew']
'''

'''
i.	Compere the list and perform the appropriate all results.
'''
list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 7]
if list_1 == list_2:
    print("Both lists are equal.")
else:
    print("Both lists are not equal.")
common_elements = set(list_1) & set(list_2)
if common_elements:
    print("Common elements:", list(common_elements))
else:
    print("No common elements.")
#OutPut
'''
Both lists are not equal.
Common elements: [3, 4, 5]
'''

'''
j.	Write a program for List comprehension
'''
n = int(input("Enter the value of n: "))
squares = [i**2 for i in range(1, n+1)]
print("List of Squares:", squares)
#OutPut
'''
Enter the value of n: 23
List of Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529]
'''

'''
k.	Use following in built function –
i.	append()
ii.	strip()
iii.	len()
iv. insert()
v.	extend()
vi.	sort()
vii.	remove()
viii.	reverse()
ix.	pop())
'''
'''
# Create an empty list
my_list = []

# i. append(): Add elements to the end of the list
my_list.append("Apple")
my_list.append("Banana")
my_list.append("Cherry")

# Display the list after appending elements
print("List after append:", my_list)

# ii. strip(): Remove leading and trailing whitespaces from elements
my_list_with_spaces = ["  Orange  ", "  Mango  ", "  Pineapple  "]
stripped_list = [fruit.strip() for fruit in my_list_with_spaces]

# Display the stripped list
print("Stripped List:", stripped_list)

# iii. len(): Get the length of the list
list_length = len(my_list)
print("Length of the list:", list_length)

# iv. insert(): Insert an element at a specific index
my_list.insert(1, "Date")  # Insert "Date" at index 1
print("List after insert:", my_list)

# v. extend(): Extend the list by appending elements from another iterable
additional_fruits = ["Fig", "Grapes"]
my_list.extend(additional_fruits)
print("List after extending:", my_list)

# vi. sort(): Sort the list in ascending order
my_list.sort()
print("List after sorting:", my_list)

# vii. remove(): Remove the first occurrence of a specific element
my_list.remove("Banana")
print("List after removing 'Banana':", my_list)

# viii. reverse(): Reverse the elements of the list in-place
my_list.reverse()
print("List after reversing:", my_list)

# ix. pop(): Remove and return the element at a specific index (default is the last element)
popped_element = my_list.pop(2)  # Remove and return the element at index 2
print("List after popping element at index 2:", my_list)
print("Popped element:", popped_element)
'''
#OutPut
'''
List after append: ['Apple', 'Banana', 'Cherry']
Stripped List: ['Orange', 'Mango', 'Pineapple']
Length of the list: 3
List after insert: ['Apple', 'Date', 'Banana', 'Cherry']
List after extending: ['Apple', 'Date', 'Banana', 'Cherry', 'Fig', 'Grapes']
List after sorting: ['Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grapes']
List after removing 'Banana': ['Apple', 'Cherry', 'Date', 'Fig', 'Grapes']
List after reversing: ['Grapes', 'Fig', 'Date', 'Cherry', 'Apple']
List after popping element at index 2: ['Grapes', 'Fig', 'Cherry', 'Apple']
Popped element: Date
'''
'''
l.	Create user defined function for list –
i.	Count the number of elements.
ii.	Sort the list
iii.	Reverse the list
'''
my_list = [4, 2, 8, 1, 5]
count_result = len(my_list)
print("Number of elements in the list:", count_result)

sorted_result = sorted(my_list)
print("Sorted list:", sorted_result)

reversed_result = list(my_list)
print("Reversed list:", reversed_result)
#Output
'''
Number of elements in the list: 5
Sorted list: [1, 2, 4, 5, 8]
Reversed list: [4, 2, 8, 1, 5]
'''

'''
TUPLE
2.	Write a program for demonstration of tuple using following functions - : Create a tuple as per needed.
a.	Create a tuple and display each elements on single line.
'''
my_tuple = (1, 2, 3, 4, 5)
for element in my_tuple:
    print(element)
print(type(my_tuple))
#Output
'''
1
2
3
4
5
<class 'tuple'>
'''
'''
b.	Access the specific elements from user entered position.
'''
my_tuple = ("Apple", "Banana", "Cherry", "Date", "Fig")
print(type(my_tuple))
position = int(input("Enter the position to access (1 to {}): ".format(len(my_tuple))))
if 1 <= position <= len(my_tuple):
    selected_element = my_tuple[position - 1]
    print("Element at position {}: {}".format(position, selected_element))
else:
    print("Invalid position. Please enter a valid position.")
#Output
'''
<class 'tuple'>
Enter the position to access (1 to 5): 3
Element at position 3: Cherry
'''
'''
c.	Search the specific elements and return the position if elements is found.
'''
my_tuple = ("Apple", "Banana", "Cherry", "Date", "Fig")
search_element = input("Enter the element to search: ")
if search_element in my_tuple:
    position = my_tuple.index(search_element) + 1
    print("Element '{}' found at position {}".format(search_element, position))
else:
    print("Element '{}' not found in the tuple.".format(search_element))
#Output
'''
Enter the element to search: Cherry
Element 'Cherry' found at position 3
'''
'''
d.	Try to modify tuple. If tuple is not modify then give the appropriate message.
'''
my_tuple = ("Apple", "Banana", "Cherry", "Date", "Fig")
try:
    my_tuple[0] = "Orange"
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable and cannot be modified.")
#Output
'''
Error: 'tuple' object does not support item assignment
Tuples are immutable and cannot be modified.
'''
'''
e.	Remove the specific elements from user and display reaming elements on single line each.
'''
my_tuple = ("Apple", "Banana", "Cherry", "Date", "Fig")
element_to_remove = input("Enter the element to remove: ")
new_tuple = tuple(element for element in my_tuple if element != element_to_remove)
for element in new_tuple:
    print(element)
#Output
'''
Enter the element to remove: Date
Apple
Banana
Cherry
Fig
'''
'''
f.	Perform the following in built function on tuple –
i.	cmp()
ii.	len()
iii.	max()
iv.	tuple()
vi. type()
'''
# Creating a tuple
my_tuple = (5, 2, 8, 1, 7)

# i. len(): Get the length of the tuple
tuple_length = len(my_tuple)
print("Length of the tuple:", tuple_length)

# ii. max(): Get the maximum value in the tuple
max_value = max(my_tuple)
print("Maximum value in the tuple:", max_value)

# iii. tuple(): Convert another iterable (e.g., list) to a tuple
my_list = [10, 20, 30]
converted_tuple = tuple(my_list)
print("Converted tuple from list:", converted_tuple)

# iv. type(): Get the type of the tuple
tuple_type = type(my_tuple)
print("Type of the tuple:", tuple_type)

#Output
'''
Length of the tuple: 5
Maximum value in the tuple: 8
Converted tuple from list: (10, 20, 30)
Type of the tuple: <class 'tuple'>
'''

'''
SET and Dictionary
3.	Demonstrate all set operation .
'''
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

#OutPut
'''
Initial Dictionary: {'apple': 5, 'banana': 3, 'cherry': 8, 'date': 2}
Number of bananas: 3

Traversing and Updating:
apple: 5
banana: 3
cherry: 8
date: 2

Dictionary after appending 'grape': {'apple': 5, 'banana': 3, 'cherry': 8, 'date': 2, 'grape': 4}
Dictionary after updating 'cherry': {'apple': 5, 'banana': 3, 'cherry': 10, 'date': 2, 'grape': 4}
Dictionary after removing 'date': {'apple': 5, 'banana': 3, 'cherry': 10, 'grape': 4}
Removed value: 2

Dictionary after appending 'kiwi': {'apple': 5, 'banana': 3, 'cherry': 10, 'grape': 4, 'kiwi': 6}
'''
'''
4.	Demonstrate following dictionary operations –
a.	Create dictionary.
b.	Access the elements from dictionary
c.	Traversing, Appending, Updating and deleting elements.
d.	Appending element to dictionary
'''
# Create two sets
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# 1. Union of sets
union_result = set_A | set_B
print("Union of sets:", union_result)

# 2. Intersection of sets
intersection_result = set_A & set_B
print("Intersection of sets:", intersection_result)

# 3. Difference between sets (elements in set_A but not in set_B)
difference_result_A_B = set_A - set_B
print("Difference A - B:", difference_result_A_B)

# 4. Difference between sets (elements in set_B but not in set_A)
difference_result_B_A = set_B - set_A
print("Difference B - A:", difference_result_B_A)

# 5. Symmetric difference between sets (elements in either set, but not both)
symmetric_difference_result = set_A ^ set_B
print("Symmetric Difference:", symmetric_difference_result)

# 6. Check if one set is a subset of another
is_subset = set_A.issubset(set_B)
print("Is A a subset of B?", is_subset)

# 7. Check if one set is a superset of another
is_superset = set_A.issuperset(set_B)
print("Is A a superset of B?", is_superset)

# 8. Add an element to a set
set_A.add(6)
print("Set A after adding 6:", set_A)

# 9. Remove an element from a set
set_B.remove(8)
print("Set B after removing 8:", set_B)

#OutPut
'''
Union of sets: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection of sets: {4, 5}
Difference A - B: {1, 2, 3}
Difference B - A: {8, 6, 7}
Symmetric Difference: {1, 2, 3, 6, 7, 8}
Is A a subset of B? False
Is A a superset of B? False
Set A after adding 6: {1, 2, 3, 4, 5, 6}
Set B after removing 8: {4, 5, 6, 7}
'''
'''
5.	Use Dictionary function - :\
a.	cmp()
b.	len()
c.	clear()
d.	get()
e.	has_key()
f.	values()
g.	items()
h.	key()
i.	update()
j.	values()
k.	items()
l.	key()
m.	update()
'''
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

#OutPut
'''
Length of the dictionary: 4
Dictionary after clear: {}
Value for 'apple': Not found
Values in the dictionary: []
Key-Value pairs: []
Dictionary after updating: {'grape': 4, 'kiwi': 6}
Updated values in the dictionary: [4, 6]
Updated Key-Value pairs: [('grape', 4), ('kiwi', 6)]
Dictionary after additional update: {'grape': 4, 'kiwi': 6, 'orange': 3}
'''
'''
'''