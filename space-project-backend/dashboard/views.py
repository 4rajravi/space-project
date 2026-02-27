from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from django.db.models import Avg

from tracking.models import ISSLocation
from core.permissions import IsAdminUserRole


User = get_user_model()


class AdminDashboardStatsView(APIView):

    permission_classes = [IsAuthenticated, IsAdminUserRole]

    def get(self, request):

        total_users = User.objects.count()
        total_iss_records = ISSLocation.objects.count()

        latest_location = ISSLocation.objects.order_by("-created_at").first()

        avg_altitude = ISSLocation.objects.aggregate(
            Avg("altitude")
        )["altitude__avg"]

        avg_velocity = ISSLocation.objects.aggregate(
            Avg("velocity")
        )["velocity__avg"]

        return Response({
            "total_users": total_users,
            "total_iss_records": total_iss_records,
            "latest_location": {
                "latitude": latest_location.latitude if latest_location else None,
                "longitude": latest_location.longitude if latest_location else None,
            },
            "average_altitude": avg_altitude,
            "average_velocity": avg_velocity,
        })
    