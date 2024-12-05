class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        print(f"Title: {self.title}")
        print("fAuthor: {self.author}")
        print(f"Year: {self.year}")

    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}, Year: {self.year}"

        
book = Book("1984", "George Orwell", 1949)
book.display_info()
print(book)