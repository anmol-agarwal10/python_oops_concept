# the abstraction example

from abc import ABC, abstractmethod

class Vehicle(ABC):

    # Class Variable
    total_vehicles = 0

    def __init__(self, brand, speed):
        self.brand = brand              # Instance Variable
        self.__speed = speed            # Private Variable

        Vehicle.total_vehicles += 1

    # Getter
    @property
    def speed(self):
        return self.__speed

    # Abstract Method
    @abstractmethod
    def start(self):
        pass

    # Another Abstract Method
    @abstractmethod
    def fuel_type(self):
        pass

    # Concrete Method
    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.__speed}")

    # Class Method
    @classmethod
    def vehicle_count(cls):
        print("Total Vehicles:", cls.total_vehicles)

    # Static Method
    @staticmethod
    def company_policy():
        print("Wear seat belt while driving.")


# Child Class
class Car(Vehicle):

    def start(self):
        print("Car starts with key.")

    def fuel_type(self):
        return "Petrol"


# Child Class
class ElectricCar(Vehicle):

    def start(self):
        print("Electric Car starts with button.")

    def fuel_type(self):
        return "Battery"


# Objects
c1 = Car("BMW", 220)
e1 = ElectricCar("Tesla", 250)

# Polymorphism
vehicles = [c1, e1]

for v in vehicles:
    v.start()               # Runtime Polymorphism
    print(v.fuel_type())
    v.display()
    print()

Vehicle.vehicle_count()
Vehicle.company_policy()