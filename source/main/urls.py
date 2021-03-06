"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import UserListView, UserDetailView, PostDetailView, PostListView, FavoritesView, PostCreateView, PostUpdateView, CommentCreateView, CommentUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('', PostListView.as_view(), name='posts_list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('favorites/<int:pk>', FavoritesView.as_view(), name='favorites'),
    path('posts/create', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('comments/create', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/update', CommentUpdateView.as_view(), name='comment_update'),
]
