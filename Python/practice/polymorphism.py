class a():
    def a1(self):
        print("Hello")
    def a2(self, m):
        self.m=m
        print(m)
class A():
    def A1(self):
        print("Harsh")
    def A2(self):
        print("Aditya")
a = a()
b = A()

a.a1()
b.A1()
a.a2(10)