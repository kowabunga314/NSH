from asteroids.models import Approach
from asteroids.views import get_closest_approach, get_fastest_asteroid, get_largest_asteroid
from clients.neows import NeoWs
from django.test import TestCase


# Create your tests here.
class TestApproachViews(TestCase):

    def test_get_closest_approach_returns_model(self):
        """
        Test that the get_closest_approach endpoint returns an Approach model
        """
        closest_approach = get_closest_approach()
        # print(closest_approach)
        self.assertIsInstance(closest_approach, Approach)

    def test_get_largest_asteroid_returns_model(self):
        """
        Test that the get_largest_asteroid endpoint returns an Approach model
        """
        largest_asteroid = get_largest_asteroid()
        # print(largest_asteroid)
        self.assertIsInstance(largest_asteroid, Approach)

    def test_get_fastest_asteroid_returns_model(self):
        """
        Test that the get_fastest_asteroid endpoint returns an Approach model
        """
        fastest_asteroid = get_fastest_asteroid()
        # print(fastest_asteroid)
        self.assertIsInstance(fastest_asteroid, Approach)

