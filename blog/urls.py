from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts-list"),
    path("posts/<slug:slug>", views.single_post, name="post-page")
]
