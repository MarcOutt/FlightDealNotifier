import requests

SHEETY_PRICES_ENDPOINT = "https://sheetdb.io/api/v1/l7n52g8kqo09l"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        response.raise_for_status()
        self.destination_data = response.json()
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                    "IATA Code": city['IATA Code']
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/City/{city['City']}",
                json=new_data
            )
            response.raise_for_status()
