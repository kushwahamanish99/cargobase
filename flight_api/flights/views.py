# flights/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from .scraper import scrape_flight_data

@api_view(['GET'])
def flight_info(request):
    airline_code = request.GET.get('airline_code')
    flight_number = request.GET.get('flight_number')
    departure_date = request.GET.get('departure_date')

    if not (airline_code and flight_number and departure_date):
        return Response({'error': 'Missing parameters'}, status=400)

    try:
        date_obj = datetime.strptime(departure_date, "%Y-%m-%d").date()
    except ValueError:
        return Response({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=400)

    data = scrape_flight_data(airline_code, flight_number, date_obj)
    return Response(data)
