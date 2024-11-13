# 5] Write a Python function that takes a list and returns a new list with unique elements of
# the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5] 

a = [1,2,3,3,3,3,4,5]
uni = []
for i in a:
    if i not in uni:
        uni.append(i)
print(uni)