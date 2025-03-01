from django.shortcuts import render

# Create your views here.

def list_books(request):
    return render(request, 'relationship_app/list_books.html')

def library_detail(request):
    return render(request, 'relationship_app/library_detail.html')