from django.urls import path
from .views import check_heat_wave

urlpatterns = [
    path('check/', check_heat_wave, name='check_heat_wave'),
]
