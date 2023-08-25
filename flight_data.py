class FlightData:

    def __init__(self, price, departure_city, departure_iata_code, arrival_city, arrival_iata_code
                 , departure_date, return_date):
        self.price = price
        self.departure_city = departure_city
        self.departure_iata_code = departure_iata_code
        self.arrival_city = arrival_city
        self.arrival_iata_code = arrival_iata_code
        self.departure_date = departure_date
        self.return_date = return_date
