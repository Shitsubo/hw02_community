from django.shortcuts import render, get_object_or_404

from .constants import post_count
from .models import Post, Group


def index(request):
    """Создать метод, который обрабатывает запрос.
    Запрашивает у models данные, берет необходимый шаблон и возвращает пользователю."""
    template = 'posts/index.html'
    """Взять шаблон из templates."""
    posts = Post.objects.select_related('author')[:post_count]
    """Создать переменную со списком постов."""
    context = {
        'posts': posts,
    }
    """Создать словарь с списком постов и их атрибутами."""

    return render(request, template, context)
    """Вернуть ответ на запрос пользователя."""


def group_posts(request, slug):
    """Создать метод, который обрабатывает запрос, делает запрос к models.
    Берет необходимый шаблон и возвращает пользователю."""
    group = get_object_or_404(Group, slug=slug)
    """Взять объект из моедли Group, где уникальный url фрагмент будет соответствовать фрагменту в запросе."""
    posts = group.posts.select_related('author').filter(group=group)[:post_count]
    """Создать переменную со списком постов."""
    template = 'posts/group_list.html'
    """Взять шаблон из templates."""
    context = {
        'group': group,
        'posts': posts,
    }
    """Создать словарь с списком постов, групп и их атрибутами."""

    return render(request, template, context)
    """Вернуть ответ на запрос пользователя."""
