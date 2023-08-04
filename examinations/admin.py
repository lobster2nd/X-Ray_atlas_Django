from django.contrib import admin

from .models import *


class ExaminationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'time_create', 'image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Examinations, ExaminationsAdmin)
admin.site.register(Category, CategoryAdmin)
