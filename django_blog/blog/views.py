from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, TemplateView


class home(TemplateView):
    template_name = "blog/home.html"


class posts(ListView):
    model = Post
    template_name = "blog/posts.html"
    ordering = ["-published_date"]
