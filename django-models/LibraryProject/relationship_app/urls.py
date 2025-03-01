from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='home'),
    path('library/', views.library_detail, name='library'),
]