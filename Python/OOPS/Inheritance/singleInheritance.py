#Simple Methode Using constructor
# class sample:
#     def __init__(self):
#         print("This ia single inheritance")
# class sample2(sample):
#     def show(self):
#         print("In second class we have extends with first class")
# s = sample2()
# s.show()

#Constructor with return arguments
# class Peraon():
#     def __init__(self, name):
#         self.name = name
    
#     def getName(self):
#         return self.name

#     def isEmployee(self):
#         return False
# class Employee(Peraon):
#     def isEmployee(self):
#         return True
# p = Peraon("Chhagan")
# print(p.getName(), p.isEmployee())

# e = Employee("Chhagan")
# print(e.getName(), e.isEmployee())


class Company():
    def __inti__(self, cName, cPlace):
        self.cName = cName
        self.cPlace = cPlace
    def Display(self):
        print(self.cName)
        print(self.cPlace)
class Employee(Company):
    def __init__(self,cName, cPlace, eName, eSal):
        self.eName = eName
        self.eSal = eSal
        Company.__inti__(self,cName,cPlace)
    def show(self):
        print(self.eName)
        print(self.eSal)

e = Employee("Wipro", "Pune", "Chhagan", 830000)
e.Display()
e.show()