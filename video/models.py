from django.db import models
from django.utils import timezone


class Video(models.Model):
    title = models.CharField(max_length=250)
    destination = models.CharField(max_length=100)
    video_url = models.CharField(max_length=1000)
    embed_url = models.CharField(max_length=1000)
    thumb_url = models.FileField(blank=True, upload_to='thumb/%Y%m/%d')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
