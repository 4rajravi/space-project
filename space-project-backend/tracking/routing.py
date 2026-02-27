from django.urls import path
from .consumers import ISSConsumer

websocket_urlpatterns = [
    path("ws/satellite/<int:norad_id>/", ISSConsumer.as_asgi()),
]
 