from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home.as_view(), name="home"),
    path("posts/", views.posts.as_view(), name="posts"),
    path("register/", views.register.as_view(), name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="blog/logout.html"),
        name="logout",
    ),
    path('profile/', views.profile, name='profile'),
    path('profile/update', views.update_profile, name='profile-update'),
]
