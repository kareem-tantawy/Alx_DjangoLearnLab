from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout, user_register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', list_books, name='home'),
    path('library/<int:pk>/', LibraryDetailView, name='library_detail'),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
]
