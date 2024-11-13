arr = [20,9,6,3,1]
n = len(arr)

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print('Array after sorting')
print(arr)
