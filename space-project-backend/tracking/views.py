from django.shortcuts import render
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ISSLocationView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        url = "https://api.wheretheiss.at/v1/satellites/25544"

        response = requests.get(url)

        data = response.json()

        result = {
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "altitude": data.get("altitude"),
            "velocity": data.get("velocity"),
            "visibility": data.get("visibility"),
            "timestamp": data.get("timestamp"),
        }

        return Response(result)