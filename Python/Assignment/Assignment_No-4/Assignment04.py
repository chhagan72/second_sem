'''
1.	Use regular expression for –
a.	Email validation
'''
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

email = "user@example.com"
if validate_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
#Output
'''
user@example.com is a valid email address.
'''
'''

b.	IP address Validation
'''
import re

def validate_ip_address(ip_address):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
    return re.match(pattern, ip_address) is not None

ip_address = "192.168.1.1"
if validate_ip_address(ip_address):
    print(f"{ip_address} is a valid IP address.")
else:
    print(f"{ip_address} is not a valid IP address.")

#Output
'''
192.168.1.1 is a valid IP address.
'''
'''

c.	Date Validation
'''
import re

def validate_date(date):
    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(19|20)\d\d$'
    return re.match(pattern, date) is not None

date = "03/10/2024"
if validate_date(date):
    print(f"{date} is a valid date.")
else:
    print(f"{date} is not a valid date.")

#Output
'''
03/10/2024 is a valid date.
'''
'''

d.	Mobile number validation
'''
import re

def validate_mobile_number(mobile_number):
    pattern = r'^[1-9]\d{9}$'
    return re.match(pattern, mobile_number) is not None

mobile_number = "1234567890"
if validate_mobile_number(mobile_number):
    print(f"{mobile_number} is a valid mobile number.")
else:
    print(f"{mobile_number} is not a valid mobile number.")

#Output
'''
1234567890 is a valid mobile number.
'''
'''

2.	Demonstrate any five standard module of python?
'''
import math
import json
from datetime import datetime
import random
import os
# 1.math Module:
# The math module provides mathematical functions.
# Calculate the square root of a number
number = 25
sqrt_result = math.sqrt(number)
print(f"Square root of {number}: {sqrt_result}")

# 2. datetime Module:
# The datetime module is used for working with dates and times.
# Get the current date and time
current_datetime = datetime.now()
print(f"Current date and time: {current_datetime}")

# 3. random Module:
# The random module is used for generating random numbers.
# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")

# 4. os Module:
# The os module provides a way of using operating system-dependent functionality.
# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# 5. json Module:
# The json module is used for encoding and decoding JSON data.
# Encode a Python dictionary into JSON format
data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data)
print(f"JSON representation of the data: {json_data}")
# Output
'''
Square root of 25: 5.0
Current date and time: 2024-03-19 18:39:54.552023
Random number between 1 and 10: 10
Current working directory: C:\Users\Chhagan\Desktop\MCA SEM-II\Python\Assignment\Assignment_No-4     
JSON representation of the data: {"name": "John", "age": 30, "city": "New York"}

'''
'''
3.	Use built in packages for following program –
a.	Get copyright information
'''
import sys
copyright_info = sys.copyright
print(copyright_info)
#Output
'''
Copyright (c) 2001-2023 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
'''
'''
b.	Get the size of object
'''
import sys

my_list = [1, 2, 3, 4, 5]
object_size = sys.getsizeof(my_list)
print(f"Size of the list object: {object_size} bytes")
#Output
'''
Size of the list object: 104 bytes
'''
'''
c.	Get the users environments.
'''
import os

user_environment = os.environ
print(f"User's environment variables: {user_environment}")
#Output
'''
User's environment variables: environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Chhagan\\AppData\\Roaming', 'CHOCOLATEYINSTALL': 'C:\\ProgramData\\chocolatey', 'CHOCOLATEYLASTPATHUPDATE': '133363873540332777', 'CHROME_CRASHPAD_PIPE_NAME': '\\\\.\\pipe\\crashpad_7968_HMSAOAQXAJUUCMDC', 'CLASSPATH': 'C:\\mysql-connector-j-8.1.0.jar;.;', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-L347H2E', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Chhagan', 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-17\\bin', 'LOCALAPPDATA': 'C:\\Users\\Chhagan\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-L347H2E', 'M2_HOME': 'C:\\software\\apache-maven-3.9.6', 'NUMBER_OF_PROCESSORS': '2', 'ONEDRIVE': 'C:\\Users\\Chhagan\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\Chhagan\\OneDrive', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'OS': 'Windows_NT', 'PATH': 'C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\Python311\\Scripts\\;C:\\Python311\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\ProgramData\\chocolatey\\bin;C:\\Program Files\\nodejs;C:\\software\\openjdk-11.0.0.1_windows-x64_bin\\jdk-11.0.0.1\\bin;C:\\Program Files\\PuTTY\\;C:\\software\\apache-maven-3.9.6\\bin;C:\\Program Files\\Git\\cmd;C:\\Program Files\\nodejs\\;C:\\Users\\Chhagan\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\Chhagan\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\Chhagan\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW;.CPL', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 15 Stepping 13, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '0f0d', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Users\\Chhagan\\Documents\\WindowsPowerShell\\Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\Chhagan\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\Chhagan\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-L347H2E', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-L347H2E', 'USERNAME': 'Chhagan', 'USERPROFILE': 'C:\\Users\\Chhagan', 'WINDIR': 'C:\\Windows', 'PYTHONSTARTUP': 'c:\\Users\\Chhagan\\.vscode\\extensions\\ms-python.python-2024.2.1\\pythonFiles\\pythonrc.py', 'TERM_PROGRAM': 'vscode', 'TERM_PROGRAM_VERSION': '1.87.2', 'LANG': 'en_US.UTF-8', 'COLORTERM': 'truecolor', 'GIT_ASKPASS': 'c:\\Users\\Chhagan\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass.sh', 'VSCODE_GIT_ASKPASS_NODE': 'C:\\Users\\Chhagan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '', 'VSCODE_GIT_ASKPASS_MAIN': 'c:\\Users\\Chhagan\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass-main.js', 'VSCODE_GIT_IPC_HANDLE': '\\\\.\\pipe\\vscode-git-d5473c6c75-sock', 'VSCODE_INJECTION': '1'})
'''
'''
d.	Retrieve the file properties.
'''
import os

