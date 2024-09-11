from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form":form})

class LoginView(LoginView):
    template_name = "login.html"

def profile(request):
    return render(request, "profile.html")

def base(request):
    return render(request, "base.html")

def blog_posts(request):
    posts = Post.objects.all()
    return render(request, "blog/blog_posts.html", {"posts":posts})

