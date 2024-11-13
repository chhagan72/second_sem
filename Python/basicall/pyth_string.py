""" 
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".
 """

print("This is a python String session")

a = "This is a python String session"
print(a)
print(type(a))

b = """
chhagan,
chhagan,
chhagan rathode
"""
print(b)
print(type(b))

c = '''
chhagan,
ramesh,
kumawat
'''
print(c)

print("\n")

""" Slicing Strings

Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
 """

d = "You can return a range of characters by using the slice syntax."
print(d)
print(d[1])
print(d[-2])
print(d[1:5])
print(d[-10:-1])
print(d[:1])
print(d[1:])
print(d[::1])
print(d[::-1])

print("\n")

""" Modify Strings

Python has a set of built-in methods that you can use on strings.
 """
# Upper Case
e = "Python has a set of built-in methods that you can use on strings."
print(e)
print(e.upper())

print("\n")

# Lower Case
f = "PYTHON HAS A SET OF BUILT-IN METHODS THAT YOU CAN USE ON STRING."
print(f)
print(f.lower())

print("\n")
# Remove Whitespace

g = "            Python has a set of built-in methods that you can use on strings. "
print(g)
print(g.strip())

print("\n")

# Replace String
h = "Python has not a set of built-in methods that you can use on strings"
print(h)
print(h.replace("Python","JAVA"))

print("\n")

# Split String 
i = "Python, has not a set of, built-in, methods that you can use on, strings"
print(i)
print(i.split(","))

print("\n")



""" Python - String Concatenation

String Concatenation
To concatenate, or combine, two strings you can use the + operator.
 """

j = "String Concatenation : "
k = " To concatenate, or combine, two strings you can use the + operator."
print(j)
print(k)
print(j+k)

""" Python - Format - Strings
String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this


 """

age = 24
print("The my age is ",age)

""" txt = "The my age is " + age
print(txt)

txt = "The my age is " + age
          ~~~~~~~~~~~~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str

 """
txt = "The my age is {} "
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))

""" 
String Methods
Python has a set of built-in methods that you can use on strings.
 """
txt = "chhagan"

print(txt)
print(txt.capitalize())
print(txt.upper())
print(txt.zfill(2))
print(txt.swapcase())


txt1 = "CHHAGAN IS GOOD"
print(txt1)
print(txt1.lower())
print(txt1.startswith("GOOD"))