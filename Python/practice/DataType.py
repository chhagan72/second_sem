'''
Immutable Built-in Data Types in Python
Numbers
Booleans
Strings
Bytes
Tuples
Mutable Built-in Data Types in Python
Lists
Dictionaries
Sets


Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

x1 = str("Hello World")	
x2 = int(20)	
x3 = float(20.5)	
x4 = complex(1j)	
x5 = list(("apple", "banana", "cherry"))		
x6 = tuple(("apple", "banana", "cherry"))	
x7 = range(6)	
x8 = dict(name="John", age=36)		
x9 = set(("apple", "banana", "cherry"))	
x0 = frozenset(("apple", "banana", "cherry"))	
x10 = bool(5)	
x11 = bytes(5)	
x12 = bytearray(5)		
x13 = memoryview(bytes(5))	
print(type(x1)," ", type(x2)," ", type(x3)," ", type(x4)," ",type(x5)," ",type(x6)," ", type(x7)," ", type(x8)," ", type(x9)," ", type(x10)," ", type(x11)," ", type(x12)," ", type(x13))