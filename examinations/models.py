from django.db import models
from django.urls import reverse


class Examinations(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Описание исследования')
    image = models.ImageField(upload_to="images", blank=True, verbose_name='Изображение')
    video_link = models.URLField(blank=True, verbose_name='Видео')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Область исследования')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('exam', kwargs={'exam_slug': self.slug})

    class Meta:
        verbose_name = 'Исследования'
        verbose_name_plural = 'Исследования'
        ordering = ['title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']