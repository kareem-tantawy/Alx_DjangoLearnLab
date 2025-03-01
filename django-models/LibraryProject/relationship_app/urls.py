from django.urls import path
from .views import list_books, library_detail

urlpatterns = [
    path('', list_books, name='home'),
    path('library/<int:pk>/', library_detail, name='library_detail')
]
