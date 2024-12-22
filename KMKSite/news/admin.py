from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News
from django import forms




class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'id')
    list_editable = ['is_published']
    fields = ('title', 'content', 'photo', 'get_photo', 'is_published', 'created_at')
    readonly_fields = ('get_photo', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='75px'>")
        else:
            return 'Фото нет'

    get_photo_description = 'Миниатюра'

admin.site.register(News, NewsAdmin)

admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'