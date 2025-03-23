from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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
