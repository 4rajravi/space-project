from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({"message": "Space Monitor API running 🚀"})


urlpatterns = [

    path('', home),

    path('admin/', admin.site.urls),

    path('api/auth/', include('accounts.urls')),

    path('api/tracking/', include('tracking.urls')),
    path('api/dashboard/', include('dashboard.urls')),

]