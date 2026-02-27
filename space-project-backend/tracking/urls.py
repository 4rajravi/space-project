from django.urls import path
from .views import ISSLocationView, ISSHistoryView, ISSTrailView

urlpatterns = [
    path("iss/", ISSLocationView.as_view()),
    path("history/", ISSHistoryView.as_view()),
    path("trail/", ISSTrailView.as_view()),
]
