'''
 Write a program to create a list of words from the given string which are
less than size ‘A’ .
Input String: “Python programming language has lot of applications in
data analytics”.
Input n = 8
'''

def fun(s,n):
    words = s.split()
    filter=[word for word in words if len(word)<n ]
    return filter
s="Python programming language has lot of applications in data analytics "
n = 8
result =fun(s,n)
print("Word less then size",n,":",result)
