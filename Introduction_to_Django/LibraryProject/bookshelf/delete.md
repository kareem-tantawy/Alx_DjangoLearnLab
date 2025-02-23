from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion
exists = Book.objects.filter(title="Nineteen Eighty-Four").exists()
print(f"Book exists: {exists}")