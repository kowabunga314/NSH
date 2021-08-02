import unittest
from clients.neows import NeoWs


class TestNeows(unittest.TestCase):

    #==--- Test "browse" endpoint ---==#
    def test_browse_returns_200(self):
        """
        Test that the browse endpoint returns a 200 code
        """
        n = NeoWs()
        response = n.browse()
        self.assertEqual(response.get('status_code'), 200)
        self.assertIsInstance(response.get('data'), dict)

    def test_browse_response_data_format(self):
        """
        Test that the browse endpoint returns a dict called 'data'
        """
        n = NeoWs()
        response = n.browse()
        self.assertIsInstance(response.get('data'), dict)

    #==--- Test "get_approaches_by_date" endpoint ---==#
    def test_get_approaches_by_date_no_args_status_code(self):
        """
        Test that the get_approaches_by_date endpoint returns a 200 code
        """
        n = NeoWs()
        response = n.get_approaches_by_date()
        self.assertEqual(response.get('status_code'), 200)

    def test_get_approaches_by_date_response_data_format(self):
        """
        Test that the get_approaches_by_date endpoint returns a dict called 'data'
        """
        n = NeoWs()
        response = n.get_approaches_by_date()
        self.assertIsInstance(response.get('data'), dict)

    #==--- Test "get_asteroid_detail" endpoint ---==#
    def test_get_asteroid_detail_no_args_status_code(self):
        """
        Test that the get_asteroid_detail endpoint returns a 200 code
        """
        n = NeoWs()
        response = n.get_asteroid_detail()
        self.assertEqual(response.get('status_code'), 200)

    def get_asteroid_detail(self):
        """
        Test that the get_asteroid_detail endpoint returns a dict called 'data'
        """
        n = NeoWs()
        response = n.browse()
        self.assertIsInstance(response.get('data'), dict)


if __name__ == '__main__':
    unittest.main()