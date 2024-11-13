# Python Lists
'''
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
'''
mylist=[1,2,3,4,5]
print(mylist," ", type(mylist))

t = ["apple", "banana", "cherry", "apple", "cherry"]
print(t)

# List Length
print(len(t)  , "This is the length of list t")

# List Items - Data Types
list1 =[True, False, True]
print(list1)

list2 = ["apple", "banana",True, False, True,1,2,3,4,5]
print(list2)

# type()
l1=type(list2)
print(l1)

# The list() Constructor
l3 = list(("apple","banana"))
print(l3, type(l3))


# Python - Access List Items
# Access Items
list3 = ["apple", "banana",True, False, True,1,2,3,4,5]
print(list3[3])

# Negative Indexing
print(list3[-6])

# Range of Indexes
print(list3[2:5])

# Revercing list using slicing
print(list3[::-1])

print(list3[-6:-1])
print(list3[-6:-1:2])
print(list3[-6:-1:3])

# Check if Item Exists
if True in list3:
    print("Yes True exists in the list")

# Check if Item Exists or not Exists
if "Trueee" in list3:
    print("Yes Trueee exists in the list")
else:
    print("No Trueee exists in the list")


# Change List Items
# Change Item Value

l2 = ["apple", "banana",True, False, True,1,2,3,4,5]
print(l2)
l2[2]=False
print(l2)

# Change a Range of Item Values
l2[0:2]=[9,"orange"]
print(l2)


# Add List Items
# Append Items
l3 = ["apple", "banana",True, False, True,1,2,3,4,5]
l3.append("mango")
print(l3)

# Insert Items
l3.insert(1,"cherry")
print(l3)


# Extend List
l4 = ["apple", "banana", "cherry", "apple", "cherry"]
l3.extend(l4)
print(l3)

# Remove List Items
# Remove Specified Item
l5 = ["apple", "banana",True, False, True,1,2,3,4,5]
print(l5)
l5.remove(4)
print(l5)

# Remove Specified Index
l5.pop()
print(l5)
l5.pop(2)
print(l5)

# using del keyword
del l5[0]
print(l5)

# #  To delete list
# del l5
# print(l5)


# Clear the List
l5.clear()
print(l5)


# Loop Lists
# Loop Through a List
l6 = ["apple", "banana",True, False, True,1,2,3,4,5]

for x in l6:
    print(x)


for i in range(len(l6)):
    print(l6[i])

# Using a While Loop
'''
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration
'''

while i < len(l6):
    print(l6[i])
    i+=1


while i < len(l6):
    print(i)
    i+=1
print(i)

# Looping Using List Comprehension
[print(x) for x in l6]

# Python - List Comprehension
'''
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside
'''
l7 = ["apple", "banana"]
nl =[]
for x in l7:
    if "a" in x:
        nl.append(x)
print(nl)


'''
The Syntax
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.

Condition
The condition is like a filter that only accepts the items that valuate to True.
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)


# Sort Lists
# Sort List Alphanumerically
l8 = ["apple", "banana","Aqq"]
l8.sort()
print(l8)

# Sort Descending
l8.sort(reverse=True)
print(l8)

l8.sort(reverse=False)
print(l8)

# Customize Sort Function
'''
You can also customize your own function by using the keyword argument key = function.
The function will return a number that will be used to sort the list (the lowest number first)
'''

def myfunc(n):
    return abs(n - 50)

l9 = [100, 50, 65, 82, 23]
l9.sort(key=myfunc)
print(l9)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

ll1 = ["banana", "Orange", "Kiwi", "cherry"]
ll1.sort(key = str.lower)
print(ll1)


# Reverse Order
ll2 = ["banana", "Orange", "Kiwi", "cherry"]
ll2.reverse()
print(ll2)

# Copy a List
'''
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
There are ways to make a copy, one way is to use the built-in List method copy().
'''

ll3 = ll2.copy()
print(ll3)

ll4 = list(ll3)
print(ll4)


# Join Lists
'''
Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.
One of the easiest ways are by using the + operator.
'''

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1+list2
print(list3)

print(list1)

for x in list2:
    list1.append(x)
print(list1)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list
list1.extend(list2)
print(list1)


'''
List Methods
Python has a set of built-in methods that you can use on lists.
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''