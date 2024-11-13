# Write a program to check the number entered by user is even or odd.
# Program should accept integer digits only

try:
    num =int(input("Enter your number"))
    if num%2==0:
        print("Even")
    else:
        print("Odd")
except:
    print("Enter only integer")
    
    

