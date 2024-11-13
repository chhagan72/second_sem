# Strings
print("Hello Chhagan")

# Assign String to a Variable
a = "Good Morining"
print(a," ", type(a))

# Multiline Strings
b = """
Hello chhagan kumawat,
Good Morning,
How are you
"""
print(b," ",type(b))

# Strings are Arrays
c = "Chhagan kumawat"
print(c[0]," ",c[1])  

# Looping Through a String
for d in "Chhagan":
    print(d)
    # print(d," ",type(d))

# String Length
e = "Chhagan"
print(len(e))

# Check String
f = "My name is chhagan"
print("name" in f)
if "name" in f:
    print("Yes this is word in present in this string")
else:
    print("No This is not word in present in this string ")

# Check if NOT
if "z" not in f:
    print("No This is not word in present in this string ")
else:
    print("Yes this is word in present in this string")

# Slicing
print(f[1])
print(f[1:8])

# Slice From the Start
print(f[:8])

# Slice To the End
print(f[3:])

# Negative Indexing
print(f[-5:-2])

# Upper Case
print(f.upper())

# Lower Case
print(f.lower())

# Remove Whitespace
print(f.strip())

# Replace String
print(f.replace("n","N"))

# Split String
print(f.split(","))

# String Concatenation
g = " kumawat"
print(f + g)

# String Format
h = f + ", Age is 23"
print(h)

'''
But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {}
'''
i="My name {}"
print(i.format(e))

j = "my name is \" Chhagan\" and my age is 23"
print(j)


# Methods in String
'''
capitalize():-	Converts the first character to upper case
casefold():-	Converts string into lower case
center():-	Returns a centered string
count():-	Returns the number of times a specified value occurs in a string
encode():-	Returns an encoded version of the string
endswith():-	Returns true if the string ends with the specified value
expandtabs():-	Sets the tab size of the string
find():-	Searches the string for a specified value and returns the position of where it was found
format():-	Formats specified values in a string
format_map():-	Formats specified values in a string
index():-	Searches the string for a specified value and returns the position of where it was found
isalnum():-	Returns True if all characters in the string are alphanumeric
isalpha():-	Returns True if all characters in the string are in the alphabet
isascii():-	Returns True if all characters in the string are ascii characters
isdecimal():-	Returns True if all characters in the string are decimals
isdigit():-	Returns True if all characters in the string are digits
isidentifier():-	Returns True if the string is an identifier
islower():-	Returns True if all characters in the string are lower case
isnumeric():-	Returns True if all characters in the string are numeric
isprintable():-	Returns True if all characters in the string are printable
isspace():-	Returns True if all characters in the string are whitespaces
istitle():-	Returns True if the string follows the rules of a title
isupper():-	Returns True if all characters in the string are upper case
join():-	Joins the elements of an iterable to the end of the string
ljust():-	Returns a left justified version of the string
lower():-	Converts a string into lower case
lstrip():-	Returns a left trim version of the string
maketrans():-	Returns a translation table to be used in translations
partition():-	Returns a tuple where the string is parted into three parts
replace():-	Returns a string where a specified value is replaced with a specified value
rfind():-	Searches the string for a specified value and returns the last position of where it was found
rindex():-	Searches the string for a specified value and returns the last position of where it was found
rjust():-	Returns a right justified version of the string
rpartition():-	Returns a tuple where the string is parted into three parts
rsplit():-	Splits the string at the specified separator, and returns a list
rstrip():-	Returns a right trim version of the string
split():-	Splits the string at the specified separator, and returns a list
splitlines():-	Splits the string at line breaks and returns a list
startswith():-	Returns true if the string starts with the specified value
strip():-	Returns a trimmed version of the string
swapcase():-	Swaps cases, lower case becomes upper case and vice versa
title():-	Converts the first character of each word to upper case
translate():-	Returns a translated string
upper():-	Converts a string into upper case
zfill():-	Fills the string with a specified number of 0 values at the beginning
'''
# capitalize()
print(j.capitalize())
# Count()
print(f.count('a'))

# zfill()
print(j.zfill(2))


# Boolean Value
print(10 > 9)
print(10 == 9)
print(10 < 9)