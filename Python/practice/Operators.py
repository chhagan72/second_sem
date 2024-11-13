# Python Arithmetic Operators
a=b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

# Python Assignment Operators
# print(a=b)
'''
Operator	Example	    Same As	
=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3	
-=	        x -= 3	    x = x - 3	
*=	        x *= 3	    x = x * 3	
/=	        x /= 3	    x = x / 3	
%=	        x %= 3	    x = x % 3	
//=	        x //= 3 	x = x // 3	
**=	        x **= 3 	x = x ** 3	
&=	        x &= 3	    x = x & 3	
|=	        x |= 3	    x = x | 3	
^=	        x ^= 3	    x = x ^ 3	
>>=	        x >>= 3 	x = x >> 3	
<<=	        x <<= 3 	x = x << 3
'''

# Python Comparison Operators
c=3

if a == b:
    print(True)
else:
    print(False)

if a != b:
    print(True)
else:
    print(False)

if c > b:
    print(True)
else:
    print(False)

if a < c:
    print(True)
else:
    print(False)

if a >= b:
    print(True)
else:
    print(False)

if c <= b:
    print(True)
else:
    print(False)


print("Python Logical Operators")
# Python Logical Operators
if c == b or a!=b or a<c or b>a or b<=c or c>=a:
    print(True)
else:
    print(False)

print("Python Logical Operators")
if c == b and a!=b and a<c and b>a and b<=c and c>=a:
    print(True)
else:
    print(False)

print("Python Logical Operators")
if not(c == b and a!=b and a<c and b>a and b<=c and c>=a):
    print(True)
else:
    print(False)

# Python Identity Operators

print("Python Identity Operators")
if c is b:
    print(True)
else:
    print(False)

print("Python Identity Operators")
if c is not b:
    print(True)
else:
    print(False)
    
# Python Membership Operators
# print("Python Membership Operators")
# if c in b:
#     print(True)
# else:
#     print(False)

# print("Python Membership Operators")
# if c not in  b:
#     print(True)
# else:
#     print(False)


# Python Bitwise Operators
'''
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
'''

if c & b:
    print(True)
else:
    print(False)

if c | b:
    print(True)
else:
    print(False)

if c ^ b:
    print(True)
else:
    print(False)