class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False 
    def return_book(self):
        self.is_borrowed = False
        print(self.title, "has been returned")
    def borrow(self):
        self.is_borrowed = True
        print(self.title, "has been borrowed")

b1 = Book("Harry Potter", "JK Rowling")
b2 = Book("The Alchemist", "Paul Coiler")       
b3 = Book("Jungle Book", "Jake Dim")
for object in (b1, b2, b3):
    object.borrow()
    object.return_book()