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
        
# if number%2 == 0:
#     count +=1
#     print("Total Even number is: ",count)
# else:
#     count +=1
#     print("Total ODD number is: ",count)