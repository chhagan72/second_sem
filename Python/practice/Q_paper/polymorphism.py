class IND():
    def capital(self):
        print("The New Delhi is capital of indeia")
    def language(self):
        print("Hindi is the most widely spoken language of india")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developed country")
a = IND()
b = USA()
for country in (a,b):
    country.capital()
    country.language()
    country.type()