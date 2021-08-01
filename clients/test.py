import unittest
from clients.neows import NeoWs


class TestNeows(unittest.TestCase):

    def test_browse_status_code(self):
        """
        Test that the browse endpoint returns a 200 code
        """
        n = NeoWs()
        response = n.browse()
        self.assertEqual(response.status_code, 200)

    def test_get_approaches_by_date_no_args_status_code(self):
        """
        Test that the get_approaches_by_date endpoint returns a 200 code
        """
        n = NeoWs()
        response = n.get_approaches_by_date()
        self.assertEqual(response.status_code, 200)

    def test_get_asteroid_detail_no_args_status_code(self):
        """
        Test that the get_asteroid_detail endpoint returns a 200 code
        """
        n = NeoWs()
        response = n.get_asteroid_detail()
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()