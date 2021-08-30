from django.test import TestCase, SimpleTestCase

# import django.urls 
from django.urls import reverse

# Create your tests here.
class TestingPages(SimpleTestCase): # enhirate django.test.SimpleTestCase
    def test_home(self):
        # arrange
        url = reverse('home')
        # assign the status code
        response = self.client.get(url)
        # assert
        self.assertEqual(response.status_code, 200)

        
    # test the home page if return status code 200 (means OK)
    def test_home_status_code(self):
        # arrange
        url = reverse('home')
        # assign the status code
        response = self.client.get(url)
        # assert
        self.assertEqual(response.status_code, 200)