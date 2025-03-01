from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='home'),
    path('library/<int:pk>/', views.library_detail, name='library_detail')
]
