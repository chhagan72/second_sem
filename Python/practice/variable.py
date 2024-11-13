# Creating Variables
x = 5
print(x)
y = type(x)
print(y)

z ="Chhagan"
print(z)
w = type(z)
print(w)

a = 5.3
print(a)
b= type(a)
print(b)

# Casting
c = int(22)
d = float("10.2")
print(c,' Type of data ', type(c))
print(d,' Type of data ', type(d))


# Variable Names
# Legal variable
e = 23
_e = 24
print(e, _e)

# Illegal variable
# 2e = 23
# e-3 = 12
# e w = 34
# print(2e,e-3, e w)

# One Value to Multiple Variables
f=g=h = "Chhagan"
print(f," ",g," ",h)

# Unpack a Collection
i = [1,2,3,4]
j=i
print(j)

# Output Variables : The Python "print()" function is often used to output variables.
print(a)


# Global Variables
k = "Chhagan"
def func():
    print(k)
func()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

k = "Chhagan"
def func():
    k = "Chhagan kumawat"
    print(k," : This is local variable ")
func()
print(k, " : This is a global variable")

# The global Keyword

k = "Chhagan"
def func():
    global k
    print(k," : This is local variable ")
    k = "Chhagan kumawat"
func()
print(k, " : This is a global variable")