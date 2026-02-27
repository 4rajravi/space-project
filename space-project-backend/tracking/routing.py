from django.urls import path
from .consumers import ISSConsumer

websocket_urlpatterns = [
    path("ws/iss/", ISSConsumer.as_asgi()),
]
 