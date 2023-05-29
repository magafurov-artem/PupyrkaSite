from django.db import models


class Specialties(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    image_preview_url = models.CharField(max_length=255)
