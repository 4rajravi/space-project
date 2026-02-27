from django.db import models

class Satellite(models.Model):

    name = models.CharField(max_length=100)
    norad_id = models.IntegerField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ISSLocation(models.Model):

    satellite = models.ForeignKey(
        Satellite,
        on_delete=models.CASCADE,
        related_name="locations"
    )

    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    velocity = models.FloatField()

    visibility = models.CharField(max_length=50)
    timestamp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    