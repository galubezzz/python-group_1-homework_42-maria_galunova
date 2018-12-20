from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from webapp.models import User, Post, Comment, Rating
from webapp.forms import PostForm, CommentForm, CommentUpdateForm
from django.urls import reverse, reverse_lazy


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

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('posts_list')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm
    success_url = reverse_lazy('posts_list')


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment_update.html'
    form_class = CommentUpdateForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})