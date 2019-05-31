from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()

class Chef(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="restaurant")

class FoodCritic(models.Model):
    name = models.CharField(max_length=255)
    
class Publication(models.Model):
    name = models.CharField(max_length=255)

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="restaurant_review")
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="publication_review")
    foodcritic = models.ForeignKey(FoodCritic, on_delete=models.CASCADE, related_name="foodcritic_review")
    