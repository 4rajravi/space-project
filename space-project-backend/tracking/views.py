import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import ISSLocation


class ISSLocationView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        url = "https://api.wheretheiss.at/v1/satellites/25544"

        response = requests.get(url)
        data = response.json()

        # Save to database
        location = ISSLocation.objects.create(
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            altitude=data.get("altitude"),
            velocity=data.get("velocity"),
            visibility=data.get("visibility"),
            timestamp=data.get("timestamp"),
        )

        return Response({
            "latitude": location.latitude,
            "longitude": location.longitude,
            "altitude": location.altitude,
            "velocity": location.velocity,
            "visibility": location.visibility,
            "timestamp": location.timestamp,
        })

class ISSHistoryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        locations = ISSLocation.objects.order_by("-created_at")[:50]

        data = [
            {
                "latitude": loc.latitude,
                "longitude": loc.longitude,
                "altitude": loc.altitude,
                "velocity": loc.velocity,
                "timestamp": loc.timestamp,
                "created_at": loc.created_at,
            }
            for loc in locations
        ]

        return Response(data)
    
class ISSTrailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        locations = ISSLocation.objects.order_by("-created_at")[:100]
        locations = reversed(locations)

        trail = [
            {
                "latitude": loc.latitude,
                "longitude": loc.longitude,
                "timestamp": loc.timestamp,
            }
            for loc in locations
        ]

        return Response(trail)
    