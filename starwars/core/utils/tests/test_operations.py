"""
Tests for functions in operations file
"""

from core.utils import operations
from django.test import TestCase


class OperationsTests(TestCase):
    """Testing operations"""

    def test_connect_to_api(self):
        """Test if connection to api is valid and successful"""
        res = operations.handler()
        self.assertEqual(res.status_code, 200)

    def test_get_homeworld(self):
        """Test if function returns a correct member. WARNING! - test is vulnerable for a changes in api"""
        url = 'https://swapi.dev/api/planets/1/'
        homeworld = 'Tatooine'
        homeworld_api = operations.get_homeworld(url)
        self.assertEqual(homeworld_api, homeworld)

    def test_download_data_from_api(self):
        """Test downloading and daving data to file is successful"""
        filename, download_date, status = operations.download_data_from_api()  # Generates file, needs work not to
        self.assertEqual(status, True)
