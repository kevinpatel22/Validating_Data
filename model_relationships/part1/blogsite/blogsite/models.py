from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Thread(models.Model):
    topic = models.CharField(max_length=255)
    create_thread = models.TextField(max_length=5000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_thread")

class Replies(models.Model):
    thread_id = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="thread_replies")
    
class Views(models.Model):
    number_of_views = models.IntegerField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="thread_views")
    replies= models.ForeignKey(Replies, on_delete=models.CASCADE, related_name="replies_views")

