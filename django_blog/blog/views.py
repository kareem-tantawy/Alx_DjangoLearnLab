from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.generic import ListView, TemplateView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class home(TemplateView):
    template_name = "blog/home.html"


class posts(ListView):
    model = Post
    template_name = "blog/posts.html"
    ordering = ["-published_date"]


# class register(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('home')
#     template_name = 'blog/register.html'


class register(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login-form")
    template_name = "blog/register.html"

    def form_valid(self, form):

        response = super().form_valid(form)

        username = form.cleaned_data.get("username")
        messages.success(
            self.request, f"Account created for {username}! You can now log in."
        )

        return response


# class Profile(LoginRequiredMixin, DetailView):
#     model = CustomUser
#     template_name = 'blog/profile.html'


@login_required
def profile(request):
    return render(request, "blog/profile.html")


@login_required
def update_profile(request):
    if request.method == "POST":
        u_form = CustomUserChangeForm(
            request.POST, request.FILES, instance=request.user
        )
        if u_form.is_valid():
            u_form.save()
        messages.success(request, f"Your account has been updated!")
        return redirect("profile")

    else:
        u_form = CustomUserChangeForm(instance=request.user)

    context = {"u_form": u_form}
    return render(request, "blog/update_profile.html", context)


class post(DetailView):
    model = Post
    context_object_name = "post"
    # context_object_name = 'post-detail'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/create_post.html"
    fields = ["title", "content"]
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/create_post.html"
    fields = ["title", "content"]
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
            
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    template_name = "blog/post_delete_confirm.html"
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
