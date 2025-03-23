from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('posts/', views.posts.as_view(), name='posts'),
]
