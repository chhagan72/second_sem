# 2] Write a code in python to count number of vowels in given string
# Steps:
# a. Accept string from user in variable named STR1.
# b. Count the number of vowels in STR1 and print.
# Eg.
# 1.STR1 = 'COCONUT' => 3
# 2.STR1 = 'CONFIDence' => 4
vowels = ['a', 'e', 'i', 'o', 'u']
str1 = input("Enter the string : ")
count = 0
for i in str1:
    for a in vowels:
        if i.lower() == a :
            count += 1
            
print(f"Total vowels in the {str1} is {count}")
    
    
    