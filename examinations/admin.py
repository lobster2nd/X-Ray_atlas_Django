from django.contrib import admin

from .models import *


class ExaminationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'time_create', 'image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Examinations, ExaminationsAdmin)
admin.site.register(Category, CategoryAdmin)
