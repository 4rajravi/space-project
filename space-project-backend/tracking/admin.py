from django.contrib import admin
from .models import ISSLocation


@admin.register(ISSLocation)
class ISSLocationAdmin(admin.ModelAdmin):

    list_display = ("id", "latitude", "longitude", "velocity", "created_at")