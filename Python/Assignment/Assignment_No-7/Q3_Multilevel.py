class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def play(self):
        print("Puppy plays")

puppy = Puppy()
puppy.speak()  
puppy.bark()
puppy.play()