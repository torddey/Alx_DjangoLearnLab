from django.urls import path
from .views import base, register, LoginView, profile, PostListView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", base, name="base"),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(next_page="base"), name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("posts/", PostListView.as_view, name="posts")
]