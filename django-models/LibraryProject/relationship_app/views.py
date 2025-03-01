from django.shortcuts import render
from .models import Book, Author, Library, Librarian

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html')

def library_detail(request):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    # return render(request, 'relationship_app/library_detail.html')