from requests import api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from asteroids.api import AsteroidApi
from asteroids.serializers import ApproachSerializer
from clients.neows import NeoWs
from django.shortcuts import render


@api_view(['GET'])
def get_closest_approach(request):
    # Initialize NeoWs API
    asteroid_api = AsteroidApi()
    # Get data from NeoWs API
    closest_approach_data = asteroid_api.get_closest_approach()

    # Return closest approach
    ca_model = ApproachSerializer().create(closest_approach_data)

    return Response(data=ca_model.__dict__())


@api_view(['GET'])
def get_largest_asteroid(request):
    # Initialize NeoWs API
    asteroid_api = AsteroidApi()
    # Get data from NeoWs API
    largest_approach_data = asteroid_api.get_largest_approach()

    # Return closest approach
    ca_model = ApproachSerializer().create(data=largest_approach_data)

    return Response(data=ca_model.__dict__())


@api_view(['GET'])
def get_fastest_asteroid(request):
    # Initialize NeoWs API
    asteroid_api = AsteroidApi()
    # Get data from NeoWs API
    fastest_approach_data = asteroid_api.get_fastest_approach()

    # Return closest approach
    ca_model = ApproachSerializer().create(data=fastest_approach_data)

    return Response(data=ca_model.__dict__())


@api_view(['GET'])
def get_notable_encounters(request):
    # Initialize NeoWs API
    asteroid_api = AsteroidApi()
    # Get data from NeoWs API
    closest_approach_data = ApproachSerializer().create(asteroid_api.get_closest_approach())
    largest_approach_data = ApproachSerializer().create(asteroid_api.get_largest_approach())
    fastest_approach_data = ApproachSerializer().create(asteroid_api.get_fastest_approach())
    data = {
        'closest_approach': closest_approach_data.__dict__(),
        'largest_approach': largest_approach_data.__dict__(),
        'fastest_approach': fastest_approach_data.__dict__(),
    }

    # Return closest approach
    return Response(data=data)
