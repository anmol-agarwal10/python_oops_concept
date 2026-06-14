# a library class, containing basic properties of oops
# encapsulation , polymorphism (method overloading)
# Getter Property (@property)
# Abstraction (weak relationship -- has a)


class Library:  # Class (Blueprint/Object-Oriented Programming)

    def __init__(self, name):  # Constructor
        self.libname = name  # Instance attribute

        # Encapsulation (private attributes using name mangling)
        self.__allbooks = {}
        self.__allmembers = {}
        self.__transection = []

    def add_book(self, Book):  # Method
        # Association: Library object works with Book object
        if Book.book_id in self.__allbooks:
            self.__allbooks[Book.book_id].copies += 1
        else:
            self.__allbooks[Book.book_id] = Book
        return Book

    def remove_book(self, Book):
        # Association with Book class
        if Book.book_id in self.__allbooks:
            pwd = int(input("Enter the password: "))
            if 123 == pwd:
                del self.__allbooks[Book.book_id]
                print("successfully deleted")
        else:
            print("Book not Found")

    def search_book(self, id: int = None, name: str = None):
        # Method Overloading-like behavior using default parameters
        # (Python doesn't support true method overloading)
        if id in self.__allbooks and id != None:
            book = self.__allbooks[id]
            return book

        if name != None:
            for book in self.__allbooks:
                if name == self.__allbooks[book].name:
                    book = self.__allbooks[book]
                    return book

        print("Book Not Found")

    def add_member(self, Member):
        # Association: Library uses Member object
        if Member.mid not in self.__allmembers:
            self.__allmembers[Member.mid] = Member
            print("Successfully added")
        else:
            print("ALready Exist")

    def book_issue(self, mid, book_id):
        # Encapsulation: accessing private data through class methods
        if mid in self.__allmembers:

            member = self.__allmembers[mid]  # Association with Member object

            if book_id in self.__allbooks:

                book = self.__allbooks[book_id]  # Association with Book object

                if book_id not in member.books_issued:

                    # Aggregation/Association:
                    # Member stores reference to Book object
                    member.books_issued[book_id] = book

                    book.copies -= 1

                    self.__transection.append([
                        book.book_id,
                        book.name,
                        "issued by",
                        member.mid,
                        member.name
                    ])

                    print("Successfully Issued")
                else:
                    print("Alread Issued this Book.")
            else:
                print("Book Not Found")
        else:
            print("Not a Member")

    def book_return(self, mid, book_id):
        if mid in self.__allmembers:

            member = self.__allmembers[mid]  # Association

            if book_id in self.__allbooks:

                book = self.__allbooks[book_id]  # Association

                if book_id in member.books_issued:

                    book.copies += 1
                    del member.books_issued[book_id]

                    self.__transection.append([
                        book.book_id,
                        book.name,
                        "return by",
                        member.mid,
                        member.name
                    ])

                else:
                    print("record not found")
            else:
                print("Book not Found in all Books!")
        else:
            print("Not a Member")

    @property  # Property Decorator (Getter)
    # Abstraction: User accesses data without knowing internal structure
    def allbooks(self):

        headers = ["Book ID", "Title", "Author", "Copies"]
        all_books = []

        for id, book in self.__allbooks.items():
            all_books.append([
                id,
                book.name,
                book.author,
                book.copies
            ])

        print(all_books)

    @property  # Getter Property
    # Encapsulation + Abstraction
    def all_trasection(self):

        headers = [
            "Book ID",
            "Book Name",
            "Type",
            "Member Id",
            "Member Name"
        ]

        print(self.__transection, headers)

    @property  # Getter Property
    # Encapsulation + Abstraction
    def all_members(self):

        headers = ["Member ID", "Name"]
        all_members = []

        for id, member in self.__allmembers.items():
            all_members.append([id, member.name])

        print(headers, headers)