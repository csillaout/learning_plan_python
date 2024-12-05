class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        print(f"Title: {self.title}")
        print("fAuthor: {self.author}")
        print(f"Year: {self.year}")
        

print(Book("1984", "George Orwell", 1949))