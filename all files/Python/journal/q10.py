# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any
# vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on
# full fare as a maintenance charge. So total fare for bus instance will become the final amount =
# total fare + 10% of the total fare. 
class Vehicle:
    def __init__(self, color, max_speed, capacity):
        self.color = color
        self.max_speed = max_speed
        self.capacity = capacity

    def fare_charge(self):
        fare = self.capacity * 100
        return fare


class Bus(Vehicle):
    def __init__(self, color, max_speed, capacity):
        super().__init__(color, max_speed, capacity)

    def fare_charge(self):
        fare = super().fare_charge()
        if isinstance(self, Bus):
            fare += fare * 0.1  # Adding 10% maintenance charge for buses
        return fare


# Example usage
bus = Bus("Yellow", 60, 50)
print("Total fare for bus:", bus.fare_charge())
