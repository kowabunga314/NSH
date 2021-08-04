from requests import api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from asteroids.serializers import ApproachSerializer
from clients.neows import NeoWs
from django.shortcuts import render


class NeoWsAPI():
    """
    The NeoWsAPI class contains most of the logic for the asteroid views
    """

    def get_closest_approach(self):
        n = NeoWs()
        this_week = n.get_approaches_by_date()
        data = this_week.get('data')

        # Initialize closest approach tracker
        closest_approach = dict(day=None, distance=None, pos=-1)

        # Data is grouped by day, iterate over each day
        for day in data['near_earth_objects']:
            # Day contains list of approaches, iterate over each approach
            for i, approach in enumerate(data['near_earth_objects'][day]):
                # Get distance of this approach
                distance = approach['close_approach_data'][0]['miss_distance']['kilometers']
                # Compare this approach to current closest approach
                if closest_approach['distance'] is None or distance > closest_approach['distance']:
                    closest_approach = dict(day=day, distance=distance, pos=i)
        
        # Return approach
        return data['near_earth_objects'][closest_approach['day']][closest_approach['pos']]

    def get_largest_approach(self):
        n = NeoWs()
        this_week = n.get_approaches_by_date()
        data = this_week.get('data')

        # Initialize closest approach tracker
        largest_encounter = dict(day=None, size=None, pos=-1)

        # Data is grouped by day, iterate over each day
        for day in data['near_earth_objects']:
            # Day contains list of approaches, iterate over each approach
            for i, approach in enumerate(data['near_earth_objects'][day]):
                # Get distance of this approach
                size = (
                    approach['estimated_diameter']['kilometers']['estimated_diameter_min']
                    + approach['estimated_diameter']['kilometers']['estimated_diameter_max']
                ) / 2
                # Compare this approach to current closest approach
                if largest_encounter['size'] is None or size > largest_encounter['size']:
                    largest_encounter = dict(day=day, size=size, pos=i)
        
        # Return approach
        return data['near_earth_objects'][largest_encounter['day']][largest_encounter['pos']]

    def get_fastest_approach(self):
        n = NeoWs()
        this_week = n.get_approaches_by_date()
        data = this_week.get('data')

        # Initialize closest approach tracker
        fastest_encounter = dict(day=None, r_vel=None, pos=-1)

        # Data is grouped by day, iterate over each day
        for day in data['near_earth_objects']:
            # Day contains list of approaches, iterate over each approach
            for i, approach in enumerate(data['near_earth_objects'][day]):
                # Get distance of this approach
                r_vel = approach['close_approach_data'][0]['relative_velocity']['kilometers_per_second']
                # Compare this approach to current closest approach
                if fastest_encounter['r_vel'] is None or r_vel > fastest_encounter['r_vel']:
                    fastest_encounter = dict(day=day, r_vel=r_vel, pos=i)

        # Return approach
        data['near_earth_objects'][fastest_encounter['day']][fastest_encounter['pos']]



#########################################################
#################### View Endpoints #####################
#########################################################

@api_view(['GET'])
def get_closest_approach(request):
    # Initialize NeoWs API
    na = NeoWsAPI()
    # Get data from NeoWs API
    closest_approach_data = na.get_closest_approach()

    # Return closest approach
    ca_model = ApproachSerializer().create(closest_approach_data)

    return Response(data=ca_model.__dict__())


@api_view(['GET'])
def get_largest_asteroid(request):
    # Initialize NeoWs API
    na = NeoWsAPI()
    # Get data from NeoWs API
    largest_approach_data = na.get_largest_approach()

    # Return closest approach
    ca_model = ApproachSerializer().create(data=largest_approach_data)

    return Response(data=ca_model.__dict__())


@api_view(['GET'])
def get_fastest_asteroid(request):
    # Initialize NeoWs API
    na = NeoWsAPI()
    # Get data from NeoWs API
    fastest_approach_data = na.get_fastest_approach()

    # Return closest approach
    ca_model = ApproachSerializer().create(data=fastest_approach_data)

    return Response(data=ca_model.__dict__())


@api_view(['GET'])
def get_notable_encounters(request):
    # Initialize NeoWs API
    na = NeoWsAPI()
    # Get data from NeoWs API
    closest_approach_data = na.get_closest_approach()
    largest_approach_data = na.get_largest_approach()
    fastest_approach_data = na.get_fastest_approach()
    data = {
        'closest_approach': closest_approach_data,
        'largest_approach': largest_approach_data,
        'fastest_approach': fastest_approach_data,
    }

    # Return closest approach
    ca_model = ApproachSerializer().create(data=data)

    return Response(data=ca_model.__dict__())
