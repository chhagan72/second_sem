# For Loops
'''
For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''

fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
# for x in "apple":
#     print(x)


# break Statement
# With the break statement we can stop the loop before it has looped through all the items
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break

for x in fruits:
    if x == "banana":
        break
    print(x)

# continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range() Function
'''
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
'''

# for i in range(6):
#     print(i)

# for ii in range(2,6):
#     print(ii)

for i in range(2,30,6):
    print(i)
