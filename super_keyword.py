# using super keyword
class A:
    def greet(self):
        print("A")
        super().greet()

class B:
    def greet(self):
        print("B")
        super().greet()

class C:
    def greet(self):
        print("C")

class D(A, B, C):
    pass

d = D()
d.greet()