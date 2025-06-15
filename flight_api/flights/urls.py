from django.urls import path
from .views import flight_info

urlpatterns = [
    path('flight/', flight_info, name='flight_info'),
]
