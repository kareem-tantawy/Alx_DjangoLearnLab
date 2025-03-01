from django.shortcuts import render
from .models import Library, Book, Author, Librarian
from django.views.generic.detail import DetailView

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html')

def LibraryDetailView(request):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    # return render(request, 'relationship_app/library_detail.html')