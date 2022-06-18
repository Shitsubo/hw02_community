from django.contrib import admin

from .models import Post, Group


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Создать объект для управления моделью в админке."""
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    """"Вывести в интерфейсе админки поля из бд:
    pk - идентификатор
    text - содержание
    pub_date - дата публикации
    author - автор поста
    group - группа связанная с постом.
    """
    search_fields = ('text',)
    """Добавить в админку поиск по тексту."""
    list_editable = ('group',)
    """Добавить возможность редактирование поля группы у постов."""
    list_filter = ('pub_date',)
    """Добавить фильтрацию по дате публикации."""
    empty_value_display = '-пусто-'
    """Заменить пустые поля строкой '-пусто-'"""


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
