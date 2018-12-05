from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=1000)
    seo_url = models.CharField(max_length=1000, unique=True)
    destination = models.CharField(max_length=100)
    picture_url = models.CharField(max_length=1000)
    short_description = models.TextField()
    content = models.TextField()
    date_written = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
