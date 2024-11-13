# 1.	Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# Ans

num1 = int(input("Enter a number: "))
if num1%2 == 0:
    print(num1," is Even number")
else:
    print(num1," is ODD number")

# OutPut
# Enter a number: 12
# 12  is Even number

# a.	If the number is a multiple of 4, print out a different message.
    
    num = int(input("Eneter a number: "))
num1 = int(input("Eneter a number: "))
if num % num1 == 0:
    print("The number is devided Evenly ",num)

    if num%4 == 0:
        print(num,"The number is devided by: ",num1)
else:
    print("The number is not devided by ",num)

# OutPut
# Eneter a number: 12
# Eneter a number: 1
# The number is devided Evenly  12
# 12 The number is devided by:  1
    
# b.	Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
    num = int(input("Enter a number"))
check= int(input("Enter a check number"))
if num%check ==0:
    print(num," This number is evenly: ",check)
else:
    print("This number is not evenly ",num)


# OutPut
# Enter a number22
# Enter a check number2
# 22  This number is evenly:  2

# 2.	Write a program that determines a student’s grade. The program will read three

# scores and determine the grade based on the following rules:
# -if the average score =90% =>grade=A
# -if the average score >= 70% and <90% => grade=B
# -if the average score>=50% and <70% =>grade=C
# -if the average score<50% =>grade=F

score = int(input("Enter student score: "))
if score >=90:
    print("A")
elif score >= 70 and score < 90:
    print("B")
elif score >= 50 and score < 70:
    print("C")
elif score < 50:
    print("F")

# Output
# Enter student score: 23
# F

'''3.	Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5 Number of odd numbers : 4'''
num = [1,2,3,4,5,6,7,8,9]
count = 0
count1 = 0
n = len(num)
print(type(num))
for i in range(0,n):
    if (num[i]%2==0):
        count+=1
    else:
        count1+=1
print(count)
print(count1)

# <class 'list'>
# 4
# 5
'''
4.	Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5'''
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i)

# OutPut

# 0
# 1
# 2
# 4
# 5


'''
5.	Write a Python program to get the Fibonacci series between 0 to 50. Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it. Expected Output : 1 1 2 3 5 8 13 21 34
'''
num = int(input("Enter a number "))
num2 = int(input("Enter a number "))
# num,num2 = (0,1)
while num <50:
    print(num2)
    num,num2 = num2,num + num2

# OutPut
'''
2
14
16
30
46
76
'''
'''
6.	Write a Python program which takes two digits m (row) and n (column) as input
and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.
Test Data : Rows = 3, Columns = 4 Expected Result :	0, 0, 0, 0
0, 1, 2, 3
0, 2, 4, 6'''

r = 3
c = 4
g =[]
for i in range(r):
    r1 = []
    for j in range(c):
        r1.append(i*j)
    g.append(r1)
    print(r1)

# OutPut
'''
[0, 0, 0, 0]
[0, 1, 2, 3]
[0, 2, 4, 6]
'''

'''
7.	Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010
'''
sample_data = "0100,0011,1010,1001,1100,1001"
num=sample_data.split(',')
result=[]
for i in num:
    d_num=int(i,2)
    if d_num % 5 ==0:
        result.append(i)
output = ','.join(result)
print(output)


# OutPut
'''
1010
'''

'''
8.	Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.'''

items = []
for i in range(100, 400):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        items.append(s)
print(",".join(items))

# OutPut
'''
200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,264,266,268,280,282,284,286,288
'''

'''
9.	Write a Python program to print alphabet pattern 'A',B,D,E,H,T,F,X,W,M,N,Z. For Eg of A.
* * *

*	*

*	*

*****

*	*

*	*

*	*'''

result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n" 
print(result_str) 


# OutPut
'''
  ***  
 *   *
 *   *
 *****
 *   *
 *   *
 *   *
'''

'''
10.	Write a Python program that accepts a word from the user and reverse it'''

word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)


# OutPut
'''
Enter a word: Chhagan
Reversed word: nagahhC
'''

