# 1. Inheritance (IS-A)

# A child class is a type of parent class.

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

d = Dog()
d.eat()


# 2. Composition (Strong HAS-A)

# One object contains another object and owns its lifecycle.

class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()


# 3. Association

# Association is the general relationship between two independent objects. (general means genral like in our daily life, as in example teacher teaches students,)
# One-to-One || One-to-Many  || Many-to-Many

class Teacher:
    pass

class Student:
    pass

teacher = Teacher()
student = Student()