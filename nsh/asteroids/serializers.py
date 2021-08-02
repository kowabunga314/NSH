from rest_framework import serializers
from asteroids.models import Asteroid, Approach


class AsteroidSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, data):
        params = {
            'body_id': data['id'],
            'name': data['name'],
            'absolute_magnitude_h': data['absolute_magnitude_h'],
            'diameter': data['estimated_diameter']['kilometers'],
            'first_observed': data['orbital_data']['first_observation_date'],
            'last_observed': data['orbital_data']['last_observation_date'],
            'eccentricity': data['orbital_data']['eccentricity'],
            'inclination': data['orbital_data']['inclination'],
            'semi_major_axis': data['orbital_data']['semi_major_axis'],
            'orbital_period': data['orbital_data']['orbital_period'],
            'aphelion': data['orbital_data']['perihelion_distance'],
            'perihelion': data['orbital_data']['aphelion_distance'],
        }
        asteroid = Asteroid(**params)
        return asteroid.save()

    class Meta:
        model = Asteroid
        fields = '__all__'


class ApproachSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, data):
        """
        This method uses JPL data from NeoWs API to track asteroid encounters

        "data" uses the schema from NeoWs "encounter"
        """
        params = {
            'body_id': data['id'],
            'time': data['close_approach_data'][0]['close_approach_date'],
            'relative_velocity': data['close_approach_data'][0]['relative_velocity']['kilometers_per_second'],
            'miss_distance': data['close_approach_data'][0]['miss_distance']['kilometers'],
        }
        return Approach(**params)

    class Meta:
        model = Approach
        fields = '__all__'
