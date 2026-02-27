import requests
from .models import ISSLocation
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Satellite

def fetch_and_store_iss():

    satellites = Satellite.objects.all()

    if not satellites.exists():
        print("No satellites configured")
        return

    for sat in satellites:

        url = f"https://api.wheretheiss.at/v1/satellites/{sat.norad_id}"

        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to fetch {sat.name}")
            continue

        data = response.json()

        if "latitude" not in data:
            print(f"Invalid data for {sat.name}: {data}")
            continue

        location = ISSLocation.objects.create(
            satellite=sat,
            latitude=data["latitude"],
            longitude=data["longitude"],
            altitude=data["altitude"],
            velocity=data["velocity"],
            visibility=data.get("visibility", "unknown"),
            timestamp=data["timestamp"],
        )

        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            f"sat_{sat.norad_id}",
            {
                "type": "send_iss_update",
                "data": {
                    "satellite": sat.name,
                    "latitude": location.latitude,
                    "longitude": location.longitude,
                    "altitude": location.altitude,
                    "velocity": location.velocity,
                }
            }
        )

    print("Satellite update cycle complete")
