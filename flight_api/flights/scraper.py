import json
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re

def scrape_flight_data(airline_code: str, flight_number: str, departure_date: str):
    url = f"https://www.flightstats.com/v2/flight-tracker/{airline_code}/{flight_number}?year={departure_date.year}&month={departure_date.month}&date={departure_date.day}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)

        # Wait for __NEXT_DATA__ script to load
        content = page.content()
        browser.close()

    soup = BeautifulSoup(content, "html.parser")
        #print(soup)
        #next_data_script = soup.find("script", id="__NEXT_DATA__")
    next_data_script = None
    for script in soup.find_all("script"):
        if script.string and "__NEXT_DATA__" in script.string:
            next_data_script = script
            break
    #print(next_data_script)
    # Clean and extract JSON string
    #raw_js = next_data_script.string.strip()
    #json_str = raw_js.split("=", 1)[1].strip(" ;")
    #print(json_str)
    
    match = re.search(r'__NEXT_DATA__\s*=\s*(\{.*?\})\s*;', next_data_script.string, re.DOTALL)
    if not match:
        return {"status": "Unavailable", "error": "Failed to extract JSON from script"}

    json_str = match.group(1)

    try:
        next_data = json.loads(json_str)
    except json.JSONDecodeError as e:
        return {"status": "Unavailable", "error": f"JSON decode failed: {e}"}

    
    try:
        flight_info = next_data["props"]["initialState"]["flightTracker"]["flight"]
        scheduled_dep = flight_info["schedule"]["scheduledDeparture"]
        scheduled_arr = flight_info["schedule"]["scheduledArrival"]
        dep_airport = flight_info["departureAirport"]["fs"]
        arr_airport = flight_info["arrivalAirport"]["fs"]
        status = flight_info["status"]["status"]

        return {
            "status": status,
            "departure_airport": dep_airport,
            "arrival_airport": arr_airport,
            "scheduled_departure": scheduled_dep,
            "scheduled_arrival": scheduled_arr
        }
    except KeyError as e:
        return {"status": "Unavailable", "error": f"Missing key in JSON: {e}"}