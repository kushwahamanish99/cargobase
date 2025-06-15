from django.db import models

class Flight(models.Model):
    airline_code = models.CharField(max_length=10)
    flight_number = models.CharField(max_length=10)
    departure_date = models.DateField()
    status = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    scheduled_departure = models.DateTimeField()
    scheduled_arrival = models.DateTimeField()

    def __str__(self):
        return f"{self.airline_code}{self.flight_number}"
