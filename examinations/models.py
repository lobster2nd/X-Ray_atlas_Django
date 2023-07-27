from django.db import models


class Examinations(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images")
    video_link = models.URLField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
