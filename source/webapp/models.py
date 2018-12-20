from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя пользователя")
    email = models.CharField(max_length=50, verbose_name="E-mail")
    favorites = models.ManyToManyField('Post', blank=True, related_name='favored_by', verbose_name='Избранное')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    text = models.TextField(max_length=5000, verbose_name="Текст")
    date = models.DateTimeField(default=datetime.now, verbose_name='Дата')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts_by_user', verbose_name='Автор')

    def __str__(self):
        return self.title

    def parent_comments(self):
        return self.comments.filter(parent_comment__isnull=True)


class Comment(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Комментарий")
    date = models.DateTimeField(default=datetime.now, verbose_name='Дата')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comments', verbose_name='Автор')
    parent_comment = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.PROTECT, related_name='child_comments', verbose_name='Родительский комментарий')
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments', verbose_name='Пост')

    def __str__(self):
        return self.text



class Rating(models.Model):
    RATING_1 = 'awful'
    RATING_2 = 'bad'
    RATING_3 = 'average'
    RATING_4 = 'well'
    RATING_5 = 'excellent'

    RATING_CHOICES = (
        (RATING_1, 'Посредственно'),
        (RATING_2, 'Неудовлетворительно'),
        (RATING_3, 'Удовлетворительно'),
        (RATING_4, 'Хорошо'),
        (RATING_5, 'Отлично')
    )

    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='ratings', verbose_name='Пост')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ratings', verbose_name='Пользователь')
    value = models.CharField(max_length=20, choices=RATING_CHOICES, verbose_name='Оценка')

    def __str__(self):
        return self.get_value_display()