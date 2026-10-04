class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {"title": title, "author": author}
        self.books.append(book)
        return book

    def get_all_books(self):
        return self.books

    def search_book(self, title):
        return [book for book in self.books if title.lower() in book["title"].lower()]