from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

if __name__ == "__main__":
    # Example usage of the queries
    print("Books by Author 'Author Name':", get_books_by_author('Author Name'))
    print("Books in Library 'Library Name':", get_books_in_library('Library Name'))
    print("Librarian for Library 'Library Name':", get_librarian_for_library('Library Name'))
