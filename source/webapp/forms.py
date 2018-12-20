from django import forms
from webapp.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'date']


class PostSearchForm(forms.Form):
    post_keywords = forms.CharField(max_length=200, required=False, label='Ключевые слова')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['parent_comment', 'text', 'post', 'author']


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']