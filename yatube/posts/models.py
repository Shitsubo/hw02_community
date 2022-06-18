from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Создать таблицу Group с полями: title, slug, description."""
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальный фрагмент url адреса'
    )
    description = models.TextField(verbose_name='Описание группы')

    def __str__(self):
        """Вернуть значение из поля tittle в виде текста."""
        return self.title


class Post(models.Model):
    """Создать таблицу Post с полями: text, pub_date, author, group"""
    text = models.TextField(verbose_name='Контент в посте')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор поста',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        related_query_name='post',
        verbose_name='Группа которой принадлежит пост',
    )

    class Meta:
        ordering = ['-pub_date']
        """Отсортировать по дате от ранних к поздним"""
