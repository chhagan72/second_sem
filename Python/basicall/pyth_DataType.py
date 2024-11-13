""" 
*** Data Types ***

In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

 """

a = 5 
print(a)
print(type(a))

# String Data Type

string = "Jay bholenath"
print(string)
print(type(string))

# Float Data type 
float = 3.4
print(float)
print(type(float))

# complex Data type
complexDtype = 1j
print(complexDtype)
print(type(complexDtype))


#list Data type

listDtype = ['1,2,3,4,5,6,7']
print(listDtype)
print(type(listDtype))

#tuple Data Type
tupleDtype = (1,2,3,4,"Chhagan")
print(tupleDtype)
print(type(tupleDtype))


# Range Data type
rangeDtype = range(5)
print(type(rangeDtype))

# Dictionary Data type 
dictDtype = {"Name ":" Chhagan", "Address" : " Pune"}
print(type(dictDtype))

# Set Data Type
setDtype = {1,2,3,4,5}
print(type(setDtype))

# boolean Data type 
boolDtype = True
print(type(boolDtype))

# byte Data type 
byteDtype = b"chhagan"
print(byteDtype)
print(type(byteDtype))

# frozenset Data type 
frozensetDtype = ({1,2,3,"Chhagan"})
print(frozensetDtype)
print(type(frozensetDtype))


# bytearray Data type 
bytearrayDtype = bytearray(7)
print(bytearrayDtype)
print(type(bytearrayDtype))

# memoryview Data type 
memoryviewDtype = memoryview(bytes(7))
print(memoryviewDtype)
print(type(memoryviewDtype))

# none Data type 
noneDtype = None
print(noneDtype)
print(type(noneDtype))