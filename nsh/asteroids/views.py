from asteroids.serializers import ApproachSerializer
from clients.neows import NeoWs
from django.shortcuts import render

# Create your views here.
def get_closest_approach():
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

    # Return closest approach
    ca_model = ApproachSerializer().create(data=data['near_earth_objects'][closest_approach['day']][closest_approach['pos']])

    return ca_model
