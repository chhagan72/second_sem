num = 7
num2 = 7
a=[]
# int(input("Enter a number "))
# print(type(num))
# count = 0
for i in range(num):
    r=[]
    for j in range(num2):
        r.append(i*j)
        a.append(r)
    print(a)
for r in a:
    print(r)