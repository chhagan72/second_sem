'''
 Explain the concept of modules and packages with suitable example.
 Ans:

Modules:
A module is a single Python file that contains functions, classes, and variables.
It allows you to logically organize your Python code into reusable units.
Modules can be imported into other Python scripts or modules using the import statement.

Example:
Let's say you have a Python file named math_operations.py containing mathematical operations:

# math_operations.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

    
Now, you can import this module into another Python script and use its functions:

# main.py
import math_operations

result = math_operations.add(5, 3)
print("Addition:", result)


Packages:
A package is a collection of Python modules organized in directories.
It allows you to further organize modules into a hierarchical structure.
Packages are also modules but can contain sub-packages or modules.

Example:
Let's organize our math_operations.py module into a package named utils, and create an additional module geometry.py for geometric calculations:

utils/              # Package (Directory)
    __init__.py     # Required to treat the directory as a package
    math_operations.py  # Module
    geometry.py     # Module

math_operations.py and geometry.py will contain similar functions but related to different areas of mathematics.
# math_operations.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# geometry.py
def area_circle(radius):
    return 3.14 * radius ** 2

def perimeter_circle(radius):
    return 2 * 3.14 * radius

Now, you can import modules from the package and use their functions:
# main.py
from utils import math_operations, geometry

result = math_operations.add(5, 3)
print("Addition:", result)

circle_area = geometry.area_circle(5)
print("Area of Circle:", circle_area)


'''

