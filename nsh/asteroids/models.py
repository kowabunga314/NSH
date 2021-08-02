from django.core.exceptions import PermissionDenied
from django.db import models


# Create your models here.
class Asteroid(models.Model):
    body_id = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    absolute_magnitude_h = models.FloatField()
    diameter = models.FloatField()  # meters
    first_observed = models.DateField()
    last_observed = models.DateField()
    eccentricity = models.FloatField()
    inclination = models.FloatField()
    semi_major_axis = models.FloatField()
    period = models.FloatField()
    aphelion = models.FloatField()
    perihelion = models.FloatField()

class Approach(models.Model):
    body_id = models.CharField(max_length=16)
    time = models.DateTimeField()
    relative_velocity = models.FloatField()
    miss_distance = models.FloatField() # km

    def __str__(self):
        return f'Asteroid {self.body_id}: {self.miss_distance} km at {self.time}'

    def __dict__(self):
        return {
            'body_id': self.body_id,
            'time': self.time,
            'relative_velocity': self.relative_velocity,
            'miss_distance': self.miss_distance
        }

