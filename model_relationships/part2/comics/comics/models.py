from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=255)

class Writer(models.Model):
    name = models.CharField(max_length=255)
    
class Artist(models.Model):
    name = models.CharField(max_length=255)

class Issue(models.Model):
    number = models.IntegerField()
    comic_id = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name="comic_issue")
    writer = models.ManyToManyField(Writer)
    artist = models.ManyToManyField(Artist)
   