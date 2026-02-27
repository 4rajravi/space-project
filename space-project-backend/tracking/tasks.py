import requests
from .models import ISSLocation


def fetch_and_store_iss():

    url = "https://api.wheretheiss.at/v1/satellites/25544"

    response = requests.get(url)
    data = response.json()

    ISSLocation.objects.create(
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
        altitude=data.get("altitude"),
        velocity=data.get("velocity"),
        visibility=data.get("visibility"),
        timestamp=data.get("timestamp"),
    )

    print("ISS location saved automatically")
    