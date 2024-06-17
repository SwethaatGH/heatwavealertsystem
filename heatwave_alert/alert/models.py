from django.db import models

class Subscriber(models.Model):
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.phone_number
