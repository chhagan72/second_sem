# 8 Create a child class Bus that will inherit all of the variables and methods of the Vehicle class 
class Vehicle:
    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed

    def display_info(self):
        print(f"Color: {self.color}, Max Speed: {self.max_speed}")


class Bus(Vehicle):
    def __init__(self, color, max_speed, capacity):
        # Call the constructor of the parent class (Vehicle) to initialize color and max_speed
        super().__init__(color, max_speed)
        self.capacity = capacity

    def display_info(self):
        # Call the display_info method of the parent class (Vehicle)
        super().display_info()
        print(f"Capacity: {self.capacity}")


# Example usage
bus = Bus("Yellow", 60, 50)
bus.display_info()
