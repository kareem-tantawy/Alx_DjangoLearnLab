from django.contrib import admin
from .models import Book
# Register your models here.
# Book.site.register(Book)
admin.ModelAdmin(Book)