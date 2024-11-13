# class A():
#     def __init__(self):
#         print("This is a constructor...")
#     def main(self):
#         print("This is a function")
# obj = A()
# obj.main()

# Type of constructor

class A():
    # def __init__(self):
    #     print("Default constructor...")
        # Parameterized constructor
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a)
        print(self.b)

# obj = A()

obj=A(23,3)
obj.display()    