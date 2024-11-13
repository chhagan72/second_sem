# 4] Write a program that accepts a sentence and calculate the number of letters and
# digits. Suppose the following input is supplied to the program: hello world! 123 Then, the
# output should be: ALPHABETS 10 DIGITS 3
# (Note : Special symbols are not alphabets) 

a = input("Enter the sentence")
dcount = 0
acount = 0
for i in a:
    if i.isdigit():
        dcount += 1
    if i.isalpha():
        acount += 1
        
print(f"The total alphabets is {acount} and digit is {dcount}")

        