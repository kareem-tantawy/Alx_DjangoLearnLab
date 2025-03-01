from django.shortcuts import render
from .models import Library, Book, Author, Librarian
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html')

def LibraryDetailView(request):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    # return render(request, 'relationship_app/library_detail.html')
    
# User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to home after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# User Registration View
def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
