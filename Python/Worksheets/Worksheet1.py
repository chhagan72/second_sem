# # Q1.
# # str ="Hello"
# # str[:2]
# # print(str[:2])

# # Q2
# # str ='Hello'
# # res =""
# # for i in range(len(str)):
# #     res=res+str[i]
# # print(res)

# # Q3
# # s='Hi!'
# # s1='Hello'
# # s2=s[:2]+s1[len(s1)-2:]
# # print(s2)

# # Q4
# # print('ba'+'na'*2)

# # Q5
# # s = 'Welcome to python4csip.com'
# # print(s.find('come'))
# # s.count('o')


# # Q6 
# # s ='Hello'
# # for i in s:
# #     print(i,end='#')

# # Q7
# # for i in 'hardik': 
# #     print(i.upper()) 

# # Q8
# # s ='Hello'
# # for i in s:
# #     print('Welcome')


# # Q9
# # str = 'virat'
# # for i in str:
# #     print(str.upper())

# # Q10
# # a = 'hello'
# # b = 'virat'
# # for i in range(len(a)):
# #     print(a[i], b[i])


# # Q11
# # a='hello' 
# # b='virat' 
# # for i in range(len(a)): 
# #     print(a[i].upper(),b[i]) 

# # Q12
# # print("xyyzxyzxzxyy".count('xyy', 2, 11)) 

# # Q13
# # print(“hello”+1+2+3) 

# # Q14
# # str1 = "PYTHONORG1.COM" 
# # print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1]) 

# # Q15
# # str = "my name is kunfu pandya"; 
# # print (str.capitalize()) 

# # Q16
# # str1 = 'Hello' 
# # str2 ='World!' 
# # print('str1 + str2 = ', str1 + str2) 
# # print('str1 * 3 =', str1 * 3) 

# # Q17
# # count = 0 
# # for letter in 'Hello World': 
# #     if(letter == 'l'): 
# #         count += 1 
# # print(count,'letters found') 

# # Q18
# # s="python4csip" 
# # n = len(s) 
# # m='' 
# # for i in range(0, n): 
# #     if (s[i] >= 'a' and s[i] <= 'm'): 
# #         m = m + s[i].upper() 
# #     elif (s[i] >= 'n' and s[i] <= 'z'): 
# #         m = m + s[i-1] 
# #     elif (s[i].isupper()): 
# #         m = m + s[i].lower() 
# #     else: 
# #         m = m + '#' 
# # print(m) 

# # Q19
# # a = "Mahender Singh Dhoni" 
# # b= a.split() 
# # c= a[0][0]+". "+a[1][0]+". "+a[2] 
# # print (b) 

# # Q20
# # s='Mahender, Singh, Dhoni' 
# # s1=s.split() 
# # for i in s1: 
# #     print(i) 

# # Q21
# # print("Welcome to Python4csip.com".split() )

# # Q22
# # str ='Hello Python' 
# # print(str) 
# # print(str[0]) 
# # print(str[2:8]) 
# # print(str[3:]) 
# # print(str * 3) 
# # print (str + "String") 

# # Q23
# # line = "PYTHON IS EASY TO LEARN" 
# # L = line.split('a') 
# # for i in L: 
# #     print(i, end=' ') 

# # Q24
# # s='mahender, singh, dhoni' 
# # s1=s.split() 
# # for i in s1: 
# #     if(i>'n'): 
# #         print(i.upper()) 
# #     else: 
# #         print(i)

# # Q25 
# # my_string = 'PYTHON4CSIP' 
# # for i in range(len(my_string)): 
# #     print  (my_string) 
# #     my_string ='#' 

# # Q26
# # str="Pythoncsip.com"
# # for i in range(len(str)):
# #     if(str[i].isalpha()):
# #         print(str[i-1],end='')
# #     if(str[i].isdigit()):
# #         print(str[i],end='')

# # # Q27
# # str="AB145CVD124N"
# # for i in range(len(str)):
# #     if(str[i].isalpha()):
# #         print(str[i-1],end='')
# #     if(str[i].isdigit()):
# #         print('#',end='')

# # Q28
# # str="PYTHON4CSIP" 
# # for i in range(len(str)): 
# #     if(str[i].isdigit()): 
# #         print(str[i],end='') 
# #     if(str[i]=='N'or str[i]=='Y'): 
# #         print('#',end='')

# # Q29
# # string = "chhagan" 
# # vowels = "aeiouAEIOU"
# # count = sum(string.count(vowel)for vowel in vowels)
# # print(count)

# # Q30
# # str = "Chhagan is a good boy"
# # print(str)
# # str = str.replace(" ","_")
# # print(str)

# # Q31
# # str = "Chhagan"
# # count = 0
# # for i in str:
# #     count+=1
# # print(count)

# # Q32
# # str = "Chhagan is a good"
# # wCount = 0
# # cCount = 0
# # w = str.split()
# # wCount = len(w)
# # for i in w:
# #     cCount += len(i)
# # print(wCount)
# # print(cCount)

# # Q33
# str1 = "Chhagan kumawat"
# str2 = "Rahul rathode"
# l1=0
# l2=0
# for i in str1:
#     l1+=1
# for i in str2:
#     l2+=1
# if l1>l2:
#     print(str1)
# elif l2>l1:
#     print(str2)
# else:
#     print("The both string are the equal")

# Q34
# str = "Chhagan"
# count = 0 
# for i in str:
#     if i.islower():
#         count+=1

# print(count)

# Q35
# str = "abba"
# str1 = str.replace(" ", " ").lower()
# if str==str1[::-1]:
#     print("The string is palindrome.")
# else:
#     print("The string is not palindrome.")

# Q36
# str = "CHHagan"
# uCount = 0
# lCount = 0
# for i in str:
#     if i.isupper():
#         uCount+=1
#     elif i.islower():
#         lCount+=1
#     else:
#         print("You are define number so this is not Upper case and Lower case")
# print(uCount)
# print(lCount)

# Q37
# str = input("Enter a string")
# dCount=0
# lCount=0
# for i in str:
#     if i.isdigit():
#         dCount+=1
#     elif i.isalpha():
#         lCount+=1
#     else:
#         print("Error")
# print(dCount)
# print(lCount)

# Q38
# str = "He is a good boy"
# if len(str)<2:
#     print("String length is shorted")
# else:
#     newStr = str[:2]+str[-2:]
#     print(newStr)

# Q39
# str = "For each word, we check if it's already in the word_count dictionary. If it is, we increment its count. If not, we add it to the dictionary with a count of 1."
# str = str.lower()
# for i in ".,?!":
#     str = str.replace(i,'')
# w = str.split()
# wCount ={}
# for j in w:
#     if j in wCount:
#         wCount[j]+=1
#     else:
#         wCount[j]=1
# print(wCount)

# Q40

# str1 = "Chhagan Kumawat"
# subStr = "Kumawat"
# print("Your name is ",subStr," And last name is", str1)
# if subStr in str1:
#     print("YES")
# else:
#     print("NO")

# Q41
# str = "Chhagan Kumawat"
# char = "K"
# s = 0
# for i in range(len(str)):
#     if str[i] == char:
#         s =1
#         break
# if s == 0:
#     print("We have not found the search character in string")
# else:
#     print("The first Occurence of ",char," is found at position", i + 1)

# Q42
# char ="A"
# ord(char)
# a = ord(char)
# print(a)

# Q43
# str = "Chhagan"
# char ="a"
# print(str)
# index = str.rfind(char)
# if index != -1:
#     print(str[:index]+ str[index+1:])
# else:
#     print(str)















