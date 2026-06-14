# inheritance example // contains 
# single level inheritance// multilevel inheritance// multiple inheritance
# method overriding

# Base Class
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor")

    def show(self):
        print(f"Name: {self.name}")

    def role(self):
        print("I am a person")


# Single Inheritance
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)   # Calling parent constructor
        self.roll_no = roll_no
        print("Student constructor")

    def show(self):
        super().show()           # Calling parent method
        print(f"Roll No: {self.roll_no}")

    # Method Overriding
    def role(self):
        print("I am a student")


# Another Parent Class
class Athlete:
    def __init__(self):
        print("Athlete constructor")

    def sport(self):
        print("Plays football")


# Multiple Inheritance
class StudentAthlete(Student, Athlete):
    def __init__(self, name, roll_no):
        Student.__init__(self, name, roll_no)
        Athlete.__init__(self)
        print("StudentAthlete constructor")

    def role(self):
        print("I am a student athlete")


# Multilevel Inheritance
class Monitor(StudentAthlete):
    def __init__(self, name, roll_no):
        super().__init__(name, roll_no)
        print("Monitor constructor")

    def duty(self):
        print("Maintains classroom discipline")


# Create Object
m = Monitor("Ali", 101)

print("\n--- Methods ---")
m.show()          # Inherited method
m.sport()         # Multiple inheritance method
m.duty()          # Own method

print("\n--- Polymorphism / Overriding ---")
m.role()

print("\n--- MRO ---")
print(Monitor.mro())