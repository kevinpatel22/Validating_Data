from django.db import models

class Artists(models.Model):
    name = models.CharField(max_length=255)

class Tracks(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name='artist')

class Listeners(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ManyToManyField(Artists)
