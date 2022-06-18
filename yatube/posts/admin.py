from django.contrib import admin

from .models import Post, Group


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Создать объект для управления моделью в админке."""
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    search_fields = ('text',)
    list_editable = ('group',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
