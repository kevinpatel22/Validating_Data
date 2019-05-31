from django.db import models

class Airlines(models.Model):
    name = models.CharField(max_length=255)

class CrewMembers(models.Model):
    name = models.CharField(max_length=255)
    
class Passengers(models.Model):
    name = models.CharField(max_length=255)

class FlightSchedule(models.Model):
    time = models.IntegerField()
    airline = models.ForeignKey(Airlines, on_delete=models.CASCADE, related_name="airline_schedule")
    crewmembers = models.ManyToManyField(CrewMembers)
    passengers = models.ManyToManyField(Passengers)
   