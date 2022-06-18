from django.shortcuts import render, get_object_or_404

from .constants import TOTAL_POSTS
from .models import Post, Group


def index(request):
    """Формирует главную страницу с самыми новыми постами."""
    template = 'posts/index.html'
    posts = Post.objects.select_related('author', 'group')[:TOTAL_POSTS]
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def group_posts(request, slug):
    """Формирует страницу группы с постами этой группы."""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:TOTAL_POSTS]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }

    return render(request, template, context)
