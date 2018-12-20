from django import forms
from webapp.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['parent_comment', 'text', 'post', 'author']


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']