import django
import os

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# Query 2: List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Sample Data Insertion (Optional)
def populate_sample_data():
    author1 = Author.objects.create(name="J.K. Rowling")
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    
    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book2)
    
    librarian1 = Librarian.objects.create(name="John Doe", library=library1)

    print("Sample data added!")

# Uncomment to populate data
# populate_sample_data()

# Uncomment to test queries
# print(get_books_by_author("J.K. Rowling"))
# print(get_books_in_library("Central Library"))
# print(get_librarian_for_library("Central Library"))
