# Write a program, which will find all such numbers between 2000 and 3000 (both included)
# such that each digit of the number is an even number. eg. 2000, 2002...2888.
for i in range(2000,3001,2):
    count = 0
    i = str(i)
    for a in i :
        a = int(a)
        if a % 2 == 0:
            count +=1
    if count == len(i):
        print(i ,end="\t")
    
