from django.db import models


class ISSLocation(models.Model):

    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    velocity = models.FloatField()

    visibility = models.CharField(max_length=50)

    timestamp = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ISS @ {self.latitude}, {self.longitude}"
    