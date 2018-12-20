from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from webapp.models import User, Post, Comment, Rating


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_details.html'


class PostListView(ListView):
    model = Post
    template_name = 'posts_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class FavoritesView(DetailView):
    model = User
    template_name = 'favorites.html'