from django.urls import path

from .views import ISSLocationView


urlpatterns = [

    path("iss/", ISSLocationView.as_view()),

]