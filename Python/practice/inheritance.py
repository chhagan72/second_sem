# ! Single Inheritance

# class a():
#     def a1(self):
#         print("This is a first class methods")
# class b(a):
#     def b1(self):
#         print("Second class method")

# b = b()
# b.a1()
# b.b1()

# # 2 Multiple inheritance
# class a():
#     def a1(self):
#         print("This is a first class methods........................")
# class c():
#     def c1(self):
#         print("This is a first class methods")
# class b(a,c):
#     def b1(self):
#         print("Second class method")

# b = b()
# b.a1()
# b.b1()
# b.c1()


# 3 Multilevel inheritance
class a():
    def a1(self):
        print("This is a first class methods........................")
class c(a):
    def c1(self):
        print("This is a first class methods")
class b(c):
    def b1(self):
        print("Second class method")

b = b()
b.a1()
b.b1()
b.c1()