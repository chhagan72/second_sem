class Flyable:
    def fly(self):
        print("Flying high")

class Animal:
    def speak(self):
        print("Animal speaks")

class Bird(Animal, Flyable):
    def chirp(self):
        print("Bird chirps")

bird = Bird()
bird.speak() 
bird.fly()
bird.chirp()  