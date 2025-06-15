
# Cargobase - Flight Tracker API

Cargobase Assessement is a Django-based web API that retrieves real-time flight information by scraping data from [FlightStats](https://www.flightstats.com/) using Playwright.

This project demonstrates how to scrape modern JavaScript-rendered websites and expose the data through a RESTful API.

---

## Features

- REST API built with Django and Django REST Framework
- Scrapes live flight data from FlightStats using Playwright
- Parses the `__NEXT_DATA__` script to extract flight details
- Returns structured JSON with flight status, airports, times, and aircraft info
- Handles errors like missing data or dynamic content issues

---

## How It Works

1. Accepts airline code, flight number, and departure date as query parameters
2. Uses Playwright (headless browser) to load the FlightStats page
3. Parses the HTML to extract JSON from the `__NEXT_DATA__` script tag
4. Processes and returns relevant flight data via the API

---

## Requirements

- Python 3.10+
- Playwright (Chromium)
- Django
- Django REST Framework
- BeautifulSoup4

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/kushwahamanish99/cargobase.git
cd cargobase
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4. Run the Server

```bash
python manage.py runserver
```

Access the API at: `http://localhost:8000/api/flight/`

---

## API Usage

### Endpoint

```
GET /api/flight/
```

### Query Parameters

| Name             | Type   | Example       | Description                     |
|------------------|--------|---------------|---------------------------------|
| `airline_code`   | string | AI            | Airline IATA code               |
| `flight_number`  | string | 173           | Flight number                   |
| `departure_date` | string | 2025-06-16     | Date in `YYYY-MM-DD` format     |

### Example Request

```bash
curl "http://localhost:8000/api/flight/?airline_code=AI&flight_number=173&departure_date=2025-06-16"
```

### Example Response

```json
{
  "status": "Scheduled",
  "departure_airport": "DEL",
  "arrival_airport": "SFO",
  "scheduled_departure": "2025-06-16T03:00:00.000",
  "scheduled_arrival": "2025-06-16T07:00:00.000",
  "estimated_arrival": "2025-06-16T06:37:00.000",
  "aircraft": "Boeing 777-200LR"
}
```

---

## Project Structure

```
cargobase/
├── flight_api/
│   └── flights/
│       ├── scraper.py       # Web scraping logic
│       ├── views.py         # API view
│       └── urls.py          # API route config
├── manage.py
└── requirements.txt
```

---

## Disclaimer

This project is for Assessement for cargobase only.  
FlightStats may not permit automated scraping. Please review their [terms of use](https://www.flightstats.com/company/terms-of-use/) before using this in production.

---

## Author

Manish Kushwaha  
GitHub: [kushwahamanish99](https://github.com/kushwahamanish99)

