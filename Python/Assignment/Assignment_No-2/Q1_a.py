num = int(input("Eneter a number: "))
num1 = int(input("Eneter a number: "))
if num % num1 == 0:
    print("The number is devided Evenly ",num)

    if num%4 == 0:
        print(num,"The number is devided by: ",num1)
else:
    print("The number is not devided by ",num)




# num = int(input("Please enter the number to check: "))
# check = int(input("Please enter the number to divide by: "))

# # Check if the second number divides evenly into the first number
# if num % check == 0:
#     print(f"{check} divides evenly into {num}.")
    
#     # Check if the number is a multiple of 4
#     if num % 4 == 0:
#         print(f"{num} is also a multiple of 4.")
# else:
#     print(f"{check} does not divide evenly into {num}.")