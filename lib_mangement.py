from bookandmember import Book, Member
from oops_prac.library import Library

mylibrary = Library()

def details():
    book_id = int(input('enter book id: '))
    name = input("enter book name: ")
    author = input("enter book author: ")
    copies = int(input("enter no of copies: "))
    return book_id, name, author, copies

while True:
    d = int(input("""
    1.add book
    2.search book
    3.remove book
    4.add member
    5.book issue
    6.book return
    7.show all books
    8.show all transections
    """
    ))
    if d == 1:
        book_id, name, author, copies = details()
        mylibrary.add_book(Book(book_id,name,author,copies))

    if d == 2:
        search_by = input("search by name/Id:")
        if search_by == "id":
            book_id = input('enter book id: ')
            book = mylibrary.search_book(id=book_id)
            print(book)
        else:
            name = input("enter book name: ")
            book = mylibrary.search_book(name=name)
            print(book)

    if d == 3:
        book_id, name, author, copies = details()
        mylibrary.remove_book(Book(book_id,name,author,copies))

    if d == 4:
        mid = input("Enter the Member Id: ")
        m_name = input("Enter the Mmeber Name: ")
        mylibrary.add_member(Member(int(mid), m_name))
        
    if d == 7:
        print(mylibrary.allbooks)