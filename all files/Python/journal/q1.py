# 1]Write a python code to find given number is Armstrong Number or
# Not. Steps:
# a. Accept Number from user in variable named as X.
# b. Print message whether number X is Armstrong or not.
# Note: Armstrong number is a number that is equal to the sum of cubes of its digits. For
# example 153. (1^3 + 5^3 + 3^3 = 153)

a = input("Enter the number : ")
sum = 0
for i in a:
    ina = int(i)
    cube = ina ** 3
    sum += cube

if sum == int(a):
    print(a , " is Armstrong number ")
else:
    print(a , " is not a Armstrong number")
