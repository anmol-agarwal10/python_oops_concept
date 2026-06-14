# creating classes for association

class Book:
    def __init__(self, book_id: int, name: str, author: str, copies=1):
        self.book_id = book_id      # Instance Attribute
        self.name = name            # Instance Attribute
        self.author = author        # Instance Attribute
        self.copies = copies        # Instance Attribute

    def __str__(self):
        # Polymorphism (Method Overriding)
        # Overrides the default __str__() method inherited from object class
        return f"{self.book_id} | {self.name} | {self.author} | {self.copies}"
    

class Member:
    def __init__(self, mid, name):
        self.mid = mid                    # Instance Attribute
        self.name = name                  # Instance Attribute

        # Aggregation
        # Member stores Book objects issued to him
        self.books_issued = {}