from django.db import models


class Puppy(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()