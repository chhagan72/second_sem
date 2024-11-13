# If ... Else
'''
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
'''

a = 33
b = 200
if b > a:
  print("b is greater than a")


c = 33
d = 33
if d > c:
  print("d is greater than c")
elif c == d:
  print("c and d are equal")


if d > c:
    print("d is greater than c")
elif c == d:
  print("c and d are equal")
else:
  print("a is greater than b")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")