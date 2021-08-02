from django.urls import path
from asteroids.views import get_fastest_asteroid, get_largest_asteroid, get_closest_approach

urlpatterns = [
    path('get_closest_approach/', get_closest_approach, name='get_closest_approach'),
    path('get_largest_asteroid/', get_largest_asteroid, name='get_largest_asteroid'),
    path('get_fastest_asteroid/', get_fastest_asteroid, name='get_fastest_asteroid'),
]