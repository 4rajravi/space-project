from django.contrib import admin
from .models import ISSLocation, Satellite


@admin.register(ISSLocation)
class ISSLocationAdmin(admin.ModelAdmin):

    list_display = ("id", "latitude", "longitude", "velocity", "created_at")

@admin.register(Satellite)
class SatelliteAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "norad_id")