file_path = "example.txt"
file_properties = os.stat(file_path)
print(f"File properties for {file_path}:\n{file_properties}")
#Output
'''
File properties for example.txt:
os.stat_result(st_mode=33206, st_ino=4785074604254985, st_dev=2922366934, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1710124134, st_mtime=1710077466, st_ctime=1710077466)
'''
'''
e.	Display system time and date.
'''
import datetime

current_datetime = datetime.datetime.now()
print(f"Current system date and time: {current_datetime}")
#Output
'''
Current system date and time: 2024-03-19 18:49:53.614297
'''
'''
4.	Create two user defined module.one is Maths. Define class MathsOperations with c methods to find the maximum and minimum of three numbers.
Create another module Stats. Define class StatsOperations with methods to find the average and median of three numbers. Use these methods in main to perform operations on three integers accepted  user input.


'''
# Q4_1_a.py
class MathsOperations:
    @staticmethod
    def find_maximum(num1, num2, num3):
        return max(num1, num2, num3)

    @staticmethod
    def find_minimum(num1, num2, num3):
        return min(num1, num2, num3)
    
# Q4_1_b.py
from Q4_1_a import MathsOperations

# Usage of the user-defined module
num1, num2, num3 = 10, 5, 8
math_operations_instance = MathsOperations()

# Find the maximum of three numbers
max_result = math_operations_instance.find_maximum(num1, num2, num3)
print(f"Maximum of {num1}, {num2}, and {num3} is: {max_result}")

# Find the minimum of three numbers
min_result = math_operations_instance.find_minimum(num1, num2, num3)
print(f"Minimum of {num1}, {num2}, and {num3} is: {min_result}")

#Output
'''
Maximum of 10, 5, and 8 is: 10
Minimum of 10, 5, and 8 is: 
'''

# Q4_1_a.py
class MathsOperations:
    @staticmethod
    def find_maximum(num1, num2, num3):
        return max(num1, num2, num3)

    @staticmethod
    def find_minimum(num1, num2, num3):
        return min(num1, num2, num3)
# Q4_2_a.py
class StatsOperations:
    @staticmethod
    def find_average(num1, num2, num3):
        return (num1 + num2 + num3) / 3

    @staticmethod
    def find_median(num1, num2, num3):
        numbers = [num1, num2, num3]
        numbers.sort()
        return numbers[1]  
# Q4_2_b.py
from Q4_1_a import MathsOperations
from Q4_2_a import StatsOperations

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

math_operations_instance = MathsOperations()
stats_operations_instance = StatsOperations()

max_result = math_operations_instance.find_maximum(num1, num2, num3)
min_result = math_operations_instance.find_minimum(num1, num2, num3)

average_result = stats_operations_instance.find_average(num1, num2, num3)
median_result = stats_operations_instance.find_median(num1, num2, num3)

print(f"\nMath Operations:")
print(f"Maximum of {num1}, {num2}, and {num3} is: {max_result}")
print(f"Minimum of {num1}, {num2}, and {num3} is: {min_result}")

print(f"\nStats Operations:")
print(f"Average of {num1}, {num2}, and {num3} is: {average_result}")
print(f"Median of {num1}, {num2}, and {num3} is: {median_result}")

'''
Enter the first number: 12
Enter the second number: 2
Enter the third number: 23

Math Operations:
Maximum of 12.0, 2.0, and 23.0 is: 23.0
Minimum of 12.0, 2.0, and 23.0 is: 2.0

Stats Operations:
Average of 12.0, 2.0, and 23.0 is: 12.333333333333334
Median of 12.0, 2.0, and 23.0 is: 12.0
'''