from django.db import models

class About(models.Model):
    name = models.CharField(max_length=500)
    picture_url = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    about_me = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
