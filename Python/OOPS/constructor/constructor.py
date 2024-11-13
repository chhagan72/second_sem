# This is a default constructor 
# The constructor are calling by it self.
class sample:
    def __init__(self):
        print("This is a default constructor....")

s = sample() 

# The construcor are calling by using object.
class sample:
    def __init__(self):
        print("This is a default constructor....")
    def us(self):
        print("This is a...")
s = sample()
s.us()


# Parameterized Constructor

class Para:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c = a + b
    def displayAddition(self):
        
        print(self.c)
a = Para(3,4)
a.displayAddition()
        
class loopC:
    n = 20
    m = 30
    def __init__(self):
        if(self.n == self.m):
            print("This n And m is equaly")
        else:
            print("The n And m is not equaly")
    def greater(self):
        if self.n > self.m :
            print("The n is greater")
        else:
            print("The m is greater")
l = loopC()
l.greater()

