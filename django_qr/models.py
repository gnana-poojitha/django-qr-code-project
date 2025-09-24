from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    menu_url = models.URLField()

    def __str__(self):
        return self.name

class QRScan(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    scanned_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.restaurant.name} scanned at {self.scanned_at}"












