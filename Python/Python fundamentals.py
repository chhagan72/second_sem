#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Token
n=-22
print(n)


# In[ ]:





# In[6]:


ad = 3000
hha = 200
print((ad+hha))


# In[16]:


# numerical
num = 3
comple =( 4 + 3j)
print(comple)
name = """vaibhav"""


# In[25]:


#Escape sequence
print("this is \npython")
print("hello\bbro")
#above code will be delete one char befor the excape sequence char
print("this\"s")


# In[32]:


#arithmatic operators
print(22+300)
print(22-30)
print(3*5)
print(2/3)
print(10 % 2)
print(33 // 4)
print(5**1201)


# In[ ]:


#/ in single "/" it will always return float value 
# when we use // or floor division in that int is avalilable it will return int, if there is float it will return float value. 


# In[37]:


# "durga"+10
print("durga"+"10")
print("name "*9)


# In[41]:


print(10 ==10)
print(32 > 40)
print(32 < 40)
print(32 <= 40)
print(32 != 40)
print(32 >= 40)
# we can apply relation opeartion for string also


# In[42]:


if(5 > 4):
    print("hello")
else:
    print("not greater")


# In[ ]:




print(10<20<30<30)
print(10<20<30<=30)
# In[49]:


if("vaibhav"=="vaibhav"):
    print("hello")
else:
    print("tuj se nahi ho paiga")


# ba = "vaibhav"
# ca = "vaibhav"
# dd = "mahajan"
# ff = "sanjay"
# if(ba == ca or ff == dd):
#     print("true")
#     
# if(ba == ca and ff == dd):
#     print("true")
# else:
#     print("false")
#     
# if(ba == ca not ff == dd):
#     print("true")
# else:
#     print("false")

# In[58]:


print(10<<4)
print(160>>4)


# In[73]:


x = 0
for i in range(0,20):
    x += 1
print(x)


# In[77]:


a,b = 20,40
x = 40 if a>b else 30
print(x)


# In[2]:


n1 = int(input("enter the num"))
n2 = int(input("enter the num"))
n3 = int(input("enter the num"))
 
mx = (n1 if (n1 > n2 and n1 > n3) else (n2 if (n2 > n1 and n2 > n3) else n3))
     
print(mx)


# In[1]:


p,q,r = 10,10,20
print(id(p))
print(id(q))
print(p is q)
print(p is r)
print(p is not q)
print(p is not r)


# a = "hi"
# b = "hi"
# c = input("Enter hi")
# print(id(a))
# print(id(b))
# print(id(c))
# #the resone behind the this behavior is that there are few cases where python creates two different object that store the same value 
# # these are:
# # input the string from console
# # writing interger litrals with many digits very big integers
# 

# In[4]:


a = 30
b = [10,20,30]
if a in b:
    print("yes it is present")
else:
    print("No the element is not present")
    
    
a = 30
b = [10,20,30]
if a not in b:
    print("yes it is present")
else:
    print("No the element is not present")


# In[8]:


print(4*85/50//3)
print(((4*85)/50)//3)

print(2**3**4)

# if an expression contains **,then this exponentiation operator has right to left associativity while execution


# # datatypes in python

# In[ ]:


# number 
#     interger 
#     floation point
#     complex
# boolen
# none
# Sequences
#     string 
#     tuple 
#     list
# mapping
#     dictionary
#     sets


# mutable 
# list ,dictionaries and sets
# immutable
# int, float, booleans, string, tuples


# In[15]:


# int() function convert any data type to interger

a = "20"
print(type(a))
print(type(int(a)))

# float() function convert any data type to decimal values
b = "3.5"
print(type(b))
print(type(float(b)))

zz  = complex(30,20)
print(zz)


print(bool(9))
print(bool(-8))
print(bool(0))
print(bool(0.7))
print(bool(-0.2))
print(bool(2))
print(bool(0.0))
print(bool(0+0j))


# In[17]:


# in python we can use both ('') and ("") 
a = "computer is a machine"
count = -1
for i in a:
    print(f"{i} {a[count]} ")
    count -= -1


# In[23]:


b = " hello this is a sample code"
print(b[:13])
print(b[4:])
print(b[-9:-2])
print(b[-2:-6])

email = "vaibhavmahajan@gmail.com"
res = ""
for i in email:
    if(i == "@"):
        print(res)
    res += i


# In[17]:


import math as m
print(m.sqrt(4))
print(m.pow(9,0))
print(m.fabs(-99))
print(m.floor(44.5))
print(m.floor(-44.5))
print(m.ceil(-99.9))
print(m.ceil(99.9))
print(m.exp(44.5))
print(m.sin(44.5))
print(m.cos(44.5))
print(m.tan(44.5))
print(m.log(44.5))
print(m.log10(44.5))
print(m.degrees(44.5))
print(m.radians(44.5))


# In[24]:


u=40
t = 9
f =9
y = 9
x =5
print(u*t+1/2*f*t*t)
print(u*t+(1/2)*f*m.pow(t,2))
print(m.fabs(m.exp(2*y)-x))


# In[25]:


import math
a = math.pow(2,5)
print(a)
print(math.sqrt(81))
print(math.ceil(12.8))
print(math.floor(12.8))
print(math.ceil(-38.5))
print(math.floor(-38.5))


# In[26]:


name =  input("enter the name")
if name == "vaibhav":
    print("hello vaibhav ")
elif name == "chhagan":
    print("hello chhagan")
else:
    print("enter the name")
    


# In[29]:


a = int(input("enter the number"))
if (a %2 == 0):
    print("number is even")
else:
    print("number is odd")


# In[30]:


a = int(input("Enter the number you want to check neg or pov"))
if(a > 0):
    print(a ,"is positive")
elif(a==0 ):
    print("Number is 0 ")
else:
    print(a ,"is negative")


# In[33]:


# Write a python program accept radious if radious is even calculate area of circle else calculate perimeter of circle
a = int(input("enter the number"))
if(a > 0):
    #find area
    area = 3.14 * a * a
    print(area)
else:
    #find perimeter
    peri = 2 * 3.14 * a * a
    print(peri)


# In[36]:


# write a python program accept day of week and print name of the day
i = int(input("Enter the number between 1 to 7  := \n"))
if i == 1:
    print("Sunday")
elif i == 2:
    print("Monday")
elif i == 3:
    print("tuesday")
elif i == 4:
    print("wednesday")
elif i == 5:
    print("Thusday")
elif i == 6:
    print("Friday")
elif i == 7:
    print("Saturday")
else:
    print("number must be in 1 to 7")


# In[8]:


# write a python program to accept roll name and marks of 5 sum to calculate the total % and grade if 70 > a,
roll = int(input("enter the Roll number \n"))
Name = input("enter Your name \n")
eng = int(input("enter the marks of English"))
hindi = int(input("enter the marks of Hindi"))
marathi = int(input("enter the marks of Marathi"))
aci = int(input("enter the marks of Science"))
sst = int(input("enter the marks of Social Science"))

tot = eng + hindi + marathi + aci + sst 
ans = tot / 5
grade = ""
if ans >= 70:
    grade +="A grade"
elif ans <= 60 and ans >= 46:
    grade +="B grade"
elif ans <= 45 and ans >= 34 :
    grade +="C grade"
elif ans >= 35 and ans >=33:
    grade +="D grade"
else:
    grade += "Failed"
    
print(f"Name : {Name} Rollno : {roll} has  {ans} {grade} ")




# In[ ]:





# In[11]:


# WAP  to enter monthly sale of saleman and give him commisioin i.e if the monthly sale is more than 500000 then commision will


# In[ ]:


#WAp a program to take 3 num from user and arrenge them using acesinding order using nested if
x = int(input("Enter first num"))
y = int(input("Enter first num"))
z = int(input("Enter first num"))
if y>= x <= z :
    if y <= z :
        min,mid,max = x ,z ,y
    else :
            min,mid,max = x,z,y
elif x>= y <= z :
    if x<= z:
        min,mid,max = y,x,z 
    else :
            min,mid,max = y,z,x
elif x>= z <= y :
    if x<= z:
        min,mid,max = x ,z ,y 
    else :
            min,mid,max = x ,z ,y
        


# In[ ]:


# Write a python program to find maximum num between 4 using nested if statement


# In[23]:


a  = input("Enter the name")
b = input("enter y want to find")
if b in a:
    print("yes")
else:
    print("no")


# In[35]:


# p = []
# for i in range(1,11):
#     p.append(i)
# print(p)
# if 5 in p :
#     print("True")
    
# ke = "vaibhavmahajan021"
# for i in ke:
#     print(i)

for i in range(2,101,2):
    print(i,end='\t')


# In[36]:


co  = 0
for i in range(2,101,2):
    co += i
print(co)


# In[47]:


for i in range(1,101):
    if(i%5==0)or (i%7 ==0):
        print(i,end="\t")


# In[50]:


for i in range(1,11):
    mj = 5 * i
    print(f"5 * {i} = {mj}")


# In[ ]:


# write a program to enter any age and check it is teenager or not
a = int(input("Enter your age :"))
if a >=13 and a <= 17:
    print("You are teenager")
else:
    print("You are not")


# In[ ]:


# write a program to enter monthly sale of saleman and gice him commission i.e if the monthly sale is more than 500000 then commision will be 10% of the monthly otherwise 5%
a =  int(input("Enter the monthly sale"))
if a >= 500000:
    per = (10 / 100) * 500000
else:
    per = (5 /100) * 500000
print(f"the total monthly sale is {a} and you will get {per} commision")


# In[5]:


var = 4
for i in range(1,var):
    var*= i
print(var)


# In[ ]:


# 2 question photo in mobile


# In[6]:


i = True
c = 0
while (i):
    print("Hello")
    c += 1
    if(c ==9):
        i = False


# In[23]:


# write a python program which is divisivbe by 6 and 9 in bewtteen 1 to 100
i = 1
while(i<101):
    if i %9 ==0 and i%6 ==0:
        print(i )
    i+=1
         
    


# In[4]:


num = int(input("Enter the number "))
rev = 0 
num1 = num
while num >0:
    rem = num %10
    rev = rev * 10 + rem
    num //= 10
print(f"Reverse number is {rev}")


# In[6]:


# write a python program accept a number and sum of digit
num = int(input("Enter the number "))
rev = 0 
num1 = num
while num >0:
    rem = num %10
    rev +=  rem
    num //= 10
print(f"Sum is {rev}")


# In[11]:


# write a python program accept a number to check the givn number id palimdrome or not
num = int(input("Enter the number "))
f = num
rev = 0 
while num >0:
    rem = num %10
    rev = rev * 10 + rem
    num //= 10
print(rev)
if(f == rev):
    print("Number is palindrome")
else:
    print("No")


# In[26]:


# WAP accept number to check given numer is amstrong or not
num = int(input("Enter the number "))
f = num
rev = 0 
su = 0
while num >0:
    rem = num %10
    rev = rev + rem ** 3
    num //= 10
if(rev == f):
    print("Enter number is amstrong")
else:
    print("no")




# In[5]:


# write a python program print sum of odd digits and product of even digit
i = 1
pro = 1
sum = 0
while(i!=100):
    if(i%2==0):
        pro *= i
        print(pro)
    else:
        sum += i
        print(sum)
    i +=1
    


# In[4]:


for i in range(1,101):
    if(i == 15):
        continue
    elif (i == 20):
        pass
    elif(i == 50):
        break
    print(i,end='\t')


# In[6]:


stri = " rejoy"
for i in stri:
    print(i)
else:
    print("bas kar bhai")


# In[1]:


inp1 =input("Enter the number")

sum = 0
while(inp >= 0):
    sum += inp
    inp = input("Enter the number")
    try:
        n = inp1
        inp = int(inp1)
        
    except:
        pass
    if(n == "N"):
        break
print(sum)


# In[4]:


num = int(input("Enter the number"))
lim = num//2 +1
for i in range(2,lim):
    rem = num % i
    if rem == 0:
        print(num,"is not a prime number")
        break
else:
    print(num,"Is a prime number")


# In[5]:


import random
for i in range(1,11):
    print(random.randint(1,10))
        


# In[6]:


for i in range(2,11):
    print("table of ", i)
    for j in range(1,11):
        res = i * j
        print(f"{i} *{j} = {res} ")


# In[11]:


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# In[12]:


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


# In[17]:


j = 1
for i in range(1, 5):
    for j in range(j, j+i, 1):
        print(j, end="")
    j += 1
print()


# In[19]:


li = [1,2,3,4,5,6]
def cube(a):
    return a** 3
wel = list(map(cube,li))
print(wel)


# In[23]:


count = 0
for i in range(5):
    for j in range(5):
        if(i==j)or(i+j == 4):
            print("$",end=" ")
            count += 1
        else:
            print("*",end=" ")
        print(count)


# In[25]:


for i in range(5):
    for j in range(5):
        print(i+j,end="")
    print()


# In[ ]:


for i in range(5):
    j , k = 5-i,0
    while j > 0:
        print(" ", end=" ")
        j-=1
    while k <= i:
        print("*", end=" ")
        

