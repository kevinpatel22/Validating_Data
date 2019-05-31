from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Events(models.Model):
    event_type = models.CharField(max_length=255)
    location = models.TextField(max_length=500)
    preson_id = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="preson_in_event")

class Tickets(models.Model):
    topic = models.IntegerField()
    events_id = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="tickets_for_events")
    preson_id = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="tickets_for_person")
    