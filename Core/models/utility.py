"""Core > models > utility.py"""
from django.db import models


class SocialMediaName(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    icone  = models.CharField(max_length=255)

    def __str__(self):
        return self.name
