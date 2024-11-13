"""***Python Booleans***
Booleans represent one of two values: True or False.

Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False. """


print(1>9)
print(1<9)
print(1==9)
print(1 != 9)

a = 120
b = 31
if a > b:
    print("The A is greater then B")
else:
    print("The B is greater then A")

if a > b or a == b:
    print("The A is greater then And Equal to B.")
else: 
    print("The B is greater then And Equal to A")

print("\n")
print(bool("Hello"))
print(bool(15))

print("\n")

print(bool(a))

print("\n")

c ="Chhagan"
d =(["chhagan","Durgesh"])
print(bool(c))
print(bool(d))

print("\n")

class abc():
    def __len__(self):
        return 0
xyz = abc()
print(bool(xyz))

def ck():
    return True
print(bool(ck()))

print("\n")

def ifelse():
    return True
if ifelse():
    print("YES")
else:
    print("NO")

print("\n")
ck1 = 200
print(isinstance(ck1, ))