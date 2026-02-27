import requests
from .models import ISSLocation
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def fetch_and_store_iss():

    url = "https://api.wheretheiss.at/v1/satellites/25544"

    response = requests.get(url)
    data = response.json()

    location = ISSLocation.objects.create(
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
        altitude=data.get("altitude"),
        velocity=data.get("velocity"),
        visibility=data.get("visibility"),
        timestamp=data.get("timestamp"),
    )

    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        "iss_group",
        {
            "type": "send_iss_update",
            "data": {
                "latitude": location.latitude,
                "longitude": location.longitude,
                "altitude": location.altitude,
                "velocity": location.velocity,
            }
        }
    )

    print("ISS location saved + broadcasted")
    