'''
11.	Write a Python program that accepts a string and calculate the number of digits and letters.
Sample Data : Python 3.2 Expected Output :
 
Letters 6
Digits 2
'''
input_string = input("Enter a string:")
num_letters = 0
num_digits = 0
for char in input_string:
    if char.isalpha():
        num_letters += 1
    elif char.isdigit():
        num_digits += 1
print("Letters:", num_letters)
print("Digits:", num_digits)



# OutPut
'''
Enter a string:Chhagan
Letters: 7
Digits: 0
'''

'''
12.	Wite A Python program to use a Math Function in python and explain its use (Any 10 Built in Function)'''
# abs(x):
# Use: Returns the absolute value of a number.
result = abs(-5)
print(result)
  # Output: 5

# pow(x, y):
# Use: Returns x raised to the power y.
result = pow(2, 3)
print(result)
  # Output: 8

# sqrt(x):
# Use: Returns the square root of x.
import math
result = math.sqrt(25)
print(result) 
 # Output: 5.0

# ceil(x):
# Use: Returns the smallest integer greater than or equal to x.
import math
result = math.ceil(4.3)
print(result) 
 # Output: 5

# floor(x):
# Use: Returns the largest integer less than or equal to x.
import math
result = math.floor(4.9)
print(result) 
 # Output: 4

# round(x):
# Use: Rounds x to the nearest integer.
result = round(4.6)
print(result) 
 # Output: 5

# sin(x):
# Use: Returns the sine of x (in radians).
import math
result = math.sin(math.pi / 2)
print(result) 
 # Output: 1.0

# cos(x):
# Use: Returns the cosine of x (in radians).
import math
result = math.cos(0)
print(result) 
 # Output: 1.0

# tan(x):
# Use: Returns the tangent of x (in radians).
import math
result = math.tan(math.pi / 4)
print(result) 
 # Output: 1.0

# log(x, base):
# Use: Returns the logarithm of x with the specified base. If base is not specified, the natural logarithm (base e) is calculated.
import math
result = math.log(8, 2)
print(result)
  # Output: 3.0

'''
13.	Write A Python programming to use a Date() And Time() Function in Python Its Use (Any 5 Built in finction)'''
'''
1. datetime.datetime.now():
# Use: Returns the current date and time as a datetime object.
from datetime import datetime

current_datetime = datetime.now()
print(current_datetime)

2. datetime.date.today():
# Use: Returns the current date as a date object.
from datetime import date

current_date = date.today()
print(current_date)

3. datetime.timedelta(days=n) (timedelta function):
# Use: Represents the duration between two dates or times.
from datetime import datetime, timedelta

current_datetime = datetime.now()
future_datetime = current_datetime + timedelta(days=7)
print(future_datetime)

4. strftime(format) (string format time function):
# Use: Converts a datetime object to a string with a specified format.
from datetime import datetime

current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

5. strptime(date_string, format) (string parse time function):
# Use: Parses a string representing a date and time into a datetime object.
from datetime import datetime

date_string = "2022-03-10 14:30:00"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_datetime)

'''

'''
14.	Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
Expected Output:
Input the month (e.g. January, February etc.): july Input the day: 31
Season is autumn'''

month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))
if month in ('January', 'February', 'March'):
    season = 'winter'
elif month in ('April', 'May', 'June'):
    season = 'spring'
elif month in ('July', 'August', 'September'):
    season = 'summer'
else:
    season = 'autumn'
if (month == 'March') and (day > 19):
    season = 'spring'
elif (month == 'June') and (day > 20):
    season = 'summer'
elif (month == 'September') and (day > 21):
    season = 'autumn'
elif (month == 'December') and (day > 20):
    season = 'winter'
print("Season is", season) 


# OutPut
'''
Input the month (e.g. January, February etc.): February
Input the day: 23
Season is winter
'''

'''
15.	Write a Python program to find the median of three values.
Expected Output:
Input first number: 15 Input second number: 26 Input third number: 29 The median is 26.0'''
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
print("The median is", median)



# OutPut
'''
Input first number: 12
Input second number: 23
Input third number: 34
The median is 23.0
'''

