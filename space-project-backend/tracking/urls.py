from django.urls import path
from .views import ISSLocationView, ISSHistoryView

urlpatterns = [
    path("iss/", ISSLocationView.as_view()),
    path("history/", ISSHistoryView.as_view()),
]