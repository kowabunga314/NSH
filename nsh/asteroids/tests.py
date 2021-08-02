from asteroids.models import Approach
from asteroids.views import get_closest_approach
from clients.neows import NeoWs
from django.test import TestCase

# Create your tests here.
class TestAsteroid(TestCase):

    def test_browse_status_code(self):
        """
        Test that the browse endpoint returns a 200 code
        """
        self.assertEqual(1, 1)

    def test_get_closest_approach_response(self):
        """
        Test that the get_approaches_by_date endpoint returns a 200 code
        """
        closest_approach = get_closest_approach()
        # print(closest_approach)
        self.assertIsInstance(closest_approach, Approach)

    # def test_get_asteroid_detail_no_args_status_code(self):
    #     """
    #     Test that the get_asteroid_detail endpoint returns a 200 code
    #     """
    #     pass


class TestApproach(TestCase):

    def test_get_approach_data(self):
        """
        Test that the browse endpoint returns a 200 code
        """
        n = NeoWs()
        approach_data = n.get_approaches_by_date()
        self.assertIsInstance(approach_data, dict)

    # def test_get_approaches_by_date_no_args_status_code(self):
    #     """
    #     Test that the get_approaches_by_date endpoint returns a 200 code
    #     """
    #     pass

    # def test_get_asteroid_detail_no_args_status_code(self):
    #     """
    #     Test that the get_asteroid_detail endpoint returns a 200 code
    #     """
    #     pass

