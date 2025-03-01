from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout, user_register, admin_view, librarian_view, member_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', list_books, name='home'),
    path('library/<int:pk>/', LibraryDetailView, name='library_detail'),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
]


# "views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="


urlpatterns = [
    path("admin-panel/", admin_view, name="admin_view"),
    path("librarian-dashboard/", librarian_view, name="librarian_view"),
    path("member-home/", member_view, name="member_view"),
]
