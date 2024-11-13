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
