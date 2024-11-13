# Position arguments
def simple(a):
    return a
print(simple("Hello"))

# Keyword arguments
def keyword(a,b):
    return a+b
print(keyword(a=1,b=2))

# Default arguments
def default(a,b=2):
    return a+b
print(default(1))

# Variable length arguments
def variable(*args):
    return args
print(variable(1,2,3,4,5))

# Variable length keyword arguments
def variable_keyword(**kwargs):
    return kwargs
print(variable_keyword(a=1,b=2,c=3))