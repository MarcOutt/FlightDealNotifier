from datetime import datetime, timedelta

import requests

from private_infos import tequila_api_key

HOME = "PAR"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = tequila_api_key


class FlightSearch:

    def get_iata_code_city(self, city):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        headers = {
            "apikey": TEQUILA_API_KEY
        }

        query = {
            "term": city,
        }

        response = requests.get(url=location_endpoint, params=query, headers=headers)
        response.raise_for_status()
        data = response.json()
        iata_code = data['locations'][0]['code']
        return iata_code

    def get_flight_price(self, city):
        today = datetime.now()
        date_to = today + timedelta(days=180)

        search_endpoint = f"{TEQUILA_ENDPOINT}/search"

        headers = {
            "apikey": TEQUILA_API_KEY
        }

        query = {
            "fly_from": HOME,
            "fly_to": city,
            "date_from": today.strftime("%Y-%m-%d"),
            "date_to": date_to.strftime("%Y-%m-%d"),
            "limit": 2
        }

        response = requests.get(url=search_endpoint, params=query, headers=headers)
        response.raise_for_status()
        data = response.json()
        flights = data['data']
        return flights