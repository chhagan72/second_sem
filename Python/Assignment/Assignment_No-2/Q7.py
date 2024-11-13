sample_data = "0100,0011,1010,1001,1100,1001"
num=sample_data.split(',')
result=[]
for i in num:
    d_num=int(i,2)
    if d_num % 5 ==0:
        result.append(i)
output = ','.join(result)
print(output)