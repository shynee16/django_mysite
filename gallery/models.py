from django.db import models
from django.utils import timezone


class Album(models.Model):
    name = models.CharField(max_length=250)
    cover_url = models.FileField(blank=True,upload_to='thumb/%Y%m/%d')
    caption = models.TextField(blank=True, default='')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Picture(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    picture_url = models.FileField(blank=True,upload_to='picture/%Y%m/%d')
    caption = models.TextField(blank=True, default='')
    date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
