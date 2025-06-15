from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from datetime import date

class FlightTestCase(TestCase):
    def test_flight_api(self):
        response = self.client.get('/api/flight/', {
            'airline_code': 'AX',
            'flight_number': '202',
            'departure_date': str(date.today())
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('airline_code', response.json())