'''
16.	Write a Python program to get next day of a given date.
Expected Output:
Input a year: 2016
Input a month [1-12]: 08
Input a day [1-31]: 23
The next date is [yyyy-mm-dd] 2016-8-24
'''
year = int(input("Input a year: "))
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False
month = int(input("Input a month [1-12]: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30
day = int(input("Input a day [1-31]: "))
if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))



# OutPut
'''
Input a year: 2000
Input a month [1-12]: 7
Input a day [1-31]: 2
The next date is [yyyy-mm-dd] 2000-7-3.
'''

'''
17.	Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.'''
print("Input some integers to calculate their sum and average. Input 0 to exit.")
count = 0
sum = 0.0
number = 1
while number != 0:
    number = int(input(""))
    sum = sum + number
    count += 1
if count == 0:
    print("Input some numbers")
else:
    print("Average and Sum of the above numbers are: ", sum / (count-1), sum)
	


# OutPut
'''
Input some integers to calculate their sum and average. Input 0 to exit.
12
4
32
7
12
43
0
Average and Sum of the above numbers are:  18.333333333333332 110.0
'''

'''
18.	Write a Python program to construct the following pattern, using a nested loop
number.
Expected Output:
1
22
333
4444
55555
666666
7777777
88888888
999999999
 
'''
for i in range(10):
    print(str(i) * i)
	


# OutPut
'''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''

'''
19.	Write A Python Program to Convert Decimal to Binary, Octal and Hexadecimal(Use user defined Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?'''
num = int(input("Enter a number: "))
binary_number = bin(num)[2:]
octal_number = oct(num)[2:]
hexadecimal_number = hex(num)[2:]
if num % 2 == 0:
    classification = "even"
else:
    classification = "odd"
print(f"Decimal: {num}")
print(f"Binary: {binary_number}")
print(f"Octal: {octal_number}")
print(f"Hexadecimal: {hexadecimal_number}")
print(f"The number is {classification}.")


# OutPut
'''
Enter a number: 22
Decimal: 22
Binary: 10110
Octal: 26
Hexadecimal: 16
The number is even.
'''

'''
20.	
1.	Write A Python Program to Find ASCII Value of Character.
'''
user_char = input("Enter a character: ")
ascii_value = ord(user_char)
print(f"The ASCII value of '{user_char}' is {ascii_value}.")

#OutPut
'''
Enter a character: c
The ASCII value of 'c' is 99.
'''
'''
2.	Write A Python Program to Find HCF or GCD and LCM.
'''
num1 = 36
num2 = 60
hcf = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("Hcf of", num1, "and", num2, "is", hcf)
#OutPut
'''
Hcf of 36 and 60 is 12
'''
'''
3.	Write A Python Program to Swap Two Variables
'''
variable1 = input("Enter the value for variable 1: ")
variable2 = input("Enter the value for variable 2: ")
print("Before swapping:")
print("Variable 1:", variable1)
print("Variable 2:", variable2)
variable1, variable2 = variable2, variable1
print("\nAfter swapping:")
print("Variable 1:", variable1)
print("Variable 2:", variable2)

#OutPut
'''
Enter the value for variable 1: 1
Enter the value for variable 2: 2
Before swapping:
Variable 1: 1
Variable 2: 2

After swapping:
Variable 1: 2
Variable 2: 1
'''
'''
4.	Write A Python Program to Generate a Random Number.
'''
import random
random_number = random.randint(1, 100)
print("Random Number:", random_number)
#OutPut
'''
Random Number: 39
'''
'''
5.	Write A Python Program to Convert Kilometers to Miles.
'''
kilometers = float(input("Enter value in kilometers: "))
conv_fac = 0.621371
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

#OutPut
'''
Enter value in kilometers: 23
23.00 kilometers is equal to 14.29 miles
'''
'''
6.	Write a program for calculate for factorial.
'''
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial) 
#OutPut
'''
Enter a number: 12
The factorial of 12 is 479001600
'''
'''
7.	Write a program for insertion, bubble, selection.
'''
arr = [20,9,6,3,1]
n = len(arr)

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print('Array after sorting')
print(arr)
#OutPut
'''
Array after sorting
[1, 3, 6, 9, 20]
'''
'''
'''
