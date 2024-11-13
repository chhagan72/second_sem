""" 
Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
 """

a,b,c = int(1),int(1.1), int("1")
print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

aa,bb,cc = float(11),float(15.1), float("18")
print(aa)
print(type(aa))

print(bb)
print(type(bb))

print(cc)
print(type(cc))

aaa,bbb,ccc = str(11),str(15.1), str("18")
print(aaa)
print(type(aaa))

print(bbb)
print(type(bbb))

print(ccc)
print(type(ccc))

