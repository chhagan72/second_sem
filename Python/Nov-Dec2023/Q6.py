'''
Write a program to accept an integer number and use try/except to catch
the exception if a floating point number is entered
'''
try:
    num = int(input("Enter you number"))
    print("You entered number : ",num)
except ValueError:
    print("You enter a floating point number")