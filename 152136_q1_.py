#NYAKIO NDAMBIRI ESTHER ICS3A CAT1 QUESTION 1: LIBRARY SYSTEM
class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books =[]

    def borrow_book(self, book):
        if book.is_borrowed == False:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print (f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} doesn't have '{book.title}'.")

    def list_borrowed_books(self):
        if len(self.borrowed_books) > 0:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books")

#examples
book1= Book("Maybe in Another Lifetime", "Taylor Reed")
book2 =Book("Seven Husbands of Evelyn Hugo", "Taylor Reed")
LibraryMember1 = Member("Nyaks",500)
LibraryMember2 = Member("Kare",501)

LibraryMember1.borrow_book(book1)
LibraryMember2.borrow_book(book1)
LibraryMember2.borrow_book(book2)
LibraryMember1.list_borrowed_books()
LibraryMember2.return_book(book2)
LibraryMember2.list_borrowed_books()        