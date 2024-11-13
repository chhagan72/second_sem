# 9 Create a Bus class that inherits from the Vehicle class. Give the capacity argument
# of Bus.seating_capacity() a default value of 50. 
class Vehicle:
    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed

    def display_info(self):
        print(f"Color: {self.color}, Max Speed: {self.max_speed}")


class Bus(Vehicle):
    def __init__(self, color, max_speed, capacity=50):
        super().__init__(color, max_speed)
        self.capacity = capacity

    def seating_capacity(self):
        print(f"Seating Capacity of the Bus: {self.capacity}")


# Example usage
bus = Bus("Yellow", 60)
bus.display_info()
bus.seating_capacity()
