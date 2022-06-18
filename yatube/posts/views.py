from django.shortcuts import render, get_object_or_404

from .constants import post_count
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.select_related('author')[:post_count]
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author').filter(group=group)[:post_count]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }

    return render(request, template, context)
