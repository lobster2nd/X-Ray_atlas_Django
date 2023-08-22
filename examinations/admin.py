from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ExaminationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'time_create', 'get_html_image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'cat', 'content', 'image', 'get_html_image', 'is_published',)
    readonly_fields = ('time_create', 'time_update', 'get_html_image', )

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}', width=50>")

    get_html_image.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Examinations, ExaminationsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ-панель атласа'
admin.site.site_header = 'Админ-панель атласа'
